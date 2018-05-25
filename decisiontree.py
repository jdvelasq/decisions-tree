

class DecisionModel:
    """Creates and evaluates a decision tree model.


    Creates a empty tree
    >>> m = DecisionModel()

    Adds a terminal node (4).
    >>> m.terminal_node(nodename = 'CALC',
    ...                expr = '(BID-COST) * (1 if BID < COMPBID else 0)')

    Creates a probabilistic node (3).
    >>> vCost = [(25.0,  200,  'CALC'),  # branch 1
    ...          (50.0,  400,  'CALC'),  # branch 2
    ...          (25.0,  600,  'CALC')]  # branch 3
    >>> m.chance_node(nodename = 'COST', values = vCost)

    Creates another probabilistic node (2).
    >>> vCompbid = [(35.0,  400,  'COST'),  # branch 1
    ...             (50.0,  600,  'COST'),  # brabch 2
    ...             (15.0,  800,  'COST')]  # branch 3
    >>> m.chance_node( nodename = 'COMPBID', values = vCompbid)

    Creates a decision node (root).
    >>> vBid = [(500,  'COMPBID'),   # branch 1
    ...         (700,  'COMPBID')]   # branch 2
    >>> m.decision_node( nodename = 'BID', values = vBid)

    Display the variables.
    >>> m.display_variables()  # doctest: +NORMALIZE_WHITESPACE
    BID:
        Type: DECISION
        Branches:
                          Outcomes  Sucessor Node
                           500.000  COMPBID
                           700.000  COMPBID
    <BLANKLINE>
    CALC:
        Type: TERMINAL
        Expr: (BID-COST) * (1 if BID < COMPBID else 0)
    <BLANKLINE>
    COMPBID:
        Type: CHANCE
        Branches:
              Chance       Outcome  Sucessor Node
               35.00       400.000  COST
               50.00       600.000  COST
               15.00       800.000  COST
    <BLANKLINE>
    COST:
        Type: CHANCE
        Branches:
              Chance       Outcome  Sucessor Node
               25.00       200.000  CALC
               50.00       400.000  CALC
               25.00       600.000  CALC
    <BLANKLINE>

    Tree computation.

    >>> m.Evaluate()
    >>> m.display_tree()
    +--[D-0] BID,  Exp Val = 65.0
        +--[C-1] BID=500,  Exp Val = 65.0
        |   +--[C-2] Prob = 35.00%, COMPBID = 400,  Exp Val = 0.0
        |   |   +--[T] Prob = 25.00%, COST = 200 ---- CALC = 0
        |   |   +--[T] Prob = 50.00%, COST = 400 ---- CALC = 0
        |   |   +--[T] Prob = 25.00%, COST = 600 ---- CALC = 0
        |   +--[C-3] Prob = 50.00%, COMPBID = 600,  Exp Val = 100.0
        |   |   +--[T] Prob = 25.00%, COST = 200 ---- CALC = 300
        |   |   +--[T] Prob = 50.00%, COST = 400 ---- CALC = 100
        |   |   +--[T] Prob = 25.00%, COST = 600 ---- CALC = -100
        |   +--[C-4] Prob = 15.00%, COMPBID = 800,  Exp Val = 100.0
        |       +--[T] Prob = 25.00%, COST = 200 ---- CALC = 300
        |       +--[T] Prob = 50.00%, COST = 400 ---- CALC = 100
        |       +--[T] Prob = 25.00%, COST = 600 ---- CALC = -100
        +--[C-5] BID=700,  Exp Val = 45.0
            +--[C-6] Prob = 35.00%, COMPBID = 400,  Exp Val = 0.0
            |   +--[T] Prob = 25.00%, COST = 200 ---- CALC = 0
            |   +--[T] Prob = 50.00%, COST = 400 ---- CALC = 0
            |   +--[T] Prob = 25.00%, COST = 600 ---- CALC = 0
            +--[C-7] Prob = 50.00%, COMPBID = 600,  Exp Val = 0.0
            |   +--[T] Prob = 25.00%, COST = 200 ---- CALC = 0
            |   +--[T] Prob = 50.00%, COST = 400 ---- CALC = 0
            |   +--[T] Prob = 25.00%, COST = 600 ---- CALC = 0
            +--[C-8] Prob = 15.00%, COMPBID = 800,  Exp Val = 300.0
                +--[T] Prob = 25.00%, COST = 200 ---- CALC = 500
                +--[T] Prob = 50.00%, COST = 400 ---- CALC = 300
                +--[T] Prob = 25.00%, COST = 600 ---- CALC = 100

    >>> m.display_tree(policy_suggestion=True)
    +--[D-0] BID,  Exp Val = 65.0
        +--[C-1] BID=500,  Exp Val = 65.0
            +--[C-2] Prob = 35.00%, COMPBID = 400,  Exp Val = 0.0
            |   +--[T] Prob = 25.00%, COST = 200 ---- CALC = 0
            |   +--[T] Prob = 50.00%, COST = 400 ---- CALC = 0
            |   +--[T] Prob = 25.00%, COST = 600 ---- CALC = 0
            +--[C-3] Prob = 50.00%, COMPBID = 600,  Exp Val = 100.0
            |   +--[T] Prob = 25.00%, COST = 200 ---- CALC = 300
            |   +--[T] Prob = 50.00%, COST = 400 ---- CALC = 100
            |   +--[T] Prob = 25.00%, COST = 600 ---- CALC = -100
            +--[C-4] Prob = 15.00%, COMPBID = 800,  Exp Val = 100.0
                +--[T] Prob = 25.00%, COST = 200 ---- CALC = 300
                +--[T] Prob = 50.00%, COST = 400 ---- CALC = 100
                +--[T] Prob = 25.00%, COST = 600 ---- CALC = -100



    >>> m.display_tree(maxdeep=1)
    +--[D-0] BID,  Exp Val = 65.0

    >>> m.display_tree(maxdeep=2)
    +--[D-0] BID,  Exp Val = 65.0
        +--[C-1] BID=500,  Exp Val = 65.0
        +--[C-5] BID=700,  Exp Val = 45.0

    >>> m.display_tree(maxdeep=2, policy_suggestion=True)
    +--[D-0] BID,  Exp Val = 65.0
        +--[C-1] BID=500,  Exp Val = 65.0

    >>> m.display_tree(maxdeep=3)
    +--[D-0] BID,  Exp Val = 65.0
        +--[C-1] BID=500,  Exp Val = 65.0
        |   +--[C-2] Prob = 35.00%, COMPBID = 400,  Exp Val = 0.0
        |   +--[C-3] Prob = 50.00%, COMPBID = 600,  Exp Val = 100.0
        |   +--[C-4] Prob = 15.00%, COMPBID = 800,  Exp Val = 100.0
        +--[C-5] BID=700,  Exp Val = 45.0
            +--[C-6] Prob = 35.00%, COMPBID = 400,  Exp Val = 0.0
            +--[C-7] Prob = 50.00%, COMPBID = 600,  Exp Val = 0.0
            +--[C-8] Prob = 15.00%, COMPBID = 800,  Exp Val = 300.0

    >>> m.display_tree(maxdeep=3, policy_suggestion=True) # doctest: +NORMALIZE_WHITESPACE
    +--[D-0] BID,  Exp Val = 65.0
        +--[C-1] BID=500,  Exp Val = 65.0
            +--[C-2] Prob = 35.00%, COMPBID = 400,  Exp Val = 0.0
            +--[C-3] Prob = 50.00%, COMPBID = 600,  Exp Val = 100.0
            +--[C-4] Prob = 15.00%, COMPBID = 800,  Exp Val = 100.0

    >>> m.display_tree(maxdeep=4)
    +--[D-0] BID,  Exp Val = 65.0
        +--[C-1] BID=500,  Exp Val = 65.0
        |   +--[C-2] Prob = 35.00%, COMPBID = 400,  Exp Val = 0.0
        |   |   +--[T] Prob = 25.00%, COST = 200 ---- CALC = 0
        |   |   +--[T] Prob = 50.00%, COST = 400 ---- CALC = 0
        |   |   +--[T] Prob = 25.00%, COST = 600 ---- CALC = 0
        |   +--[C-3] Prob = 50.00%, COMPBID = 600,  Exp Val = 100.0
        |   |   +--[T] Prob = 25.00%, COST = 200 ---- CALC = 300
        |   |   +--[T] Prob = 50.00%, COST = 400 ---- CALC = 100
        |   |   +--[T] Prob = 25.00%, COST = 600 ---- CALC = -100
        |   +--[C-4] Prob = 15.00%, COMPBID = 800,  Exp Val = 100.0
        |       +--[T] Prob = 25.00%, COST = 200 ---- CALC = 300
        |       +--[T] Prob = 50.00%, COST = 400 ---- CALC = 100
        |       +--[T] Prob = 25.00%, COST = 600 ---- CALC = -100
        +--[C-5] BID=700,  Exp Val = 45.0
            +--[C-6] Prob = 35.00%, COMPBID = 400,  Exp Val = 0.0
            |   +--[T] Prob = 25.00%, COST = 200 ---- CALC = 0
            |   +--[T] Prob = 50.00%, COST = 400 ---- CALC = 0
            |   +--[T] Prob = 25.00%, COST = 600 ---- CALC = 0
            +--[C-7] Prob = 50.00%, COMPBID = 600,  Exp Val = 0.0
            |   +--[T] Prob = 25.00%, COST = 200 ---- CALC = 0
            |   +--[T] Prob = 50.00%, COST = 400 ---- CALC = 0
            |   +--[T] Prob = 25.00%, COST = 600 ---- CALC = 0
            +--[C-8] Prob = 15.00%, COMPBID = 800,  Exp Val = 300.0
                +--[T] Prob = 25.00%, COST = 200 ---- CALC = 500
                +--[T] Prob = 50.00%, COST = 400 ---- CALC = 300
                +--[T] Prob = 25.00%, COST = 600 ---- CALC = 100


    Pruebas para el nodo de decision.

    >>> m.risk_profile(node_number=0, cumulative=False,
    ... all_branches=False) # doctest: +NORMALIZE_WHITESPACE
    {500: {0: 35.0, 100: 32.5, -100: 16.25, 300: 16.25}}

    >>> m.risk_profile(node_number=0, cumulative=True,
    ... all_branches=False) # doctest: +NORMALIZE_WHITESPACE
    {500: {0: 51.25, 100: 83.75, -100: 16.25, 300: 100.0}}

    >>> m.risk_profile(node_number=0, cumulative=False,
    ... all_branches=True) # doctest: +NORMALIZE_WHITESPACE
    {700: {0: 85.0, 300: 7.5, 500: 3.75, 100: 3.75}, 500: {0: 35.0, 100: 32.5, -100: 16.25, 300: 16.25}}

    >>> m.risk_profile(node_number=0, cumulative=True,
    ... all_branches=True) # doctest: +NORMALIZE_WHITESPACE
    {700: {0: 85.0, 300: 96.25, 500: 100.0, 100: 88.75}, 500: {0: 51.25, 100: 83.75, -100: 16.25, 300: 100.0}}


    Risk profile for chance node C-5, 'all_branches' has no sense for chance nodes.

    >>> m.risk_profile(node_number=5, cumulative=False,
    ... all_branches=False) # doctest: +NORMALIZE_WHITESPACE
    {0: 85.0, 300: 7.5, 100: 3.75, 500: 3.75}

    >>> m.risk_profile(node_number=5, cumulative=True,
    ... all_branches=False) # doctest: +NORMALIZE_WHITESPACE
    {0: 85.0, 300: 96.25, 100: 88.75, 500: 100.0}


    >>> m.risk_profile(node_number=0, cumulative=True, all_branches=False,
    ... noprint=False) # doctest: +NORMALIZE_WHITESPACE
    Risk profile for decision node [D-0] BID=500.00
    <BLANKLINE>
             Value   Prob.
    ----------------------
           -100.00  16.25%
              0.00  51.25%
            100.00  83.75%
            300.00 100.00%


    >>> m.risk_profile(node_number=0, cumulative=False, all_branches=True,
    ... noprint = False) # doctest: +NORMALIZE_WHITESPACE
    Risk profile for decision node [D-0] BID=500.00
    <BLANKLINE>
             Value   Prob.
    ----------------------
           -100.00  16.25%
              0.00  35.00%
            100.00  32.50%
            300.00  16.25%
    <BLANKLINE>
    mean    =    65.00
    std dev =   123.59
    maximum =   300.00
    minimum =  -100.00
    Risk profile for decision node [D-0] BID=700.00
    <BLANKLINE>
             Value   Prob.
    ----------------------
              0.00  85.00%
            100.00   3.75%
            300.00   7.50%
            500.00   3.75%
    <BLANKLINE>
    mean    =    45.00
    std dev =   120.31
    maximum =   500.00
    minimum =     0.00



    >>> m.risk_profile(node_number=0, cumulative=True, all_branches=True,
    ... noprint = False) # doctest: +NORMALIZE_WHITESPACE
    Risk profile for decision node [D-0] BID=500.00
    <BLANKLINE>
             Value   Prob.
    ----------------------
           -100.00  16.25%
              0.00  51.25%
            100.00  83.75%
            300.00 100.00%
    Risk profile for decision node [D-0] BID=700.00
    <BLANKLINE>
             Value   Prob.
    ----------------------
              0.00  85.00%
            100.00  88.75%
            300.00  96.25%
            500.00 100.00%


    Risk profile for chance node C-5, 'all_branches' has no sense for chance nodes.

    >>> m.risk_profile(node_number=5, cumulative=False, all_branches=False,
    ... noprint = False) # doctest: +NORMALIZE_WHITESPACE
    Risk profile for chance node [C-5] COMPBID
    <BLANKLINE>
             Value   Prob.
    ----------------------
              0.00  85.00%
            100.00   3.75%
            300.00   7.50%
            500.00   3.75%
    <BLANKLINE>
        mean    =    45.00
        std dev =   120.31
        maximum =   500.00
        minimum =     0.00

    >>> m.risk_profile(node_number=5, cumulative=True, all_branches=False,
    ... noprint = False) # doctest: +NORMALIZE_WHITESPACE
    Risk profile for chance node [C-5] COMPBID
    <BLANKLINE>
             Value   Prob.
    ----------------------
              0.00  85.00%
            100.00  88.75%
            300.00  96.25%
            500.00 100.00%





    variation as a percent, from -25% to 25%, with 11 steps
    option with variation between suministred maximum and minimum
    or with maximum change and minium change
    # >>> m.one_way_sensititity(node_number=5, changing_node=8, changing_branch=0,
    # values=[x for x in range=])

    input     output
    value     value
    150       46.875
    160       46.5
    170       46.125
    180       45.75
    190       45.375
    200       45
    210       44.625
    220       44.25
    230       43.875
    240       43.5
    250       43.125

    # >>> m.two_way_sensititity(node_number=5,
    # ...           changing_node_x=8, changing_branch_x=0, values_x=[x for x in range=],
    # .             changing_node_y=8, changing_branch_y=0, values_x=[x for x in range=])



    """

    class Variable:

        def __init__(self, nodetag=None, nodetype=None, nodename=None, expr=None, values=None):

            self._type = nodetype
            self._name = nodename
            self._tag = nodetag
            self._expr = expr
            self._values = values
            self._expval = None
            self._node_number = None


        def copy(self):
            """Returns a deep copy of the tree"""
            obj = DecisionModel.Variable()
            obj._type = self._type
            obj._name = self._name
            obj._tag = self._tag
            obj._expr = self._expr
            obj._values = self._values
            obj._expval = self._expval
            return obj

        def __str__(self):
            txt = []
            txt.append(self._name + ':')
            txt.append('    Type: ' + self._type)
            if self._type == 'DECISION':
                txt.append('    Branches:')
                txt.append('                      Outcomes  Sucessor Node')
                for (valor, nodo) in self._values:
                    txt.append('                  {:12.3f}  {}'.format(valor, nodo))
                txt.append('')
            elif self._type == 'CHANCE':
                txt.append('    Branches:')
                txt.append('          Chance       Outcome  Sucessor Node')
                for (prob, valor, nodo) in self._values:
                    txt.append('           {:5.2f}  {:12.3f}  {}'.format(prob, valor, nodo))
                txt.append('')

            elif self._type == 'TERMINAL':
                txt.append('    Expr: ' + self._expr)
                txt.append('')
            else:
                raise ValueError('Node type unknown: ' + self_type)
            return '\n'.join(txt)


    def build_tree():
        pass

    def compute_prob():
        pass

    def compute_end_values():
        pass

    def reduce_nodes():
        pass


    def risk_profile(self, node_number, cumulative=False, all_branches=False, noprint=True):
        """
        """

        def compute_cumprob(data):
            """Computes the cumulative probability for data (dict)"""
            retval = data
            acumprob = None
            for key in sorted(retval.keys()):
                if acumprob is None:
                    acumprob = retval[key]
                else:
                    retval[key] += acumprob
                    acumprob = retval[key]
            return retval

        def reduce_node(parent_node):
            retval = {}
            for parent_key in sorted(parent_node.keys()):
                child_branch = parent_node[parent_key]
                for child_key in sorted(child_branch.keys()):
                    if child_key in retval.keys():
                        retval[child_key] += child_branch[child_key]
                    else:
                        retval[child_key] = child_branch[child_key]
            return retval


        def print_report(letter, xdict, key=None):

            if letter == 'C':
                fmt = 'Risk profile for chance node [C-{:d}] {:s}'
                print(fmt.format(node_number, self.riskprof_nodename))
            elif letter == 'D':
                fmt = 'Risk profile for decision node [D-{:d}] {:s}={:1.2f}'
                print(fmt.format(node_number, self.riskprof_nodename, key))
            else:
                raise ValueError('Invalid value for letter = ' + letter)

            print('')
            print('         Value   Prob.')
            print('----------------------')

            xmean = None
            xstd = None
            xmax = None
            xmin = None

            for key in sorted(xdict.keys()):
                print('  {:12.2f} {:6.2f}% '.format(key, xdict[key]))
                if xmean is None:
                    xmean = key * xdict[key] / 100
                    xmax = key
                    xmin = key
                    xstd = key ** 2 * xdict[key] / 100
                else:
                    xmean += key * xdict[key] / 100
                    xmax = key if key > xmax else xmax
                    xmin = key if key < xmin else xmin
                    xstd += key ** 2 * xdict[key] / 100
            xstd -= xmean ** 2
            xstd = xstd ** 0.5

            if cumulative is False:
                print('')
                print('mean    = {:8.2f}'. format(xmean))
                print('std dev = {:8.2f}'. format(xstd))
                print('maximum = {:8.2f}'. format(xmax))
                print('minimum = {:8.2f}'. format(xmin))


        self.riskprof_node = node_number
        self.Evaluate()
        self.riskprof_node = None

        # for decision chances simple=True reports only for the optimal branch
        # for simple=False reports all branches
        if self.riskprof_nodetype == 'DECISION':
            #
            if all_branches is False:
                retval = {}
                key = self.riskprof_opt_branch_key
                retval[key] = self.riskprof_data[key]
                if cumulative is True:
                    retval[self.riskprof_opt_branch_key] = compute_cumprob(retval[self.riskprof_opt_branch_key])
            else:
                retval = self.riskprof_data
                if cumulative is True:
                    for parent_key in self.riskprof_data.keys():
                        retval[parent_key] = compute_cumprob(retval[parent_key])
            #
        elif self.riskprof_nodetype == 'CHANCE':
            #
            retval = reduce_node(self.riskprof_data)
            if cumulative is True:
                retval = compute_cumprob(retval)
        else:
            pass

        if noprint is True:
            return retval

        if self.riskprof_nodetype == 'DECISION':
            for key in sorted(retval.keys()):
                print_report(letter='D', xdict=retval[key], key=key)

        elif self.riskprof_nodetype == 'CHANCE':
            print_report(letter='C', xdict=retval)



    def Evaluate(self):
        """Computes the branches of the tree
        """

        def compute_node(node, probability):
            """Evaluates the current node"""

            tree_node = node.copy()
            if node._type == 'TERMINAL':
                tree_node._expval = eval(node._expr, self._globals.copy())
                #
                #
                if self.riskprof_collect is True:
                    if tree_node._expval in self.riskprof_data_branch:
                        self.riskprof_data_branch[tree_node._expval] += probability * 100
                    else:
                        self.riskprof_data_branch[tree_node._expval] = probability * 100
                #
                #
                return tree_node

            if tree_node._type == 'CHANCE':
                tree_node._node_number = self.node_number
                #

                if self.riskprof_node is not None and tree_node._node_number == self.riskprof_node:
                    self.riskprof_nodetype = 'CHANCE'
                    self.riskprof_collect = True
                    self.riskprof_data = {}
                    self.riskprof_data_branch = {}
                    self.riskprof_opt_branch_key = None
                    self.riskprof_nodename = node._name
                #
                self.node_number += 1
                tree_node._children = []
                expval = 0
                ## first evaluate all children of the current node
                for (prob, value, nextnode) in node._values:
                    self._globals[node._name] = value
                    x = compute_node(self._variables[nextnode], probability=probability*prob/100)
                    tree_node._children.append(x)
                    expval += prob * x._expval / 100
                    #
                    if self.riskprof_node is not None and tree_node._node_number == self.riskprof_node:
                        self.riskprof_data[value] = self.riskprof_data_branch
                        self.riskprof_data_branch = {}
                    #
                tree_node._expval = expval
                #
                if self.riskprof_node is not None and tree_node._node_number == self.riskprof_node:
                    self.riskprof_collect = False
                #
                return tree_node

            elif tree_node._type == 'DECISION':
                tree_node._node_number = self.node_number
                tree_node._optimal_branch = None
                #
                if self.riskprof_node is not None and tree_node._node_number == self.riskprof_node:
                    self.riskprof_nodetype = 'DECISION'
                    self.riskprof_collect = True
                    self.riskprof_data = {}
                    self.riskprof_data_branch = {}
                    self.riskprof_opt_branch_key = None
                    self.riskprof_nodename = node._name
                #
                self.node_number += 1
                ## computes the maximum value of the children
                expval = None
                tree_node._children = []
                for (value, nextnode) in node._values:
                    self._globals[node._name] = value
                    x = compute_node(self._variables[nextnode], probability=1)
                    tree_node._children.append(x)
                    if expval is None:
                        expval = x._expval
                        tree_node._optimal_branch = value
                        self.riskprof_opt_branch_key = value
                    elif expval < x._expval:
                        expval = x._expval
                        tree_node._optimal_branch = value
                        self.riskprof_opt_branch_key = value
                    #
                    if self.riskprof_node is not None and tree_node._node_number == self.riskprof_node:
                        self.riskprof_data[value] = self.riskprof_data_branch
                        self.riskprof_data_branch = {}
                    #
                tree_node._expval = expval
                #
                if self.riskprof_node is not None and tree_node._node_number == self.riskprof_node:
                    self.riskprof_collect = False
                #
                return tree_node
            else:
                raise Exception('internal error')

        self.node_number = 0
        self.riskprof_collect = False
        self._result = compute_node(node=self._root, probability=1)







    def __init__(self):
        self._variables = {}
        self._root = None
        self._globals = {}
        #
        self.riskprof_node = None
        self.riskprof_nodetype = None
        self.riskprof_collect = None
        self.riskprof_data = None
        self.riskprof_data_branch = None
        self.riskprof_opt_branch_key = None
        self.riskprof_nodename = None


    def terminal_node(self, nodename=None, expr=None):
        """Creates a tree's terminal node """
        self._variables[nodename] = self.Variable(nodetype='TERMINAL',
                                                  nodename=nodename,
                                                  expr=expr)
        self._root = self._variables[nodename]
        #

    def chance_node(self, nodename=None, values=None):
        """Creates a tree's internal chance node"""
        self._variables[nodename] = self.Variable(nodetype='CHANCE',
                                                  nodename=nodename,
                                                  values=values)
        self._root = self._variables[nodename]

    def decision_node(self, nodename=None, values=None):
        """Creates a tree's internal decision node"""
        self._variables[nodename] = self.Variable(nodetype='DECISION',
                                                  nodename=nodename,
                                                  values=values)
        self._root = self._variables[nodename]

    def display_variables(self):
        """Display all the varibles in the tree"""
        keys = sorted(self._variables.keys())
        for key in keys:
            print(self._variables[key])

    def display_treeStructure(self):
        """Display the structure of the tree"""
        pass

    def DisplaySchematicTree(self):
        """Display a schema of the tree"""
        pass


    def display_tree(self, maxdeep=None, policy_suggestion=False):
        """Display the tree as text"""

        def printNode(prefix, node, lastNode):

            self.current_deep += 1
            if node._type == 'DECISION':

                x = node._name + ',  Exp Val = ' + str(node._expval)
                print(prefix + '+--[D-{:d}] '.format(node._node_number) + x)

                if maxdeep is not None and self.current_deep == maxdeep:
                    self.current_deep -= 1
                    return

                for (i, (valor, nextnode)) in enumerate(node._values):

                    if policy_suggestion is False or (policy_suggestion is True and valor == node._optimal_branch):

                        if policy_suggestion is False:
                            is_last_node = True if i == len(node._values) - 1 else False
                        else:
                            is_last_node = True

                        if node._children[i]._type == 'DECISION':

                            x = node._name + '='  + str(valor)  + \
                                ',  Exp Val = ' + str(node._children[i]._expval)
                            print(prefix + '    +--[D-{:d}] '.format(node._children[i]._node_number) + x)

                        elif node._children[i]._type == 'CHANCE':
                            x = node._name + '='  + str(valor) + \
                                ',  Exp Val = ' + str(node._children[i]._expval)
                            print(prefix + '    +--[C-{:d}] '.format(node._children[i]._node_number) + x)
                        else:
                            x = node._name + '=' + str(valor) + ' ----  ' + \
                                node._children[i]._name + ' = ' + \
                                str(node._children[i]._expval)
                            print(prefix + '    +--[T] ' + x)

                        if node._children[i]._type != 'TERMINAL':
                            if is_last_node == True:
                                printNode(prefix + '     ', node._children[i], is_last_node)
                            else:
                                printNode(prefix + '    |', node._children[i], is_last_node)


            elif node._type == 'CHANCE':

                if maxdeep is not None and self.current_deep == maxdeep:
                    self.current_deep -= 1
                    return

                for (i, (prob, valor, nextnode)) in enumerate(node._values):

                    is_last_node = True if i == len(node._values) - 1 else False

                    if node._children[i]._type in 'DECISION':

                        x = 'Prob = ' + '{:5.2f}'.format(prob) + '%, '
                        x += node._name + ' = ' + str(valor)
                        x += ',  Exp Val = ' + str(node._children[i]._expval)
                        print(prefix + '   +--[D-{:d}] '.format(node._children[i]._node_number) + x)

                    elif node._children[i]._type == 'CHANCE':

                        x = 'Prob = ' + '{:5.2f}'.format(prob) + '%, ' + \
                            node._name + ' = ' + str(valor) + \
                            ',  Exp Val = ' + str(node._children[i]._expval)
                        print(prefix + '   +--[C-{:d}] '.format(node._children[i]._node_number) + x)

                    else:
                        x = 'Prob = ' + '{:5.2f}'.format(prob) + '%, '
                        x += node._name + ' = ' + str(valor) + ' ---- '
                        x += node._children[i]._name +  ' = ' + str(node._children[i]._expval)
                        print(prefix + '   +--[T] ' + x)

                    if node._children[i]._type != 'TERMINAL':
                        if lastNode == True:
                            if is_last_node == True:
                                printNode(prefix + '    ', node._children[i], is_last_node)
                            else:
                                printNode(prefix + '   |', node._children[i], is_last_node)
                        else:
                            if is_last_node == True:
                                printNode(prefix + '    ', node._children[i], is_last_node)
                            else:
                                printNode(prefix + '   |', node._children[i], is_last_node)

            elif node._type == 'TERMINAL':

                if maxdeep is not None and self.current_deep == maxdeep:
                    self.current_deep -= 1
                    return

                ##
                #  esta parte nunca debe ejecutarse
                #
                x = node._name + ',  Value = '  + str(node._expval)
                print(prefix + '   +-- ' + x)

            self.current_deep -= 1

        self.current_deep = 0
        printNode('', self._result, True)






if __name__ == "__main__":
    import doctest
    doctest.testmod()
