import sys
import time
import json
import orjson
import gc

def iter_json_array_objects(filename, chunk_size_mb=8):
    chunk_size = chunk_size_mb * 1024 * 1024
    in_string, escape, brace_depth, collecting = False, False, 0, False
    obj_buffer = bytearray()

    with open(filename, 'rb') as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk: break
            for b in chunk:
                if not collecting:
                    if b == ord('{'):
                        collecting, brace_depth, obj_buffer = True, 1, bytearray([b])
                    continue
                obj_buffer.append(b)
                if in_string:
                    if escape: escape = False
                    elif b == ord('\\'): escape = True
                    elif b == ord('"'): in_string = False
                    continue
                if b == ord('"'): in_string = True
                elif b == ord('{'): brace_depth += 1
                elif b == ord('}'):
                    brace_depth -= 1
                    if brace_depth == 0:
                        yield bytes(obj_buffer)
                        collecting = False
                        obj_buffer = bytearray()

def run_benchmark(lib_name, filename):
    print(f"Starting benchmark for: {lib_name}")
    count = 0
    start = time.time()

    for obj_bytes in iter_json_array_objects(filename):
        if lib_name == "json":
            _ = json.loads(obj_bytes.decode('utf-8'))
        else:
            _ = orjson.loads(obj_bytes)
        count += 1

    end = time.time()
    print(f"Finished {lib_name}: {count} objects in {end-start:.2f}s")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python benchmark_streaming.py [json|orjson]")
        sys.exit(1)

    library = sys.argv[1].lower()
    run_benchmark(library, 'large_data.json')