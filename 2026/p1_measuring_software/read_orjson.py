import orjson
import gc
import time

def main():
    start_time = time.time()
    with open("large_data.json", "rb") as f:
        data = orjson.loads(f.read())
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
    gc.collect()