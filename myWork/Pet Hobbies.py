# @TODO: Your code here
"""
Instructions
Create a dictionary to store the following:
Your pet's name
Your pet's age
A list of a few of your pet's hobbies
A dictionary of a few times you wake up during the week
Print out the following:
Your pet's name and age.
How many hobbies your pet has.
What your pet's favorite hobby is.
What time your pet wakes on one of the days of the week
"""
pet={
    "name":"Lachy",
    "age":2,
    "hobbies":[
        "run",
        "poop on turf",
        "bark at pool guy"
    ],
    "wakeuptimes":{
    "Weekdays":"5:30am",
    "Weekends":"5:30am"
    }
}
weeklyWakes={
    "Weekdays":"5:30am",
    "Weekends":"5:30am"
}
print( f" {pet['name']} is {pet['age']}" )
print(f" NUM OF HOBBIES {len(pet['hobbies'])}")
print(f" MY PET WAKES UP AT {pet['wakeuptimes']}")
