"""
Tutorial
==============================================================================

**hardDecisions** is library for representing and evaluating decision trees.



.. image:: ./images/tree_example.png
   :width: 550px
   :align: center


# >>> from hardDecisions.decisiontree import *
# >>> from hardDecisions.treenode import *
# >>> tree = DecisionTree(tree_name='test')
# >>> tree.decision_node(name='A', values=[(-50,  1), (0, 2)], max=True)
# >>> tree.chance_node(name='B', values=[(50, 250,  3), (50, 0, 4)])
# >>> tree.terminal_node(name='T4', expr='A')
# >>> tree.decision_node(name='C', values=[(-120,  5), (-50, 6), (-80, 7)], max=True)
# >>> tree.terminal_node(name='T3', expr='A+B')
# >>> tree.terminal_node(name='T1', expr='A+B+C')
# >>> tree.chance_node(name='D', values=[(50, 0,  8), (50, -120, 8)])
# >>> tree.chance_node(name='E', values=[(70, 0,  8), (30, -120, 8)])
# >>> tree.terminal_node(name='T2', expr='A+B+C+D')
#
#
#
#
# >>> tree.display_variables() # doctest: +NORMALIZE_WHITESPACE
# Node 0
# A:
#    Type: DECISION - Maximum Payoff
#    Branches:
#                      Outcomes  Sucessor Node
#                       -50.000  1
#                         0.000  2
# <BLANKLINE>
# Node 1
# B:
#    Type: CHANCE
#    Branches:
#          Chance       Outcome  Sucessor Node
#           50.00       250.000  3
#           50.00         0.000  4
# <BLANKLINE>
# Node 2
# T4:
#    Type: TERMINAL
#    Expr: A
# <BLANKLINE>
# Node 3
# C:
#    Type: DECISION - Maximum Payoff
#    Branches:
#                      Outcomes  Sucessor Node
#                      -120.000  5
#                       -50.000  6
#                       -80.000  7
# <BLANKLINE>
# Node 4
# T3:
#    Type: TERMINAL
#    Expr: A+B
# <BLANKLINE>
# Node 5
# T1:
#    Type: TERMINAL
#    Expr: A+B+C
# <BLANKLINE>
# Node 6
# D:
#    Type: CHANCE
#    Branches:
#          Chance       Outcome  Sucessor Node
#           50.00         0.000  8
#           50.00      -120.000  8
# <BLANKLINE>
# Node 7
# E:
#    Type: CHANCE
#    Branches:
#          Chance       Outcome  Sucessor Node
#           70.00         0.000  8
#           30.00      -120.000  8
# <BLANKLINE>
# Node 8
# T2:
#    Type: TERMINAL
#    Expr: A+B+C+D
# <BLANKLINE>
#
#
#
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
#
#
# >>> tree.build_tree()
#
#
# >>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
# +--[D-0] test
#    +--[C-1] A=-50
#    |   +--[D-2] B=250, Prob=50.00
#    |   |   +--[T] C=-120
#    |   |   +--[C-3] C=-50
#    |   |   |   +--[T] D=0, Prob=50.00
#    |   |   |   +--[T] D=-120, Prob=50.00
#    |   |   +--[C-4] C=-80
#    |   |       +--[T] E=0, Prob=70.00
#    |   |       +--[T] E=-120, Prob=30.00
#    |   +--[T] B=0, Prob=50.00
#    +--[T] A=0
#
#
#
# >>> tree.display_tree(maxdeep=2) # doctest: +NORMALIZE_WHITESPACE
# +--[D-0] test
#    +--[C-1] A=-50
#    |   +--[D-2] B=250, Prob=50.00
#    |   +--[T] B=0, Prob=50.00
#    +--[T] A=0
#
#
# >>> tree.compute_prob()
# >>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
# +--[D-0] test
#    +--[C-1] A=-50
#    |   +--[D-2] B=250, Prob=50.00
#    |   |   +--[T] C=-120, CProb=100.00
#    |   |   +--[C-3] C=-50
#    |   |   |   +--[T] D=0, Prob=50.00, CProb=50.00
#    |   |   |   +--[T] D=-120, Prob=50.00, CProb=50.00
#    |   |   +--[C-4] C=-80
#    |   |       +--[T] E=0, Prob=70.00, CProb=70.00
#    |   |       +--[T] E=-120, Prob=30.00, CProb=30.00
#    |   +--[T] B=0, Prob=50.00, CProb=50.00
#    +--[T] A=0, CProb=100.00
#
#
#
# >>> tree.compute_values()
# >>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
# +--[D-0] test, ExpVal=20.00
#    +--[C-1] A=-50, ExpVal=20.00
#    |   +--[D-2] B=250, Prob=50.00, ExpVal=90.00
#    |   |   +--[T] C=-120, CProb=100.00, ExpVal=80.00
#    |   |   +--[C-3] C=-50, ExpVal=90.00
#    |   |   |   +--[T] D=0, Prob=50.00, CProb=50.00, ExpVal=150.00
#    |   |   |   +--[T] D=-120, Prob=50.00, CProb=50.00, ExpVal=30.00
#    |   |   +--[C-4] C=-80, ExpVal=0.00
#    |   |       +--[T] E=0, Prob=70.00, CProb=70.00, ExpVal=0.00
#    |   |       +--[T] E=-120, Prob=30.00, CProb=30.00, ExpVal=0.00
#    |   +--[T] B=0, Prob=50.00, CProb=50.00, ExpVal=-50.00
#    +--[T] A=0, CProb=100.00, ExpVal=0.00
#
#
#
# # >>> tree.risk_profile(node_number=0, cumulative=False,
# # ... all_branches=False) # doctest: +NORMALIZE_WHITESPACE
#
#
#
# # >>> tree.risk_profile(node_number=0, cumulative=True,
# # ... all_branches=False) # doctest: +NORMALIZE_WHITESPACE
#
#
#
# # >>> tree.risk_profile(node_number=0, cumulative=False,
# # ... all_branches=True) # doctest: +NORMALIZE_WHITESPACE
#
#
#
#
# # >>> tree.risk_profile(node_number=0, cumulative=True,
# # ... all_branches=True) # doctest: +NORMALIZE_WHITESPACE
#
#
#
#
# # >>> tree.risk_profile(node_number=5, cumulative=False,
# # ... all_branches=False) # doctest: +NORMALIZE_WHITESPACE
#
#
#
# # >>> tree.risk_profile(node_number=5, cumulative=True,
# # ... all_branches=False) # doctest: +NORMALIZE_WHITESPACE
#
#
#
# # >>> tree.risk_profile(node_number=0, cumulative=True, all_branches=False,
# # ... noprint=False) # doctest: +NORMALIZE_WHITESPACE
#
#
#
# # >>> tree.risk_profile(node_number=0, cumulative=False, all_branches=True,
# # ... noprint = False) # doctest: +NORMALIZE_WHITESPACE
#
#
#
# # >>> tree.risk_profile(node_number=0, cumulative=True, all_branches=True,
# # ... noprint = False) # doctest: +NORMALIZE_WHITESPACE
#
#
#
# Risk profile for chance node C-5, 'all_branches' has no sense for chance nodes.
#
#
# # >>> tree.risk_profile(node_number=5, cumulative=False, all_branches=False,
# # ... noprint = False) # doctest: +NORMALIZE_WHITESPACE
#
#
#
#
# # >>> tree.risk_profile(node_number=5, cumulative=True, all_branches=False,
# # ... noprint = False) # doctest: +NORMALIZE_WHITESPACE
#
#
#
#
#
# variation as a percent, from -25% to 25%, with 11 steps
# option with variation between suministred maximum and minimum
# or with maximum change and minium change
# # >>> m.one_way_sensititity(node_number=5, changing_node=8, changing_branch=0,
# # values=[x for x in range=])
#
# input     output
# value     value
# 150       46.875
# 160       46.5
# 170       46.125
# 180       45.75
# 190       45.375
# 200       45
# 210       44.625
# 220       44.25
# 230       43.875
# 240       43.5
# 250       43.125
#
# # >>> m.two_way_sensititity(node_number=5,
# # ...           changing_node_x=8, changing_branch_x=0, values_x=[x for x in range=],
# # .             changing_node_y=8, changing_branch_y=0, values_x=[x for x in range=])


"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
