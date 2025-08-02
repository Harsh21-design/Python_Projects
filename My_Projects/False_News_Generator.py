#Importing Random Module
import random

#Creating News(Headline) Words
subject_list=[
    "Elon Musk",
    "A Bus Conductor from Bombay",
    "Shahrukh Khan",
    "Virat Kohli",
    "A Indore Cat",
    "Nirmala Sithraman",
    "A Group of Monkeys"
]

action_list = [
    "Sings",
    "Eats Momos",
    "Move by train",
    "launces",
    "Dances ",
    "fights"
]

places_or_things_list = [
    "at Rajwada",
    "in Scary Village",
    "at Moon",
    "in the deep Sea",
    "for hot cup of Chai",
    "for Plate of Poha Jalebi"
]

#Start the News/Headline Generation Loop
while True:
    subject = random.choice(subject_list)
    action = random.choice(action_list)
    place_or_thing = random.choice(places_or_things_list)

    print( 5*"#"," FunDay NewsPaper ",5*"#")
    headline = f"\nBREAKING NEWS: {subject} {action} {place_or_thing}."
    print(headline)

    save_headline = input("\nDo you like to save it?(Yes/No): ").strip().lower()
    save = []
    if save_headline == "y" or "yes":
        with open("save_my_headlines.txt","w") as f:
            save.append(headline)

    new_headline = input("\nDo you want to read another funny fake headline?(Yes/No): ").strip().lower()
    if new_headline == "no":
        break

print("### Thanks For Reading Our FunDay NewsPaper ####")

