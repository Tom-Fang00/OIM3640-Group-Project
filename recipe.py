import json
import requests
import pprint
import random

'''
getting a list for categories.
'''
urlCategory = ('https://www.themealdb.com/api/json/v1/1/list.php?c=list')
responseCategory = requests.request("GET", urlCategory).json()
# pprint.pprint(responseCategory)
# print(type(responseCategory))
# print(responseCategory.keys())
categoryList = list()
for i in responseCategory['meals']:
    # print(i['strCategory'])
    categoryList.append(i['strCategory'])
# print(categoryList)

'''
Getting a list for areas.
'''
urlArea = ('https://www.themealdb.com/api/json/v1/1/list.php?a=list')
responseArea = requests.request("GET", urlArea).json()
# pprint.pprint(responseArea)
# print(type(responseArea))
# print(responseArea.keys())
areaList = list()
for i in responseArea['meals']:
    # print(i['strArea'])
    areaList.append(i['strArea'])
# print(areaList)

'''
Getting a list for ingredients' names.
'''
urlIngredient = ('https://www.themealdb.com/api/json/v1/1/list.php?i=list')
responseIngredient = requests.request("GET", urlIngredient).json()
# pprint.pprint(responseIngredient)
# print(type(responseIngredient))
# print(responseIngredient.keys())
ingredientList = list()
for i in responseIngredient['meals']:
    ingredientList.append(i['strIngredient'])
print(ingredientList)

c = "Chicken"
a = "American"
i = "Salt"


def fetch(category, area, ingredient):
    cList = list()
    aList = list()
    iList = list()

    if category != "":
        urlC = ('https://www.themealdb.com/api/json/v1/1/filter.php?c='+category)
        responseC = requests.request("GET", urlC).json()
        for meal in responseC['meals']:
            cList.append(meal['idMeal'])
    else:
        cList = []

    if area != "":
        urlA = ('https://www.themealdb.com/api/json/v1/1/filter.php?a='+area)
        responseA = requests.request("GET", urlA).json()
        for meal in responseA['meals']:
            aList.append(meal['idMeal'])
    else:
        aList = []

    if ingredient != "":
        urlI = ('https://www.themealdb.com/api/json/v1/1/filter.php?i='+ingredient)
        responseI = requests.request("GET", urlI).json()
        for meal in responseI['meals']:
            iList.append(meal['idMeal'])
    else:
        iList = []

    cList.sort()
    aList.sort()
    iList.sort()
    final = list()

    if bool(cList) == False:
        for x in aList:
            if x in iList:
                final.append(x)
        print("falseC")
    elif bool(aList) == False:
        for x in cList:
            if x in iList:
                final.append(x)
        print("falseA")
    elif bool(iList) == False:
        for x in aList:
            if x in cList:
                final.append(x)
        print("falseI")
    else:
        for x in aList:
            if x in iList:
                if x in cList:
                    final.append(x)

    # print(cList)
    # print(aList)
    # print(iList)
    '''
    Variable final contains all matched recipes' ID.
    '''
    # print(final)
    
    finalUrl = list()
    for x in final:
        finalX = ('https://www.themealdb.com/api/json/v1/1/lookup.php?i='+x)
        finalUrl.append(finalX)

    if not finalUrl:
        return ["https://lh6.googleusercontent.com/Bu-pRqU_tWZV7O3rJ5nV1P6NjqFnnAs8kVLC5VGz_Kf7ws0nDUXoGTc7pP87tyUCfu8VyXi0YviIm7CxAISDr2lJSwWwXQxxz98qxVfMcKTJfLPqbcfhn-QEeOowjrlwX1LYDFJN","Not Found"]
    else:
        randomRecipe = random.choice(finalUrl)
        responseFinal = requests.request("GET", randomRecipe).json()
        # pprint.pprint(responseFinal)
        recipeList = (responseFinal['meals'])
        recipeDict = dict()
        for x in recipeList:
            recipeDict = dict(x)
            # pprint.pprint(x)
        foodImg = str(recipeDict['strMealThumb'])
        foodName = str(recipeDict['strMeal'])
        food = [foodImg, foodName]
        return food


print(fetch("","",i))
