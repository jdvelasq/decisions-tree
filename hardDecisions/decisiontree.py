"""
DecisionModel
==================

Este es un demo

.. image:: ./images/tree_example.png
   :width: 350px
   :align: center

"""
from hardDecisions.treenode import *

class DecisionModel:
    """Creates and evaluates a decision tree model."""

    def __init__(self, tree_name=None):
        """constructor"""

        # self.datatree = TreeNode(tag='DMTREE')
        self.datatree = None

        # pass
        # self.variables = new_node(parent=self.datatree, tag='VARS')
        # self.treenodes = new_node(parent=self.datatree, tag='TREENODES')
        # self.tree_name = tree_name
        # self.root = None
        # self.globals = {}



if __name__ == "__main__":
    import doctest
    doctest.testmod()
