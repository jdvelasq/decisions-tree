"""

>>> from hardDecisions.decisiontree import *
>>> from hardDecisions.treenode import *

>>> m = DecisionTree(tree_name='test')
>>> vbid = [(500,  1),
...         (700,  1)]
>>> m.decision_node(name='BID', values=vbid, max=True)
>>> vcompbid = [(35.0,  400,  2),
...             (50.0,  600,  2),
...             (15.0,  800,  2)]
>>> m.chance_node(name='COMPBID', values=vcompbid)
>>> vcost = [(25.0,  200,  3),
...          (50.0,  400,  3),
...          (25.0,  600,  3)]
>>> m.chance_node(name = 'COST', values = vcost)
>>> m.terminal_node(name='EXPR', expr='(BID-COST) * (1 if BID < COMPBID else 0)')
>>> m.display_variables() # doctest: +NORMALIZE_WHITESPACE
Node 0
BID:
    Type: DECISION - Maximum Payoff
    Branches:
                      Outcomes  Sucessor Node
                       500.000  1
                       700.000  1
<BLANKLINE>
Node 1
COMPBID:
    Type: CHANCE
    Branches:
          Chance       Outcome  Sucessor Node
           35.00       400.000  2
           50.00       600.000  2
           15.00       800.000  2
<BLANKLINE>
Node 2
COST:
    Type: CHANCE
    Branches:
          Chance       Outcome  Sucessor Node
           25.00       200.000  3
           50.00       400.000  3
           25.00       600.000  3
<BLANKLINE>
Node 3
EXPR:
    Type: TERMINAL
    Expr: (BID-COST) * (1 if BID < COMPBID else 0)
<BLANKLINE>


>>> m.build_tree()
>>> print_as_tree(m.treenodes) # doctest: +NORMALIZE_WHITESPACE
+-- TREENODES
    +-- 0 {expval: None, max: True, next_node: [1, 14], node_number: 0, type: DECISION, var: test}
    +-- 1 {expval: None, next_node: [2, 6, 10], node_number: 1, type: CHANCE, value: 500, var: BID}
    +-- 2 {expval: None, next_node: [3, 4, 5], node_number: 2, prob: 35.0, type: CHANCE, value: 400, var: COMPBID}
    +-- 3 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 200, var: COST}
    +-- 4 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 50.0, type: TERMINAL, value: 400, var: COST}
    +-- 5 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 600, var: COST}
    +-- 6 {expval: None, next_node: [7, 8, 9], node_number: 3, prob: 50.0, type: CHANCE, value: 600, var: COMPBID}
    +-- 7 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 200, var: COST}
    +-- 8 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 50.0, type: TERMINAL, value: 400, var: COST}
    +-- 9 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 600, var: COST}
    +-- 10 {expval: None, next_node: [11, 12, 13], node_number: 4, prob: 15.0, type: CHANCE, value: 800, var: COMPBID}
    +-- 11 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 200, var: COST}
    +-- 12 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 50.0, type: TERMINAL, value: 400, var: COST}
    +-- 13 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 600, var: COST}
    +-- 14 {expval: None, next_node: [15, 19, 23], node_number: 5, type: CHANCE, value: 700, var: BID}
    +-- 15 {expval: None, next_node: [16, 17, 18], node_number: 6, prob: 35.0, type: CHANCE, value: 400, var: COMPBID}
    +-- 16 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 200, var: COST}
    +-- 17 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 50.0, type: TERMINAL, value: 400, var: COST}
    +-- 18 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 600, var: COST}
    +-- 19 {expval: None, next_node: [20, 21, 22], node_number: 7, prob: 50.0, type: CHANCE, value: 600, var: COMPBID}
    +-- 20 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 200, var: COST}
    +-- 21 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 50.0, type: TERMINAL, value: 400, var: COST}
    +-- 22 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 600, var: COST}
    +-- 23 {expval: None, next_node: [24, 25, 26], node_number: 8, prob: 15.0, type: CHANCE, value: 800, var: COMPBID}
    +-- 24 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 200, var: COST}
    +-- 25 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 50.0, type: TERMINAL, value: 400, var: COST}
    +-- 26 {expr: (BID-COST) * (1 if BID < COMPBID else 0), expval: None, prob: 25.0, type: TERMINAL, value: 600, var: COST}

>>> m.display_tree() # doctest: +NORMALIZE_WHITESPACE
+--[D-0] test
    +--[C-1] BID=500
    |   +--[C-2] COMPBID=400, Prob=35.00
    |   |   +--[T] COST=200, Prob=25.00
    |   |   +--[T] COST=400, Prob=50.00
    |   |   +--[T] COST=600, Prob=25.00
    |   +--[C-3] COMPBID=600, Prob=50.00
    |   |   +--[T] COST=200, Prob=25.00
    |   |   +--[T] COST=400, Prob=50.00
    |   |   +--[T] COST=600, Prob=25.00
    |   +--[C-4] COMPBID=800, Prob=15.00
    |       +--[T] COST=200, Prob=25.00
    |       +--[T] COST=400, Prob=50.00
    |       +--[T] COST=600, Prob=25.00
    +--[C-5] BID=700
        +--[C-6] COMPBID=400, Prob=35.00
        |   +--[T] COST=200, Prob=25.00
        |   +--[T] COST=400, Prob=50.00
        |   +--[T] COST=600, Prob=25.00
        +--[C-7] COMPBID=600, Prob=50.00
        |   +--[T] COST=200, Prob=25.00
        |   +--[T] COST=400, Prob=50.00
        |   +--[T] COST=600, Prob=25.00
        +--[C-8] COMPBID=800, Prob=15.00
            +--[T] COST=200, Prob=25.00
            +--[T] COST=400, Prob=50.00
            +--[T] COST=600, Prob=25.00

>>> m.display_tree(maxdeep=0) # doctest: +NORMALIZE_WHITESPACE
+--[D-0] test

>>> m.display_tree(maxdeep=1) # doctest: +NORMALIZE_WHITESPACE
+--[D-0] test
    +--[C-1] BID=500
    +--[C-5] BID=700

>>> m.display_tree(maxdeep=2) # doctest: +NORMALIZE_WHITESPACE
+--[D-0] test
    +--[C-1] BID=500
    |   +--[C-2] COMPBID=400, Prob=35.00
    |   +--[C-3] COMPBID=600, Prob=50.00
    |   +--[C-4] COMPBID=800, Prob=15.00
    +--[C-5] BID=700
        +--[C-6] COMPBID=400, Prob=35.00
        +--[C-7] COMPBID=600, Prob=50.00
        +--[C-8] COMPBID=800, Prob=15.00

>>> m.display_tree(maxdeep=3) # doctest: +NORMALIZE_WHITESPACE
+--[D-0] test
    +--[C-1] BID=500
    |   +--[C-2] COMPBID=400, Prob=35.00
    |   |   +--[T] COST=200, Prob=25.00
    |   |   +--[T] COST=400, Prob=50.00
    |   |   +--[T] COST=600, Prob=25.00
    |   +--[C-3] COMPBID=600, Prob=50.00
    |   |   +--[T] COST=200, Prob=25.00
    |   |   +--[T] COST=400, Prob=50.00
    |   |   +--[T] COST=600, Prob=25.00
    |   +--[C-4] COMPBID=800, Prob=15.00
    |       +--[T] COST=200, Prob=25.00
    |       +--[T] COST=400, Prob=50.00
    |       +--[T] COST=600, Prob=25.00
    +--[C-5] BID=700
        +--[C-6] COMPBID=400, Prob=35.00
        |   +--[T] COST=200, Prob=25.00
        |   +--[T] COST=400, Prob=50.00
        |   +--[T] COST=600, Prob=25.00
        +--[C-7] COMPBID=600, Prob=50.00
        |   +--[T] COST=200, Prob=25.00
        |   +--[T] COST=400, Prob=50.00
        |   +--[T] COST=600, Prob=25.00
        +--[C-8] COMPBID=800, Prob=15.00
            +--[T] COST=200, Prob=25.00
            +--[T] COST=400, Prob=50.00
            +--[T] COST=600, Prob=25.00

>>> m.compute_prob()
>>> m.display_tree()
+--[D-0] test
    +--[C-1] BID=500
    |   +--[C-2] COMPBID=400, Prob=35.00
    |   |   +--[T] COST=200, Prob=25.00, CProb=8.75
    |   |   +--[T] COST=400, Prob=50.00, CProb=17.50
    |   |   +--[T] COST=600, Prob=25.00, CProb=8.75
    |   +--[C-3] COMPBID=600, Prob=50.00
    |   |   +--[T] COST=200, Prob=25.00, CProb=12.50
    |   |   +--[T] COST=400, Prob=50.00, CProb=25.00
    |   |   +--[T] COST=600, Prob=25.00, CProb=12.50
    |   +--[C-4] COMPBID=800, Prob=15.00
    |       +--[T] COST=200, Prob=25.00, CProb=3.75
    |       +--[T] COST=400, Prob=50.00, CProb=7.50
    |       +--[T] COST=600, Prob=25.00, CProb=3.75
    +--[C-5] BID=700
        +--[C-6] COMPBID=400, Prob=35.00
        |   +--[T] COST=200, Prob=25.00, CProb=8.75
        |   +--[T] COST=400, Prob=50.00, CProb=17.50
        |   +--[T] COST=600, Prob=25.00, CProb=8.75
        +--[C-7] COMPBID=600, Prob=50.00
        |   +--[T] COST=200, Prob=25.00, CProb=12.50
        |   +--[T] COST=400, Prob=50.00, CProb=25.00
        |   +--[T] COST=600, Prob=25.00, CProb=12.50
        +--[C-8] COMPBID=800, Prob=15.00
            +--[T] COST=200, Prob=25.00, CProb=3.75
            +--[T] COST=400, Prob=50.00, CProb=7.50
            +--[T] COST=600, Prob=25.00, CProb=3.75



>>> m.compute_values()
>>> m.display_tree()
+--[D-0] test, ExpVal=65.00
    +--[C-1] BID=500, ExpVal=65.00
    |   +--[C-2] COMPBID=400, Prob=35.00, ExpVal=0.00
    |   |   +--[T] COST=200, Prob=25.00, CProb=8.75, ExpVal=0.00
    |   |   +--[T] COST=400, Prob=50.00, CProb=17.50, ExpVal=0.00
    |   |   +--[T] COST=600, Prob=25.00, CProb=8.75, ExpVal=0.00
    |   +--[C-3] COMPBID=600, Prob=50.00, ExpVal=100.00
    |   |   +--[T] COST=200, Prob=25.00, CProb=12.50, ExpVal=300.00
    |   |   +--[T] COST=400, Prob=50.00, CProb=25.00, ExpVal=100.00
    |   |   +--[T] COST=600, Prob=25.00, CProb=12.50, ExpVal=-100.00
    |   +--[C-4] COMPBID=800, Prob=15.00, ExpVal=100.00
    |       +--[T] COST=200, Prob=25.00, CProb=3.75, ExpVal=300.00
    |       +--[T] COST=400, Prob=50.00, CProb=7.50, ExpVal=100.00
    |       +--[T] COST=600, Prob=25.00, CProb=3.75, ExpVal=-100.00
    +--[C-5] BID=700, ExpVal=45.00
        +--[C-6] COMPBID=400, Prob=35.00, ExpVal=0.00
        |   +--[T] COST=200, Prob=25.00, CProb=8.75, ExpVal=0.00
        |   +--[T] COST=400, Prob=50.00, CProb=17.50, ExpVal=0.00
        |   +--[T] COST=600, Prob=25.00, CProb=8.75, ExpVal=0.00
        +--[C-7] COMPBID=600, Prob=50.00, ExpVal=0.00
        |   +--[T] COST=200, Prob=25.00, CProb=12.50, ExpVal=0.00
        |   +--[T] COST=400, Prob=50.00, CProb=25.00, ExpVal=0.00
        |   +--[T] COST=600, Prob=25.00, CProb=12.50, ExpVal=0.00
        +--[C-8] COMPBID=800, Prob=15.00, ExpVal=300.00
            +--[T] COST=200, Prob=25.00, CProb=3.75, ExpVal=500.00
            +--[T] COST=400, Prob=50.00, CProb=7.50, ExpVal=300.00
            +--[T] COST=600, Prob=25.00, CProb=3.75, ExpVal=100.00

>>> m.new_display_tree()

>>> m.display_tree(policy_suggestion=True) # doctest: +NORMALIZE_WHITESPACE
+--[D-0] test, ExpVal=65.00
    +--[C-1] BID=500, ExpVal=65.00
        +--[C-2] COMPBID=400, Prob=35.00, ExpVal=0.00
        |   +--[T] COST=200, Prob=25.00, CProb=8.75, ExpVal=0.00
        |   +--[T] COST=400, Prob=50.00, CProb=17.50, ExpVal=0.00
        |   +--[T] COST=600, Prob=25.00, CProb=8.75, ExpVal=0.00
        +--[C-3] COMPBID=600, Prob=50.00, ExpVal=100.00
        |   +--[T] COST=200, Prob=25.00, CProb=12.50, ExpVal=300.00
        |   +--[T] COST=400, Prob=50.00, CProb=25.00, ExpVal=100.00
        |   +--[T] COST=600, Prob=25.00, CProb=12.50, ExpVal=-100.00
        +--[C-4] COMPBID=800, Prob=15.00, ExpVal=100.00
            +--[T] COST=200, Prob=25.00, CProb=3.75, ExpVal=300.00
            +--[T] COST=400, Prob=50.00, CProb=7.50, ExpVal=100.00
            +--[T] COST=600, Prob=25.00, CProb=3.75, ExpVal=-100.00


"""



if __name__ == "__main__":
    import doctest
    doctest.testmod()
