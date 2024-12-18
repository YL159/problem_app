'''
Leetcode 2115. Find All Possible Recipes from Given Supplies
Find the recipes that can be made from given unlimited supplies.
Recipes may contain other recipes as ingredients.

Recursively expand a new recipe with its ingredient, resolve each ingredient.
	If all available, this recipe shall be also available for future recipe.
	In case of A & B containing each other, i.e. loop in graph, check if later recipe is already visited.
Iterative method also works. Use stack to keep track of the recipes expanded and expanded ingredients.

Each new recipe is resolved only once.
'''
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        self.avail = set(supplies)
        self.rcp = dict(zip(recipes, ingredients))
        # iterative method, use stack of available + stack of nested recipe
        # here is recursive method
        res = []
        for reci in recipes:
            if self.resolve(reci, set()):
                res.append(reci)
        return res

    def resolve(self, recipe: str, visited: set) -> bool:
        if recipe in self.avail:
            return True
        if recipe not in self.rcp or recipe in visited:
            return False
        visited.add(recipe)
        for ingre in self.rcp[recipe]:
            if not self.resolve(ingre, visited):
                return False
        self.avail.add(recipe)
        return True
