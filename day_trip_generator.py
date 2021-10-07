import random
# lists
destination_list = ['gilbert', 'mesa', 'tempe']
restaurant_list = ['taco bell', 'hungry howies', 'jimmy johns']
transportation_list = ['car', 'bus', 'bike']
entertainment_list = ['movies', 'concert', 'zoo']
storage_list = []
# user_input
user_input = input("would you like this program to randomly generate a day trip for you? (y/n) ").lower()


def random_element_from_list(list):
    list_index = random.randint(0, len(list)-1)
    return list_index

# generate a random trip
def day_trip_generator(string):
    while True:
        if string == 'y':
            print("Your randomly generated day trip: ")
            destination_index = random_element_from_list(destination_list)
            restaurant_index = random.randint(0, len(restaurant_list)-1)
            transportation_index = random.randint(
                0, len(transportation_list)-1)
            entertainment_index = random.randint(0, len(entertainment_list)-1)
            print(f"You will be heading to the {entertainment_list[entertainment_index]} in {destination_list[destination_index]} using a {transportation_list[transportation_index]} as transportation. Dinner at {restaurant_list[restaurant_index]}.")
            break
        elif string == 'n':
            print("terminating program")
            break
        else:
            string = input("please use y or n to make a selection: ")
day_trip_generator(user_input)
# make sure user is satisfied with trip
while True:
    user_input = input("would you like a different day trip? (y/n) ").lower()
    if user_input == 'y':
        day_trip_generator(user_input)
    elif user_input == 'n':
        print("enjoy your trip!")
        break
    else:
        print("please use y or n to make a selction.")

def random_element_from_list(list):
    list_index = random.randint(0, len(list)-1)
    return list_index

print(f"one random element from a list: {destination_list[random_element_from_list(destination_list)]}")

user_input = input("How statisfied are you with the trip? ")

def review_storage(string):
    storage_list = [string]
    return storage_list

storage_list.append(review_storage(user_input))

print(f"CURRENT REVIEWS\n{storage_list}")
