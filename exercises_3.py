
guests = ['Asia', 'Tomek', 'Marek', 'Gosia']

print(f"\n{guests[0]} zapraszam na obiad!")
print(f"\n{guests[1]} zapraszam na obiad!")
print(f"\n{guests[2]} zapraszam na obiad!")
print(f"\n{guests[3]} zapraszam na obiad!")
print(f"\n{guests[1]} nie moze przyjsc na obiad :(")

print('\n---------------------------')

guests[1]='Robert'

print(f"\n{guests[0]} zapraszam na obiad!")
print(f"\n{guests[1]} zapraszam na obiad!")
print(f"\n{guests[2]} zapraszam na obiad!")
print(f"\n{guests[3]} zapraszam na obiad!")

print('\n---------------------------')

guests.insert(0, 'Zosia')
guests.insert(3, 'Mirek')
guests.append('Zenek')

print(f"\n{guests[0]} zapraszam na obiad!")
print(f"\n{guests[1]} zapraszam na obiad!")
print(f"\n{guests[2]} zapraszam na obiad!")
print(f"\n{guests[3]} zapraszam na obiad!")
print(f"\n{guests[4]} zapraszam na obiad!")
print(f"\n{guests[5]} zapraszam na obiad!")
print(f"\n{guests[6]} zapraszam na obiad!")

print(f"\nNiestety moge zaprosic tylko dwie osoby :(")

print('\n---------------------------')

popped_guest = guests.pop(0)
print(f"\n{popped_guest} przepraszam, niestety nie moge Cie zaprosic na obiad :(")
popped_guest = guests.pop(0)
print(f"\n{popped_guest} przepraszam, niestety nie moge Cie zaprosic na obiad :(")
popped_guest = guests.pop(0)
print(f"\n{popped_guest} przepraszam, niestety nie moge Cie zaprosic na obiad :(")
popped_guest = guests.pop(0)
print(f"\n{popped_guest} przepraszam, niestety nie moge Cie zaprosic na obiad :(")
popped_guest = guests.pop(0)
print(f"\n{popped_guest} przepraszam, niestety nie moge Cie zaprosic na obiad :(")

print(f"\n{guests[0]} zapraszam na obiad!")
print(f"\n{guests[1]} zapraszam na obiad!\n")

del guests[0]
del guests[0]

print(guests)
