import requests

# Make a request to the API
response = requests.get('http://api.open-notify.org/astros.json')

# Parse the JSON response
data = response.json()
Craft1 = []
Craft2 = []

# Get the number of people in space
number_of_people = data['number']
print(f"Number of people in space: {number_of_people}","\n")
#print("\n This is the Dictionary: \n" + str(data) + "\n")    

for person in data['people']:
    match person['craft']:
        case "ISS":
            Craft1.append(person['name'])
        case "Tiangong":
            Craft2.append(person['name'])
    print(f"Name: {person['name']}, Craft: {person['craft']}")

print('\n',"These people are in Craft ISS: ")
print('\n'.join(Craft1))

print('\n',"These other people are in Craft Tiangong: ")
print('\n'.join(Craft2))