from pathlib import Path
prompt="\nTell me your name: "
prompt += ("\nEnter 'q' to end the program ")
active=True
while active:
    guest_name = input(prompt)
    if guest_name == 'q':
        active=False
    else:
        path=Path('guests_book.txt')
        path.write_text(guest_name)