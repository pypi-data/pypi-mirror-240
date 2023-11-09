from pyconversor.modules.Tree import Tree

def convert_dict_to_xml(dictionary: dict, raw_string: bool = True) -> str:
    root = Tree.create_tree_by_dict(dictionary=dictionary)
    string = root.convert_node_to_xml(raw_string=raw_string)
    return string