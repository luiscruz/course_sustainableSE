# Energy Consumption of File Compression Across Programming Languages

## 1. Generate deterministic input files

### Requirements
- Python 3.9+ (any modern Python 3 should work)

### Generate a compressible dataset (JSONL, log-like)
From the repository root (`g22_code/`):

```bash
python data/generate_input.py --type compressible --mb 64
```

Default output:
* `data/input_compressible_64MB.jsonl`

### Generate an incompressible dataset (uniform random bytes)
```bash
python data/generate_input.py --type incompressible --mb 64
```

Default output:
* `data/input_incompressible_64MB.bin`

### Custom output path (optional)
```bash
python data/generate_input.py --type compressible --mb 256 --out data/myfile.jsonl
```

### Determinism / replication
The generator uses a fixed default seed, so for the same:
* `--type`
* `--mb`
* `--seed` (if provided)

… you will get the exact same bytes every time.

The script prints a SHA-256 hash of the generated file so you can verify your replication package.


## 2. Build and run the C++ implementation

### Requirements (Windows + MSYS2 UCRT64)

You need:
* `g++` (MinGW-w64 toolchain)
* `zlib` headers and library

If using MSYS2 UCRT64, install zlib once:
```bash
pacman -S --needed mingw-w64-ucrt-x86_64-zlib
```

### Compile
From the repository root (using the MSYS2 UCRT64 g++):
```bat
C:\msys64\ucrt64\bin\g++.exe -O2 -std=c++17 lang\cpp\zip.cpp -o lang\cpp\zip.exe -lz
```

If compilation succeeds, you will have:
* `lang/cpp/zip.exe`

### Run: compress
```bat
lang\cpp\zip.exe c data\input_compressible_64MB.jsonl data\out.gz
```

### Run: decompress
```bat
lang\cpp\zip.exe d data\out.gz data\roundtrip.jsonl
```

## 3. Test that compressible output is correct
Correctness is defined as:
1. **Round-trip integrity:**
   `decompress(compress(input)) == input` (byte-for-byte identical)

2. **Standards compatibility (recommended):**
   A reference gzip implementation can:

   * decompress your `.gz`
   * produce `.gz` files that your program can decompress


## A. Round-trip test (mandatory)
This verifies that the compressor and decompressor work together correctly.

### 1. Compress
```bat
lang\cpp\zip.exe c data\input_compressible_64MB.jsonl data\out.gz
```

### 2. Decompress
```bat
lang\cpp\zip.exe d data\out.gz data\roundtrip.jsonl
```

### 3. Compare hashes (must match exactly)
```bat
certutil -hashfile data\input_compressible_64MB.jsonl SHA256
certutil -hashfile data\roundtrip.jsonl SHA256
```

If the SHA256 values are identical, the implementation is correct.


## B. Cross-check using Python
Python’s built-in `gzip` module uses zlib and is standards-compliant. This is the simplest way to verify compatibility on Windows.


### Decompress the resulting `.gz` using Python
```bat
python -c "import gzip, shutil; shutil.copyfileobj(gzip.open('data/out.gz','rb'), open('data/python_roundtrip.jsonl','wb'))"
```

Compare hashes:
```bat
certutil -hashfile data\input_compressible_64MB.jsonl SHA256
certutil -hashfile data\python_roundtrip.jsonl SHA256
```

If hashes match, the compressor produces valid gzip output.


### Compress using Python, decompress using the implementation

```bat
python -c "import gzip, shutil; shutil.copyfileobj(open('data/input_compressible_64MB.jsonl','rb'), gzip.open('data/python_ref.gz','wb'))"
```

Now decompress with the implementation:

```bat
lang\cpp\zip.exe d data\python_ref.gz data\from_python.jsonl
```

Compare:

```bat
certutil -hashfile data\input_compressible_64MB.jsonl SHA256
certutil -hashfile data\from_python.jsonl SHA256
```

If the hashes match, the decompressor is compatible with standard gzip output.


## C. Cross-check using 7-Zip (GUI option)

If you have 7-Zip installed:

### 1. Decompress your `.gz`
* Right-click `data/out.gz`
* Choose **7-Zip → Extract Here**

### 2. Compare hashes
```bat
certutil -hashfile data\input_compressible_64MB.jsonl SHA256
certutil -hashfile data\extracted_filename.jsonl SHA256
```

If the hashes match, the `.gz` file is valid.

Additionally, you can also:

* Compress the input file using 7-Zip (gzip format)
* Decompress it with your program
* Compare hashes as above

## 4. Test that the incompressible output is correct

The methodology is exactly the same as for the compressible input. The only difference is that for a true incompressible file (uniform random bytes), the output size should be almost the same as input, or possibly slightly larger (gzip header + metadata overhead)

### Check file sizes
```bat
lang\cpp\zip.exe c data\input_incompressible_64MB.bin data\incomp.gz
lang\cpp\zip.exe d data\incomp.gz data\incomp_roundtrip.bin
certutil -hashfile data\input_incompressible_64MB.bin SHA256
certutil -hashfile data\incomp_roundtrip.bin SHA256

dir data\input_incompressible_64MB.bin
dir data\incomp.gz
```

Expected behavior is for the .gz size to be approximately the same as the original size, sometimes slightly larger (~0.1–1% overhead).