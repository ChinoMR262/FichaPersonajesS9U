
import os

filename = r"c:\Users\Chino\Desktop\files\S9U Helios Engine Data v8.html"
js_filename = r"c:\Users\Chino\Desktop\files\helios_data.js"

# Coordinates
BODY_LINE = 1877
SCRIPT_START_LINE = 2706
DATA_START_LINE = 2812
DATA_END_LINE = 3472
SCROLL_FIX_START = 6103
SCROLL_FIX_END = 6107

try:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 1. Extract Data
    # Python list matches 0-based index, line numbers are 1-based.
    # Data lines to extract: 2812 to 3472 -> indices 2811 to 3472 (exclusive? No, inclusive of 3472)
    # lines[2811] is line 2812. lines[3472-1] is line 3472.
    # range(2811, 3472) -> 2811 to 3471. We want up to 3472. So range(2811, 3472).
    # verify line 3472 is };
    
    extracted_lines = lines[DATA_START_LINE-1 : DATA_END_LINE]
    
    with open(js_filename, 'w', encoding='utf-8') as js_file:
        js_file.writelines(extracted_lines)
    
    print(f"Created {js_filename} with {len(extracted_lines)} lines.")

    # 2. Modify HTML
    new_html_lines = []
    
    # - Up to body
    new_html_lines.extend(lines[0 : BODY_LINE]) # 0 to 1876 (lines 1 to 1877)
    
    # - Insert scroll fix
    new_html_lines.append("  <script>if('scrollRestoration' in history){history.scrollRestoration='manual';}window.scrollTo(0,0);</script>\n")
    
    # - Up to script start
    new_html_lines.extend(lines[BODY_LINE : SCRIPT_START_LINE-1]) # 1877 to 2704 (lines 1878 to 2705)
    
    # - Insert JS script tag BEFORE the main script
    new_html_lines.append('  <script src="helios_data.js"></script>\n')
    
    # - Main script start up to data block
    new_html_lines.extend(lines[SCRIPT_START_LINE-1 : DATA_START_LINE-1]) # 2705 to 2810 (lines 2706 to 2811)
    
    # - SKIP data block (2812 to 3472)
    # Next line to include is 3473 (index 3472)
    
    # - From end of data block to scroll fix in onload (6103)
    new_html_lines.extend(lines[DATA_END_LINE : SCROLL_FIX_START-1]) # 3472 to 6102 (lines 3473 to 6102)
    
    # - SKIP scroll fix lines (6103 to 6107) -> lines[6102] to lines[6106]
    # Next line is 6108 (index 6107)
    
    new_html_lines.extend(lines[SCROLL_FIX_END:]) # 6107... (lines 6108...)

    # Write back
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(new_html_lines)
        
    print("HTML file updated successfully.")

except Exception as e:
    print(f"Error: {e}")
