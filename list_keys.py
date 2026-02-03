
import json

json_path = r'c:\Users\Chino\Desktop\files\assets_b64.json'

try:
    with open(json_path, 'r', encoding='utf-8-sig') as f:
        data = json.load(f)
        print("Keys found in assets_b64.json:")
        for key in data.keys():
            print(key)
except Exception as e:
    print(f"Error reading JSON: {e}")
