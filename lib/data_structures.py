spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

#Using list comprehension here we can iterate through each food in the list of dictionaries and only return a list of the names
def get_names(spicy_foods):
    names = [food['name'] for food in spicy_foods]
    return names

#Using list comprehension again we can iterate through each food in the list of dictionaries and return only the foods that fit the filter of a heat level over 5
def get_spiciest_foods(spicy_foods):
    spicy_filter = [heat for heat in spicy_foods if heat['heat_level'] > 5]
    return spicy_filter
    
#By using a for loop we can iterate over the list of dictionaries and for each instance we return the food but in a string that fits the requested strcuture
def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

#With another for loop we again iterate over the list of dictionaries and filter them to only return if the second argument in the function matches the cuisine in the original list.
def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food['cuisine'] == cuisine:
            return food

#This function uses a combination of two above functions by filtering based off heat level and returning the food in the fomrat that fits the request.
def print_spiciest_foods(spicy_foods):
    spicy_filter = [heat for heat in spicy_foods if heat['heat_level'] > 5]
    for food in spicy_filter:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

#With the first line of this function we get a sum of all the heat levels in the original list, we then grab the length of the list in the second line and finally we create a variable to store the average and return it.
def get_average_heat_level(spicy_foods):
    total_heat_level = sum(food['heat_level'] for food in spicy_foods)
    num_of_spicy_foods = len(spicy_foods)
    average_heat = total_heat_level / num_of_spicy_foods
    return average_heat

#Here we just append the second argument in the function(a new food) and return the original list.
def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods

