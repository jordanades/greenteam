"""
Need to add:
I either added a function or added a line in an existing docstring with one of the below things we need to add.
Add implementation of these in your new assigned method/function or in the existing method/function.

Jesse - sequence unpacking
Jamie - set operations on sets or frozensets
Ikenna - comprehensions or generator expressions
Jesse - use of a key function (which can be a lambda expression) with one of the following commands: list.sort(), sorted(), min(), or max()
Ikenna - magic methods other than __init__()
"""
"""The name and technique for each function/method are in the docstrings. 
The technique (if one is being claimed) will be denoted with '###'
"""


import pandas as pd
import argparse
import sys
import matplotlib as plt

active_shopping_lists = []

class RecipeManager:
    """This class is for a recipe manager, this is similar to a Recipe Book that contains recipes.
    
    Attributes:
        recipes (list): the list of recipes in the manager
        recipe_dict (dict): dictionary of recipe and its category
        recipe_names (list): list of strings of the names of the recipes in the book
    """
    def __init__(self):
        """Jordan
        
        Initializes a new instance of the class.
        
        Side effects:
            Initializes empty lists `recipes`, `recipe_dict`, and `recipe_names` as attributes of the instance.
        """
        self.recipes = []
        self.recipe_dict = {} 
        self.recipe_names = []
        
    def add_recipe(self, recipe):
        """Jordan
        
        Adds a recipe to the recipe collection.
        
        Args:
            recipe (Recipe): The recipe object to add.
            
        Side effects:
            Modifies the lists `recipes`, `recipe_dict`, and `recipe_names` by adding the provided recipe.
        """
        self.recipes.append(recipe)
        self.recipe_dict[recipe.name] = recipe.category  
        self.recipe_names.append(recipe.name) 
        
    def search_for_ingredient(self, ingredient):
        """Jamie
        This method will search through the recipes and return a list of
        recipes that contain the given ingredient
        
        Args:
            ingredient (str): ingredient name to search for
        
        Returns:
            matchRecipes (list): list of recipes that contain the ingredient
        
        ### Conditional Expression ###
        """
        matchRecipes = []
        for rec in self.recipes:
            matchRecipes.append(rec) if ingredient in rec.ingredients else None
        return matchRecipes
    
    def recipe_count(self):
        """Anthony
        Prints the number of recipes in the Recipe manager
        
        Returns:
        None
        
        Side Effects
            Prints number of recipes in recipe_manager class
        """
        print(f"Number of recipes: {len(self.recipes)}")
        
    def display_all_recipes(self):
        """Jesse
        Display all recipes and their categories.

        Utilizes sequence unpacking to iterate through the keys and values of the recipe_dict,
        printing each recipe name along with its corresponding category.

        Returns:
            None
            
        ### sequence unpacking ###
        """
        for x, y in self.recipe_dict.items():
            print(f"{x}: {y}")
        
    def chart_recipes(self):
        """Anthony
        Visualizes the number of recipes in each category using pyplot
        
        This function creates a bar chart showing the number of recipes in each
        category. It retrieves the data utilizing the categorize_recipes method
        and plots the data using pyplot.
        
        Returns:
        None
        
        Side Effects:
            Displays a bar chart showing number of recipes in each category.
        
        """
        categorized = self.categorize_recipes()
        categories = list(categorized.keys())
        counts = [len(categorized[category]) for category in categories]
        
        plt.figure(figsize=(10,6))
        plt.bar(categories, counts, color='skyblue')
        plt.xlabel('Categories')
        plt.ylabel('Number of Recipes')
        plt.title('Recipe Category Breakdown')
        plt.xticks(rotation=45)
        plt.show()
        
    def categorize_recipes(self):
        """Ikenna
        
        ### List comprehension ###
        
        Categorizes recipes into lists based on their categories.
        
        This method utilizes list comprehensions to create a dictionary where each key is a recipe category
        and the value is a list of recipes names belonging to that category.

        Returns:
            dict: A dictionary where keys are categories and values are lists of recipe names in those categories.
        """
        
        categorized = {category: [recipe.name for recipe in self.recipes if recipe.category == category]
                    for category in set(recipe.category for recipe in self.recipes)}
        return categorized
    
    def sort_recipes(self, condition):
        """Jesse
        Sorts the recipes list based on a specified condition.

        Args:
        condition (str): The condition to sort the recipes by. Supported options are:
            'ingredients': Sorts the recipes by the number of ingredients.
            'directions': Sorts the recipes by the length of directions.
            'name': Sorts the recipes alphabetically by name.

        Raises:
            ValueError: If an unsupported condition is provided.

        Returns:
            None
            
        ### use of a key function (which can be a lambda expression) with one of the following commands: list.sort(), sorted(), min(), or max() ###
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
    """This class is for a specific recipe, it contains the recipe information.
    
    Attributes:
        name (str): The name of the recipe.
        ingredients (list of str): The list of ingredients needed for the recipe.
        directions (str): The cooking directions for the recipe.
        category (str, optional): The category of the recipe. Defaults to "Recipe".
    """
    def __init__(self, name, ingredients, directions, category="Recipe"):
        """Jordan
        
        Initializes the Recipe class. Recipe category value will change but is 'Recipe' by default.
        
        Args:
            name (str): The name of the recipe.
            ingredients (list of str): The list of ingredients needed for the recipe.
            directions (str): The cooking directions for the recipe.
            category (str, optional): The category of the recipe. Defaults to "Recipe".
            
        ### optional parameters and/or keyword arguments ###
        """
        self.name = name
        self.ingredients = ingredients
        self.directions = directions
        self.category = category
    def add_ingredients(self, ingredient_list):
        """Jordan
        
        This method adds ingredients to the recipe.
        
        Args:
            ingredient_list (str): A comma-separated string containing the ingredients to add.
        Side effects:
            Modifies the list of ingredients by appending the provided ingredients.
        """
        ingredient_list = ingredient_list.split(", ")
        for ingredient in ingredient_list:
            self.ingredients.append(ingredient)
            
    def __str__(self):
        """Ikenna
        
        ### Magic method other than init ###
        
        Provides a string representation of the recipe suitable for printing.

        This method formats the recipe details including the name, ingredients, directions, and category into a readable string.

        Returns:
            str: A formatted string representing the recipe.
        """
        ingredients_str = ", ".join(self.ingredients) 
        return (f"Recipe Name: {self.name}\n"
                f"Category: {self.category}\n"
                f"Ingredients: {ingredients_str}\n"
                f"Directions: {self.directions}")
    
class ShoppingList:
    """Class for a shopping list, contains list contents and operations.
    
    Attributes:
        shopping_list (set): set of ingredients
        name (str): name of shopping list
    """
    def __init__(self, name):
        """Jordan
        
        Initializes the ShoppingList class.
        
        Args:
            name (str): name of shopping list
            
        Side effects:
            Creates empty set for shopping_list
        """
        self.shopping_list = {}
        self.name = name
    def __str__(self):
        """Jordan
        
        Defines formal str representation of the class.
        
        Returns:
            self.name (str): name of the list
        """
        return self.name
    def add_to_list(self, recipe):
        """Jesse
        Update the shopping list with ingredients from the given Recipe object.

        This method takes a Recipe object as input and iterates through its list of ingredients.
        If an ingredient is not already on the shopping list, it will be added.

        Args:
            recipe (Recipe): The Recipe object from which ingredients will be added to the shopping list.

        Returns:
            None
        """
        for ingredient in recipe.ingredients:
            if ingredient not in self.shopping_list:
                self.shopping_list.append(ingredient)
    def __add__(self, other_list):
        """Jamie
        Returns new list that contains unique ingredients from both recipes
        
        Args:
            other_list (list): shopping list to union current list with
        
        Returns:
            combined_list (list): combined list of two given lists
        ### Set operations ###
        """
        combined_list = self.shopping_list.union(other_list)
        return combined_list    
        
        
        
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
    """Jordan
    Parses command-line arguments.

    Args:
        arglist (list of str): The list of command-line arguments.

    Returns:
        argparse.Namespace: An object containing the parsed arguments.
        
    ### The ArgumentParser class from the argparse module ###
    """
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
            sort_choice = input("\nWhat would you like to sort your recipes by? Supported conditions are 'ingredients', 'directions', or 'name'.\n")
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
