"""
This is a funny word game. There will be blanks and you have to fill those blanks with relatable words.
"""
story="""
    This morning %s woke up feeling %s.It is going to be a %s day!
    Outside, a bunch of %ss were protesting to keep %s in stores.
    They began to %s to the rhythm of the %s, which made all the %ss very %s.
    Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s.
    %s woke up in the year %s, in a world where %ss ruled the world."""
 

print ("Eureka!!!!The game has started! ")
name= input("Enter your name first: ")


adj1= input("Enter an adjective: ")
adj2= input("Enter a second adjective: ")
adj3= input("Enter annother adjective: ")

verb1=input("Enter a verb: ")

noun1=input("Enter a noun: ")
noun2=input("Enter the second noun: ")

animal=input("Enter an animal: ")

food =input("Enter a food: ")
fruit=input("Enter a fruit: ")

superhero=input("Enter a superhero: ")
country = input("Enter a country: ")
dessert =  input("Enter a dessert: ")
year = input("Enter a year: ")


print  (story %(name,adj1,adj2,animal,food,verb1,noun1,fruit,adj3,name,superhero,name,country,name,dessert,name,year,noun2))
