class TreeNode:
    def __init__(self, tag, attrib={}):
        self.tag = tag
        self.attrib = attrib.copy()
        self.children = []
        self.text = None

    def __repr__(self):
        return '<Node {}>'.format(repr(self.tag))

    # methods operating over subelements
    def __len__(self):
        """Returns the number of children nodes"""
        return len(self.children)

    def __iter__(self):
        return self.children.__iter__()

    def __getitem__(self, index):
        return self.children[index]

    def __setitem__(self, index, value):
        self.children[index] = value

    def __delitem__(self, index):
        del self.children[index]

    def __str__(self):
        txt = '{0}'.format(self.tag)
        if len(self.attrib):
            txt += ' '
            keys = sorted(list(self.attrib.keys()))
            txt += '{'
            for k in keys:
                txt += k + ': '
                txt += str(self.attrib[k])
                if k != keys[-1]:
                    txt += ', '
            txt += '}'
        if not self.text is None:
            txt += ' :' + self.text
        return txt

    def append(self, subnode):
        self.children.append(subnode)

    def extend(self, subnodes):
        self.children.extend(subnodes)

    def insert(self, index, subnode):
        self.children.insert(index, subnode)

    def find(self, match):
        for node in self.children:
            if node.tag == match:
                return node
        return None

    def findall(self, match):
        result = []
        for node in self.children:
            if node.tag == match:
                result.append(node)
        return result

    def search(self, match, key, value):
        for node in self.children:
            if node.tag == match and node.attrib[key] == value:
                return node
        return None

    def searchall(self, match, key, value):
        result = []
        for node in self.children:
            if node.tag == match and node.attrib[key] == value:
                result.append(node)
        return result


    def iter(self, tag=None):
        for children in self.children:
            yield from children.iter(tag)


    # metodos que operan sobre los atributos (dict)
    def clear(self):
        self.text = None
        self.attrib.clear()
        self.children = []


    def get(self, key, default=None):
        return self.attrib.get(key, default)


    def set(self, key, value):
        self.attrib[key] = value


    def keys(self):
        return self.attrib.keys()


    def values(self):
        return self.attrib.values()


    def items(self):
        return self.attrib.items()




def new_node(parent, tag, attrib={}):
    """Returns a new node"""
    parent.append(TreeNode(tag, attrib))
    return parent.children[-1]

def print_as_tree(node):
    """Prints the tree in text"""
    def print_tree_node(prefix, node, last_node):
        print(prefix + '+-- ' + str(node))
        for index, children in enumerate(node.children):
            is_last_node = True if index == len(node.children) - 1 else False
            if last_node is True:
                print_tree_node(prefix + '    ', children, is_last_node)
            else:
                print_tree_node(prefix + '|   ', children, is_last_node)
    print_tree_node('', node, True)
