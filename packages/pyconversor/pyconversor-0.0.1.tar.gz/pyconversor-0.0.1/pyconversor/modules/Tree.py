from pyconversor.modules.Node import Node

class Tree:
    def create_tree_by_dict(dictionary: dict):
        
        for key in dictionary:
            root = Node(name= key, value = dictionary[key])

        return root 
    