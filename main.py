import recipes

if __name__ == "__main__":
    rec_list = []

    with open("recipe/satisfactory.recipes") as f:
        for line in f.readlines():
            if line != "\n":
                rec_list.append(recipes.parse_recipe(line))

    for r in rec_list:
        print(r)