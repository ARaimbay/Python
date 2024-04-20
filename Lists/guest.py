guests=['danara', 'asylzada', 'gaukhar']
print(f"Please join thanksgiving dinner {guests[0].title()}!")
print(f"Please join christmas celebration dinner {guests[1].title()}!")
print(f"Please join birthday party celebration {guests[2].title()}!")

#removing person from the list at the end and show the person's name
edited_list_guests=guests.pop()
print(edited_list_guests.title())

#replacing person from the original list
guests=['danara', 'asylzada', 'gaukhar']
guests[2]='meka'
print(f"Please join our celebration {guests[0].title()}")
print(f"Please join our celebration {guests[1].title()}")
print(f"Please join our celebration {guests[2].title()}")

#found bigger table and adding person to the begining of the list, middle and append at the end
guests=['danara', 'asylzada', 'gaukhar']
guests.insert(0, 'meka')
guests.insert(2, 'peter')
guests.append('lola')
print(guests)
print(f"Please join our celebration {guests[0].title()}")
print(f"Please join our celebration {guests[1].title()}")
print(f"Please join our celebration {guests[2].title()}")
print(f"Please join our celebration {guests[3].title()}")
print(f"Please join our celebration {guests[4].title()}")
print(f"Please join our celebration {guests[5].title()}")

#now you can invite only 2 people to the dinner
guests=['danara', 'asylzada', 'gaukhar']
guests.insert(0, 'meka')
guests.insert(2, 'peter')
guests.append('lola')
print("\nI can invite only 2 people to the celebration")
new_list_guests=guests.pop()
print(f"I am sorry I can't invite {new_list_guests.title()} to the dinnner")
new_list_guests=guests.pop()
print(f"I am sorry I can't invite {new_list_guests.title()} to the dinnner")
new_list_guests=guests.pop()
print(f"I am sorry I can't invite {new_list_guests.title()} to the dinnner")
new_list_guests=guests.pop()
print(f"I am sorry I can't invite {new_list_guests.title()} to the dinnner")
print(f"{guests[0].title()} still invited to the celebration dinner")
print(f"{guests[1].title()} still invited to the celebration dinner")
del guests[0]
del guests[0]
print(guests[-1])