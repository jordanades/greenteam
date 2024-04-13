"""Write your function where I put your name. Commit to github when you
finish your part.
"""

class RecipeManager:
    def __init__(self):
        """Jordan
        """
        self.recipes = []
        
    def search_for_ingredient(self, ingredient):
        """Jamie
        This method will search through the recipes and return a list of
        recipes that contain the given ingredient
        """
        matchRecipes = []
        for rec in self.recipes:
            if ingredient in rec.ingredients:
                matchRecipes.append(rec)
        return matchRecipes
            
        
    def categorize_recipes(self):
        """Ikenna
        This method will search through the recipes and return a list of
        lists that contain the recipes for the different categories
        (list for desserts, for appetizers, etc.)"""
        categorized = {}
    for recipe in self.recipes:
        if recipe.category in categorized:
            categorized[recipe.category].append(recipe)
        else:
            categorized[recipe.category] = [recipe]
    return categorized

class Recipe:
    def __init__(self):
        """Jordan
        Recipe category value will change but is 'Recipe' by default.
        """
        self.ingredients = []
        self.directions = ""
        self.category = "Recipe"
    def add_ingredients(self, ingredient_list):
        """Jordan
        """
        for ingredient in ingredient_list:
            self.ingredients.append(ingredient)
    
class ShoppingList:
    def __init__(self):
        """Jordan
        """
        self.shopping_list = []
    def add_to_list(self, Recipe):
        """Jesse
        This method will take a Recipe object as input and will search through
        it's list of ingredients, and add the ingredients not already on the 
        shopping list to self.shopping_list.
        """
        for ingredient in Recipe.ingredients:
            if ingredient not in self.shopping_list:
                self.shopping_list.append(ingredient)
        
        
def view_recipe(recipe):
    """Anthony
    Takes a recipe object as an input and displays all of its properties in a
    good looking format.
    """
    
    """ Confirms that the input is a Recipe Instance. """
    if not isinstance(recipe, Recipe):
        raise ValueError("Expected a Recipe instance")
    
    """ Displays the category of the recipe. """
    print(f"Category: {recipe.category}")
    print("\nIngredients:")
    
    """ Lists all the ingredients of the recipe. """
    for ingredient in recipe.ingredients:
        print(f"- {ingredient}")
    
    """ Displays the directions of the recipe. """ 
    print("\nDirections:")
    print(recipe.directions)
