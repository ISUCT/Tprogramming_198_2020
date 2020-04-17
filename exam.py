print("Рецепт бутерброда:")
ingredients = ['слизни', 'пиявки', 'катышки из пупка гориллы', 'брови гусеницы', 'пальцы многоножки']
length = len(ingredients)
for i in range(length):
    print(str(i+1), ") ", ingredients[i], sep="", end=";\n")
    