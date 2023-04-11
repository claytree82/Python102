#!/bin/python3

#Importing
print("Importing is important:")

import sys #system functions and parameters

from datetime import datetime 
print(datetime.now())

from datetime import datetime as dt #importing with an alias
print(dt.now())


def new_line():
	print('\n')

new_line()

#Advanced Strings
print("Adcanced strings:")
my_name = "Clay"
print(my_name[0]) #First initial
print(my_name[-1]) #Last letter

sentence = "This is a sentence."

print(sentence[:4]) #first word
print(sentence[-9:-1]) #last word

print(sentence.split()) #split sentence by delimiter (space)

sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join)
print('\n'.join(sentence_split))


quoteception = "I said, 'give me all the money'"
print(quoteception)


quoteception = "I said, \"give me all the money\""
print(quoteception)

print("A" in "Apple")
letter = "a"
word = "Apple"
print(letter.lower() in word.lower()) #Improved - case insensitive

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower() in word_two.lower()))

too_much_space = "             hello            "
print(too_much_space.strip())

full_name = "ebron James"
print(full_name.replace("ebron", "Lebron"))
print(full_name.find("James"))

movie = "The Hangover"
print("My favorite movie is {}.".format(movie))

def favorite_book(title, author):
	fav = "My favorite book is \"{}\", which is written by {}.".format(title,author)
	return fav
	
print(favorite_book("Hunger Games","Lebron James"))

#Dictionaries
print("Dictionaries are keys and values:")
drinks = {"White Russian": 7, "Old Fashion" : 10, "Lemon Drop": 8, "Henny and Coke": 7} #drink is key price is value
print(drinks)

employees = {"Cyber": ["Bob", "Linda", "Tom"], "Finance": ["Gene", "Billy", "Peter"], "HR": ["Timmy", "Kenny", "Lois"]}
print(employees)

employees['Legal'] = ["Mr. Fond"] #add new key: value pair
print(employees)


employees.update({"Sales": ["Andie", "Ollie"]})
print(employees)

drinks['White Russian'] = 8
print(drinks)


print(drinks.get("White Russian"))
print(drinks.get("Martini"))
print(drinks["White Russian"])

#List and dictionaries
movies = ["The Hangover", "Step Brothers", "Dragon Ball Z", "Air"]
person = ["Clay", "Victoria", "Colin", "Ghost"]
combined = zip(movies, person)
movie_dictionary = {key: value for key, value in combined}

print(movie_dictionary)

#python3 -m http.server 80, hosts a web server where you can have a directory listing of everything in that folder

#python -m pyftpdlib -p 21 w, sets up ftp
