from pathlib import Path
prompt="\nEnter your first_name and last_name: "
prompt += ("\nEnter 'quit' to end the program ") 
guest_name=""
while guest_name != 'quit':
    guest_name=input(prompt)
    if guest_name != 'quit':
        path=Path('guest.txt')
        path.write_text(guest_name)