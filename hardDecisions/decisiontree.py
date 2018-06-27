"""
Functions
==============================================================================


"""

import math

class DecisionTree:
    """Creates and evaluates a decision tree model. """

    def __init__(self):
        """Decision tree constructor.
        """
        self.data = []
        self.tree = []
        self.globals = {}
        self.utility_function = None
        self.inv_utility_function = None
        self.R = None


    def exponential_utility_fcn(self, x):
        """Computes the exponential utility function defined as `1 - exp(-x/R)`."""
        return 1 - math.exp(-x / self.R)

    def inv_exponential_utility_fcn(self, u):
        """Computes the inverse exponential utility function defined as `-R * log(1 - U)`."""
        return -self.R * math.log(1 - u)

    def logarithmic_utility_fcn(self, x):
        """Computes the logarithmic utility function defined as `log(x + R)`."""
        return math.log(x + self.R)

    def inv_logarithmic_utility_fcn(self, u):
        """Computes the inverse logarithmic utility function defined as `exp(U) - R`."""
        return math.exp(u) - self.R

    def square_root_utility_fcn(self, x):
        """Computes the square root utility function defined as `sqrt(x + R)`."""
        return math.sqrt(x + self.R)

    def inv_square_root_utility_fcn(self, u):
        """Computes the inverse square root utility function defined as `U**2 - R`."""
        return math.pow(u, 2) - self.R


    def use_utility_function(self,
                             exponential=None,
                             logarithmic=None,
                             square_root=None,
                             R = None):
        """This function specify the use of utility functions for all
        internal computations in the decision tree.

        Args:
            exponential (logical, None): When it is True, the exponential utility
                function is used for computing the expected utility in the nodes
                of the tree.
            logarithmic (logical, None): When it is True, the logarithmic utility
                function is used for computing the expected utility in the nodes
                of the tree.
            square_root (logical, None): When it is True, the square root utility
                function is used for computing the expected utility in the nodes
                of the tree.
            R (float): Value of the R parameter of the utility function.

        Returns:
            None.

        """
        self.utility_function = None
        self.inv_utility_function = None
        self.R = None
        if exponential is True:
            self.utility_function = self.exponential_utility_fcn
            self.inv_utility_function = self.inv_exponential_utility_fcn
            self.R = R
            return
        if logarithmic is True:
            self.utility_function = self.logarithmic_utility_fcn
            self.inv_utility_function = self.inv_logarithmic_utility_fcn
            self.R = R
            return
        if square_root is True:
            self.utility_function = self.square_root_utility_fcn
            self.inv_utility_function = self.inv_square_root_utility_fcn
            self.R = R
            return

    def terminal_node(self, expr=None):
        """Creates a decision tree's terminal node.

        Args:
            expr (string, None): It is a valid python code used for computing
                the value of the terminal node in the tree. The name of the
                nodes can be used in the expression. When the value is `None`,
                the expression is created as a sum of the names of the
                branches in the tree.

        Returns: None.

        The following example creates a simple terminal node.

        >>> tree = DecisionTree()
        >>> tree.terminal_node(expr='python code')
        >>> tree.display_nodes() # doctest: +NORMALIZE_WHITESPACE
        Node 0
            Type: TERMINAL
            Expr: python code
        <BLANKLINE>


        """
        self.data.append({'type':'TERMINAL',
                          'expr':expr,
                          'id':len(self.data)})

    def chance_node(self, name=None, branches=None, ignore=False):
        """Creates a decisions tree's internal chance node.

        Args:
            name (string): A valid name for variablesl in Python.
            branches (list): A list of tuples, where each tuple contains the
                corresponding information of each branch in the node. Each tuple
                has the probability, the value of the branch and the index of
                the next node.
            ignore (bool): When it is `True`, the name of the node is not used
                for creating the default expression for the terminal nodes in
                the path containing this node.

        Returns: None.

        The following example creates a tree with a chance node in the root with
        four branches finished in the same terminal node.

        >>> tree = DecisionTree()
        >>> tree.chance_node(name='ChanceNode',
        ...                  branches=[(20.0, 100,  1),
        ...                            (30.0, 200,  1),
        ...                            (50.0, 300,  1)])
        >>> tree.terminal_node()
        >>> tree.display_nodes() # doctest: +NORMALIZE_WHITESPACE
        Node 0
            Type: CHANCE
            Name: ChanceNode
            Branches:
                  Chance         Value  Next Node
                   20.00       100.000  1
                   30.00       200.000  1
                   50.00       300.000  1
        <BLANKLINE>
        Node 1
            Type: TERMINAL
            Expr: (cumulative)
        <BLANKLINE>

        """
        self.data.append({'tag':name,
                          'type':'CHANCE',
                          'branches':branches,
                          'ignore':ignore,
                          'id':len(self.data)})

    def decision_node(self, name=None, branches=None, max=True, ignore=False):
        """Creates a decisions tree's internal decision node.

        Args:
            name (string): A valid name for variablesl in Python.
            branches (list): A list of tuples, where each tuple contains the
                corresponding information of each branch in the node. Each tuple
                has the value of the branch and the index of
                the next node.
            max (bool): When it is `True`, selects the branch with the
                maximum expected value.
            ignore (bool): When it is `True`, the name of the node is not used
                for creating the default expression for the terminal nodes in
                the path containing this node.

        Returns: None.

        The following example creates a tree with a decision node in the root with
        four branches finished in the same terminal node.

        >>> tree = DecisionTree()
        >>> tree.decision_node(name='DecisionNode',
        ...                    branches=[(100,  1),
        ...                              (200,  1),
        ...                              (300,  1),
        ...                              (400,  1)],
        ...                    max=True)
        >>> tree.terminal_node()
        >>> tree.display_nodes() # doctest: +NORMALIZE_WHITESPACE
        Node 0
            Type: DECISION - Maximum Payoff
            Name: DecisionNode
            Branches:
                                 Value  Next Node
                               100.000  1
                               200.000  1
                               300.000  1
                               400.000  1
        <BLANKLINE>
        Node 1
            Type: TERMINAL
            Expr: (cumulative)
        <BLANKLINE>

        """
        self.data.append({'tag':name,
                          'type':'DECISION',
                          'branches':branches,
                          'max':max,
                          'ignore':ignore,
                          'id':len(self.data)})

    def display_nodes(self):
        """Display all the data nodes in the decision tree.
        """
        txt = []
        for index, node in enumerate(self.data):
            #
            txt.append('Node {:d}'.format(index))
            #
            if node.get('type') == 'DECISION':
                #
                txt.append('    Type: ' + node.get('type'))
                txt[-1] += ' - Maximum Payoff' if node.get('max') is True else ' - Minimum Payoff'
                txt.append('    Name: ' + node.get('tag'))
                txt.append('    Branches:')
                txt.append('                         Value  Next Node')
                for (outcome, next_node) in node.get('branches'):
                    txt.append('                  {:12.3f}  {:d}'.format(outcome, next_node))
                txt.append('')
                #
            elif node.get('type') == 'CHANCE':
                #
                txt.append('    Type: ' + node.get('type'))
                txt.append('    Name: ' + node.get('tag'))
                txt.append('    Branches:')
                txt.append('          Chance         Value  Next Node')
                for (prob, outcome, next_node) in node.get('branches'):
                    txt.append('           {:5.2f}  {:12.3f}  {:d}'.format(prob, outcome, next_node))
                txt.append('')
                #
            elif  node.get('type') == 'TERMINAL':
                #
                txt.append('    Type: ' + node.get('type'))
                if node.get('expr') is None:
                    txt.append('    Expr: (cumulative)')
                else:
                    txt.append('    Expr: ' + node.get('expr'))
                txt.append('')
                #
            else:
                raise ValueError('Node type unknown: ' + node.tag + ', ' +  node.get('type'))
        print('\n'.join(txt))

    ##
    ##
    ##
    def build_tree(self):
        """Builds the decision tree using the information in the variables.
        """
        def get_current_branch(id):
            for var_id, var_branch in self.stack:
                if var_id == id:
                    return var_branch
            return None


        def find_value(data):
            if isinstance(data, tuple):
                id, values = data
                return find_value(values[get_current_branch(id)])
            return data


        def new_branch():
            ### Creates a new branch in the tree.
            self.tree.append({'ExpVal':None,
                              'sel_strategy':None,
                              'id':len(self.tree)})
            #
            return (len(self.tree)- 1, self.tree[-1])


        def set_branch_data(this_branch, this_node, path):

            def set_terminal():
                this_branch['type'] = this_node.get('type')
                if this_branch.get('ignore', True) is False:
                    path.append(this_branch.get('tag'))
                this_branch['expr'] = '+'.join(path) if this_node.get('expr') is None else this_node.get('expr')

            def set_decision():
                #
                this_branch['type'] = this_node.get('type')
                this_branch['forced_branch_idx'] = None
                this_branch['next_branches'] = []
                this_branch['max'] = this_node.get('max')
                if this_branch.get('ignore', True) is False:
                    path.append(this_branch.get('tag'))
                #
                for idx, (value, next_node) in enumerate(this_node.get('branches')):
                    #
                    self.stack.append((this_node['id'], idx))
                    #
                    next_branch_id, next_branch = new_branch()
                    this_branch['next_branches'].append(next_branch_id)
                    next_branch['ignore'] = this_node.get('ignore')
                    next_branch['tag'] = this_node.get('tag')
                    next_branch['value'] = find_value(value)
                    #
                    set_branch_data(this_branch=next_branch,
                                    this_node=self.data[next_node],
                                    path=path.copy())
                    #
                    self.stack.pop()

            def set_chance():
                #
                this_branch['type'] = this_node.get('type')
                this_branch['forced_branch_idx'] = None
                this_branch['next_branches'] = []
                if this_branch.get('ignore', True) is False:
                    path.append(this_branch.get('tag'))
                #
                for idx, (prob, value, next_node) in enumerate(this_node.get('branches')):
                    #
                    self.stack.append((this_node['id'], idx))
                    #
                    next_branch_id, next_branch = new_branch()
                    this_branch['next_branches'].append(next_branch_id)
                    next_branch['ignore'] = this_node.get('ignore')
                    next_branch['tag'] = this_node.get('tag')
                    next_branch['value'] = find_value(value)
                    next_branch['prob'] = find_value(prob)
                    #
                    set_branch_data(this_branch=next_branch,
                                    this_node=self.data[next_node],
                                    path=path.copy())
                    #
                    self.stack.pop()
            ####
            if this_node.get('type') == 'DECISION':
                set_decision()
            elif this_node.get('type') == 'CHANCE':
                set_chance()
            elif this_node.get('type') == 'TERMINAL':
                set_terminal()
            else:
                pass
        ###
        self.stack = []
        self.tree = []
        path = []
        _ , this_branch = new_branch()
        set_branch_data(this_branch=this_branch,
                        this_node=self.data[0],
                        path=path.copy())
        del self.stack



    def display_tree(self, maxdeep=None, selected_strategy=False):
        """Prints the tree as a text diagram.

        Args:
            maxdeep (int, None): maximum deep of tree to print.
            selected_strategy (bool): When it is `True`, only the
                optimal (or forced branches) in the tree are displayed.

        Returns:
            None.

        The following example creates a decision tree with a unique decision
        node at the root of the tree. When the tree has not been evaluated,
        this function shows only the number of the branch and the name and
        value of the variable representing the type of node.

        >>> tree = DecisionTree()
        >>> tree.decision_node(name='DecisionNode',
        ...                    branches=[(100,  1),
        ...                              (200,  1),
        ...                              (300,  1),
        ...                              (400,  1)],
        ...                    max=True)
        >>> tree.terminal_node()
        >>> tree.build_tree()
        >>> tree.display_tree()  # doctest: +NORMALIZE_WHITESPACE
        |
        | #0
        \-------[D]
                 |
                 | #1
                 | DecisionNode=100
                 +-------[T] DecisionNode
                 |
                 | #2
                 | DecisionNode=200
                 +-------[T] DecisionNode
                 |
                 | #3
                 | DecisionNode=300
                 +-------[T] DecisionNode
                 |
                 | #4
                 | DecisionNode=400
                 \-------[T] DecisionNode

        When the tree is evaluated, additional information is displayed for
        each branch. `PathProb` is the path probability for the corresponding
        branch of the tree. `ExpVal` is the expected value of the node.
        `(selected strategy)` indicates the branches corresponding to the
        optimal (or forced) decision strategy.

        >>> tree.evaluate()
        >>> tree.display_tree()  # doctest: +NORMALIZE_WHITESPACE
        |
        | #0
        | ExpVal=400.00
        | (selected strategy)
        \-------[D]
                 |
                 | #1
                 | DecisionNode=100
                 | PathProb=0.00
                 | ExpVal=100.00
                 +-------[T] DecisionNode
                 |
                 | #2
                 | DecisionNode=200
                 | PathProb=0.00
                 | ExpVal=200.00
                 +-------[T] DecisionNode
                 |
                 | #3
                 | DecisionNode=300
                 | PathProb=0.00
                 | ExpVal=300.00
                 +-------[T] DecisionNode
                 |
                 | #4
                 | DecisionNode=400
                 | PathProb=100.00
                 | ExpVal=400.00
                 | (selected strategy)
                 \-------[T] DecisionNode


        The parameter `selected_strategy` are used to print the branches of
        tree in the optimal decision strategy. This option allows the user
        to analyze the sequence of optimal decisions.

        >>> tree.display_tree(selected_strategy=True)  # doctest: +NORMALIZE_WHITESPACE
        |
        | #0
        | ExpVal=400.00
        | (selected strategy)
        \-------[D]
                 |
                 | #4
                 | DecisionNode=400
                 | PathProb=100.00
                 | ExpVal=400.00
                 | (selected strategy)
                 \-------[T] DecisionNode
        """

        def print_branch(prefix, this_branch, is_node_last_branch):

            print(prefix + '|')

            type = this_branch.get('type')
            if 'id' in this_branch.keys():
                print(prefix + '| #' + str(this_branch.get('id')))

            ## prints the name and value of the variable
            if 'tag' in this_branch.keys():
                var = this_branch['tag']
                if 'value' in this_branch.keys():
                    txt = "| " + var + "=" + str(this_branch['value'])
                else:
                    txt = "| " + var
                print(prefix + txt)

            ## prints the probability
            if 'prob' in this_branch.keys():
                txt = "| Prob={:1.2f}".format(this_branch['prob'])
                print(prefix + txt)

            ## prints the cumulative probability
            if type == 'TERMINAL' and 'PathProb' in this_branch.keys():
                txt = "| PathProb={:1.2f}".format(this_branch['PathProb'])
                print(prefix + txt)

            if 'ExpVal' in this_branch.keys() and this_branch['ExpVal'] is not None:
                txt = "| ExpVal={:1.2f}".format(this_branch['ExpVal'])
                print(prefix + txt)

            if 'ExpUtl' in this_branch.keys() and this_branch['ExpUtl'] is not None:
                txt = "| ExpUtl={:1.2f}".format(this_branch['ExpUtl'])
                print(prefix + txt)

            if 'CE' in this_branch.keys() and this_branch['CE'] is not None:
                txt = "| CE={:1.2f}".format(this_branch['CE'])
                print(prefix + txt)


            if 'RiskProfile' in this_branch.keys() and type != 'TERMINAL':
                print(prefix + "| Risk Profile:")
                print(prefix + "|      Value  Prob")
                for key in sorted(this_branch['RiskProfile']):
                    txt = "|   {:8.2f} {:5.2f}".format(key, this_branch['RiskProfile'][key])
                    print(prefix + txt)

            if 'sel_strategy' in this_branch.keys() and this_branch['sel_strategy'] is True:
                txt = "| (selected strategy)"
                print(prefix + txt)

            if 'forced_branch_idx' in this_branch.keys() and this_branch['forced_branch_idx'] is not None:
                txt = "| (forced branch = {:1d})".format(this_branch['forced_branch_idx'])
                print(prefix + txt)


            next_branches = this_branch['next_branches'] if 'next_branches' in this_branch.keys() else None

            if is_node_last_branch is True:
                if type == 'DECISION':
                    txt = '\-------[D]'
                if type == 'CHANCE':
                    txt = '\-------[C]'
                if type == 'TERMINAL':
                    txt = '\-------[T] {:s}'.format(this_branch['expr'])
            else:
                if type == 'DECISION':
                    txt = '+-------[D]'
                if type == 'CHANCE':
                    txt = '+-------[C]'
                if type == 'TERMINAL':
                    txt = '+-------[T] {:s}'.format(this_branch['expr'])
            print(prefix + txt)

            if maxdeep is not None and self.current_deep == maxdeep:
                return

            self.current_deep += 1

            if next_branches is not None:

                if selected_strategy is True and type == 'DECISION':
                    optbranch = this_branch['opt_branch_idx']
                    if is_node_last_branch is True:
                        print_branch(prefix + ' ' * 9, self.tree[next_branches[optbranch]], is_node_last_branch=True)
                    else:
                        print_branch(prefix + '|' + ' ' * 8, self.tree[next_branches[optbranch]], is_node_last_branch=True)
                else:
                    for next_branch_idx, next_branch_id in enumerate(next_branches):
                        is_last_tree_branch = True if next_branch_idx == len(next_branches) - 1 else False
                        if is_node_last_branch is True:
                            print_branch(prefix + ' ' * 9, self.tree[next_branch_id], is_node_last_branch=is_last_tree_branch)
                        else:
                            print_branch(prefix + '|' + ' ' * 8, self.tree[next_branch_id], is_node_last_branch=is_last_tree_branch)

            self.current_deep -= 1

        self.current_deep = 0
        print_branch(prefix='', this_branch=self.tree[0], is_node_last_branch=True)




    def evaluate(self, locals=locals()):
        """Evalute the tree. First, the cumulative probabilities in all nodes
        are calculated. Finally, the algorithm computes the expected values.

        Args:
            None.

        Returns:
            None.

        """

        def compute_expected_values():
            """computes expected values.
            """
            def compute_branch_expvalue(this_branch):

                if this_branch.get('type') == 'DECISION':
                    #
                    if 'tag' in this_branch.keys():
                        self.globals[this_branch['tag']] = this_branch['value']
                    ismax = this_branch['max']
                    expval = None
                    exputl = None
                    CE = None
                    #
                    if self.utility_function is None:

                        for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                            compute_branch_expvalue(this_branch=self.tree[branch_id])
                            if this_branch['forced_branch_idx'] is None:
                                    if expval is None:
                                        expval = self.tree[branch_id].get('ExpVal')
                                        this_branch['opt_branch_idx'] = branch_idx
                                    if ismax is True and expval < self.tree[branch_id].get('ExpVal'):
                                        expval = self.tree[branch_id].get('ExpVal')
                                        this_branch['opt_branch_idx'] = branch_idx
                                    if ismax is False and expval > self.tree[branch_id].get('ExpVal'):
                                        expval = self.tree[branch_id].get('ExpVal')
                                        this_branch['opt_branch_idx'] = branch_idx
                            else:
                                if branch_idx == this_branch['forced_branch_idx']:
                                    expval = self.tree[branch_id].get('ExpVal')
                                    this_branch['opt_branch_idx'] = branch_idx

                        this_branch['ExpVal'] = expval

                    else:

                        for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                            compute_branch_expvalue(this_branch=self.tree[branch_id])
                            if this_branch['forced_branch_idx'] is None:
                                if expval is None:
                                    expval = self.tree[branch_id].get('ExpVal')
                                    exputl = self.tree[branch_id].get('ExpUtl')
                                    CE = self.tree[branch_id].get('CE')
                                    this_branch['opt_branch_idx'] = branch_idx
                                if exputl < self.tree[branch_id].get('ExpUtl'):
                                    expval = self.tree[branch_id].get('ExpVal')
                                    exputl = self.tree[branch_id].get('ExpUtl')
                                    CE = self.tree[branch_id].get('CE')
                                    this_branch['opt_branch_idx'] = branch_idx
                            else:
                                if branch_idx == this_branch['forced_branch_idx']:
                                    expval = self.tree[branch_id].get('ExpVal')
                                    exputl = self.tree[branch_id].get('ExpUtl')
                                    CE = self.tree[branch_id].get('CE')
                                    this_branch['opt_branch_idx'] = branch_idx


                        this_branch['ExpVal'] = expval
                        this_branch['ExpUtl'] = exputl
                        this_branch['CE'] = CE


                if this_branch.get('type') == 'CHANCE':

                    self.globals[this_branch['tag']] = this_branch['value']
                    expval = 0
                    exputl = 0
                    CE = None
                    #
                    if self.utility_function is None:

                        if this_branch['forced_branch_idx'] is None:
                            for branch_id in this_branch['next_branches']:
                                compute_branch_expvalue(this_branch=self.tree[branch_id])
                                expval += self.tree[branch_id].get('ExpVal') * self.tree[branch_id].get('prob') / 100
                        else:
                            for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                                if branch_idx == this_branch['forced_branch_idx']:
                                    compute_branch_expvalue(this_branch=self.tree[branch_id])
                                    expval += self.tree[branch_id].get('ExpVal')
                                else:
                                    compute_branch_expvalue(this_branch=self.tree[branch_id])
                                    expval += 0
                        this_branch['ExpVal'] = expval

                    else:

                        if this_branch['forced_branch_idx'] is None:
                            for branch_id in this_branch['next_branches']:
                                compute_branch_expvalue(this_branch=self.tree[branch_id])
                                expval += self.tree[branch_id].get('ExpVal') * self.tree[branch_id].get('prob') / 100
                                exputl += self.tree[branch_id].get('ExpUtl') * self.tree[branch_id].get('prob') / 100

                        else:
                            for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                                if branch_idx == this_branch['forced_branch_idx']:
                                    compute_branch_expvalue(this_branch=self.tree[branch_id])
                                    expval += self.tree[branch_id].get('ExpVal')
                                    exputl += self.tree[branch_id].get('ExpUtl')
                                else:
                                    compute_branch_expvalue(this_branch=self.tree[branch_id])
                                    expval += 0
                                    exputl += 0

                        this_branch['ExpVal'] = expval
                        this_branch['ExpUtl'] = exputl
                        this_branch['CE'] = self.inv_utility_function(exputl)

                # if this_branch.get('type') == 'TERMINAL':
                #     var = this_branch['tag']
                #     value = this_branch['value']
                #     self.globals[var] = value
                #     glb = self.globals.copy()
                #     glb.update(locals().copy())
                #     # this_branch['ExpVal'] = eval(this_branch['expr'], self.globals.copy())
                #     this_branch['ExpVal'] = eval(this_branch['expr'], glb.copy())
                #
                #     if self.utility_function is not None:
                #         this_branch['ExpUtl'] = self.utility_function(this_branch['ExpVal'])
                #         this_branch['CE'] = this_branch['ExpVal']

                if this_branch.get('type') == 'TERMINAL':
                    var = this_branch['tag']
                    value = this_branch['value']
                    self.globals[var] = value
                    #
                    #globals = globals()
                    #self.globals.copy()
                    #for var in self.globals:
                    #    eval(var + ' = ' + str(self.globals[var]))
                    #
                    this_branch['ExpVal'] = eval(this_branch['expr'], self.globals.copy(), locals.copy())


                    if self.utility_function is not None:
                        this_branch['ExpUtl'] = self.utility_function(this_branch['ExpVal'])
                        this_branch['CE'] = this_branch['ExpVal']



            compute_branch_expvalue(this_branch=self.tree[0])


        def compute_path_probabilities():
            """Computes the probabilities in all tree branches.
            """
            def compute_branch_prob(this_branch, probability, sel_strategy):

                if this_branch['type'] == 'DECISION':
                    this_branch['sel_strategy'] = sel_strategy
                    if sel_strategy is True:
                        for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                            if branch_idx == this_branch['opt_branch_idx']:
                                compute_branch_prob(this_branch=self.tree[branch_id],
                                                  probability=probability,
                                                  sel_strategy=True)
                            else:
                                compute_branch_prob(this_branch=self.tree[branch_id],
                                                  probability=0,
                                                  sel_strategy=False)
                    else:
                        if sel_strategy is True:
                            current_prob = probability
                        else:
                            current_prob = 0
                        for branch_id in this_branch['next_branches']:
                            compute_branch_prob(this_branch=self.tree[branch_id],
                                              probability=current_prob,
                                              sel_strategy=False)
                if this_branch['type'] == 'CHANCE':
                    this_branch['sel_strategy'] = sel_strategy
                    if this_branch['forced_branch_idx'] is None:
                        for branch_id in this_branch['next_branches']:
                            prob = self.tree[branch_id]['prob']
                            compute_branch_prob(this_branch=self.tree[branch_id],
                                              probability=probability * prob/100,
                                              sel_strategy = sel_strategy)
                    else:
                        for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                            if branch_idx == this_branch['forced_branch_idx']:
                                prob = self.tree[branch_id]['prob']
                                prob = 100
                                compute_branch_prob(this_branch=self.tree[branch_id],
                                                  probability=probability * prob/100,
                                                  sel_strategy = True)
                            else:
                                prob = self.tree[branch_id]['prob']
                                prob = 0
                                compute_branch_prob(this_branch=self.tree[branch_id],
                                                  probability=probability * prob/100,
                                                  sel_strategy = False)
                if this_branch['type'] == 'TERMINAL':
                    this_branch['sel_strategy'] = sel_strategy
                    this_branch['PathProb'] = probability * 100
            #
            compute_branch_prob(this_branch=self.tree[0], probability=1.0, sel_strategy=True)

        for branch in self.tree:
            if 'RiskProfile' in branch.keys():
                del branch['RiskProfile']

        self.cumvalue = 0
        compute_expected_values()
        compute_path_probabilities()


    def force_branch(self, branch_id, branch_idx=None):
        self.tree[branch_id]['forced_branch_idx'] = branch_idx

    def compute_risk_profile(self):
        """Computes the risk profile for the selected strategy.

        In the following example, a decision tree with a decision node in the
        root followed by a chance node is created and evaluated.


        >>> tree = DecisionTree()
        >>> tree.decision_node(name='DecisionNode',
        ...                    branches=[(100,  1),
        ...                              (200,  1)],
        ...                    max=True)
        >>> tree.chance_node(name='ChanceNode',
        ...                  branches=[(25, 300,  2),
        ...                            (50, 400,  2),
        ...                            (25, 500,  2)])
        >>> tree.terminal_node()
        >>> tree.build_tree()
        >>> tree.evaluate()

        Next, the risk profile for the branches corresponding to the sequence of
        optimal decisions is computed.

        >>> tree.compute_risk_profile()
        >>> tree.display_tree()  # doctest: +NORMALIZE_WHITESPACE
        |
        | #0
        | ExpVal=600.00
        | Risk Profile:
        |      Value  Prob
        |     500.00 25.00
        |     600.00 50.00
        |     700.00 25.00
        | (selected strategy)
        \-------[D]
                 |
                 | #1
                 | DecisionNode=100
                 | ExpVal=500.00
                 +-------[C]
                 |        |
                 |        | #2
                 |        | ChanceNode=300
                 |        | Prob=25.00
                 |        | PathProb=0.00
                 |        | ExpVal=400.00
                 |        +-------[T] DecisionNode+ChanceNode
                 |        |
                 |        | #3
                 |        | ChanceNode=400
                 |        | Prob=50.00
                 |        | PathProb=0.00
                 |        | ExpVal=500.00
                 |        +-------[T] DecisionNode+ChanceNode
                 |        |
                 |        | #4
                 |        | ChanceNode=500
                 |        | Prob=25.00
                 |        | PathProb=0.00
                 |        | ExpVal=600.00
                 |        \-------[T] DecisionNode+ChanceNode
                 |
                 | #5
                 | DecisionNode=200
                 | ExpVal=600.00
                 | Risk Profile:
                 |      Value  Prob
                 |     500.00 25.00
                 |     600.00 50.00
                 |     700.00 25.00
                 | (selected strategy)
                 \-------[C]
                          |
                          | #6
                          | ChanceNode=300
                          | Prob=25.00
                          | PathProb=25.00
                          | ExpVal=500.00
                          | (selected strategy)
                          +-------[T] DecisionNode+ChanceNode
                          |
                          | #7
                          | ChanceNode=400
                          | Prob=50.00
                          | PathProb=50.00
                          | ExpVal=600.00
                          | (selected strategy)
                          +-------[T] DecisionNode+ChanceNode
                          |
                          | #8
                          | ChanceNode=500
                          | Prob=25.00
                          | PathProb=25.00
                          | ExpVal=700.00
                          | (selected strategy)
                          \-------[T] DecisionNode+ChanceNode


        Risk profile values can be acceced using the `risk_profile` variable
        of the nodes in the optimal sequence of decisions. In the following  code
        the risk profile is obtained for the root node. Risk profile is retuned
        as a dictionary where the keys are the expected values and the values
        stored in the dictionary are the probabilities of the corresponding
        expected values.

        >>> tree.tree[0]['RiskProfile'] # doctest: +NORMALIZE_WHITESPACE
        {500: 25.0, 600: 50.0, 700: 25.0}



        """

        def collect(this_branch):

            if this_branch['sel_strategy'] is False:
                return

            if this_branch['type'] == 'DECISION':
                for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                    collect(this_branch=self.tree[branch_id])
                next_opt_branch = this_branch['next_branches'][this_branch['opt_branch_idx']]
                this_branch['RiskProfile'] = self.tree[next_opt_branch]['RiskProfile']

            if this_branch['type'] == 'CHANCE':
                for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                    collect(this_branch=self.tree[branch_id])
                this_branch['RiskProfile'] = {}
                for branch_id in this_branch['next_branches']:
                    next_branch = self.tree[branch_id]['RiskProfile']
                    for key in next_branch.keys():
                        if key in this_branch['RiskProfile'].keys():
                            this_branch['RiskProfile'][key] += next_branch[key]
                        else:
                            this_branch['RiskProfile'][key] = next_branch[key]

            if this_branch['type'] == 'TERMINAL':
                this_branch['RiskProfile'] = {this_branch['ExpVal']: this_branch['PathProb']}


        collect(this_branch=self.tree[0])




if __name__ == "__main__":
    import doctest
    doctest.testmod()
