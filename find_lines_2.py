
filename = r"c:\Users\Chino\Desktop\files\S9U Helios Engine Data v8.html"
targets = [
    "<body",
    "const VILLAIN_PRESETS ="
]

try:
    with open(filename, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            for target in targets:
                if target in line:
                    print(f"Found '{target}' at line {i}")
except Exception as e:
    print(f"Error: {e}")
