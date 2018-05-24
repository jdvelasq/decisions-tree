"""
Introduction
===============================================================================

**hardDecisions** is library for representing and evaluating decision trees.



.. image:: ./images/tree_example.png
   :width: 550px
   :align: center


# >>> from hardDecisions.decisiontree import *
# >>> from hardDecisions.treenode import *
# >>> tree = DecisionTree(tree_name='tree-test')
# >>> tree.decision_node(name='A', values=[(-50,  1), (0, 2)], max=True)
# >>> tree.chance_node(name='B', values=[(50, 250,  3), (50, 0, 4)])
# >>> tree.terminal_node(name='T4', expr='A')
# >>> tree.decision_node(name='C', values=[(-120,  5), (-50, 6), (-80, 7)], max=True)
# >>> tree.terminal_node(name='T3', expr='A+B')
# >>> tree.terminal_node(name='T1', expr='A+B+C')
# >>> tree.chance_node(name='D', values=[(50, 0,  8), (50, -120, 8)])
# >>> tree.chance_node(name='E', values=[(70, 0,  8), (30, -120, 8)])
# >>> tree.terminal_node(name='T2', expr='A+B+C+D')
# >>> print_as_tree(tree.variables) # doctest: +NORMALIZE_WHITESPACE
# +-- VARS
#     +-- A {max: True, type: DECISION, values: [(-50, 1), (0, 2)]}
#     +-- B {type: CHANCE, values: [(50, 250, 3), (50, 0, 4)]}
#     +-- T4 {expr: A, type: TERMINAL}
#     +-- C {max: True, type: DECISION, values: [(-120, 5), (-50, 6), (-80, 7)]}
#     +-- T3 {expr: A+B, type: TERMINAL}
#     +-- T1 {expr: A+B+C, type: TERMINAL}
#     +-- D {type: CHANCE, values: [(50, 0, 8), (50, -120, 8)]}
#     +-- E {type: CHANCE, values: [(70, 0, 8), (30, -120, 8)]}
#     +-- T2 {expr: A+B+C+D, type: TERMINAL}

"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
