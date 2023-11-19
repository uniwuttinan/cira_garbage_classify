import os
import json

OUTPUT_JSON_DIR = "C:/Users/vmuser/Desktop/cira_garbage_classify/output_data"

data = payload
img_name = payload["ImageSlide"]["img_name"]

os.makedirs(OUTPUT_JSON_DIR, exist_ok=True)

save_path = os.path.join(OUTPUT_JSON_DIR, f"{img_name}.json")

with open(save_path, 'w') as f:
    json_str = json.dumps(data)
    f.write(json_str)
    print(f"Saved {img_name} to {save_path}")