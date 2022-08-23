
# Trwale sortowanie list

cars1 = ['bmw', 'audi', 'toyota', 'bubaru']
cars1.sort()
print(cars1)

cars2 = ['bmw', 'audi', 'toyota', 'bubaru']
cars2.sort(reverse=True)
print(cars2)

# Tymczasowe sortowanie list

cars = ['bmw', 'audi', 'toyota', 'bubaru']

print("\nOto lista poczatkowa:")
print(cars)

print("\nOto lista posortowana:")
print(sorted(cars))

print("\nOto ponownie lista poczatkowa:")
print(cars)

# Odwrocenie kolejnosci na liscie

cars3 = ['bmw', 'audi', 'toyota', 'bubaru']
print(f"\n{cars3}")

cars3.reverse()
print(f"\n{cars3}")

# okreslenie wielkosci listy

cars4 = ['bmw', 'audi', 'toyota', 'bubaru']
print(f"\n{len(cars4)}")
