#at least three commits with descriptive messages.
#destinations, restaurants, mode of transportations, and entertainments in their own separate lists.
#destinations, restaurants, mode of transportations, and entertainments to be randomly selected for my day trip.
#able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things
#confirm that my day trip is “complete” once I like all of the random selections.
#display my completed trip in the console.
#each function should do just one thing
import random
from tkinter import Y


Destinations_List = ["Jacksonville", "New Bern", "Raleigh", "Surf City"]
Restaurants_List = ["El Cerro Grande", "Bay Leaf", "The Farmer's Market", "Buddy's Crab House" ]
Transportation_List = ["Rental Vehical", "Uber", "Train"]
Entertainment_List = ["Cracked It! Escape Games venue", "Birthplace of Pepsi", "Museum of Art", "Bumblebee Market"]


def confirm_destination():
    Destination_approval = False
    Destination = (random.choice(Destinations_List))
    Destination_choice = input(f'Does visiting {Destination} sound good? Y/N ')
    
    while Destination_approval == False:
        if Destination_choice == "Y":
            Destination_approval = True
            print("Great! Let's move on to your dinner selection.")
            return Destination
        elif Destination_choice == "N":
            Destinations_List.remove(Destination)
            Destination = (random.choice(Destinations_List))
            Destination_choice = input(f'Okay, does visiting {Destination} sound better? Y/N ')
        else:
            Destination_choice = input(f'Sorry, that was an incorrect response. Does visiting {Destination} sound okay? Y/N ')

def confirm_restaurant():
    Restaurant_approval = False
    Restaurant = (random.choice(Restaurants_List))
    Restaurant_choice = input(f'Does having dinner at {Restaurant} sound good? Y/N ')

    while Restaurant_approval == False:
        if Restaurant_choice == "Y":
            Restaurant_approval = True
            print("Great! Let's move on to your transportation selection.")
            return Restaurant
        elif Restaurant_choice == "N":
            Restaurants_List.remove(Restaurant)
            Restaurant = (random.choice(Restaurants_List))
            Restaurant_choice = input(f'Okay, does having dinner at {Restaurant} sound better? Y/N ')
        else:
            Restaurant_choice = input(f'Sorry, that was an incorrect response. Does having dinner at {Restaurant} sound okay? Y/N ')
    
def confirm_transportation():    
    Transportation_approval = False
    Transportation = (random.choice(Transportation_List))
    Transportation_choice = input(f'Does traveling via {Transportation} sound good? Y/N ')

    while Transportation_approval == False:
        if Transportation_choice == "Y":
            Transportation_approval = True
            print("Great! Let's move on to your entertainment selection.")
            return Transportation
        elif Transportation_choice == "N":
            Transportation_List.remove(Transportation)
            Transportation = (random.choice(Transportation_List))
            Transportation_choice = input(f'Okay, does traveling via {Transportation} sound better? Y/N ')
        else:
             Transportation_choice = input(f'Sorry, that was an incorrect response. Does traveling via {Transportation} sound okay? Y/N ')    

def confirm_entertainment():
    Entertainment_approval = False
    Entertainment = (random.choice(Entertainment_List))
    Entertainment_choice = input(f'Does spending the afternoon at the {Entertainment} sound good? Y/N ')

    while Entertainment_approval == False:
        if Entertainment_choice == "Y":
            Entertainment_approval = True
            print("Great! Let's recap your trip selections.")
            return Entertainment
        elif Entertainment_choice == "N":
            Entertainment_List.remove(Entertainment)
            Entertainment = (random.choice(Entertainment_List))
            Entertainment_choice = input(f'Okay, does spending your afternoon at {Entertainment} sound better? Y/N ')
        else:
            Entertainment_choice = input(f'Sorry, that was an incorrect response. Does spending your afternoon at {Entertainment} sound okay? Y/N ')    

def confirm_trip(Destination, Restaurant, Transportation, Entertainment):
    Finalized_plan = False
    while Finalized_plan == False:
        Plan_approval = input(f"You've decided to take a trip to {Destination}! While on vacation, you'll be travelling via {Transportation}, spending the afternoon at {Entertainment} and having dinner at {Restaurant}. Is this plan the one you've decided on? Y/N ")
        if Plan_approval == "Y":
            Finalized_plan = True
            print("Great! Thank you for using our trip generator!")
        elif Plan_approval == "N":
            print("Sorry about that. Let's start from the beginning.")
            return Finalized_plan
        else:
                Plan_approval = input("Sorry, that was an incorrect response. You've decided to take a trip to {Destination}! While on vacation, you'll be travelling via {Random_Transportation}, spending the afternoon at {Entertainment} and having dinner at {Restaurant}. Is this plan the one you've decided on? Y/N ")    

def generate_trip():
    confirmed_destination = confirm_destination()
    confirmed_restaurant = confirm_restaurant()
    confirmed_transportation = confirm_transportation()
    confirmed_entertainment = confirm_entertainment()
    
    confirm_trip(confirmed_destination, confirmed_restaurant, confirmed_transportation, confirmed_entertainment)

generate_trip()
