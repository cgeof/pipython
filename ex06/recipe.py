'''Nested dictionarie'''


import sys

Sandwich = {
  "ingredients" : ['ham', 'bread', 'cheese', 'tomatoes'],
  "meal" : 'lunch',
  "prep_time" : 10 
}
Cake = {
  "ingredients" : ['flour', 'sugar', 'eggs'],
  "meal" : 'dessert',
  "prep_time" : 60 
}
Salad = {
  "ingredients" : ['avocado', 'arugula', 'tomatoes', 'spinach'],
  "meal" : 'lunch',
  "prep_time" : 15 
}

cookbook = {
  "Sandwich" : Sandwich,
  "Cake" : Cake,
  "Salad" : Salad
} 

def liste_recettes(val):
    values = cookbook.keys()
    print(values)

# print(liste_recettes(cookbook))

def print_recette(val):
    recipe_name = input("Please enter a recipe name to get its details:")
    if recipe_name in cookbook:
        print('Recipe for', recipe_name, ':' '\n\tIngredients list:', cookbook[recipe_name]["ingredients"], '\n\tTo be eaten for', cookbook[recipe_name]["meal"], '\n\tTakes', cookbook[recipe_name]["prep_time"], 'minutes of cooking') 
        
    else:
        print("la recette n'existe pas, n'hesite pas à l'ajouter, poil au nez")
    

def delete_recette(val):
    recipe_name = input("enter a recipe name:")
    if recipe_name in cookbook:
        del(cookbook[recipe_name])

# delete_recette(cookbook)   
# print(liste_recettes(cookbook))

def nouvelle_recette(val):
    recipe_name = input("enter a recipe name:")
    cookbook[recipe_name] = recipe_name
    ingredient_name = []
    ingredient_length = 3

    for idx in range (ingredient_length):
        item = input("enter ingredient:")
        ingredient_name.append(item)
    meal_type_name = input("enter a meal type:")
    prep_time_name = input("enter a preparation time:")    
    
    cookbook[recipe_name] = {
    "ingredients" : ingredient_name,
    "meal" : meal_type_name,
    "prep_time" : prep_time_name
    }


    return(liste_recettes(cookbook))
    



def commande(val):
    option = input("Please select an option:")
    if option == "1":
        nouvelle_recette(cookbook)
        commande(val)
    elif option == "2":
        delete_recette(cookbook)
        commande(val)
    elif option == "3":
        print_recette(cookbook)
        commande(val)
    elif option == "4":
        liste_recettes(cookbook)
        commande(val)
    elif option == "5":
        print("Cookbook closed. Goodbye !")
        sys.exit()  
    else:
        print("Sorry, this option does not exist. \nList of available options: \n1: Add a recipe \n2: Delete a recipe \n3: Print a recipe \n4: Print the cookbook \n5: Quit")
        commande(val)
# nouvelle_recette(cookbook)

print("Welcome to the Python Cookbook ! \nList of available options: \n1: Add a recipe \n2: Delete a recipe \n3: Print a recipe \n4: Print the cookbook \n5: Quit")
commande(cookbook)