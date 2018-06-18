"""
Tutorial
==============================================================================

**hardDecisions** is library for representing and evaluating decision trees.



.. image:: ./images/tree_example.png
   :width: 550px
   :align: center

>>> from hardDecisions.decisiontree import *

>>> tree = DecisionTree()


>>> tree.decision_node(name='A',
...                    branches=[(-50, 1),
...                            (  0, 2)],
...                    max=True)


>>> tree.chance_node(name='B',
...                  branches=[(50, 250, 3),
...                          (50,   0, 4)])

>>> tree.terminal_node(expr='A')

>>> tree.decision_node(name='C',
...                    branches=[(-120, 5),
...                            ( -50, 6),
...                            ( -80, 7)],
...                    max=True)


>>> tree.terminal_node(expr='A+B')

>>> tree.terminal_node(expr='A+B+C')


>>> tree.chance_node(name='D',
...                  branches=[(50,   0,  8),
...                          (50, -120, 8)])


>>> tree.chance_node(name='E',
...                  branches=[(70,   0,  9),
...                          (30, -120, 9)])

>>> tree.terminal_node(expr='A+B+C+D')

>>> tree.terminal_node(expr='A+B+C+E')







>>> tree.display_nodes() # doctest: +NORMALIZE_WHITESPACE
Node 0
   Type: DECISION - Maximum Payoff
   Name: A
   Branches:
                        Value  Next Node
                      -50.000  1
                        0.000  2
<BLANKLINE>
Node 1
   Type: CHANCE
   Name: B
   Branches:
         Chance         Value  Next Node
          50.00       250.000  3
          50.00         0.000  4
<BLANKLINE>
Node 2
   Type: TERMINAL
   Expr: A
<BLANKLINE>
Node 3
   Type: DECISION - Maximum Payoff
   Name: C
   Branches:
                        Value  Next Node
                     -120.000  5
                      -50.000  6
                      -80.000  7
<BLANKLINE>
Node 4
   Type: TERMINAL
   Expr: A+B
<BLANKLINE>
Node 5
   Type: TERMINAL
   Expr: A+B+C
<BLANKLINE>
Node 6
   Type: CHANCE
   Name: D
   Branches:
         Chance         Value  Next Node
          50.00         0.000  8
          50.00      -120.000  8
<BLANKLINE>
Node 7
   Type: CHANCE
   Name: E
   Branches:
         Chance         Value  Next Node
          70.00         0.000  9
          30.00      -120.000  9
<BLANKLINE>
Node 8
   Type: TERMINAL
   Expr: A+B+C+D
<BLANKLINE>
Node 9
   Type: TERMINAL
   Expr: A+B+C+E
<BLANKLINE>


>>> tree.build_tree()
>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
\-------[D]
        |
        | #1
        | A=-50
        +-------[C]
        |        |
        |        | #2
        |        | B=250
        |        | Prob=50.00
        |        +-------[D]
        |        |        |
        |        |        | #3
        |        |        | C=-120
        |        |        +-------[T] A+B+C
        |        |        |
        |        |        | #4
        |        |        | C=-50
        |        |        +-------[C]
        |        |        |        |
        |        |        |        | #5
        |        |        |        | D=0
        |        |        |        | Prob=50.00
        |        |        |        +-------[T] A+B+C+D
        |        |        |        |
        |        |        |        | #6
        |        |        |        | D=-120
        |        |        |        | Prob=50.00
        |        |        |        \-------[T] A+B+C+D
        |        |        |
        |        |        | #7
        |        |        | C=-80
        |        |        \-------[C]
        |        |                 |
        |        |                 | #8
        |        |                 | E=0
        |        |                 | Prob=70.00
        |        |                 +-------[T] A+B+C+E
        |        |                 |
        |        |                 | #9
        |        |                 | E=-120
        |        |                 | Prob=30.00
        |        |                 \-------[T] A+B+C+E
        |        |
        |        | #10
        |        | B=0
        |        | Prob=50.00
        |        \-------[T] A+B
        |
        | #11
        | A=0
        \-------[T] A

>>> tree.display_tree(maxdeep=2) # doctest: +NORMALIZE_WHITESPACE
|
| #0
\-------[D]
        |
        | #1
        | A=-50
        +-------[C]
        |        |
        |        | #2
        |        | B=250
        |        | Prob=50.00
        |        +-------[D]
        |        |
        |        | #10
        |        | B=0
        |        | Prob=50.00
        |        \-------[T] A+B
        |
        | #11
        | A=0
        \-------[T] A






>>> tree.evaluate()
>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=20.00
| (selected strategy)
\-------[D]
         |
         | #1
         | A=-50
         | ExpVal=20.00
         | (selected strategy)
         +-------[C]
         |        |
         |        | #2
         |        | B=250
         |        | Prob=50.00
         |        | ExpVal=90.00
         |        | (selected strategy)
         |        +-------[D]
         |        |        |
         |        |        | #3
         |        |        | C=-120
         |        |        | PathProb=0.00
         |        |        | ExpVal=80.00
         |        |        +-------[T] A+B+C
         |        |        |
         |        |        | #4
         |        |        | C=-50
         |        |        | ExpVal=90.00
         |        |        | (selected strategy)
         |        |        +-------[C]
         |        |        |        |
         |        |        |        | #5
         |        |        |        | D=0
         |        |        |        | Prob=50.00
         |        |        |        | PathProb=25.00
         |        |        |        | ExpVal=150.00
         |        |        |        | (selected strategy)
         |        |        |        +-------[T] A+B+C+D
         |        |        |        |
         |        |        |        | #6
         |        |        |        | D=-120
         |        |        |        | Prob=50.00
         |        |        |        | PathProb=25.00
         |        |        |        | ExpVal=30.00
         |        |        |        | (selected strategy)
         |        |        |        \-------[T] A+B+C+D
         |        |        |
         |        |        | #7
         |        |        | C=-80
         |        |        | ExpVal=84.00
         |        |        \-------[C]
         |        |                 |
         |        |                 | #8
         |        |                 | E=0
         |        |                 | Prob=70.00
         |        |                 | PathProb=0.00
         |        |                 | ExpVal=120.00
         |        |                 +-------[T] A+B+C+E
         |        |                 |
         |        |                 | #9
         |        |                 | E=-120
         |        |                 | Prob=30.00
         |        |                 | PathProb=0.00
         |        |                 | ExpVal=0.00
         |        |                 \-------[T] A+B+C+E
         |        |
         |        | #10
         |        | B=0
         |        | Prob=50.00
         |        | PathProb=50.00
         |        | ExpVal=-50.00
         |        | (selected strategy)
         |        \-------[T] A+B
         |
         | #11
         | A=0
         | PathProb=0.00
         | ExpVal=0.00
         \-------[T] A



>>> tree.display_tree(selected_strategy=True) # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=20.00
| (selected strategy)
\-------[D]
         |
         | #1
         | A=-50
         | ExpVal=20.00
         | (selected strategy)
         \-------[C]
                  |
                  | #2
                  | B=250
                  | Prob=50.00
                  | ExpVal=90.00
                  | (selected strategy)
                  +-------[D]
                  |        |
                  |        | #4
                  |        | C=-50
                  |        | ExpVal=90.00
                  |        | (selected strategy)
                  |        \-------[C]
                  |                 |
                  |                 | #5
                  |                 | D=0
                  |                 | Prob=50.00
                  |                 | PathProb=25.00
                  |                 | ExpVal=150.00
                  |                 | (selected strategy)
                  |                 +-------[T] A+B+C+D
                  |                 |
                  |                 | #6
                  |                 | D=-120
                  |                 | Prob=50.00
                  |                 | PathProb=25.00
                  |                 | ExpVal=30.00
                  |                 | (selected strategy)
                  |                 \-------[T] A+B+C+D
                  |
                  | #10
                  | B=0
                  | Prob=50.00
                  | PathProb=50.00
                  | ExpVal=-50.00
                  | (selected strategy)
                  \-------[T] A+B




>>> tree.tree[2]['forced_branch_idx'] = 2
>>> tree.evaluate()
>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=17.00
| (selected strategy)
\-------[D]
         |
         | #1
         | A=-50
         | ExpVal=17.00
         | (selected strategy)
         +-------[C]
         |        |
         |        | #2
         |        | B=250
         |        | Prob=50.00
         |        | ExpVal=84.00
         |        | (selected strategy)
         |        | (forced branch = 2)
         |        +-------[D]
         |        |        |
         |        |        | #3
         |        |        | C=-120
         |        |        | PathProb=0.00
         |        |        | ExpVal=80.00
         |        |        +-------[T] A+B+C
         |        |        |
         |        |        | #4
         |        |        | C=-50
         |        |        | ExpVal=90.00
         |        |        +-------[C]
         |        |        |        |
         |        |        |        | #5
         |        |        |        | D=0
         |        |        |        | Prob=50.00
         |        |        |        | PathProb=0.00
         |        |        |        | ExpVal=150.00
         |        |        |        +-------[T] A+B+C+D
         |        |        |        |
         |        |        |        | #6
         |        |        |        | D=-120
         |        |        |        | Prob=50.00
         |        |        |        | PathProb=0.00
         |        |        |        | ExpVal=30.00
         |        |        |        \-------[T] A+B+C+D
         |        |        |
         |        |        | #7
         |        |        | C=-80
         |        |        | ExpVal=84.00
         |        |        | (selected strategy)
         |        |        \-------[C]
         |        |                 |
         |        |                 | #8
         |        |                 | E=0
         |        |                 | Prob=70.00
         |        |                 | PathProb=35.00
         |        |                 | ExpVal=120.00
         |        |                 | (selected strategy)
         |        |                 +-------[T] A+B+C+E
         |        |                 |
         |        |                 | #9
         |        |                 | E=-120
         |        |                 | Prob=30.00
         |        |                 | PathProb=15.00
         |        |                 | ExpVal=0.00
         |        |                 | (selected strategy)
         |        |                 \-------[T] A+B+C+E
         |        |
         |        | #10
         |        | B=0
         |        | Prob=50.00
         |        | PathProb=50.00
         |        | ExpVal=-50.00
         |        | (selected strategy)
         |        \-------[T] A+B
         |
         | #11
         | A=0
         | PathProb=0.00
         | ExpVal=0.00
         \-------[T] A

>>> tree.tree[2]['forced_branch_idx'] = None
>>> tree.evaluate()
>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=20.00
| (selected strategy)
\-------[D]
         |
         | #1
         | A=-50
         | ExpVal=20.00
         | (selected strategy)
         +-------[C]
         |        |
         |        | #2
         |        | B=250
         |        | Prob=50.00
         |        | ExpVal=90.00
         |        | (selected strategy)
         |        +-------[D]
         |        |        |
         |        |        | #3
         |        |        | C=-120
         |        |        | PathProb=0.00
         |        |        | ExpVal=80.00
         |        |        +-------[T] A+B+C
         |        |        |
         |        |        | #4
         |        |        | C=-50
         |        |        | ExpVal=90.00
         |        |        | (selected strategy)
         |        |        +-------[C]
         |        |        |        |
         |        |        |        | #5
         |        |        |        | D=0
         |        |        |        | Prob=50.00
         |        |        |        | PathProb=25.00
         |        |        |        | ExpVal=150.00
         |        |        |        | (selected strategy)
         |        |        |        +-------[T] A+B+C+D
         |        |        |        |
         |        |        |        | #6
         |        |        |        | D=-120
         |        |        |        | Prob=50.00
         |        |        |        | PathProb=25.00
         |        |        |        | ExpVal=30.00
         |        |        |        | (selected strategy)
         |        |        |        \-------[T] A+B+C+D
         |        |        |
         |        |        | #7
         |        |        | C=-80
         |        |        | ExpVal=84.00
         |        |        \-------[C]
         |        |                 |
         |        |                 | #8
         |        |                 | E=0
         |        |                 | Prob=70.00
         |        |                 | PathProb=0.00
         |        |                 | ExpVal=120.00
         |        |                 +-------[T] A+B+C+E
         |        |                 |
         |        |                 | #9
         |        |                 | E=-120
         |        |                 | Prob=30.00
         |        |                 | PathProb=0.00
         |        |                 | ExpVal=0.00
         |        |                 \-------[T] A+B+C+E
         |        |
         |        | #10
         |        | B=0
         |        | Prob=50.00
         |        | PathProb=50.00
         |        | ExpVal=-50.00
         |        | (selected strategy)
         |        \-------[T] A+B
         |
         | #11
         | A=0
         | PathProb=0.00
         | ExpVal=0.00
         \-------[T] A



>>> tree.tree[1]['forced_branch_idx'] = 0
>>> tree.tree[4]['forced_branch_idx'] = 0
>>> tree.evaluate()
>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=150.00
| (selected strategy)
\-------[D]
         |
         | #1
         | A=-50
         | ExpVal=150.00
         | (selected strategy)
         | (forced branch = 0)
         +-------[C]
         |        |
         |        | #2
         |        | B=250
         |        | Prob=50.00
         |        | ExpVal=150.00
         |        | (selected strategy)
         |        +-------[D]
         |        |        |
         |        |        | #3
         |        |        | C=-120
         |        |        | PathProb=0.00
         |        |        | ExpVal=80.00
         |        |        +-------[T] A+B+C
         |        |        |
         |        |        | #4
         |        |        | C=-50
         |        |        | ExpVal=150.00
         |        |        | (selected strategy)
         |        |        | (forced branch = 0)
         |        |        +-------[C]
         |        |        |        |
         |        |        |        | #5
         |        |        |        | D=0
         |        |        |        | Prob=50.00
         |        |        |        | PathProb=100.00
         |        |        |        | ExpVal=150.00
         |        |        |        | (selected strategy)
         |        |        |        +-------[T] A+B+C+D
         |        |        |        |
         |        |        |        | #6
         |        |        |        | D=-120
         |        |        |        | Prob=50.00
         |        |        |        | PathProb=0.00
         |        |        |        | ExpVal=30.00
         |        |        |        \-------[T] A+B+C+D
         |        |        |
         |        |        | #7
         |        |        | C=-80
         |        |        | ExpVal=84.00
         |        |        \-------[C]
         |        |                 |
         |        |                 | #8
         |        |                 | E=0
         |        |                 | Prob=70.00
         |        |                 | PathProb=0.00
         |        |                 | ExpVal=120.00
         |        |                 +-------[T] A+B+C+E
         |        |                 |
         |        |                 | #9
         |        |                 | E=-120
         |        |                 | Prob=30.00
         |        |                 | PathProb=0.00
         |        |                 | ExpVal=0.00
         |        |                 \-------[T] A+B+C+E
         |        |
         |        | #10
         |        | B=0
         |        | Prob=50.00
         |        | PathProb=0.00
         |        | ExpVal=-50.00
         |        \-------[T] A+B
         |
         | #11
         | A=0
         | PathProb=0.00
         | ExpVal=0.00
         \-------[T] A




>>> tree.tree[1]['forced_branch_idx'] = None
>>> tree.tree[4]['forced_branch_idx'] = None
>>> tree.evaluate()
>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=20.00
| (selected strategy)
\-------[D]
         |
         | #1
         | A=-50
         | ExpVal=20.00
         | (selected strategy)
         +-------[C]
         |        |
         |        | #2
         |        | B=250
         |        | Prob=50.00
         |        | ExpVal=90.00
         |        | (selected strategy)
         |        +-------[D]
         |        |        |
         |        |        | #3
         |        |        | C=-120
         |        |        | PathProb=0.00
         |        |        | ExpVal=80.00
         |        |        +-------[T] A+B+C
         |        |        |
         |        |        | #4
         |        |        | C=-50
         |        |        | ExpVal=90.00
         |        |        | (selected strategy)
         |        |        +-------[C]
         |        |        |        |
         |        |        |        | #5
         |        |        |        | D=0
         |        |        |        | Prob=50.00
         |        |        |        | PathProb=25.00
         |        |        |        | ExpVal=150.00
         |        |        |        | (selected strategy)
         |        |        |        +-------[T] A+B+C+D
         |        |        |        |
         |        |        |        | #6
         |        |        |        | D=-120
         |        |        |        | Prob=50.00
         |        |        |        | PathProb=25.00
         |        |        |        | ExpVal=30.00
         |        |        |        | (selected strategy)
         |        |        |        \-------[T] A+B+C+D
         |        |        |
         |        |        | #7
         |        |        | C=-80
         |        |        | ExpVal=84.00
         |        |        \-------[C]
         |        |                 |
         |        |                 | #8
         |        |                 | E=0
         |        |                 | Prob=70.00
         |        |                 | PathProb=0.00
         |        |                 | ExpVal=120.00
         |        |                 +-------[T] A+B+C+E
         |        |                 |
         |        |                 | #9
         |        |                 | E=-120
         |        |                 | Prob=30.00
         |        |                 | PathProb=0.00
         |        |                 | ExpVal=0.00
         |        |                 \-------[T] A+B+C+E
         |        |
         |        | #10
         |        | B=0
         |        | Prob=50.00
         |        | PathProb=50.00
         |        | ExpVal=-50.00
         |        | (selected strategy)
         |        \-------[T] A+B
         |
         | #11
         | A=0
         | PathProb=0.00
         | ExpVal=0.00
         \-------[T] A




>>> tree17 = DecisionTree()
>>> tree17.decision_node(name='A',
...                    branches=[(-300, 1),
...                            (   0, 2)],
...                    max=True)
>>> tree17.chance_node(name='B',
...                  branches=[(60, 600, 3),
...                          (40, 100, 3)])
>>> tree17.terminal_node(expr='A')
>>> tree17.terminal_node(expr='A+B')
>>> tree17.build_tree()
>>> tree17.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
\-------[D]
         |
         | #1
         | A=-300
         +-------[C]
         |        |
         |        | #2
         |        | B=600
         |        | Prob=60.00
         |        +-------[T] A+B
         |        |
         |        | #3
         |        | B=100
         |        | Prob=40.00
         |        \-------[T] A+B
         |
         | #4
         | A=0
         \-------[T] A

>>> tree17.evaluate()
>>> tree17.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=100.00
| (selected strategy)
\-------[D]
         |
         | #1
         | A=-300
         | ExpVal=100.00
         | (selected strategy)
         +-------[C]
         |        |
         |        | #2
         |        | B=600
         |        | Prob=60.00
         |        | PathProb=60.00
         |        | ExpVal=300.00
         |        | (selected strategy)
         |        +-------[T] A+B
         |        |
         |        | #3
         |        | B=100
         |        | Prob=40.00
         |        | PathProb=40.00
         |        | ExpVal=-200.00
         |        | (selected strategy)
         |        \-------[T] A+B
         |
         | #4
         | A=0
         | PathProb=0.00
         | ExpVal=0.00
         \-------[T] A



>>> sensitivity = []
>>> for p in range(0, 101, 10):
...    tree17.data[1]['branches'] = [(p,  600,  3), (100-p,  100,  3)]
...    tree17.build_tree()
...    tree17.evaluate()
...    sensitivity.append(tree17.tree[0]['exp_val'])
>>> sensitivity
[0, 0, 0, 0, 0.0, 50.0, 100.0, 150.0, 200.0, 250.0, 300.0]



>>> sensitivity = []
>>> for p1 in range(100, -1, -10):
...     aux = []
...     for p2 in range(0, 101, 10):
...         tree.data[6]['branches'] = [(p1,  0,  8), (100-p1, -120,  8)]
...         tree.data[7]['branches'] = [(p2,  0,  9), (100-p2, -120,  9)]
...         tree.build_tree()
...         tree.evaluate()
...         aux.append(tree.tree[2]['opt_branch_idx'])
...     sensitivity.append(aux)
>>> for x in sensitivity:
...     print(x) # doctest: +NORMALIZE_WHITESPACE
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
[1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
[1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2]
[0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2]





"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
