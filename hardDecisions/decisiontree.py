"""
DecisionTree
==================


plopt 

.. image:: ./images/tree_example.png
   :width: 550px
   :align: center

"""
from hardDecisions.treenode import *

class DecisionTree:
    """Creates and evaluates a decision tree model.

    """

    def __init__(self, tree_name):
        self.datatree = TreeNode('DMTREE')
        self.variables = new_node(parent=self.datatree, tag='VARS')
        self.treenodes = new_node(parent=self.datatree, tag='TREENODES')
        self.tree_name = tree_name
        self.root = None
        self.globals = {}

    def terminal_node(self, name=None, expr=None):
        """Creates a tree's terminal node

        >>> m = DecisionTree(tree_name='tree-test')
        >>> m.terminal_node(name='EXPR', expr='(BID-COST) * (1 if BID < COMPBID else 0)')
        >>> print_as_tree(m.variables) # doctest: +NORMALIZE_WHITESPACE
        +-- VARS
            +-- EXPR {expr: (BID-COST) * (1 if BID < COMPBID else 0), type: TERMINAL}

        """
        node = new_node(parent=self.variables,
                        tag=name,
                        attrib={'type':'TERMINAL', 'expr':expr})


    def chance_node(self, name=None, values=None):
        """Creates a tree's internal chance node

        >>> m = DecisionTree(tree_name='tree-test')
        >>> vcost = [(25.0,  200,  0),
        ...          (50.0,  400,  0),
        ...          (25.0,  600,  0)]
        >>> m.chance_node(name = 'COST', values = vcost)
        >>> print_as_tree(m.variables) # doctest: +NORMALIZE_WHITESPACE
        +-- VARS
            +-- COST {type: CHANCE, values: [(25.0, 200, 0), (50.0, 400, 0), (25.0, 600, 0)]}
        """
        node = new_node(parent=self.variables,
                        tag=name,
                        attrib={'type':'CHANCE', 'values':values})


    def decision_node(self, name=None, values=None, max=True):
        """Creates a tree's internal decision node

        >>> m = DecisionTree(tree_name='tree-test')
        >>> vbid = [(500,  0),
        ...         (700,  0)]
        >>> m.decision_node(name='BID', values=vbid, max=True)
        >>> print_as_tree(m.variables) # doctest: +NORMALIZE_WHITESPACE
        +-- VARS
           +-- BID {max: True, type: DECISION, values: [(500, 0), (700, 0)]}

        """
        node = new_node(parent=self.variables,
                        tag=name,
                        attrib={'type':'DECISION', 'values':values, 'max':max})


    def display_variables(self):
        """Display all the varibles in the tree

        >>> m = DecisionTree(tree_name='tree-test')
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

        """
        txt = []
        for index, var in enumerate(self.variables):
            #
            txt.append('Node {:d}'.format(index))
            txt.append(var.tag + ':')
            txt.append('    Type: ' + var.get('type'))
            #
            if  var.get('type') == 'DECISION':
                #
                if  var.get('max') is True:
                    txt[-1] += ' - Maximum Payoff'
                else:
                    txt[-1] += ' - Minimum Payoff'
                txt.append('    Branches:')
                txt.append('                      Outcomes  Sucessor Node')
                for (value, next_node) in var.get('values'):
                    txt.append('                  {:12.3f}  {:d}'.format(value, next_node))
                txt.append('')
                #
            elif  var.get('type') == 'CHANCE':
                #
                txt.append('    Branches:')
                txt.append('          Chance       Outcome  Sucessor Node')
                for (prob, value, next_node) in var.get('values'):
                    txt.append('           {:5.2f}  {:12.3f}  {:d}'.format(prob, value, next_node))
                txt.append('')
                #
            elif  var.get('type') == 'TERMINAL':
                #
                txt.append('    Expr: ' + var.get('expr'))
                txt.append('')
                #
            else:
                raise ValueError('Node type unknown: ' + var.tag + ', ' +  var.get('type'))
        print('\n'.join(txt))


    def build_tree(self):
        """

        >>> m = DecisionTree(tree_name='tree-test')
        >>> vbid = [(500,  1),
        ...         (700,  1)]
        >>> m.decision_node(name = 'BID', values = vbid)
        >>> vcompbid = [(35.0,  400,  2),
        ...             (50.0,  600,  2),
        ...             (15.0,  800,  2)]
        >>> m.chance_node(name='COMPBID', values=vcompbid)
        >>> vcost = [(25.0,  200,  3),
        ...          (50.0,  400,  3),
        ...          (25.0,  600,  3)]
        >>> m.chance_node(name = 'COST', values = vcost)
        >>> m.terminal_node(expr='(BID-COST) * (1 if BID < COMPBID else 0)')
        >>> m.build_tree()
        >>> print_as_tree(m.treenodes) # doctest: +NORMALIZE_WHITESPACE
        +-- TREENODES
            +-- 0 {expval: None, max: True, next_node: [1, 14], node_number: 0, type: DECISION, var: tree-test}
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


        """

        def build_node(parent, var):

            if var.get('type') == 'TERMINAL':
                parent.set('type', var.get('type'))
                parent.set(key='expr', value=var.get('expr'))
                parent.set(key='expval', value=None)

            if var.get('type') == 'CHANCE':
                parent.set('type', var.get('type'))
                parent.set(key='node_number', value=self.node_number)
                parent.set(key='expval', value=None)
                self.node_number += 1
                for child in var.get('values'):
                    prob, value, next_node = child
                    tree_node = new_node(self.treenodes, tag=len(self.treenodes))
                    tree_node.set(key='var', value=var.tag)
                    tree_node.set(key='value', value=value)
                    tree_node.set(key='prob', value=prob)
                    if 'next_node' in parent.keys():
                        parent.get(key='next_node').append(len(self.treenodes)- 1)
                    else:
                        parent.set(key='next_node', value=[len(self.treenodes) - 1])
                    build_node(parent=tree_node, var=self.variables[next_node])

            if var.get('type') == 'DECISION':
                parent.set('type', var.get('type'))
                parent.set('max', var.get('max'))
                parent.set(key='node_number', value=self.node_number)
                parent.set(key='expval', value=None)
                self.node_number += 1
                for child in var.get('values'):
                    value, next_node = child
                    tree_node = new_node(self.treenodes, tag=len(self.treenodes))
                    tree_node.set(key='var', value=var.tag)
                    tree_node.set(key='value', value=value)
                    tree_node.set(key='expval', value=None)
                    if 'next_node' in parent.keys():
                        parent.get(key='next_node').append(len(self.treenodes) - 1)
                    else:
                        parent.set(key='next_node', value=[len(self.treenodes) - 1])
                    build_node(parent=tree_node, var=self.variables[next_node])



        self.node_number = 0
        parent = new_node(self.treenodes, tag=0)
        parent.set('var', self.tree_name)
        build_node(parent=parent, var=self.variables[0])



    def display_tree(self, maxdeep=None, policy_suggestion=False):
        """
        >>> m = DecisionTree(tree_name='tree-test')
        >>> vbid = [(500,  1),
        ...         (700,  1)]
        >>> m.decision_node(name = 'BID', values = vbid)
        >>> vcompbid = [(35.0,  400,  2),
        ...             (50.0,  600,  2),
        ...             (15.0,  800,  2)]
        >>> m.chance_node(name='COMPBID', values=vcompbid)
        >>> vcost = [(25.0,  200,  3),
        ...          (50.0,  400,  3),
        ...          (25.0,  600,  3)]
        >>> m.chance_node(name = 'COST', values = vcost)
        >>> m.terminal_node(expr='(BID-COST) * (1 if BID < COMPBID else 0)')
        >>> m.build_tree()
        >>> m.display_tree() # doctest: +NORMALIZE_WHITESPACE
        +--[D-0] tree-test
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
        +--[D-0] tree-test

        >>> m.display_tree(maxdeep=1) # doctest: +NORMALIZE_WHITESPACE
        +--[D-0] tree-test
            +--[C-1] BID=500
            +--[C-5] BID=700

        >>> m.display_tree(maxdeep=2) # doctest: +NORMALIZE_WHITESPACE
        +--[D-0] tree-test
            +--[C-1] BID=500
            |   +--[C-2] COMPBID=400, Prob=35.00
            |   +--[C-3] COMPBID=600, Prob=50.00
            |   +--[C-4] COMPBID=800, Prob=15.00
            +--[C-5] BID=700
                +--[C-6] COMPBID=400, Prob=35.00
                +--[C-7] COMPBID=600, Prob=50.00
                +--[C-8] COMPBID=800, Prob=15.00

        >>> m.display_tree(maxdeep=3) # doctest: +NORMALIZE_WHITESPACE
        +--[D-0] tree-test
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


        """

        def print_node(prefix, node, last_node):

            txt = prefix
            node_number = node.get(key='node_number')
            var = node.get(key='var')
            type = node.get(key='type')

            if type == 'DECISION':
                txt += '+--[D-{:d}] '.format(node_number)
            if type == 'CHANCE':
                txt += '+--[C-{:d}] '.format(node_number)
            if type == 'TERMINAL':
                txt += '+--[T] '

            if 'value' in node.keys():
                txt += var + "=" + str(node.get(key='value'))
            else:
                txt += var

            if 'prob' in node.keys():
                txt += ", Prob={:1.2f}".format(node.get(key='prob'))

            if 'cprob' in node.keys():
                txt += ", CProb={:1.2f}".format(node.get(key='cprob'))

            if 'expval' in node.keys() and node.get(key='expval') is not None:
                txt += ", ExpVal={:1.2f}".format(node.get(key='expval'))

            print(txt)

            next_node = node.get(key='next_node') if 'next_node' in node.keys() else None


            if maxdeep is not None and self.current_deep == maxdeep:
                return

            self.current_deep += 1

            if next_node is not None:

                if policy_suggestion is True and type == 'DECISION':
                    optbranch = node.get(key='optbranch')
                    # raise ValueError(optbranch.__repr__())
                    print_node(prefix + '    ', self.treenodes[next_node[optbranch]], last_node=True)
                else:
                    for index, node in enumerate(next_node):
                        is_last_node = True if index == len(next_node) - 1 else False
                        if last_node is True:
                            print_node(prefix + '    ', self.treenodes[node], last_node=is_last_node)
                        else:
                            print_node(prefix + '|   ', self.treenodes[node], last_node=is_last_node)

            self.current_deep -= 1


        self.current_deep = 0
        print_node(prefix='', node=self.treenodes[0], last_node=True)




    def compute_prob(self):
        """
        >>> m = DecisionTree(tree_name='tree-test')
        >>> vbid = [(500,  1),
        ...         (700,  1)]
        >>> m.decision_node(name='BID', values=vbid, max=False)
        >>> vcompbid = [(35.0,  400,  2),
        ...             (50.0,  600,  2),
        ...             (15.0,  800,  2)]
        >>> m.chance_node(name='COMPBID', values=vcompbid)
        >>> vcost = [(25.0,  200,  3),
        ...          (50.0,  400,  3),
        ...          (25.0,  600,  3)]
        >>> m.chance_node(name = 'COST', values = vcost)
        >>> m.terminal_node(expr='(BID-COST) * (1 if BID < COMPBID else 0)')
        >>> m.build_tree()
        >>> m.compute_prob()
        >>> m.display_tree()
        +--[D-0] tree-test
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
        """
        def compute_node_prob(node, probability):

            type = node.get(key='type')

            if type == 'DECISION':
                next_node = node.get(key='next_node')
                for numnode in next_node:
                    compute_node_prob(node=self.treenodes[numnode], probability=1.0)

            if type == 'CHANCE':
                next_node = node.get(key='next_node')
                for numnode in next_node:
                    prob = self.treenodes[numnode].get(key='prob')
                    compute_node_prob(node=self.treenodes[numnode], probability=probability * prob/100)

            if type == 'TERMINAL':
                node.set(key='cprob', value=probability * 100)

        compute_node_prob(node=self.treenodes[0], probability=1.0)


    def compute_values(self):
        """

        >>> m = DecisionTree(tree_name='tree-test')
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
        >>> m.terminal_node(expr='(BID-COST) * (1 if BID < COMPBID else 0)')
        >>> m.build_tree()
        >>> m.compute_prob()
        >>> m.compute_values()
        >>> m.display_tree()
        +--[D-0] tree-test, ExpVal=65.00
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

        >>> m.display_tree(policy_suggestion=True) # doctest: +NORMALIZE_WHITESPACE
        +--[D-0] tree-test, ExpVal=65.00
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
        def compute_node_value(node):

            type = node.get(key='type')

            if type == 'DECISION':
                var = node.get(key='var')
                value = node.get(key='value')
                self.globals[var] = value
                next_node = node.get(key='next_node')
                ismax = node.get(key='max')
                expval = None

                for index, numnode in enumerate(next_node):
                    compute_node_value(node=self.treenodes[numnode])
                    if expval is None:
                        expval = self.treenodes[numnode].get('expval')
                        node.set(key='optbranch', value=index)
                    if ismax is True and expval < self.treenodes[numnode].get('expval'):
                        expval = self.treenodes[numnode].get('expval')
                        node.set(key='optbranch', value=index)
                    if ismax is False and expval > self.treenodes[numnode].get('expval'):
                        expval = self.treenodes[numnode].get('expval')
                        node.set(key='optbranch', value=index)
                node.set(key='expval', value=expval)


            if type == 'CHANCE':
                var = node.get(key='var')
                value = node.get(key='value')
                self.globals[var] = value
                next_node = node.get(key='next_node')
                expval = 0
                for numnode in next_node:
                    compute_node_value(node=self.treenodes[numnode])
                    expval += self.treenodes[numnode].get('expval') * self.treenodes[numnode].get('prob') / 100
                node.set(key='expval', value=expval)


            if type == 'TERMINAL':
                var = node.get(key='var')
                value = node.get(key='value')
                self.globals[var] = value
                node.set(key='expval', value=eval(node.get('expr'), self.globals.copy()))


        compute_node_value(node=self.treenodes[0])

    def risk_profile(self, node_number, cumulative=False, all_branches=False, noprint=True):
        """


        """




        ### 
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






if __name__ == "__main__":
    import doctest
    doctest.testmod()
