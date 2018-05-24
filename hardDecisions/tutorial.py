"""
Introduction
===============================================================================

**hardDecisions** is library for representing and evaluating decision trees.



.. image:: ./images/tree_example.png
   :width: 550px
   :align: center


>>> from hardDecisions.decisiontree import *
>>> from hardDecisions.treenode  import *
>>> tree = DecisionTree(tree_name='tree-test')
>>> A = [(-50,  1),
...      (  0,  2)]
>>> tree.decision_node(name='A', values=A, max=True)

>>> print_as_tree(tree.variables) # doctest: +NORMALIZE_WHITESPACE
+-- VARS
   +-- A {max: True, type: DECISION, values: [(-50, 1), (0, 2)]}
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
