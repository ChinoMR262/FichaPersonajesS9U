
filename = r"c:\Users\Chino\Desktop\files\S9U Helios Engine Data v8.html"
targets = [
    "const ANIMALES =", 
    "const UNIVERSOS =", 
    "const RANGOS =", 
    "const RASGOS_CAT =", 
    "const VESTIMENTA_CAT =", 
    "const DESEOS =", 
    "const SALUDOS =",
    "window.onload",
    "window.scrollTo"
]

try:
    with open(filename, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f, 1):
            for target in targets:
                if target in line:
                    print(f"Found '{target}' at line {i}")
except Exception as e:
    print(f"Error: {e}")
