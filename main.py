#at least three commits with descriptive messages.
#destinations, restaurants, mode of transportations, and entertainments in their own separate lists.
#destinations, restaurants, mode of transportations, and entertainments to be randomly selected for my day trip.
#able to randomly re-select a destination, restaurant, mode of transportation, and/or form of entertainment if I don’t like one or more of those things
#confirm that my day trip is “complete” once I like all of the random selections.
#display my completed trip in the console.
#each function should do just one thing

Destinations_List = ["Jacksonville", "New Bern", "Raleigh", "Surf City"]
Restaurants_List = ["El Cerro Grande", "Bay Leaf", "Farmer's Market", "Buddy's Crab House" ]
Transportation_List = ["Rental Vehical", "Uber", "Train"]
Entertainment_List = ["Cracked It! Escape Games venue", "Birthplace of Pepsi", "Museum of Art", "Bumblebee Market"]

import random
print(f'For your destination selection, how does visiting {random.choice(Destinations_List)} sound?')

import random
print(f'For your restaurant selection, how does having dinner at {random.choice(Restaurants_List)} sound?')

import random
print(f'For your transportation selection, how does riding in a {random.choice(Transportation_List)} sound?')

import random
print(f'For your entertainment selection, how does going to the {random.choice(Entertainment_List)} sound?')