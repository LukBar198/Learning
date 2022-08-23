
places = ['Tokyo', 'Sydney', 'Berlin', 'Pekin', 'New York']

print(f"\nLista pierwotna:")
print(places)

print(f"\nPosortowana tymczasowo lista:")
print(sorted(places))

print(f"\nLista pierwotna raz jeszcze:")
print(places)

print(f"\nLista posortowana odwrotnie:")
print(sorted(places, reverse=True))

print(f"\nLista pierwotna raz jeszcze:")
print(places)

places.reverse()
print(f"\nLista odwrocona")
print(places)

places.reverse()
print(f"\nLista drugi raz odwrocona")
print(places)

places.sort()
print(places)

places.sort(reverse=True)
print(places)
