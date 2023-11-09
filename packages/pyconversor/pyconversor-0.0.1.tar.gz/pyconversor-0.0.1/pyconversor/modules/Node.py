class Node:
    def __init__(self, name, value, path:str = '/') -> None:
    
        if type(value) is dict:
            self.value = []
            for key in value:
                self.value.append(Node(name=key, value=value[key], path= path+f"/{name}"))
                self.name = name
                self.path=path

        else:
            self.value = value
            self.name = name
            self.path = path

    def print_Node(self,cont = 0):
        print( f"\r{cont*'   ' }<{self.name}>")
        if type(self.value) is list:
            for node in self.value:
                node.print_Node(cont = cont+1)
        else:
            print(f"\r{cont*'   ' }"+str(self.value))

        print(f"\r{cont*'   ' }</{self.name}>")


    def convert_node_to_xml(self, raw_string: bool = True):
        
        stringify_node = self.stringify_node_value()
        string= '<?xml version="1.0" encoding="utf-8"?>' + stringify_node

        return repr(string) if raw_string else string 

    def stringify_node_value(self, string='', )->str:
        string+=f"<{self.name}>"
        initial_string = "\r\n"
        if type(self.value) is list:
            for node in self.value:
                string += initial_string + node.stringify_node_value()
        else:
            string += initial_string+ str(self.value)
        string+= initial_string + f"</{self.name}>"
        return string

    