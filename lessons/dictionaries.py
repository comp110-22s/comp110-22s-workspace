"""This is how you can the capabilities of the dictionary data type."""

# declaring its type and setting it up as an empty dictionary:
schools: dict[str, int]
schools = dict()

# Set a key value:
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

print(schools)

# Access a value by its key/"looking up" a value:
print(f"UNC has {schools['UNC']} students")

# Removing a key value pair by its key:
schools.pop("Duke")

# Testing for the existence of a key:
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Reassigning a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)


# More practice:
# print(schools["UNCC"])

# Example looping over the keys of a dict
# for key in schools:
#     print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")