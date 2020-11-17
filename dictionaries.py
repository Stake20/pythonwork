
monthConversions = {
    "Jan": "January",       # Key value pairs
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversions["Mar"]) # calling a key in the dictionary
print(monthConversions.get("Luv", "Not a valid key"))      # specifying a default value if key is not found
monthConversions["Moz"] = "Mozembuary" # Adding a dict item
print(monthConversions)
print(monthConversions.keys()) # Get dict keys
print(monthConversions.items()) # Get dict items
del(monthConversions['Moz']) # Deleting an item in dict
'''monthConversions.pop('Jan') # Popping an item of the dict
print(monthConversions)'''
monthConversions.clear() # Clearing a dict
print(monthConversions)

person = dict(first_name='Sara', last_name='Lance')
print(person, type(person))

person2 = person.copy()
person2['Job'] = 'Captain Of The WaveRider'

print(person2, len(person2))

The_Legends_Of_Tommorow = [ # list of dict
    {'name': 'Sara Lance', 'Job': 'Captain Of The WaveRider'},
    {'name': 'Ray Palmer', 'Job': 'The Atom'},
    {'name': 'Jefferson Jackson', 'Job': 'FireStorm'}

]

print(The_Legends_Of_Tommorow)
print(The_Legends_Of_Tommorow[1])
print(The_Legends_Of_Tommorow[2]['Job'])