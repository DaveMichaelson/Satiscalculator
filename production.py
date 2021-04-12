import recipes
import networkx as nx
from collections import defaultdict

class ProductionTree(nx.DiGraph):
    
    def __init__(self, product, recipes_list):
        super().__init__()
        self.recipes = defaultdict(float)
        self.add_node(self._get_next_node_id(), product=product)
        self._generate_tree(0, product, recipes_list)

    def _generate_tree(self, parent_node_id, product, recipes_list):
        possible_recipes = (r for r in recipes_list if product in r.output.keys())
        recipe = next(possible_recipes, None)

        if not recipe:
            return

        self.recipes[recipe] += 1
        id = self._get_next_node_id()
        self.add_node(id, recipe=recipe, product=product)
        self.add_edge(id, parent_node_id)

        for input_prod in recipe.input.keys():
            self._generate_tree(id, input_prod, recipes_list)

    def _get_next_node_id(self):
        return self.number_of_nodes()

    def _get_root(self):
        return self[0]

    def __str__(self):
        string = ""

        for recipe, times in self.recipes.items():
            string += f"{recipe}\t{times}x\n"

        string += self._tree_to_string(0, "")

        return string

    def _tree_to_string(self, node_id, string, pre_string=""):
        node = self.nodes[node_id]
        # string += pre_string + ("->" if pre_string else "") + node['product']
        string += pre_string + "->" + node['product']

        if 'recipe' in node:
            string += f": {node['recipe']}"
        
        string += "\n"

        pre = list(self.predecessors(node_id))
        pre_string += 2 * " " + "|" * len(pre)#(len(pre) - 1)
        
        for child in pre:
            string += pre_string + "\n"
            string += self._tree_to_string(child, "", pre_string[:-1])
            pre_string = pre_string[:-1].rstrip()

        return string
        
