
import os

html_path = r'c:\Users\Chino\Desktop\files\S9U Helios Engine Data v8.html'
search_term = "anime_animal_dragon"

try:
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    index = content.find(search_term)
    if index != -1:
        start = max(0, index - 50)
        end = min(len(content), index + 100)
        print(f"Found '{search_term}' at index {index}")
        print(f"Context: ...{content[start:end].encode('ascii', 'ignore').decode('ascii')}...")
    else:
        print(f"'{search_term}' not found in file.")

except Exception as e:
    print(f"Error: {e}")
