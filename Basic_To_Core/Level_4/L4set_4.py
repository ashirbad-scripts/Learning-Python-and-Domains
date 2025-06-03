# Create a list of dictionaries where each dictionary has name and age.
people = [
    {"name":"John", "age": 25},
    {"name":"alice", "age": 28},
    {"name":"kylke", "age": 54},
    {"name":"putin", "age": 51}
    ]
print(people)
# Access the age of the second dictionary in the list.
print(people[1]["age"])

# Create a dictionary where the value is a list of marks in 
# 3 subjects.
student = {"mark" : [24, 52, 45]}
print(student)
# Add a new mark to the list inside the dictionary.
student["mark"].append(92)
print(student)
# Remove mark from list
student["mark"].remove(92)
print(student)


# Create a list of tuples representing coordinates (x, y).
coordinates = [(0,0), (1,2), (3,4)]
print("Coordinates are: ",coordinates)
# Access the y-coordinate of the third tuple.
print("y-coordinate of the third tuple: ",coordinates[2][1])


# Create a dictionary that contains another dictionary as value.
profile = {
    "user" : {
        "name" : "dave",
        "age" : 25
    }
}
print(profile)

# Access a nested value from the inner dictionary.
print(profile["user"]["age"])
# Update a value inside a nested dictionary.

profile["user"]["name"] = "alice"
print(profile)


#  Loop through a list of dictionaries and print each person's name.
peoples = [
    {"name":"John", "age": 25},
    {"name":"alice", "age": 28},
    {"name":"kylke", "age": 54},
    {"name":"putin", "age": 51}
    ]
for eachIndex in peoples:
    print(eachIndex["name"])  
    # cuz eachPerson holds each dictionary, so we have to 
    # access name from each person not peoples
 
