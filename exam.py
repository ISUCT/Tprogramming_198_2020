print("Рецепт бутерброда:")
ingredients = ['хлеб', 'масло', 'сыр']
length = len(ingredients)
for i in range(length):
    print(str(i+1), ") ", ingredients[i], sep="", end=";\n")
    