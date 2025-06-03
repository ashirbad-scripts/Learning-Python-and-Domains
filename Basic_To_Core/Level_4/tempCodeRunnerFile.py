#  Loop through a list of dictionaries and print each person's name.
peoples = [
    {"name":"John", "age": 25},
    {"name":"alice", "age": 28},
    {"name":"kylke", "age": 54},
    {"name":"putin", "age": 51}
    ]
for eachPerson in peoples:
    print(eachPerson["name"])  
    # cuz eachPerson holds each dictionary, so we have to 
    # access name from each person not peoples
 
