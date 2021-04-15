import recipes
import networkx as nx
from collections import defaultdict
import math

class ProductionTree(nx.DiGraph):
    
    def __init__(self, product, recipes_list):
        super().__init__()
        self.recipes = defaultdict(float)
        self.ressources = defaultdict(float)
        self.add_node(self._get_next_node_id(), product=product, frequency=1)
        self._generate_tree(0, recipes_list, product)

    def _generate_tree(self, parent_node_id, recipes_list, product, frequency=1):
        possible_recipes = (r for r in recipes_list if product in r.output.keys())
        recipe = next(possible_recipes, None)

        if not recipe:
            self.ressources[product] += frequency
            return

        # The amount of times this recipe has to be applied to meet the reqiured output
        factor = frequency * recipe.time / recipe.output[product]
        int_factor = math.ceil(factor)
        efficiency = factor / int_factor
        self.recipes[recipe] += factor
        id = self._get_next_node_id()
        self.add_node(id, recipe=recipe, product=product, 
            factor=int_factor, efficiency=efficiency)
        self.add_edge(id, parent_node_id, product=product)

        for input_prod, amount in recipe.input.items():
            self._generate_tree(id, recipes_list, input_prod, amount * factor / recipe.time)

    def update_end_product_frequency(self, frequency):
        self.recipes = defaultdict(float)
        self.ressources = defaultdict(float)
        self.nodes[0]['frequency'] = frequency
        self.nodes[0]['frequency'] = frequency
        self._update_tree(1, self.nodes[0]['product'], frequency)

    def _update_tree(self, node_id, product, frequency):
        node = self.nodes[node_id]
        recipe = node['recipe']
        factor = frequency * recipe.time / recipe.output[product]
        int_factor = math.ceil(factor)
        efficiency = factor / int_factor
        self.recipes[recipe] += factor

        node['factor'] = int_factor
        node['efficiency'] = efficiency

        is_child = True
        for child, _, data in self.in_edges(node_id, data=True):
            is_child = False
            input_product = data['product']
            self._update_tree(child, 
                input_product, recipe.input[input_product] * factor / recipe.time)

        if is_child:
            for input_product, amount in recipe.input.items():
                self.ressources[input_product] += factor * amount / recipe.time

    def _get_next_node_id(self):
        return self.number_of_nodes()

    def _get_root(self):
        return self[0]

    def __str__(self):
        string = ""

        for recipe, times in self.recipes.items():
            string += f"{recipe}\t{times}x\n"

        for ressource, frequency in self.ressources.items():
            string += f"{ressource}\t{frequency}/s\n"

        string += self._tree_to_string(0, "")

        return string

    def _tree_to_string(self, node_id, string, pre_string=""):
        node = self.nodes[node_id]
        arrow = ""
        if node_id:
            arrow = f"- {node['factor']}x {node['efficiency'] * 100}% > "
        else:
            arrow = f"- {node['frequency']}/s > "
        string += pre_string + arrow + node['product']

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
        
