counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

for county in counties:
    print(county)


counties_dict= {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict: 
    print(counties_dict[county])


for voters in counties_dict.values():
    print(voters)


for county in counties_dict: 
    print(counties_dict[county])


voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)


for county_dict in voting_data:
        for value in county_dict.values():
            print(value)

for county_dict in voting_data:
    print(county_dict['county'])




counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(f" {county} county has {voters} registered voters.")


candidate_votes = int(3345)
total_votes = int(23123)
message_to_candidate = (
        f"You receieved {candidate_votes} number of votes. "
        f"The total number of votes in the election was {total_votes}. "
        f"You receieved {candidate_votes / total_votes * 100:.2f}% of the total votes. ")
candidate_votes = 3345
total_votes = 23,123

print(message_to_candidate)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f" {county} county has {voters} registered voters.")

voting_data = ['' {"county": "Arapahoe", "registered_voters":  422829}, {"county": "Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for county, voters in voting_data.items():   
    print(f" {county} county has {voting_data} registered voters. ")