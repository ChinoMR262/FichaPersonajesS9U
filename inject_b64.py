
import json
import os

html_path = r'c:\Users\Chino\Desktop\files\S9U Helios Engine Data v8.html'
json_path = r'c:\Users\Chino\Desktop\files\assets_b64.json'

with open(json_path, 'r', encoding='utf-8-sig') as f:
    b64_data = json.load(f)

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

for filename, b64_str in b64_data.items():
    # unexpected quirk: JSON keys might be filenames, HTML has 'assets/' prefix
    search_str = f"assets/{filename}"
    if search_str in html_content:
        print(f"Replacing {search_str}...")
        html_content = html_content.replace(search_str, b64_str)
    else:
        print(f"Warning: {search_str} not found in HTML.")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Injection complete.")
