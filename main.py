first_name = "Lukasz"
last_name = "Baran"
full_name1 = first_name + " " + last_name
print("\nfull_name1: ")
print(full_name1)

full_name2 = f"{first_name} {last_name}"
print("\nfull_name2: ")
print(full_name2)

print(f"\nHello, {full_name2.title()}")

message = f"\nHow You doin' {full_name2}?"
print(message)

test = "  hhjjdd  "
print(test)
test = test.lstrip()
test = test.rstrip()
print(test)