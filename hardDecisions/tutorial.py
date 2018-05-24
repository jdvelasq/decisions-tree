"""
Tutorial
==============================================================================

**hardDecisions** is library for representing and evaluating decision trees.



.. image:: ./images/tree_example.png
   :width: 550px
   :align: center


>>> from hardDecisions.decisiontree import *
>>> from hardDecisions.treenode import *
>>> tree = DecisionTree(tree_name='tree-test')
>>> tree.decision_node(name='A', values=[(-50,  1), (0, 2)], max=True)
>>> tree.chance_node(name='B', values=[(50, 250,  3), (50, 0, 4)])
>>> tree.terminal_node(name='T4', expr='A')
>>> tree.decision_node(name='C', values=[(-120,  5), (-50, 6), (-80, 7)], max=True)
>>> tree.terminal_node(name='T3', expr='A+B')
>>> tree.terminal_node(name='T1', expr='A+B+C')
>>> tree.chance_node(name='D', values=[(50, 0,  8), (50, -120, 8)])
>>> tree.chance_node(name='E', values=[(70, 0,  8), (30, -120, 8)])
>>> tree.terminal_node(name='T2', expr='A+B+C+D')




>>> tree.display_variables() # doctest: +NORMALIZE_WHITESPACE
Node 0
A:
   Type: DECISION - Maximum Payoff
   Branches:
                     Outcomes  Sucessor Node
                      -50.000  1
                        0.000  2
<BLANKLINE>
Node 1
B:
   Type: CHANCE
   Branches:
         Chance       Outcome  Sucessor Node
          50.00       250.000  3
          50.00         0.000  4
<BLANKLINE>
Node 2
T4:
   Type: TERMINAL
   Expr: A
<BLANKLINE>
Node 3
C:
   Type: DECISION - Maximum Payoff
   Branches:
                     Outcomes  Sucessor Node
                     -120.000  5
                      -50.000  6
                      -80.000  7
<BLANKLINE>
Node 4
T3:
   Type: TERMINAL
   Expr: A+B
<BLANKLINE>
Node 5
T1:
   Type: TERMINAL
   Expr: A+B+C
<BLANKLINE>
Node 6
D:
   Type: CHANCE
   Branches:
         Chance       Outcome  Sucessor Node
          50.00         0.000  8
          50.00      -120.000  8
<BLANKLINE>
Node 7
E:
   Type: CHANCE
   Branches:
         Chance       Outcome  Sucessor Node
          70.00         0.000  8
          30.00      -120.000  8
<BLANKLINE>
Node 8
T2:
   Type: TERMINAL
   Expr: A+B+C+D
<BLANKLINE>



>>> print_as_tree(tree.variables) # doctest: +NORMALIZE_WHITESPACE
+-- VARS
    +-- A {max: True, type: DECISION, values: [(-50, 1), (0, 2)]}
    +-- B {type: CHANCE, values: [(50, 250, 3), (50, 0, 4)]}
    +-- T4 {expr: A, type: TERMINAL}
    +-- C {max: True, type: DECISION, values: [(-120, 5), (-50, 6), (-80, 7)]}
    +-- T3 {expr: A+B, type: TERMINAL}
    +-- T1 {expr: A+B+C, type: TERMINAL}
    +-- D {type: CHANCE, values: [(50, 0, 8), (50, -120, 8)]}
    +-- E {type: CHANCE, values: [(70, 0, 8), (30, -120, 8)]}
    +-- T2 {expr: A+B+C+D, type: TERMINAL}

"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
