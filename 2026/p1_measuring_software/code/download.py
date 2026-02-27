from huggingface_hub import hf_hub_download
import os

REPO_ID = "bartowski/Meta-Llama-3.1-8B-Instruct-GGUF"

# Download to Desktop
LOCAL_DIR = os.path.expanduser("~/Desktop/llm-energy-benchmark/models")
os.makedirs(LOCAL_DIR, exist_ok=True)

FILES = [
    "Meta-Llama-3.1-8B-Instruct-Q2_K.gguf",
    "Meta-Llama-3.1-8B-Instruct-Q3_K_M.gguf",
    "Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf",
    "Meta-Llama-3.1-8B-Instruct-Q5_K_M.gguf",
    "Meta-Llama-3.1-8B-Instruct-Q6_K.gguf",
]

for f in FILES:
    print(f"Downloading {f}...")
    p = hf_hub_download(
        repo_id=REPO_ID,
        filename=f,
        local_dir=LOCAL_DIR
    )
    print(f"  Saved to: {p}")

print("\nAll models downloaded to:")
print(LOCAL_DIR)
