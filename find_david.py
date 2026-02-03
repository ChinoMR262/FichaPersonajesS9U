
with open('c:/Users/Chino/Desktop/files/S9U Helios Engine Data v8.html', 'r', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'David' in line or 'david' in line:
            print(f"Line {i+1}: {line.strip()[:200]}")
