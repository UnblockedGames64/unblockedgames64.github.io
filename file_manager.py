import os
import shutil
import requests
from PIL import Image, ImageEnhance
import io
import re
from string import Template

TEMPLATE_FILE = "template.txt"
GAMES_FOLDER = "games"
GAMES_SRC = "games-src"
filelocation = ""

INJECT_SCRIPT = """<script>function _0x4e83(){const _0x2a5b30=['136BUpMRl','includes','16980ldAPVE','Whoa\x20buddy,\x20not\x20so\x20fast.\x20You\x20gotta\x20open\x20this\x20file\x20from\x20our\x20website.','top','This\x20page\x20is\x20embedded\x20inside\x20an\x20iframe.','836731kBUkdU','218816oaaAxC','497875oRNmyR','log','self','531kGOuND','/games/','49526BBvgfA','1509120GcfuCq','6344CzRYer','referrer'];_0x4e83=function(){return _0x2a5b30;};return _0x4e83();}function _0x1777(_0x1dce8e,_0x3e601f){const _0x4e83f2=_0x4e83();return _0x1777=function(_0x177779,_0x5a8d47){_0x177779=_0x177779-0x18b;let _0x219c4a=_0x4e83f2[_0x177779];return _0x219c4a;},_0x1777(_0x1dce8e,_0x3e601f);}(function(_0x1b89ff,_0x48b135){const _0x1e0241=_0x1777,_0x289c3b=_0x1b89ff();while(!![]){try{const _0x5914e4=-parseInt(_0x1e0241(0x18d))/0x1+-parseInt(_0x1e0241(0x193))/0x2+parseInt(_0x1e0241(0x199))/0x3*(parseInt(_0x1e0241(0x197))/0x4)+parseInt(_0x1e0241(0x18e))/0x5+parseInt(_0x1e0241(0x194))/0x6+-parseInt(_0x1e0241(0x18c))/0x7+-parseInt(_0x1e0241(0x195))/0x8*(parseInt(_0x1e0241(0x191))/0x9);if(_0x5914e4===_0x48b135)break;else _0x289c3b['push'](_0x289c3b['shift']());}catch(_0x323948){_0x289c3b['push'](_0x289c3b['shift']());}}}(_0x4e83,0x20a04),(function(){const _0x17b4fc=_0x1777,_0x16f1af=window[_0x17b4fc(0x190)]!==window[_0x17b4fc(0x19b)];_0x16f1af&&String(document[_0x17b4fc(0x196)])[_0x17b4fc(0x198)](_0x17b4fc(0x192))?console[_0x17b4fc(0x18f)](_0x17b4fc(0x18b)):(alert(_0x17b4fc(0x19a)),window['close']());}()));</script>"""

def replace_in_all_html(find_text, replace_text, root_dir="."):
    """
    Replaces all occurrences of 'find_text' with 'replace_text'
    in every HTML file in the root directory and /games/ folder.

    :param find_text: The text or substring to find.
    :param replace_text: The text to replace it with.
    :param root_dir: Root directory (default is current).
    """
    html_files = []

    # Root-level HTML files
    for file in os.listdir(root_dir):
        if file.endswith(".html") and os.path.isfile(os.path.join(root_dir, file)):
            html_files.append(os.path.join(root_dir, file))

    # /games/ folder HTML files
    games_folder = os.path.join(root_dir, "games")
    if os.path.exists(games_folder) and os.path.isdir(games_folder):
        for file in os.listdir(games_folder):
            if file.endswith(".html") and os.path.isfile(os.path.join(games_folder, file)):
                html_files.append(os.path.join(games_folder, file))

    # Loop through files and replace text
    for file_path in html_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        if find_text in content:
            new_content = content.replace(find_text, replace_text)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"✅ Replaced text in {file_path}")
        else:
            print(f"⚠️ No matches found in {file_path}")

def insert_text_in_searchresults(text_to_insert, root_dir="."):
    """
    Loops through all HTML files in root and /games/ folder, 
    inserts text at the end of #searchresults element.
    
    :param text_to_insert: The HTML/text to insert.
    :param root_dir: Root directory to start searching.
    """
    # Collect all HTML files in root and /games/
    html_files = []

    # Root HTML files
    for file in os.listdir(root_dir):
        if file.endswith(".html") and os.path.isfile(os.path.join(root_dir, file)):
            html_files.append(os.path.join(root_dir, file))

    # /games/ folder HTML files
    games_folder = os.path.join(root_dir, "games")
    if os.path.exists(games_folder) and os.path.isdir(games_folder):
        for file in os.listdir(games_folder):
            if file.endswith(".html") and os.path.isfile(os.path.join(games_folder, file)):
                html_files.append(os.path.join(games_folder, file))

    # Loop through files and insert text
    for file_path in html_files:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Regex to find the end of #searchresults div
        pattern = r'(<div\s+id="searchresults"[^>]*>)(.*?)</div>'
        
        def replacer(match):
            original_content = match.group(2)
            return f'{match.group(1)}{original_content}{text_to_insert}</div>'

        new_content, count = re.subn(pattern, replacer, content, flags=re.DOTALL)
        
        if count > 0:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Inserted text in {file_path}")
        else:
            print(f"No #searchresults found in {file_path}")

def download_and_edit_image(url, save_path):
    global filelocation

    try:
        # Get image bytes from the URL
        response = requests.get(url)
        response.raise_for_status()

        # Open image with Pillow
        image = Image.open(io.BytesIO(response.content))

        # --- Simple edits to make it unique ---
        # Resize slightly
        image = image.resize((image.width - 5, image.height - 5))

        # Crop a tiny bit from each side
        image = image.crop((2, 2, image.width - 2, image.height - 2))

        # Adjust brightness/contrast slightly
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(1.05)  # +5% brightness
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(1.05)  # +5% contrast

        # Ensure folder exists
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        
        # Save as JPEG or PNG
        image.save(save_path, format="PNG")

        print(f"✅ Image downloaded, edited, and saved to {save_path}")

    except Exception as e:
        print(f"❌ Failed to download or edit image: {e}")
        download_and_edit_image(input("Try a different url gng: "), save_path)

def replace_index_html(name_input):
    global filelocation
    # Get the path (copied from Ctrl+Shift+C)
    new_html_path = input("Enter full path to replacement HTML file: ").strip().strip('"')

    if not os.path.exists(new_html_path):
        print(f"Error: file does not exist at {new_html_path}")
        return

    # Ask user for the game name
    file_name = name_input.lower().replace(" ", "-") + ".html"

    # Determine parent folder
    parent_folder = os.path.dirname(new_html_path)
    folder_name = os.path.basename(parent_folder)

    # If top-level file (just in Downloads or no folder)
    if folder_name.lower() in ["downloads", ""] or not os.path.isdir(parent_folder):
        target_folder = GAMES_SRC
    else:
        target_folder = os.path.join(GAMES_SRC, folder_name)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

    target_path = os.path.join(target_folder, file_name)

    # Read HTML
    with open(new_html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Inject script after first <head>
    if "<head>" in html_content:
        html_content = html_content.replace("<head>", "<head>\n" + INJECT_SCRIPT, 1)
    else:
        print("Warning: No <head> tag found, appending script at top.")
        html_content = INJECT_SCRIPT + "\n" + html_content

    # Write to games-src
    os.makedirs(target_folder, exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    filelocation = target_path

    print(f"Injected script and placed HTML at {target_path}")
    print(f"File name variable is: {file_name}")

def do_it_but_not(name_input):
    global filelocation
    # Get the path (copied from Ctrl+Shift+C)
    new_html_path = input("Enter full path to replacement HTML file: ").strip().strip('"')

    if not os.path.exists(new_html_path):
        print(f"Error: file does not exist at {new_html_path}")
        return

    # Ask user for the game name
    file_name = name_input.lower().replace(" ", "-") + ".html"

    # Determine parent folder
    parent_folder = os.path.dirname(new_html_path)
    folder_name = os.path.basename(parent_folder)

    # If top-level file (just in Downloads or no folder)
    if folder_name.lower() in ["games-src", ""] or not os.path.isdir(parent_folder):
        target_folder = GAMES_SRC
    else:
        target_folder = os.path.join(GAMES_SRC, folder_name)
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

    target_path = os.path.join(target_folder, file_name)

    # Read HTML
    with open(new_html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Inject script after first <head>
    if "<head>" in html_content:
        html_content = html_content.replace("<head>", "<head>\n" + INJECT_SCRIPT, 1)
    else:
        print("Warning: No <head> tag found, appending script at top.")
        html_content = INJECT_SCRIPT + "\n" + html_content

    filelocation = target_path

    print(f"Injected script and placed HTML at {target_path}")
    print(f"File name variable is: {file_name}")

import os
import re

def add_game_to_js(game_obj, js_file="scripts/injectgames.js"):
    if not os.path.exists(js_file):
        raise FileNotFoundError(f"{js_file} not found!")

    with open(js_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Match first occurrence of var/let/const games = [ ... ];
    pattern = re.compile(r"(?:const|let|var)\s+games\s*=\s*\[(.*?)\]\s*;", re.DOTALL)
    m = pattern.search(content)
    if not m:
        raise ValueError("Couldn't find the games array (const/let/var games = [ ... ];) in the file")

    array_body = m.group(1)

    # Detect next id (use max to be robust if items are not strictly ordered)
    ids = re.findall(r"id\s*:\s*(\d+)", array_body)
    next_id = max(map(int, ids)) + 1 if ids else 0

    # Try to preserve indentation of array entries (fall back to two spaces)
    indent_match = re.search(r"\n([ \t]+)\S", array_body)
    indent = indent_match.group(1) if indent_match else "  "

    # Escape backticks and backslashes inside description so JS template literal won't break
    desc = game_obj.get("desc", "")
    desc_escaped = desc.replace("\\", "\\\\").replace("`", "\\`")

    new_entry = (
        f"\n{indent}{{\n"
        f"{indent}  id: {next_id},\n"
        f"{indent}  name: \"{game_obj['name']}\",\n"
        f"{indent}  file: \"{game_obj['file']}\",\n"
        f"{indent}  icon: \"{game_obj['icon']}\",\n"
        f"{indent}  banner: \"{game_obj['banner']}\",\n"
        f"{indent}  desc: `{desc_escaped}`,\n"
        f"{indent}  genre: \"{game_obj['genre']}\"\n"
        f"{indent}}},"
    )

    # Insert the new entry right before the closing ']' of the matched array
    new_array_body = array_body.rstrip() + new_entry.replace("\n", " ") + "\n" + ","
    new_content = content[:m.start(1)] + new_array_body + content[m.end(1):]

    with open(js_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ Added {game_obj['name']} (id={next_id}) to {js_file}")


def multiline_input(prompt=""):
    print(prompt)
    lines = []
    while True:
        line = input()
        if line.strip().lower() == "end":  # type 'end' on a new line to finish
            break
        lines.append(line)
    return "\n".join(lines)

def rename_file(filepath, new_name):

    # Ensure the file exists
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    # Extract directory and old extension
    directory = os.path.dirname(filepath)
    old_extension = os.path.splitext(filepath)[1]

    # Add extension if new_name doesn’t include one
    if not os.path.splitext(new_name)[1]:
        new_name += old_extension

    # Build full new file path
    new_path = os.path.join(directory, new_name)

    # Rename the file
    os.rename(filepath, new_path)
    print(f"✅ File renamed to: {new_path}")

def rewrite_game():
    # Ask user for filename
    name = input("Game name: ")
    
    do_it_but_not(name)

    filename = name.lower().replace(" ", "-")
    genre = input("Genre: ")
    desc = multiline_input("Description: ")
    youtubeembed = input("Youtube tutorial: ")
    filepathe = input("input file path: ")

    download_and_edit_image(input("Screenshot 1:"), "assets/screenshots/" + filename + "1.png")
    download_and_edit_image(input("Screenshot 2:"), "assets/screenshots/" + filename + "2.png")
    download_and_edit_image(input("Banner URL:"), "assets/banners/" + filename + ".png")

    # Ensure games folder exists
    if not os.path.exists(GAMES_FOLDER):
        os.makedirs(GAMES_FOLDER)

    # Read template
    if not os.path.exists(TEMPLATE_FILE):
        print(f"Error: {TEMPLATE_FILE} not found.")
        return

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Use string.Template instead of str.format
    template = Template(template_content)
    new_content = template.safe_substitute(
        name=name,
        filename=filename,
        genre=genre,
        desc=desc,
        youtubeembed=youtubeembed,
        filelocation=filelocation
    )

    # Full path inside /games
    filepath = os.path.join(GAMES_FOLDER, filename + ".html")

    # Write new file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Created {filepath} using template.")

    rename_file(filepathe, filename + ".html")

def create_game():
    # Ask user for filename
    name = input("Game name: ")
    replace_index_html(name)
    filename = name.lower().replace(" ", "-")
    genre = input("Genre:")
    desc = multiline_input("Description:")
    youtubeembed = input("Youtube tutorial:")

    download_and_edit_image(input("Icon:"), "assets/game-icons/" + filename + ".png")
    download_and_edit_image(input("Screenshot 1:"), "assets/screenshots/" + filename + "1.png")
    download_and_edit_image(input("Screenshot 2:"), "assets/screenshots/" + filename + "2.png")
    download_and_edit_image(input("Banner URL:"), "assets/banners/" + filename + ".png")

    game_obj = {
        "name": name,
        "file": "/games/" + filename,
        "icon": "/assets/game-icons/" + filename + ".png",
        "banner": "/assets/banners/" + filename + ".png",
        "desc": desc,
        "genre": genre,
        "youtube": youtubeembed
    }

    add_game_to_js(game_obj)

    # Ensure games folder exists
    if not os.path.exists(GAMES_FOLDER):
        os.makedirs(GAMES_FOLDER)

    # Read template
    if not os.path.exists(TEMPLATE_FILE):
        print(f"Error: {TEMPLATE_FILE} not found.")
        return

    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template_content = f.read()

    # Use string.Template instead of str.format
    template = Template(template_content)
    new_content = template.safe_substitute(
        name=name,
        filename=filename,
        genre=genre,
        desc=desc,
        youtubeembed=youtubeembed,
        filelocation=filelocation
    )

    # Full path inside /games
    filepath = os.path.join(GAMES_FOLDER, filename + ".html")

    # Write new file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Created {filepath} using template.")


def delete_file():
    filename = input("Enter file name to delete: ")
    filepath = os.path.join(GAMES_FOLDER, filename)

    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"Deleted {filepath}")
    else:
        print("File not found in games folder.")

def main():
    replace_in_all_html('''.netlify.app''','''.github.io''')

if __name__ == "__main__":
    main()
