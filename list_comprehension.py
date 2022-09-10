numbers = [1,2,3,4,5,6,7]

#new_list = [new_item for item in list]

new_list = [n + 1 for n in numbers]
#print(new_list)


new_range = [n * 2 for n in range(1,5)]
#print(new_range)

#conditional list comprehension

#new_list = [new_item for item in list if test]

names = ['Alex', 'Beth', 'Eleanor', 'Caroline', 'Dave', 'Freddie']

short_names = [name for name in names if len(name) < 5]
#print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
#print(long_names)

#Dictionary comprehension
#new_dict = {new_key:new_value for (key, value) in dict.items() if test}

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Sartuday": 22, 
    "Sunday": 24
}

weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)