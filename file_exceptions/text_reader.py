from pathlib import Path
def read_words(filename):
    try:
        contents=path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} doesn't exist")
    else:
        words=contents.split()
        print(words)
filenames=['cats.txt', 'dogs.txt', 'my_file.txt']
for filename in filenames:
    path=Path(filename)
    read_words(path)