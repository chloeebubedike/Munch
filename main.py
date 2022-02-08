import requests

app_id = '99b8b63d' app_key = '0d112a11f7ca60aa9ce8bd3d218f2ae3'

def recipe_search(ingredient, cuisineType): result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}&cuisineType={}'.format(ingredient, app_id, app_key, cuisineType)) data = result.json() return data['hits']

def run(): ingredient = input('Are you ready to munch! Enter all the ingredients you have: ') cuisineType = input('Which cuisine would you like to munch?') results = recipe_search(ingredient, cuisineType)

print("Good choice! You have chosen to munch on some {} food".format(cuisineType))

for result in results:
    recipe = result['recipe']
    print(recipe['label'])
    print(recipe['uri'])
    print()
run()
