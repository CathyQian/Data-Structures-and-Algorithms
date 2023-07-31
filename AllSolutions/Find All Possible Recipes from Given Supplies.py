"""
Find All Possible Recipes from Given Supplies

You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all
the needed ingredients from ingredients[i]. Ingredients to a recipe may need to be created from other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.

 

Example 1:

Input: recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]
Output: ["bread"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
Example 2:

Input: recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
Example 3:

Input: recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]
Output: ["bread","sandwich","burger"]
Explanation:
We can create "bread" since we have the ingredients "yeast" and "flour".
We can create "sandwich" since we have the ingredient "meat" and can create the ingredient "bread".
We can create "burger" since we have the ingredient "meat" and can create the ingredients "bread" and "sandwich".
 

Constraints:

n == recipes.length == ingredients.length
1 <= n <= 100
1 <= ingredients[i].length, supplies.length <= 100
1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10
recipes[i], ingredients[i][j], and supplies[k] consist only of lowercase English letters.
All the values of recipes and supplies combined are unique.
Each ingredients[i] does not contain any duplicate values.

"""

# similar to DFS in graph, but need to first build the adj_list, also need to detect for loops using the visiting dict (needed in DFS for graph solutions)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        self.canCreate = {}    
        self.visiting = {recipe: 0 for recipe in recipes} # all unvisited
        supplies = set(supplies)

        adj_list = collections.defaultdict(list)
        for recipe, ingredient in zip(recipes, ingredients):
            for item in ingredient:
                adj_list[recipe].append(item)

        ans = []
        for recipe in recipes:
            if self.canCreateHelper(recipe, adj_list, supplies):
                ans.append(recipe)
        
        return ans
 
    def canCreateHelper(self, recipe, adj_list, supplies):
        if recipe not in self.canCreate:
            self.visiting[recipe] = 1 # currently being visited
            self.canCreate[recipe] = True
            
            for ingredient in adj_list[recipe]:
                if ingredient in supplies:
                    continue
                elif ingredient in adj_list and self.visiting[ingredient] != 1:
                    res = self.canCreateHelper(ingredient, adj_list, supplies)
                    if not res:
                        self.canCreate[recipe] = False
                        break 
                else:
                    self.canCreate[recipe] = False
                    break 
            
            self.visiting[recipe] = 2 # visited

        return self.canCreate[recipe]
        