#!/usr/bin/env python3

import argparse
import json
import time
import os
from llama_cpp import Llama

N_CTX = 1024
MAX_TOKENS = 256
TEMPERATURE = 0.0
TOP_P = 1.0

PROMPT = "Explain quantization tradeoffs in LLMs in 6 bullet points."
SYSTEM_MSG = "You are a concise assistant."

N_THREADS = os.cpu_count()
N_GPU_LAYERS = 0


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    proc_start_ts = time.time()

    llm = Llama(
        model_path=args.model,
        n_ctx=N_CTX,
        n_threads=N_THREADS,
        n_gpu_layers=N_GPU_LAYERS,
        seed=args.seed,
        verbose=False,
    )

    model_loaded_ts = time.time()

    gen_start_ts = time.time()

    out = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": SYSTEM_MSG},
            {"role": "user", "content": PROMPT},
        ],
        temperature=TEMPERATURE,
        top_p=TOP_P,
        max_tokens=MAX_TOKENS,
    )

    gen_end_ts = time.time()

    text = ""
    try:
        text = out["choices"][0]["message"]["content"]
    except Exception:
        text = ""

    usage = out.get("usage", {})
    gen_tokens = usage.get("completion_tokens")

    if gen_tokens is None:
        gen_tokens = len(llm.tokenize(text.encode()))

    seconds = gen_end_ts - gen_start_ts
    tok_per_sec = gen_tokens / seconds if seconds > 0 else 0

    result = {
        "model": args.model,
        "seed": args.seed,
        "prompt": PROMPT,
        "system_message": SYSTEM_MSG,
        "n_ctx": N_CTX,
        "max_tokens": MAX_TOKENS,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "n_threads": N_THREADS,
        "n_gpu_layers": N_GPU_LAYERS,
        "generated_text": text,
        "gen_tokens": gen_tokens,
        "seconds": seconds,
        "tok_per_sec": tok_per_sec,
        "proc_start_ts": proc_start_ts,
        "model_loaded_ts": model_loaded_ts,
        "gen_start_ts": gen_start_ts,
        "gen_end_ts": gen_end_ts,
    }

    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"{gen_tokens} tokens in {seconds:.2f}s")


if __name__ == "__main__":
    main()
