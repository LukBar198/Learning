
magicians = ['zenek', 'martin', 'judasz']

for magician in magicians:
    print(f"\t{magician.title()} to byla wspaniala sztuczka!")
    print(f"\tNie moge sie doczekac twojej nastepnej sztuczki, {magician.title()}.\n")

print("Dziekuje wszystkim!")

#for value in range(1, 9):
   # print(value)

numbers =list(range(1,9))
print(numbers)

parzyste = list(range(2, 50, 2))
print(parzyste)

squares = []

for value in range(1,11):
    square = value**2
    squares.append(square)

print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))
