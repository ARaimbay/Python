from pathlib import Path
import json

fav_number=input("What is your favourite number? ")

path=Path('fav_number.json')
contents=json.dumps(fav_number)
path.write_text(contents)

print(f"We'll remember your favourite number {fav_number}")