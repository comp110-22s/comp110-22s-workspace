"""Demonstrations of dictionary capabilities."""

# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()


# Set a key value pairing in  the dictionary

schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150
schools["UNCG"] = 1000
# Print the dictionary
print(schools)


# Access a value by its key -- "lookup"
print(f"Unc has {schools['UNC']} students")

# REmove a key-value pair from a directory
# by its key
schools.pop("Duke")

# Test for existence of a key
is_duke_present = bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

# Update/Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# E,pty dictionary literal
schools = {} # Same as dict()
print(schools)

# Alternatively, intiialize key-value pairs
schools = {"UNC": 19400, 
"Dukie": 6717, 
"NCSU": 26150}
print(schools)

# print(schools["UNCC"])

# Example looping over the keys of a dict
# for key in schools:
#     print(f"Key: {key} -> Value: {schools[key]}")

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")