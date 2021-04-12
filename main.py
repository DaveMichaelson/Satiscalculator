import recipes
import production

if __name__ == "__main__":
    rec_list = []

    with open("recipe/satisfactory.recipes") as f:
        for line in f.readlines():
            if line != "\n":
                rec_list.append(recipes.parse_recipe(line))

    for r in rec_list:
        print(r)

    # print("\n---------Graph---------")
    # prod_tree = production.ProductionTree("Beton", rec_list)
    # print(prod_tree)

    # print("\n---------Graph---------")
    # prod_tree = production.ProductionTree("Kabel", rec_list)
    # print(prod_tree)

    print("\n---------Graph---------")
    prod_tree = production.ProductionTree("Rotor", rec_list)
    print(prod_tree)