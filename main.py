first_name = "Lukasz"
last_name = "Baran"
full_name1 = first_name + " " + last_name
print("\nfull_name1: ")
print(full_name1)

full_name2 = f"{first_name} {last_name}"
print("\nfull_name2: ")
print(full_name2)

print(f"\nHello, {full_name2.title()}")
message = f"\nHow You doin' {full_name2}?"  # Apostrophe ' inside " " - no problems.
print(message)

test = "  hhjjdd  "
print(test)
# Way to delete blank spaces
test2 = test.lstrip()
test2 = test2.rstrip()
print(test2)

# Better way to delete blank spaces
test3 = test.strip()
print(test3)
