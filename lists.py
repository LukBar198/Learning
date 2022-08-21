
bicycles = ['aaa', 'bbb', 'ccc', 'ddd']
print(bicycles)

print(bicycles[2].title())

print(bicycles[-1])  # [-1] - last element of the list

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles2 = []  # creating new, blank list
motorcycles2.append('honda')
motorcycles2.append('yamaha')
motorcycles2.append('ducati')
motorcycles2.append('suzuki')
print(motorcycles2)

XXX = []
XXX.insert(0, 'CCC2')
XXX.insert(3, 'CCC3')
print(XXX)

# pusta lista - dodanie na jakakolwiek pozycje elementu powoduje dodanie elementu na pos. 0

del XXX[2]
print(XXX)
