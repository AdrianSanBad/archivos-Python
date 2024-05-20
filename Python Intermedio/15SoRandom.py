

import random
from functools import reduce

prefixes = ['Mystic', 'Golden', 'Dark', 'Shadow', 'Silver']
suffixes = ['storm', 'song', 'fire', 'blade', 'whisper']



def create_fantasy_name(list_1, list_2):
  return random.choice(list_1) + ' ' + random.choice(list_2)

def capitalize_suffix(name):
    return name.capitalize()

suficosCapitalizados=list(map(capitalize_suffix,suffixes))

random_names=[create_fantasy_name(prefixes,suficosCapitalizados) for i in range(10)]

def fire_name(name):
   return "Fire" in name 

def concat_names(acc,name):
    return acc + ', ' + name

filtered_names=list(filter(fire_name,random_names))

reducidos=list(reduce(concat_names,filtered_names))

def display_name_info():
    print("nombres random:")
    for name in random_names:
        print(name)
    print("nombres filtrados con fuego:")
    for name in filtered_names:
        print(name)
    print("nombres reducidos:")
    for name in reducidos:
        print(name)

display_name_info()
