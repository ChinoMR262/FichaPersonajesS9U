
import os

html_path = r'c:\Users\Chino\Desktop\files\S9U Helios Engine Data v8.html'
search_term = "radicks"
try:
    with open(html_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if search_term in line:
                print(f"Found '{search_term}' on line {i+1}")
                # Print a small snippet if possible, but be careful with length
                index = line.find(search_term)
                start = max(0, index - 50)
                end = min(len(line), index + 100)
                print(f"Context: ...{line[start:end].encode('ascii', 'ignore').decode('ascii')}...")
                break
except Exception as e:
    print(f"Error: {e}")
