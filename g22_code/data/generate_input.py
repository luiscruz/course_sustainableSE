"""
Usage examples:
  python data/generate_input.py --type compressible --mb 256 --out data/input_compressible_256MB.jsonl
  python data/generate_input.py --type incompressible --mb 256 --out data/input_incompressible_256MB.bin
  python data/generate_input.py --mb 64   # defaults to compressible, outputs under data/
"""

from __future__ import annotations

import argparse
import hashlib
import os
from dataclasses import dataclass
from typing import Iterator


# Deterministic PRNG (uniform bytes)

@dataclass(frozen=True)
class Sha256CtrPrng:
    """
    SHA-256 counter-mode PRNG.

    Given a seed (bytes) and a counter, output = SHA256(seed || counter_le64).
    Concatenating outputs for successive counters yields a deterministic byte stream.

    Properties:
    - Deterministic across platforms/versions
    - Output bytes are "uniform-ish" for experimental purposes (cryptographic hash output)
    - Suitable for generating incompressible data
    """
    seed: bytes
    counter: int = 0

    def stream(self) -> Iterator[bytes]:
        c = self.counter
        seed = self.seed
        while True:
            # 8-byte little-endian counter; stable everywhere.
            ctr_bytes = c.to_bytes(8, "little", signed=False)
            block = hashlib.sha256(seed + ctr_bytes).digest()  # 32 bytes
            yield block
            c += 1

    def take(self, n: int) -> bytes:
        """Convenience for small reads (not used for huge files)."""
        out = bytearray()
        for block in self.stream():
            need = n - len(out)
            if need <= 0:
                break
            out += block[:need]
        return bytes(out)


def _seed_to_bytes(seed_str: str) -> bytes:
    # Normalize seed string into bytes deterministically.
    # Using SHA-256 of the UTF-8 seed makes seed handling stable.
    return hashlib.sha256(seed_str.encode("utf-8")).digest()


# Dataset generators

def generate_incompressible(path: str, total_bytes: int, prng: Sha256CtrPrng, chunk_bytes: int = 1 << 20) -> str:
    """
    Write an incompressible binary file consisting of uniform PRNG bytes.
    Returns hex SHA-256 of the file for verification.
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    sha = hashlib.sha256()
    remaining = total_bytes
    blocks = prng.stream()

    with open(path, "wb") as f:
        while remaining > 0:
            # Build up to chunk_bytes from 32-byte blocks to reduce Python overhead.
            to_write = min(remaining, chunk_bytes)
            buf = bytearray()

            while len(buf) < to_write:
                buf.extend(next(blocks))
            buf = buf[:to_write]

            f.write(buf)
            sha.update(buf)
            remaining -= to_write

    return sha.hexdigest()


def generate_compressible_jsonl(path: str, total_bytes: int, prng: Sha256CtrPrng, chunk_bytes: int = 1 << 20) -> str:
    """
    Write a very compressible, log-like JSONL file (newline-delimited JSON).

    Design choices to make it compressible:
    - Repeated keys and repeated structure per line
    - Mostly repeated categorical values (level/service/region/action/user_agent/template)
    - Small variable fields derived from PRNG (so still deterministic and non-constant)
    - Lots of repeated punctuation/whitespace patterns typical of logs

    Returns hex SHA-256 of the file for verification.
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)

    # Small vocabularies (high repetition => high compressibility)
    levels = ["DEBUG", "INFO", "WARN", "ERROR"]
    services = ["auth", "payments", "search", "profile", "content"]
    regions = ["eu-west-1", "eu-central-1", "us-east-1", "ap-southeast-1"]
    actions = ["login", "logout", "purchase", "query", "update", "delete", "refresh"]
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (X11; Linux x86_64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5)",
    ]
    templates = [
        "request completed",
        "cache hit",
        "cache miss",
        "rate limit exceeded",
        "db query ok",
        "db timeout",
        "upstream unavailable",
    ]

    # Helper to draw deterministic integers from PRNG bytes
    blocks = prng.stream()
    pool = bytearray()

    def get_u32() -> int:
        nonlocal pool
        while len(pool) < 4:
            pool.extend(next(blocks))
        v = int.from_bytes(pool[:4], "little", signed=False)
        del pool[:4]
        return v

    def pick(lst: list[str]) -> str:
        return lst[get_u32() % len(lst)]

    # Deterministic "timestamp" progression
    base_ts = 1700000000  # fixed epoch seconds anchor
    line_no = 0

    sha = hashlib.sha256()
    remaining = total_bytes

    with open(path, "wb") as f:
        # Write in chunks: build a chunk of many lines, then flush.
        while remaining > 0:
            buf = bytearray()
            target = min(remaining, chunk_bytes)

            while len(buf) < target:
                # Mild variability, but lots of repetition
                lvl = pick(levels)
                svc = pick(services)
                reg = pick(regions)
                act = pick(actions)
                ua = pick(user_agents)
                tmpl = pick(templates)

                # Some deterministic numeric fields
                latency_ms = 5 + (get_u32() % 500)          # 5..504
                status = [200, 200, 200, 201, 204, 400, 401, 403, 404, 429, 500, 503][get_u32() % 12]
                bytes_out = 200 + (get_u32() % 20000)       # 200..20199
                user_id = get_u32() % 10000                 # repeats often
                session = get_u32() % 1000000               # repeats sometimes

                ts = base_ts + line_no  # one-second increments per line (deterministic)

                # Fixed JSON shape (repeated keys/ordering)
                # Note: keep formatting stable for exact reproducibility.
                line = (
                    f'{{"ts":{ts},"level":"{lvl}","service":"{svc}","region":"{reg}",'
                    f'"action":"{act}","status":{status},"latency_ms":{latency_ms},'
                    f'"bytes_out":{bytes_out},"user_id":{user_id},"session":{session},'
                    f'"user_agent":"{ua}","msg":"{tmpl}"}}\n'
                ).encode("utf-8")

                # If adding the full line would exceed the exact target, truncate at the end.
                # Truncation is deterministic; file size is exact. (Last line may be partial.)
                space = target - len(buf)
                if space <= 0:
                    break
                if len(line) <= space:
                    buf.extend(line)
                else:
                    buf.extend(line[:space])
                    break

                line_no += 1

            f.write(buf)
            sha.update(buf)
            remaining -= len(buf)

    return sha.hexdigest()


# CLI
def main() -> int:
    parser = argparse.ArgumentParser(description="Deterministic input generator for gzip energy experiments.")
    parser.add_argument(
        "--type",
        choices=["compressible", "incompressible"],
        default="compressible",
        help="Dataset type: compressible JSONL (log-like) or incompressible random binary.",
    )
    parser.add_argument("--mb", type=int, required=True, help="Output size in MB (1 MB = 1,000,000 bytes).")
    parser.add_argument(
        "--seed",
        type=str,
        default="cs4575-energy-project-seed-v1",
        help="Seed string. Keep default for replication package unless you have a reason to change it.",
    )
    parser.add_argument(
        "--out",
        type=str,
        default=None,
        help="Output file path. If omitted, a sensible default under data/ is used.",
    )

    args = parser.parse_args()

    if args.mb <= 0:
        raise SystemExit("--mb must be > 0")

    total_bytes = args.mb * 1_000_000  # explicit MB definition for replication clarity

    out = args.out
    if out is None:
        if args.type == "compressible":
            out = os.path.join("data", f"input_compressible_{args.mb}MB.jsonl")
        else:
            out = os.path.join("data", f"input_incompressible_{args.mb}MB.bin")

    prng = Sha256CtrPrng(seed=_seed_to_bytes(args.seed), counter=0)

    if args.type == "compressible":
        digest = generate_compressible_jsonl(out, total_bytes, prng)
    else:
        digest = generate_incompressible(out, total_bytes, prng)

    print(f"Wrote: {out}")
    print(f"Size:  {total_bytes} bytes")
    print(f"SHA256:{digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())