import json
import uuid
import random
import os

def generate_json_file(filename, target_size_mb):
    target_bytes = target_size_mb * 1024 * 1024
    roles = ['admin', 'user', 'editor', 'guest', 'support']

    print(f"Generating {filename} ({target_size_mb} MB)...")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write('[\n')
        current_size = 0
        first_record = True
        record_count = 0

        while current_size < target_bytes:
            record = {
                "id": record_count,
                "uuid": str(uuid.uuid4()),
                "username": f"user_name_{record_count}",
                "email": f"contact_{record_count}@example-domain.com",
                "profile": {
                    "first_name": random.choice(['John', 'Jane', 'Alex', 'Max', 'Sarah']),
                    "last_name": random.choice(['Smith', 'Doe', 'Johnson', 'Brown', 'Lee']),
                    "bio": "This is a repeating string used to fill up space. " * 3,
                },
                "role": random.choice(roles),
                "is_active": random.choice([True, False]),
                "permissions": ["read", "write", "delete"] if record_count % 10 == 0 else ["read"],
                "created_at": "2023-10-27T10:00:00Z",
                "updated_at": "2024-01-15T14:30:22Z"
            }

            json_str = json.dumps(record, indent=2)
            if not first_record:
                f.write(',\n')
            f.write(json_str)
            first_record = False
            record_count += 1

            if record_count % 500 == 0:
                f.flush()
                current_size = os.path.getsize(filename)

        f.write('\n]')
    print(f"Finished! Total Records: {record_count}\n")

if __name__ == "__main__":
    # You can lower this to 500 or 1000 for faster testing
    generate_json_file('large_data.json', 5000)