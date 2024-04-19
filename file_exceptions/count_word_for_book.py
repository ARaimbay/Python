from pathlib import Path
path=Path('my_life.txt')
contents=path.read_text()
lines=contents.lower().count('the')
print(lines)