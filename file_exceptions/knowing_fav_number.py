from pathlib import Path
import json

path=Path('fav_number.json')
contents=path.read_text()
fav_number=json.loads(contents)

print(f"I know your favourite number! It's {fav_number}")