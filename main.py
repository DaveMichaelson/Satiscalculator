import recipes
import production
import argparse

def _read_recipes_from_file(file):
    rec_list = []

    with open(file) as f:
        for line in f.readlines():
            if line != "\n":
                rec_list.append(recipes.parse_recipe(line))

    return rec_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("recipes", type=_read_recipes_from_file)
    parser.add_argument("product")
    parser.add_argument("-f", "--frequency", dest='frequency', type=float)
    args = parser.parse_args()

    prod_tree = production.ProductionTree(args.product, args.recipes)
    if args.frequency:
        prod_tree.update_end_product_frequency(args.frequency)
    print(prod_tree)