# Turn the emoji scheme into the one that vscode uses
import json

# Read the gitmojis json file
with open("gitmojis.json") as f:
    gitmojis = json.load(f)

vscode_json = []
for emoji in gitmojis['gitmojis']:
    o = {"emoji": emoji["emoji"], "colon": emoji["code"], "text": emoji["description"]}
    vscode_json.append(o)

print(json.dumps(vscode_json, indent=4))
