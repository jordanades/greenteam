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

class RecipeManager:
    def __init__(self):
        """Jordan
        """
        self.recipes = []
        self.recipe_dict = {} 
    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        self.recipe_dict[recipe.name] = recipe.category   
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
                categorized[recipe.category].append(recipe)
            else:
                categorized[recipe.category] = [recipe]
        return categorized
    def sort_recipes(self, condition):
        """Jesse
        ### use key functions ###
        
        Make a method that sorts the self.recipes list by number of ingredients, directions length, etc.
        The thing you sort by is the condition variable, make if statements for a few different options of
        condition and raise an error if its something else
        """

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
        ingredient_list.split(", ")
        for ingredient in ingredient_list:
            self.ingredients.append(ingredient)
    def __str__(self):
        """Ikenna
        ### Magic method other than init ###
        
        Make a string representation of a recipe if we were to use print()
        """
    
class ShoppingList:
    def __init__(self):
        """Jordan
        """
        self.shopping_list = {}
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
        
    for recipe in Recipe_Book.recipes:
        view_recipe(recipe)