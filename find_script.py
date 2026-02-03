
filename = r"c:\Users\Chino\Desktop\files\S9U Helios Engine Data v8.html"
target = "<script>"

try:
    with open(filename, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            if i > 1877 and target in line:
                print(f"Found '{target}' at line {i}")
                break
except Exception as e:
    print(f"Error: {e}")
