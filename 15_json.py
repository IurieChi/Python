#JSON format

import json

#using dictionary createa a dictionary and write it to json file 

def craete_dictionary(name, title, price, scariness):
    return {'name': name, 'title': title, 'price': price, 'scariness': scariness}

def write_to_json(file, dictionary_data):
    with open(file, 'w') as write:
        json.dumps(dictionary_data, write)


#read JASON file with json library
def display_json(name):
    with open(name) as f:
        content = json.load(f)
        print(content)

#read specific key from file 
def disply_key_jason(name, key):
    with open(name) as f:
        content = json.load(f)
        print("Welcome ", content[key])

# display_json('monster.json')
# disply_key_jason('monster.json','monsterName')


monster_one = craete_dictionary('Filo', 'Baker by Day, Techie by Night',29, 3)
monster_two = craete_dictionary('Timber', 'Database Expert', 19, 2)
monster_three = craete_dictionary('Blade', 'Monster APPetite', 29, 5)
write_to_json('Files/monsters.json',[monster_one, monster_two, monster_three])