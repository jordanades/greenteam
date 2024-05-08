"""
Need to add:
I either added a function or added a line in an existing docstring with one of the below things we need to add.
Add implementation of these in your new assigned method/function or in the existing method/function.

Anthony - f-strings containing expressions
Jesse - sequence unpacking
Jamie - set operations on sets or frozensets
Ikenna - comprehensions or generator expressions
Jesse - use of a key function (which can be a lambda expression) with one of the following commands: list.sort(), sorted(), min(), or max()
Anthony - visualizing data with pyplot
Ikenna - magic methods other than __init__()
"""



import pandas as pd
import argparse
import sys

active_shopping_lists = []

class RecipeManager:
    def __init__(self):
        """Jordan
        """
        self.recipes = []
        self.recipe_dict = {} 
        self.recipe_names = []
    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        self.recipe_dict[recipe.name] = recipe.category  
        self.recipe_names.append(recipe.name) 
    def search_for_ingredient(self, ingredient):
        """Jamie
        This method will search through the recipes and return a list of
        recipes that contain the given ingredient
        """
        matchRecipes = []
        for rec in self.recipes:
            matchRecipes.append(rec) if ingredient in rec.ingredients else None
        return matchRecipes
    def recipe_count(self):
        """Anthony
        Prints the number of recipes in the Recipe manager
        
        ### f-string containing expression ###
        """    
    def display_all_recipes(self):
        """Jesse
        
        ### Sequence unpacking ###
        
        Use sequence unpacking to display the keys and values (recipe name and category) 
        from the recipe_dict
        """
        for x, y in self.recipe_dict.items():
            print(f"{x}: {y}")
        
    def chart_recipes(self):
        """Anthony
        
        ### Visualizing data with pyplot ###
        Make a function that makes a bar or pie chart showing how many recipes we have in each category
        """
    def categorize_recipes(self):
        """Ikenna
        This method will search through the recipes and return a list of
        lists that contain the recipes for the different categories
        (list for desserts, for appetizers, etc.)
        
        ### List comprehention ###
        """
        categorized = {}
        for recipe in self.recipes:
            if recipe.category in categorized:
                categorized[recipe.category].append(recipe.name)
            else:
                categorized[recipe.category] = [recipe.name]
        return categorized
    
    def sort_recipes(self, condition):
        """Jesse
        ### use key functions ###
        
        Make a method that sorts the self.recipes list by number of ingredients, directions length, etc.
        The thing you sort by is the condition variable, make if statements for a few different options of
        condition and raise an error if its something else
        """
        if condition == "ingredients":
            print(self.recipes.sort(key=lambda x: len(x.ingredients)))
        elif condition == "directions":
            print(self.recipes.sort(key=lambda x: len(x.directions)))
        elif condition == "name":
            print(self.recipes.sort(key=lambda x: x.name))
        else:
            raise ValueError("Invalid condition! Supported conditions are 'ingredients', 'directions', or 'name'.")
    

class Recipe:
    def __init__(self, name, ingredients, directions, category="Recipe"):
        """Jordan
        Recipe category value will change but is 'Recipe' by default.
        """
        self.name = name
        self.ingredients = ingredients
        self.directions = directions
        self.category = category
    def add_ingredients(self, ingredient_list):
        """Jordan
        """
        ingredient_list = ingredient_list.split(", ")
        for ingredient in ingredient_list:
            self.ingredients.append(ingredient)
    def __str__(self):
        """Ikenna
        ### Magic method other than init ###
        
        Make a string representation of a recipe if we were to use print()
        """
    
class ShoppingList:
    def __init__(self, name):
        """Jordan
        """
        self.shopping_list = {}
        self.name = name
    def __str__(self):
        return self.name
    def add_to_list(self, recipe):
        """Jesse
        This method will take a Recipe object as input and will search through
        it's list of ingredients, and add the ingredients not already on the 
        shopping list to self.shopping_list.
        """
        for ingredient in recipe.ingredients:
            if ingredient not in self.shopping_list:
                self.shopping_list.append(ingredient)
    def __add__(self, other_list):
        """Jamie
        Returns new list that contains unique ingredients from both recipes
        
        ### Set operations ###
        """
        
        
        
def view_recipe(recipe):
    """Anthony
    Takes a recipe object as an input and displays all of its properties in a
    good looking format.
    """
    
    """ Confirms that the input is a Recipe Instance. """
    if not isinstance(recipe, Recipe):
        raise ValueError("Expected a Recipe instance")
    
    print(f"\n{recipe.name}")
    
    """ Displays the category of the recipe. """
    print(f"\nCategory: {recipe.category}")
    print("\nIngredients:")
    
    """ Lists all the ingredients of the recipe. """
    for ingredient in recipe.ingredients:
        print(f"\n- {ingredient}")
    
    """ Displays the directions of the recipe. """ 
    print("\nDirections:")
    print(f"\n{recipe.directions}")

def parse_args(arglist):
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="filepath for recipes csv")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    Recipe_Book = RecipeManager()
    df = pd.read_csv(args.file, header=0)
    for index, row in df.iterrows():
        Recipe_Book.add_recipe(Recipe(row["Name"], row["Ingredients"].split(", "), row["Directions"], row["Category"]))
        
    print("Welcome to your recipe manager. Thank you for inputting your recipes.")
    print("\nWhat would you like to do?")
    print("""\n
          1. Recipe book options
          2. Recipe options
          3. Shopping list options
          """)
    choice1 = input("\n")
    if choice1 == "1":
        print("\nWhat would you like to do with your recipe book?")
        print("""\n
              1. Add a recipe
              2. Find your recipes that contain a specific ingredient
              3. Display the number of recipes in your book
              4. Display all the recipes in your book
              5. View a graph of the category breakdown of your recipes
              6. View categorized lists of your recipes
              7. Sort your recipes
              """)
        choice2 = input("\n")
        if choice2 == "1":
            newname = input("\nWhat is the name of the recipe you would like to add?\n")
            newcat = input("\nWhat is the category of the recipe you would like to add?\n")
            newing = input("\nWhat are the ingredients of the recipe? (ingredient1, ingredient2...)\n")
            newdir = input("What are the directions for the recipe?\n")
            Recipe_Book.add_recipe(Recipe(newname, newing.split(", "), newdir, newcat))
        elif choice2 == "2":
            ing_to_search = input("We will display all your recipes that contain a given ingredient. What ingredient would you like to use?\n")
            print(Recipe_Book.search_for_ingredient(ing_to_search))
        elif choice2 == "3":
            print(Recipe_Book.recipe_count())
        elif choice2 == "4":
            Recipe_Book.display_all_recipes()
        elif choice2 == "5":
            Recipe_Book.chart_recipes()
        elif choice2 == "6":
            print(Recipe_Book.categorize_recipes())
        elif choice2 == "7":
            sort_choice = input("\nWhat would you like to sort your recipes by?\n")
            Recipe_Book.sort_recipes(sort_choice)
        else:
            raise ValueError("That was not an option")
    elif choice1 == "2":
        print("\nWhat recipe would you like to work with?")
        recipe_choice = input("\n")
        if recipe_choice in Recipe_Book.recipe_names:
            pass
        else:
            raise ValueError("This recipe is not in your Recipe Book")
        print("\nWhat would you like to do with this recipe?")
        print("""\n
              1. Add an ingredient
              2. Change the category
              3. View the recipe and its properties
              """)
        choice3 = input("\n")
        if choice3 == "1":
            ing_to_add = input("\nWhat ingredient(s) would you like to add? (ingredient1, ingredient2...)\n")
            for recipe in Recipe_Book.recipes:
                if recipe.name == recipe_choice:
                    recipe.add_ingredients(ing_to_add)
        elif choice3 == "2":
            newcat = input("\nWhat category would you like to change your recipe to?\n")
            for recipe in Recipe_Book.recipes:
                if recipe.name == recipe_choice:
                    recipe.category = newcat
        elif choice3 == "3":
            for recipe in Recipe_Book.recipes:
                if recipe.name == recipe_choice:
                    view_recipe(recipe)
        else:
            raise ValueError("That was not an option")
    elif choice1 == "3":
        print("\nWhat would you like to do?")
        print("""\n
              1. Create new shopping list
              2. Manage existing shopping list
              """)
        choice4 = input("\n")
        if choice4 == "1":
            listname = input("\nWhat would you like to call your shopping list?\n")
            active_shopping_lists.append(ShoppingList(listname))
            print(f"A shopping list called {listname} has been created!")
        elif choice4 == "2":
            print(f"Shopping lists: {active_shopping_lists}")
            list_to_manage = input("\nWhich list would you like to manage?\n")
            print(f"""\nWould you like to:
                  1. Add all ingredients from a recipe to {list_to_manage}
                  2. Add specific ingredient(s) to {list_to_manage}""")
            choice5 = input("\n")
            if choice5 == "1":
                recipetoadd = input("\nWhich recipe do you want ingredients from?\n")
                for recipe in Recipe_Book.recipes:
                    if recipe.name == recipetoadd:
                        for list in active_shopping_lists:
                            if list.name == list_to_manage:
                                list.add_to_list(recipe)
            elif choice5 == "2":
                ingtoadd = input("\nWhat ingredient(s) would you like to add? (ingredient1, ingredient2...)\n")
                ingtoadd = ingtoadd.split(", ")
                for list in active_shopping_lists:
                    if list.name == list_to_manage:
                        for item in ingtoadd:
                            list.shopping_list.add(item)
            else:
                raise ValueError("That was not an option")
    else:
        raise ValueError("That was not an option")