from pathlib import Path
path=Path('learning_python.txt')
contents=path.read_text().replace('Python', 'C')
print(contents)