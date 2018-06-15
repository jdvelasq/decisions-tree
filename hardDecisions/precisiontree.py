"""
>>> from hardDecisions.decisiontree import *

>>> tree = DecisionTree()

#0
>>> tree.decision_node(name='TEST',
...                    values=[(-55,  1),
...                            (  0, 14)],
...                    max=True)

#1
>>> tree.chance_node(name='STRUCT',
...                  values=[(38.0,  0,  2),
...                          (39.0,  0,  6),
...                          (23.0,  0, 10)])

#2
>>> tree.decision_node(name='DRILL1',
...                    values=[(-600,  3),
...                            (   0,  5)],
...                    max=True)

#3
>>> tree.chance_node(name='OILFOUND1',
...                  values=[(78.95,      0,  4),
...                          (15.79, 1500,  4),
...                          (05.26, 3400,  4)])

#4
>>> tree.terminal_node(name='T1',
...                    expr='TEST+DRILL1+OILFOUND1')

#5
>>> tree.terminal_node(name='T2',
...                    expr='TEST+DRILL1')



#6
>>> tree.decision_node(name='DRILL2',
...                    values=[(-600,   7),
...                            (   0,   9)],
...                    max=True)

#7
>>> tree.chance_node(name='OILFOUND2',
...                  values=[(38.46,    0,  8),
...                          (46.15, 1500,  8),
...                          (15.38, 3400,  8)])

#8
>>> tree.terminal_node(name='T1',
...                    expr='TEST+DRILL2+OILFOUND2')

#9
>>> tree.terminal_node(name='T2',
...                    expr='TEST+DRILL2')




#10
>>> tree.decision_node(name='DRILL3',
...                    values=[(-600,   11),
...                            (   0,   13)],
...                    max=True)

#11
>>> tree.chance_node(name='OILFOUND3',
...                  values=[(21.74,    0,  12),
...                          (26.09, 1500,  12),
...                          (52.17, 3400,  12)])

#12
>>> tree.terminal_node(name='T1',
...                    expr='TEST+DRILL3+OILFOUND3')

#13
>>> tree.terminal_node(name='T2',
...                    expr='TEST+DRILL3')




#14
>>> tree.decision_node(name='DRILL4',
...                    values=[(-600,   15),
...                            (   0,   17)],
...                    max=True)

#15
>>> tree.chance_node(name='OILFOUND4',
...                  values=[(50.0,    0,  16),
...                          (30.0, 1500,  16),
...                          (20.0, 3400,  16)])

#16
>>> tree.terminal_node(name='T1',
...                    expr='TEST+DRILL4+OILFOUND4')

#17
>>> tree.terminal_node(name='T2',
...                    expr='TEST+DRILL4')


>>> tree.display_variables() # doctest: +NORMALIZE_WHITESPACE
Node 0
   Name: TEST
   Type: DECISION - Maximum Payoff
   Branches:
                     Outcomes  Sucessor Var
                      -55.000  1
                        0.000  14
<BLANKLINE>
Node 1
   Name: STRUCT
   Type: CHANCE
   Branches:
         Chance       Outcome  Sucessor Var
          38.00         0.000  2
          39.00         0.000  6
          23.00         0.000  10
<BLANKLINE>
Node 2
   Name: DRILL1
   Type: DECISION - Maximum Payoff
   Branches:
                     Outcomes  Sucessor Var
                     -600.000  3
                        0.000  5
<BLANKLINE>
Node 3
   Name: OILFOUND1
   Type: CHANCE
   Branches:
         Chance       Outcome  Sucessor Var
          78.95         0.000  4
          15.79      1500.000  4
           5.26      3400.000  4
<BLANKLINE>
Node 4
   Name: T1
   Type: TERMINAL
   Expr: TEST+DRILL1+OILFOUND1
<BLANKLINE>
Node 5
   Name: T2
   Type: TERMINAL
   Expr: TEST+DRILL1
<BLANKLINE>
Node 6
   Name: DRILL2
   Type: DECISION - Maximum Payoff
   Branches:
                     Outcomes  Sucessor Var
                     -600.000  7
                        0.000  9
<BLANKLINE>
Node 7
   Name: OILFOUND2
   Type: CHANCE
   Branches:
         Chance       Outcome  Sucessor Var
          38.46         0.000  8
          46.15      1500.000  8
          15.38      3400.000  8
<BLANKLINE>
Node 8
   Name: T1
   Type: TERMINAL
   Expr: TEST+DRILL2+OILFOUND2
<BLANKLINE>
Node 9
   Name: T2
   Type: TERMINAL
   Expr: TEST+DRILL2
<BLANKLINE>
Node 10
   Name: DRILL3
   Type: DECISION - Maximum Payoff
   Branches:
                     Outcomes  Sucessor Var
                     -600.000  11
                        0.000  13
<BLANKLINE>
Node 11
   Name: OILFOUND3
   Type: CHANCE
   Branches:
         Chance       Outcome  Sucessor Var
          21.74         0.000  12
          26.09      1500.000  12
          52.17      3400.000  12
<BLANKLINE>
Node 12
   Name: T1
   Type: TERMINAL
   Expr: TEST+DRILL3+OILFOUND3
<BLANKLINE>
Node 13
   Name: T2
   Type: TERMINAL
   Expr: TEST+DRILL3
<BLANKLINE>
Node 14
   Name: DRILL4
   Type: DECISION - Maximum Payoff
   Branches:
                     Outcomes  Sucessor Var
                     -600.000  15
                        0.000  17
<BLANKLINE>
Node 15
   Name: OILFOUND4
   Type: CHANCE
   Branches:
         Chance       Outcome  Sucessor Var
          50.00         0.000  16
          30.00      1500.000  16
          20.00      3400.000  16
<BLANKLINE>
Node 16
   Name: T1
   Type: TERMINAL
   Expr: TEST+DRILL4+OILFOUND4
<BLANKLINE>
Node 17
   Name: T2
   Type: TERMINAL
   Expr: TEST+DRILL4
<BLANKLINE>


>>> tree.build_tree()


>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
\-------[D]
        |
        | #1
        | TEST=-55
        +-------[C]
        |        |
        |        | #2
        |        | STRUCT=0
        |        | Prob=38.00
        |        +-------[D]
        |        |        |
        |        |        | #3
        |        |        | DRILL1=-600
        |        |        +-------[C]
        |        |        |        |
        |        |        |        | #4
        |        |        |        | OILFOUND1=0
        |        |        |        | Prob=78.95
        |        |        |        +-------[T] T1=TEST+DRILL1+OILFOUND1
        |        |        |        |
        |        |        |        | #5
        |        |        |        | OILFOUND1=1500
        |        |        |        | Prob=15.79
        |        |        |        +-------[T] T1=TEST+DRILL1+OILFOUND1
        |        |        |        |
        |        |        |        | #6
        |        |        |        | OILFOUND1=3400
        |        |        |        | Prob=5.26
        |        |        |        \-------[T] T1=TEST+DRILL1+OILFOUND1
        |        |        |
        |        |        | #7
        |        |        | DRILL1=0
        |        |        \-------[T] T2=TEST+DRILL1
        |        |
        |        | #8
        |        | STRUCT=0
        |        | Prob=39.00
        |        +-------[D]
        |        |        |
        |        |        | #9
        |        |        | DRILL2=-600
        |        |        +-------[C]
        |        |        |        |
        |        |        |        | #10
        |        |        |        | OILFOUND2=0
        |        |        |        | Prob=38.46
        |        |        |        +-------[T] T1=TEST+DRILL2+OILFOUND2
        |        |        |        |
        |        |        |        | #11
        |        |        |        | OILFOUND2=1500
        |        |        |        | Prob=46.15
        |        |        |        +-------[T] T1=TEST+DRILL2+OILFOUND2
        |        |        |        |
        |        |        |        | #12
        |        |        |        | OILFOUND2=3400
        |        |        |        | Prob=15.38
        |        |        |        \-------[T] T1=TEST+DRILL2+OILFOUND2
        |        |        |
        |        |        | #13
        |        |        | DRILL2=0
        |        |        \-------[T] T2=TEST+DRILL2
        |        |
        |        | #14
        |        | STRUCT=0
        |        | Prob=23.00
        |        \-------[D]
        |                 |
        |                 | #15
        |                 | DRILL3=-600
        |                 +-------[C]
        |                 |        |
        |                 |        | #16
        |                 |        | OILFOUND3=0
        |                 |        | Prob=21.74
        |                 |        +-------[T] T1=TEST+DRILL3+OILFOUND3
        |                 |        |
        |                 |        | #17
        |                 |        | OILFOUND3=1500
        |                 |        | Prob=26.09
        |                 |        +-------[T] T1=TEST+DRILL3+OILFOUND3
        |                 |        |
        |                 |        | #18
        |                 |        | OILFOUND3=3400
        |                 |        | Prob=52.17
        |                 |        \-------[T] T1=TEST+DRILL3+OILFOUND3
        |                 |
        |                 | #19
        |                 | DRILL3=0
        |                 \-------[T] T2=TEST+DRILL3
        |
        | #20
        | TEST=0
        \-------[D]
                 |
                 | #21
                 | DRILL4=-600
                 +-------[C]
                 |        |
                 |        | #22
                 |        | OILFOUND4=0
                 |        | Prob=50.00
                 |        +-------[T] T1=TEST+DRILL4+OILFOUND4
                 |        |
                 |        | #23
                 |        | OILFOUND4=1500
                 |        | Prob=30.00
                 |        +-------[T] T1=TEST+DRILL4+OILFOUND4
                 |        |
                 |        | #24
                 |        | OILFOUND4=3400
                 |        | Prob=20.00
                 |        \-------[T] T1=TEST+DRILL4+OILFOUND4
                 |
                 | #25
                 | DRILL4=0
                 \-------[T] T2=TEST+DRILL4


>>> tree.evaluate()
>>> tree.display_tree() # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=544.92
| (selected strategy)
\-------[D]
         |
         | #1
         | TEST=-55
         | ExpVal=544.92
         | (selected strategy)
         +-------[C]
         |        |
         |        | #2
         |        | STRUCT=0
         |        | Prob=38.00
         |        | ExpVal=-55.00
         |        | (selected strategy)
         |        +-------[D]
         |        |        |
         |        |        | #3
         |        |        | DRILL1=-600
         |        |        | ExpVal=-239.31
         |        |        +-------[C]
         |        |        |        |
         |        |        |        | #4
         |        |        |        | OILFOUND1=0
         |        |        |        | Prob=78.95
         |        |        |        | PathProb=0.00
         |        |        |        | ExpVal=-655.00
         |        |        |        +-------[T] T1=TEST+DRILL1+OILFOUND1
         |        |        |        |
         |        |        |        | #5
         |        |        |        | OILFOUND1=1500
         |        |        |        | Prob=15.79
         |        |        |        | PathProb=0.00
         |        |        |        | ExpVal=845.00
         |        |        |        +-------[T] T1=TEST+DRILL1+OILFOUND1
         |        |        |        |
         |        |        |        | #6
         |        |        |        | OILFOUND1=3400
         |        |        |        | Prob=5.26
         |        |        |        | PathProb=0.00
         |        |        |        | ExpVal=2745.00
         |        |        |        \-------[T] T1=TEST+DRILL1+OILFOUND1
         |        |        |
         |        |        | #7
         |        |        | DRILL1=0
         |        |        | PathProb=38.00
         |        |        | ExpVal=-55.00
         |        |        | (selected strategy)
         |        |        \-------[T] T2=TEST+DRILL1
         |        |
         |        | #8
         |        | STRUCT=0
         |        | Prob=39.00
         |        | ExpVal=560.24
         |        | (selected strategy)
         |        +-------[D]
         |        |        |
         |        |        | #9
         |        |        | DRILL2=-600
         |        |        | ExpVal=560.24
         |        |        | (selected strategy)
         |        |        +-------[C]
         |        |        |        |
         |        |        |        | #10
         |        |        |        | OILFOUND2=0
         |        |        |        | Prob=38.46
         |        |        |        | PathProb=15.00
         |        |        |        | ExpVal=-655.00
         |        |        |        | (selected strategy)
         |        |        |        +-------[T] T1=TEST+DRILL2+OILFOUND2
         |        |        |        |
         |        |        |        | #11
         |        |        |        | OILFOUND2=1500
         |        |        |        | Prob=46.15
         |        |        |        | PathProb=18.00
         |        |        |        | ExpVal=845.00
         |        |        |        | (selected strategy)
         |        |        |        +-------[T] T1=TEST+DRILL2+OILFOUND2
         |        |        |        |
         |        |        |        | #12
         |        |        |        | OILFOUND2=3400
         |        |        |        | Prob=15.38
         |        |        |        | PathProb=6.00
         |        |        |        | ExpVal=2745.00
         |        |        |        | (selected strategy)
         |        |        |        \-------[T] T1=TEST+DRILL2+OILFOUND2
         |        |        |
         |        |        | #13
         |        |        | DRILL2=0
         |        |        | PathProb=0.00
         |        |        | ExpVal=-55.00
         |        |        \-------[T] T2=TEST+DRILL2
         |        |
         |        | #14
         |        | STRUCT=0
         |        | Prob=23.00
         |        | ExpVal=1510.13
         |        | (selected strategy)
         |        \-------[D]
         |                 |
         |                 | #15
         |                 | DRILL3=-600
         |                 | ExpVal=1510.13
         |                 | (selected strategy)
         |                 +-------[C]
         |                 |        |
         |                 |        | #16
         |                 |        | OILFOUND3=0
         |                 |        | Prob=21.74
         |                 |        | PathProb=5.00
         |                 |        | ExpVal=-655.00
         |                 |        | (selected strategy)
         |                 |        +-------[T] T1=TEST+DRILL3+OILFOUND3
         |                 |        |
         |                 |        | #17
         |                 |        | OILFOUND3=1500
         |                 |        | Prob=26.09
         |                 |        | PathProb=6.00
         |                 |        | ExpVal=845.00
         |                 |        | (selected strategy)
         |                 |        +-------[T] T1=TEST+DRILL3+OILFOUND3
         |                 |        |
         |                 |        | #18
         |                 |        | OILFOUND3=3400
         |                 |        | Prob=52.17
         |                 |        | PathProb=12.00
         |                 |        | ExpVal=2745.00
         |                 |        | (selected strategy)
         |                 |        \-------[T] T1=TEST+DRILL3+OILFOUND3
         |                 |
         |                 | #19
         |                 | DRILL3=0
         |                 | PathProb=0.00
         |                 | ExpVal=-55.00
         |                 \-------[T] T2=TEST+DRILL3
         |
         | #20
         | TEST=0
         | ExpVal=530.00
         \-------[D]
                  |
                  | #21
                  | DRILL4=-600
                  | ExpVal=530.00
                  +-------[C]
                  |        |
                  |        | #22
                  |        | OILFOUND4=0
                  |        | Prob=50.00
                  |        | PathProb=0.00
                  |        | ExpVal=-600.00
                  |        +-------[T] T1=TEST+DRILL4+OILFOUND4
                  |        |
                  |        | #23
                  |        | OILFOUND4=1500
                  |        | Prob=30.00
                  |        | PathProb=0.00
                  |        | ExpVal=900.00
                  |        +-------[T] T1=TEST+DRILL4+OILFOUND4
                  |        |
                  |        | #24
                  |        | OILFOUND4=3400
                  |        | Prob=20.00
                  |        | PathProb=0.00
                  |        | ExpVal=2800.00
                  |        \-------[T] T1=TEST+DRILL4+OILFOUND4
                  |
                  | #25
                  | DRILL4=0
                  | PathProb=0.00
                  | ExpVal=0.00
                  \-------[T] T2=TEST+DRILL4

>>> tree.compute_risk_profile()
>>> tree.display_tree(policy_suggestion=True) # doctest: +NORMALIZE_WHITESPACE
|
| #0
| ExpVal=544.92
| Risk Profile:
|      Value  Prob
|    -655.00 20.00
|     -55.00 38.00
|     845.00 24.00
|    2745.00 18.00
| (selected strategy)
\-------[D]
         |
         | #1
         | TEST=-55
         | ExpVal=544.92
         | Risk Profile:
         |      Value  Prob
         |    -655.00 20.00
         |     -55.00 38.00
         |     845.00 24.00
         |    2745.00 18.00
         | (selected strategy)
         \-------[C]
                  |
                  | #2
                  | STRUCT=0
                  | Prob=38.00
                  | ExpVal=-55.00
                  | Risk Profile:
                  |      Value  Prob
                  |     -55.00 38.00
                  | (selected strategy)
                  +-------[D]
                  |        |
                  |        | #7
                  |        | DRILL1=0
                  |        | PathProb=38.00
                  |        | ExpVal=-55.00
                  |        | (selected strategy)
                  |        \-------[T] T2=TEST+DRILL1
                  |
                  | #8
                  | STRUCT=0
                  | Prob=39.00
                  | ExpVal=560.24
                  | Risk Profile:
                  |      Value  Prob
                  |    -655.00 15.00
                  |     845.00 18.00
                  |    2745.00  6.00
                  | (selected strategy)
                  +-------[D]
                  |        |
                  |        | #9
                  |        | DRILL2=-600
                  |        | ExpVal=560.24
                  |        | Risk Profile:
                  |        |      Value  Prob
                  |        |    -655.00 15.00
                  |        |     845.00 18.00
                  |        |    2745.00  6.00
                  |        | (selected strategy)
                  |        \-------[C]
                  |                 |
                  |                 | #10
                  |                 | OILFOUND2=0
                  |                 | Prob=38.46
                  |                 | PathProb=15.00
                  |                 | ExpVal=-655.00
                  |                 | (selected strategy)
                  |                 +-------[T] T1=TEST+DRILL2+OILFOUND2
                  |                 |
                  |                 | #11
                  |                 | OILFOUND2=1500
                  |                 | Prob=46.15
                  |                 | PathProb=18.00
                  |                 | ExpVal=845.00
                  |                 | (selected strategy)
                  |                 +-------[T] T1=TEST+DRILL2+OILFOUND2
                  |                 |
                  |                 | #12
                  |                 | OILFOUND2=3400
                  |                 | Prob=15.38
                  |                 | PathProb=6.00
                  |                 | ExpVal=2745.00
                  |                 | (selected strategy)
                  |                 \-------[T] T1=TEST+DRILL2+OILFOUND2
                  |
                  | #14
                  | STRUCT=0
                  | Prob=23.00
                  | ExpVal=1510.13
                  | Risk Profile:
                  |      Value  Prob
                  |    -655.00  5.00
                  |     845.00  6.00
                  |    2745.00 12.00
                  | (selected strategy)
                  \-------[D]
                           |
                           | #15
                           | DRILL3=-600
                           | ExpVal=1510.13
                           | Risk Profile:
                           |      Value  Prob
                           |    -655.00  5.00
                           |     845.00  6.00
                           |    2745.00 12.00
                           | (selected strategy)
                           \-------[C]
                                    |
                                    | #16
                                    | OILFOUND3=0
                                    | Prob=21.74
                                    | PathProb=5.00
                                    | ExpVal=-655.00
                                    | (selected strategy)
                                    +-------[T] T1=TEST+DRILL3+OILFOUND3
                                    |
                                    | #17
                                    | OILFOUND3=1500
                                    | Prob=26.09
                                    | PathProb=6.00
                                    | ExpVal=845.00
                                    | (selected strategy)
                                    +-------[T] T1=TEST+DRILL3+OILFOUND3
                                    |
                                    | #18
                                    | OILFOUND3=3400
                                    | Prob=52.17
                                    | PathProb=12.00
                                    | ExpVal=2745.00
                                    | (selected strategy)
                                    \-------[T] T1=TEST+DRILL3+OILFOUND3




"""



if __name__ == "__main__":
    import doctest
    doctest.testmod()
