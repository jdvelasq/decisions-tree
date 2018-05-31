"""

>>> from hardDecisions.decisiontree import *

>>> tree = DecisionTree()


>>> tree.decision_node(name='BID',
...                    values=[(500,  1),
...                            (700,  1)],
...                    max=True)


>>> tree.chance_node(name='COMPBID',
...                  values=[(35.0,  400,  2),
...                          (50.0,  600,  2),
...                          (15.0,  800,  2)])


>>> tree.chance_node(name='COST',
...                  values=[(25.0,  200,  3),
...                          (50.0,  400,  3),
...                          (25.0,  600,  3)])



>>> tree.terminal_node(name='EXPR',
...                    expr='(BID-COST) * (1 if BID < COMPBID else 0)')


>>> tree.display_variables() # doctest: +NORMALIZE_WHITESPACE
Node 0
    Name: BID
    Type: DECISION - Maximum Payoff
    Branches:
                      Outcomes  Sucessor Var
                       500.000  1
                       700.000  1
<BLANKLINE>
Node 1
    Name: COMPBID
    Type: CHANCE
    Branches:
          Chance       Outcome  Sucessor Var
           35.00       400.000  2
           50.00       600.000  2
           15.00       800.000  2
<BLANKLINE>
Node 2
    Name: COST
    Type: CHANCE
    Branches:
          Chance       Outcome  Sucessor Var
           25.00       200.000  3
           50.00       400.000  3
           25.00       600.000  3
<BLANKLINE>
Node 3
    Name: EXPR
    Type: TERMINAL
    Expr: (BID-COST) * (1 if BID < COMPBID else 0)
<BLANKLINE>


>>> tree.build_tree()


>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
\-------[D]
        |
        | #1
        | BID=500
        +-------[C]
        |        |
        |        | #2
        |        | COMPBID=400
        |        | Prob=35.00
        |        +-------[C]
        |        |        |
        |        |        | #3
        |        |        | COST=200
        |        |        | Prob=25.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #4
        |        |        | COST=400
        |        |        | Prob=50.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #5
        |        |        | COST=600
        |        |        | Prob=25.00
        |        |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |
        |        | #6
        |        | COMPBID=600
        |        | Prob=50.00
        |        +-------[C]
        |        |        |
        |        |        | #7
        |        |        | COST=200
        |        |        | Prob=25.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #8
        |        |        | COST=400
        |        |        | Prob=50.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #9
        |        |        | COST=600
        |        |        | Prob=25.00
        |        |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |
        |        | #10
        |        | COMPBID=800
        |        | Prob=15.00
        |        \-------[C]
        |                 |
        |                 | #11
        |                 | COST=200
        |                 | Prob=25.00
        |                 +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |                 |
        |                 | #12
        |                 | COST=400
        |                 | Prob=50.00
        |                 +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |                 |
        |                 | #13
        |                 | COST=600
        |                 | Prob=25.00
        |                 \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |
        | #14
        | BID=700
        \-------[C]
                 |
                 | #15
                 | COMPBID=400
                 | Prob=35.00
                 +-------[C]
                 |        |
                 |        | #16
                 |        | COST=200
                 |        | Prob=25.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #17
                 |        | COST=400
                 |        | Prob=50.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #18
                 |        | COST=600
                 |        | Prob=25.00
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #19
                 | COMPBID=600
                 | Prob=50.00
                 +-------[C]
                 |        |
                 |        | #20
                 |        | COST=200
                 |        | Prob=25.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #21
                 |        | COST=400
                 |        | Prob=50.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #22
                 |        | COST=600
                 |        | Prob=25.00
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #23
                 | COMPBID=800
                 | Prob=15.00
                 \-------[C]
                          |
                          | #24
                          | COST=200
                          | Prob=25.00
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #25
                          | COST=400
                          | Prob=50.00
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #26
                          | COST=600
                          | Prob=25.00
                          \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)


>>> tree.display_tree(maxdeep=0) # doctest: +NORMALIZE_WHITESPACE
|
| #0
\-------[D]



>>> tree.display_tree(maxdeep=1) # doctest: +NORMALIZE_WHITESPACE
|
| #0
\-------[D]
        |
        | #1
        | BID=500
        +-------[C]
        |
        | #14
        | BID=700
        \-------[C]



>>> tree.display_tree(maxdeep=2) # doctest: +NORMALIZE_WHITESPACE
|
| #0
\-------[D]
        |
        | #1
        | BID=500
        +-------[C]
        |        |
        |        | #2
        |        | COMPBID=400
        |        | Prob=35.00
        |        +-------[C]
        |        |
        |        | #6
        |        | COMPBID=600
        |        | Prob=50.00
        |        +-------[C]
        |        |
        |        | #10
        |        | COMPBID=800
        |        | Prob=15.00
        |        \-------[C]
        |
        | #14
        | BID=700
        \-------[C]
                 |
                 | #15
                 | COMPBID=400
                 | Prob=35.00
                 +-------[C]
                 |
                 | #19
                 | COMPBID=600
                 | Prob=50.00
                 +-------[C]
                 |
                 | #23
                 | COMPBID=800
                 | Prob=15.00
                 \-------[C]


>>> tree.display_tree(maxdeep=3) # doctest: +NORMALIZE_WHITESPACE
|
| #0
\-------[D]
        |
        | #1
        | BID=500
        +-------[C]
        |        |
        |        | #2
        |        | COMPBID=400
        |        | Prob=35.00
        |        +-------[C]
        |        |        |
        |        |        | #3
        |        |        | COST=200
        |        |        | Prob=25.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #4
        |        |        | COST=400
        |        |        | Prob=50.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #5
        |        |        | COST=600
        |        |        | Prob=25.00
        |        |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |
        |        | #6
        |        | COMPBID=600
        |        | Prob=50.00
        |        +-------[C]
        |        |        |
        |        |        | #7
        |        |        | COST=200
        |        |        | Prob=25.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #8
        |        |        | COST=400
        |        |        | Prob=50.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #9
        |        |        | COST=600
        |        |        | Prob=25.00
        |        |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |
        |        | #10
        |        | COMPBID=800
        |        | Prob=15.00
        |        \-------[C]
        |                 |
        |                 | #11
        |                 | COST=200
        |                 | Prob=25.00
        |                 +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |                 |
        |                 | #12
        |                 | COST=400
        |                 | Prob=50.00
        |                 +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |                 |
        |                 | #13
        |                 | COST=600
        |                 | Prob=25.00
        |                 \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |
        | #14
        | BID=700
        \-------[C]
                 |
                 | #15
                 | COMPBID=400
                 | Prob=35.00
                 +-------[C]
                 |        |
                 |        | #16
                 |        | COST=200
                 |        | Prob=25.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #17
                 |        | COST=400
                 |        | Prob=50.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #18
                 |        | COST=600
                 |        | Prob=25.00
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #19
                 | COMPBID=600
                 | Prob=50.00
                 +-------[C]
                 |        |
                 |        | #20
                 |        | COST=200
                 |        | Prob=25.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #21
                 |        | COST=400
                 |        | Prob=50.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #22
                 |        | COST=600
                 |        | Prob=25.00
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #23
                 | COMPBID=800
                 | Prob=15.00
                 \-------[C]
                          |
                          | #24
                          | COST=200
                          | Prob=25.00
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #25
                          | COST=400
                          | Prob=50.00
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #26
                          | COST=600
                          | Prob=25.00
                          \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)



>>> tree.compute_prob()
>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
\-------[D]
        |
        | #1
        | BID=500
        +-------[C]
        |        |
        |        | #2
        |        | COMPBID=400
        |        | Prob=35.00
        |        +-------[C]
        |        |        |
        |        |        | #3
        |        |        | COST=200
        |        |        | Prob=25.00
        |        |        | CProb=8.75
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #4
        |        |        | COST=400
        |        |        | Prob=50.00
        |        |        | CProb=17.50
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #5
        |        |        | COST=600
        |        |        | Prob=25.00
        |        |        | CProb=8.75
        |        |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |
        |        | #6
        |        | COMPBID=600
        |        | Prob=50.00
        |        +-------[C]
        |        |        |
        |        |        | #7
        |        |        | COST=200
        |        |        | Prob=25.00
        |        |        | CProb=12.50
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #8
        |        |        | COST=400
        |        |        | Prob=50.00
        |        |        | CProb=25.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #9
        |        |        | COST=600
        |        |        | Prob=25.00
        |        |        | CProb=12.50
        |        |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |
        |        | #10
        |        | COMPBID=800
        |        | Prob=15.00
        |        \-------[C]
        |                 |
        |                 | #11
        |                 | COST=200
        |                 | Prob=25.00
        |                 | CProb=3.75
        |                 +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |                 |
        |                 | #12
        |                 | COST=400
        |                 | Prob=50.00
        |                 | CProb=7.50
        |                 +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |                 |
        |                 | #13
        |                 | COST=600
        |                 | Prob=25.00
        |                 | CProb=3.75
        |                 \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |
        | #14
        | BID=700
        \-------[C]
                 |
                 | #15
                 | COMPBID=400
                 | Prob=35.00
                 +-------[C]
                 |        |
                 |        | #16
                 |        | COST=200
                 |        | Prob=25.00
                 |        | CProb=8.75
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #17
                 |        | COST=400
                 |        | Prob=50.00
                 |        | CProb=17.50
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #18
                 |        | COST=600
                 |        | Prob=25.00
                 |        | CProb=8.75
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #19
                 | COMPBID=600
                 | Prob=50.00
                 +-------[C]
                 |        |
                 |        | #20
                 |        | COST=200
                 |        | Prob=25.00
                 |        | CProb=12.50
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #21
                 |        | COST=400
                 |        | Prob=50.00
                 |        | CProb=25.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #22
                 |        | COST=600
                 |        | Prob=25.00
                 |        | CProb=12.50
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #23
                 | COMPBID=800
                 | Prob=15.00
                 \-------[C]
                          |
                          | #24
                          | COST=200
                          | Prob=25.00
                          | CProb=3.75
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #25
                          | COST=400
                          | Prob=50.00
                          | CProb=7.50
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #26
                          | COST=600
                          | Prob=25.00
                          | CProb=3.75
                          \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)


>>> tree.compute_values()
>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=65.00
\-------[D]
        |
        | #1
        | BID=500
        | ExpVal=65.00
        +-------[C]
        |        |
        |        | #2
        |        | COMPBID=400
        |        | Prob=35.00
        |        | ExpVal=0.00
        |        +-------[C]
        |        |        |
        |        |        | #3
        |        |        | COST=200
        |        |        | Prob=25.00
        |        |        | CProb=8.75
        |        |        | ExpVal=0.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #4
        |        |        | COST=400
        |        |        | Prob=50.00
        |        |        | CProb=17.50
        |        |        | ExpVal=0.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #5
        |        |        | COST=600
        |        |        | Prob=25.00
        |        |        | CProb=8.75
        |        |        | ExpVal=0.00
        |        |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |
        |        | #6
        |        | COMPBID=600
        |        | Prob=50.00
        |        | ExpVal=100.00
        |        +-------[C]
        |        |        |
        |        |        | #7
        |        |        | COST=200
        |        |        | Prob=25.00
        |        |        | CProb=12.50
        |        |        | ExpVal=300.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #8
        |        |        | COST=400
        |        |        | Prob=50.00
        |        |        | CProb=25.00
        |        |        | ExpVal=100.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #9
        |        |        | COST=600
        |        |        | Prob=25.00
        |        |        | CProb=12.50
        |        |        | ExpVal=-100.00
        |        |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |
        |        | #10
        |        | COMPBID=800
        |        | Prob=15.00
        |        | ExpVal=100.00
        |        \-------[C]
        |                 |
        |                 | #11
        |                 | COST=200
        |                 | Prob=25.00
        |                 | CProb=3.75
        |                 | ExpVal=300.00
        |                 +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |                 |
        |                 | #12
        |                 | COST=400
        |                 | Prob=50.00
        |                 | CProb=7.50
        |                 | ExpVal=100.00
        |                 +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |                 |
        |                 | #13
        |                 | COST=600
        |                 | Prob=25.00
        |                 | CProb=3.75
        |                 | ExpVal=-100.00
        |                 \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |
        | #14
        | BID=700
        | ExpVal=45.00
        \-------[C]
                 |
                 | #15
                 | COMPBID=400
                 | Prob=35.00
                 | ExpVal=0.00
                 +-------[C]
                 |        |
                 |        | #16
                 |        | COST=200
                 |        | Prob=25.00
                 |        | CProb=8.75
                 |        | ExpVal=0.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #17
                 |        | COST=400
                 |        | Prob=50.00
                 |        | CProb=17.50
                 |        | ExpVal=0.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #18
                 |        | COST=600
                 |        | Prob=25.00
                 |        | CProb=8.75
                 |        | ExpVal=0.00
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #19
                 | COMPBID=600
                 | Prob=50.00
                 | ExpVal=0.00
                 +-------[C]
                 |        |
                 |        | #20
                 |        | COST=200
                 |        | Prob=25.00
                 |        | CProb=12.50
                 |        | ExpVal=0.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #21
                 |        | COST=400
                 |        | Prob=50.00
                 |        | CProb=25.00
                 |        | ExpVal=0.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #22
                 |        | COST=600
                 |        | Prob=25.00
                 |        | CProb=12.50
                 |        | ExpVal=0.00
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #23
                 | COMPBID=800
                 | Prob=15.00
                 | ExpVal=300.00
                 \-------[C]
                          |
                          | #24
                          | COST=200
                          | Prob=25.00
                          | CProb=3.75
                          | ExpVal=500.00
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #25
                          | COST=400
                          | Prob=50.00
                          | CProb=7.50
                          | ExpVal=300.00
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #26
                          | COST=600
                          | Prob=25.00
                          | CProb=3.75
                          | ExpVal=100.00
                          \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)


>>> tree.display_tree(policy_suggestion=True) # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=65.00
\-------[D]
        |
        | #1
        | BID=500
        | ExpVal=65.00
        \-------[C]
                 |
                 | #2
                 | COMPBID=400
                 | Prob=35.00
                 | ExpVal=0.00
                 +-------[C]
                 |        |
                 |        | #3
                 |        | COST=200
                 |        | Prob=25.00
                 |        | CProb=8.75
                 |        | ExpVal=0.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #4
                 |        | COST=400
                 |        | Prob=50.00
                 |        | CProb=17.50
                 |        | ExpVal=0.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #5
                 |        | COST=600
                 |        | Prob=25.00
                 |        | CProb=8.75
                 |        | ExpVal=0.00
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #6
                 | COMPBID=600
                 | Prob=50.00
                 | ExpVal=100.00
                 +-------[C]
                 |        |
                 |        | #7
                 |        | COST=200
                 |        | Prob=25.00
                 |        | CProb=12.50
                 |        | ExpVal=300.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #8
                 |        | COST=400
                 |        | Prob=50.00
                 |        | CProb=25.00
                 |        | ExpVal=100.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #9
                 |        | COST=600
                 |        | Prob=25.00
                 |        | CProb=12.50
                 |        | ExpVal=-100.00
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #10
                 | COMPBID=800
                 | Prob=15.00
                 | ExpVal=100.00
                 \-------[C]
                          |
                          | #11
                          | COST=200
                          | Prob=25.00
                          | CProb=3.75
                          | ExpVal=300.00
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #12
                          | COST=400
                          | Prob=50.00
                          | CProb=7.50
                          | ExpVal=100.00
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #13
                          | COST=600
                          | Prob=25.00
                          | CProb=3.75
                          | ExpVal=-100.00
                          \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)


>>> tree.compute_risk_profile()

>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=65.00
| Risk Profile:
|      Value  Prob
|    -100.00 16.67
|       0.00 33.33
|     100.00 33.33
|     300.00 16.67
\-------[D]
        |
        | #1
        | BID=500
        | ExpVal=65.00
        | Risk Profile:
        |      Value  Prob
        |    -100.00 16.67
        |       0.00 33.33
        |     100.00 33.33
        |     300.00 16.67
        +-------[C]
        |        |
        |        | #2
        |        | COMPBID=400
        |        | Prob=35.00
        |        | ExpVal=0.00
        |        | Risk Profile:
        |        |      Value  Prob
        |        |       0.00 100.00
        |        +-------[C]
        |        |        |
        |        |        | #3
        |        |        | COST=200
        |        |        | Prob=25.00
        |        |        | CProb=8.75
        |        |        | ExpVal=0.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #4
        |        |        | COST=400
        |        |        | Prob=50.00
        |        |        | CProb=17.50
        |        |        | ExpVal=0.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #5
        |        |        | COST=600
        |        |        | Prob=25.00
        |        |        | CProb=8.75
        |        |        | ExpVal=0.00
        |        |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |
        |        | #6
        |        | COMPBID=600
        |        | Prob=50.00
        |        | ExpVal=100.00
        |        | Risk Profile:
        |        |      Value  Prob
        |        |    -100.00 25.00
        |        |     100.00 50.00
        |        |     300.00 25.00
        |        +-------[C]
        |        |        |
        |        |        | #7
        |        |        | COST=200
        |        |        | Prob=25.00
        |        |        | CProb=12.50
        |        |        | ExpVal=300.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #8
        |        |        | COST=400
        |        |        | Prob=50.00
        |        |        | CProb=25.00
        |        |        | ExpVal=100.00
        |        |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |        |
        |        |        | #9
        |        |        | COST=600
        |        |        | Prob=25.00
        |        |        | CProb=12.50
        |        |        | ExpVal=-100.00
        |        |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |        |
        |        | #10
        |        | COMPBID=800
        |        | Prob=15.00
        |        | ExpVal=100.00
        |        | Risk Profile:
        |        |      Value  Prob
        |        |    -100.00 25.00
        |        |     100.00 50.00
        |        |     300.00 25.00
        |        \-------[C]
        |                 |
        |                 | #11
        |                 | COST=200
        |                 | Prob=25.00
        |                 | CProb=3.75
        |                 | ExpVal=300.00
        |                 +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |                 |
        |                 | #12
        |                 | COST=400
        |                 | Prob=50.00
        |                 | CProb=7.50
        |                 | ExpVal=100.00
        |                 +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |                 |
        |                 | #13
        |                 | COST=600
        |                 | Prob=25.00
        |                 | CProb=3.75
        |                 | ExpVal=-100.00
        |                 \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
        |
        | #14
        | BID=700
        | ExpVal=45.00
        | Risk Profile:
        |      Value  Prob
        |       0.00 66.67
        |     100.00  8.33
        |     300.00 16.67
        |     500.00  8.33
        \-------[C]
                 |
                 | #15
                 | COMPBID=400
                 | Prob=35.00
                 | ExpVal=0.00
                 | Risk Profile:
                 |      Value  Prob
                 |       0.00 100.00
                 +-------[C]
                 |        |
                 |        | #16
                 |        | COST=200
                 |        | Prob=25.00
                 |        | CProb=8.75
                 |        | ExpVal=0.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #17
                 |        | COST=400
                 |        | Prob=50.00
                 |        | CProb=17.50
                 |        | ExpVal=0.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #18
                 |        | COST=600
                 |        | Prob=25.00
                 |        | CProb=8.75
                 |        | ExpVal=0.00
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #19
                 | COMPBID=600
                 | Prob=50.00
                 | ExpVal=0.00
                 | Risk Profile:
                 |      Value  Prob
                 |       0.00 100.00
                 +-------[C]
                 |        |
                 |        | #20
                 |        | COST=200
                 |        | Prob=25.00
                 |        | CProb=12.50
                 |        | ExpVal=0.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #21
                 |        | COST=400
                 |        | Prob=50.00
                 |        | CProb=25.00
                 |        | ExpVal=0.00
                 |        +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |        |
                 |        | #22
                 |        | COST=600
                 |        | Prob=25.00
                 |        | CProb=12.50
                 |        | ExpVal=0.00
                 |        \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                 |
                 | #23
                 | COMPBID=800
                 | Prob=15.00
                 | ExpVal=300.00
                 | Risk Profile:
                 |      Value  Prob
                 |     100.00 25.00
                 |     300.00 50.00
                 |     500.00 25.00
                 \-------[C]
                          |
                          | #24
                          | COST=200
                          | Prob=25.00
                          | CProb=3.75
                          | ExpVal=500.00
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #25
                          | COST=400
                          | Prob=50.00
                          | CProb=7.50
                          | ExpVal=300.00
                          +-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)
                          |
                          | #26
                          | COST=600
                          | Prob=25.00
                          | CProb=3.75
                          | ExpVal=100.00
                          \-------[T] EXPR=(BID-COST) * (1 if BID < COMPBID else 0)






Probabilistic senstitivity

>>> b500 = []
>>> b700 = []
>>> for p in range(0, 101, 10):
...    tree.variables[2]['values'] = [(p,  200,  3), (0.0,  400,  3),  (100-p,  600,  3)]
...    tree.build_tree()
...    tree.compute_prob()
...    tree.compute_values()
...    b500.append(tree.tree[1]['expval'])
...    b700.append(tree.tree[14]['expval'])

# >>> b500

# >>> b700






"""



if __name__ == "__main__":
    import doctest
    doctest.testmod()
