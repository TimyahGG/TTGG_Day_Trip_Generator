#at least three commits with descriptive messages.
#destinations, restaurants, mode of transportations, and entertainments in their own separate lists.
#destinations, restaurants, mode of transportations, and entertainments to be randomly selected for my day trip.
#able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things
#confirm that my day trip is “complete” once I like all of the random selections.
#display my completed trip in the console.
#each function should do just one thing

Finalized_plan = False
Destinations_List = ["Jacksonville", "New Bern", "Raleigh", "Surf City"]
Restaurants_List = ["El Cerro Grande", "Bay Leaf", "The Farmer's Market", "Buddy's Crab House" ]
Transportation_List = ["Rental Vehical", "Uber", "Train"]
Entertainment_List = ["Cracked It! Escape Games venue", "Birthplace of Pepsi", "Museum of Art", "Bumblebee Market"]

import random
from tkinter import Y

while Finalized_plan == False:
    Destination_approval = False
    Random_Destination = (random.choice(Destinations_List))
    Destination_choice = input(f'Does visiting {Random_Destination} sound good? Y/N ')

    while Destination_approval == False:
        if Destination_choice == "Y":
            Destination_approval = True
            print("Great! Let's move on to your dinner selection.")
        elif Destination_choice == "N":
            Destinations_List.remove(Random_Destination)
            Random_Destination = (random.choice(Destinations_List))
            Destination_choice = input(f'Okay, does visiting {Random_Destination} sound better? Y/N ')
        else:
            Destination_choice = input(f'Sorry, that was an incorrect response. Does visiting {Random_Destination} sound okay? Y/N ')

    Restaurant_approval = False
    Random_Restaurant = (random.choice(Restaurants_List))
    Restaurant_choice = input(f'Does having dinner at {Random_Restaurant} sound good? Y/N ')

    while Restaurant_approval == False:
        if Restaurant_choice == "Y":
            Restaurant_approval = True
            print("Great! Let's move on to your transportation selection.")
        elif Restaurant_choice == "N":
            Restaurants_List.remove(Random_Restaurant)
            Random_Restaurant = (random.choice(Restaurants_List))
            Restaurant_choice = input(f'Okay, does having dinner at {Random_Restaurant} sound better? Y/N ')
        else:
            Restaurant_choice = input(f'Sorry, that was an incorrect response. Does having dinner at {Random_Restaurant} sound okay? Y/N ')
        
    Transportation_approval = False
    Random_Transportation = (random.choice(Transportation_List))
    Transportation_choice = input(f'Does traveling via {Random_Transportation} sound good? Y/N ')

    while Transportation_approval == False:
        if Transportation_choice == "Y":
            Transportation_approval = True
            print("Great! Let's move on to your entertainment selection.")
        elif Transportation_choice == "N":
            Transportation_List.remove(Random_Transportation)
            Random_Transportation = (random.choice(Transportation_List))
            Transportation_choice = input(f'Okay, does traveling via {Random_Transportation} sound better? Y/N ')
        else:
            Transportation_choice = input(f'Sorry, that was an incorrect response. Does traveling via {Random_Transportation} sound okay? Y/N ')

    Entertainment_approval = False
    Random_Entertainment = (random.choice(Entertainment_List))
    Entertainment_choice = input(f'Does spending the afternoon at the {Random_Entertainment} sound good? Y/N ')

    while Entertainment_approval == False:
        if Entertainment_choice == "Y":
            Entertainment_approval = True
            print("Great! Let's recap your trip selections.")
        elif Entertainment_choice == "N":
            Entertainment_List.remove(Random_Entertainment)
            Random_Entertainment = (random.choice(Entertainment_List))
            Entertainment_choice = input(f'Okay, does spending your afternoon at {Random_Entertainment} sound better? Y/N ')
        else:
            Entertainment_choice = input(f'Sorry, that was an incorrect response. Does spending your afternoon at {Random_Entertainment} sound okay? Y/N ')


    Plan_approval = input(f"You've decided to take a trip to {Random_Destination}! While on vacation, you'll be travelling via {Random_Transportation}, spending the afternoon at {Random_Entertainment} and having dinner at {Random_Restaurant}. Is this plan the one you've decided on? Y/N ")


    if Plan_approval == "Y":
        Finalized_plan = True
        print("Great! Thank you for using our trip generator!")
    elif Plan_approval == "N":
        Destinations_List = ["Jacksonville", "New Bern", "Raleigh", "Surf City"]
        Restaurants_List = ["El Cerro Grande", "Bay Leaf", "The Farmer's Market", "Buddy's Crab House" ]
        Transportation_List = ["Rental Vehical", "Uber", "Train"]
        Entertainment_List = ["Cracked It! Escape Games venue", "Birthplace of Pepsi", "Museum of Art", "Bumblebee Market"]
        print("Sorry about that. Let's start from the beginning.")
    else:
        Plan_approval = input("Sorry, that was an incorrect response. You've decided to take a trip to {Random_Destination}! While on vacation, you'll be travelling via {Random_Transportation}, spending the afternoon at {Random_Entertainment} and having dinner at {Random_Restaurant}. Is this plan the one you've decided on? Y/N ")