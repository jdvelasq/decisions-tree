"""
Functions in this Module
==============================================================================


"""

class DecisionTree:
    """Creates and evaluates a decision tree model. """

    def __init__(self):
        """Decision tree constructor.
        """
        self.data = []
        self.tree = []
        self.globals = {}

    def terminal_node(self, expr=None):
        """Creates a decision tree's terminal node.
        """
        self.data.append({'type':'TERMINAL',
                          'expr':expr})

    def chance_node(self, name=None, branches=None, ignore=False):
        """Creates a decisions tree's internal chance node.
        """
        self.data.append({'tag':name,
                          'type':'CHANCE',
                          'branches':branches,
                          'ignore':ignore})

    def decision_node(self, name=None, branches=None, max=True, ignore=False):
        """Creates a decisions tree's internal decision node.
        """
        self.data.append({'tag':name,
                          'type':'DECISION',
                          'branches':branches,
                          'max':max,
                          'ignore':ignore})

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

        def new_branch():
            """Creates a new branch in the tree.
            """
            self.tree.append({'exp_val':None,
                              'sel_strategy':None,
                              'id':len(self.tree)})
            #
            return (len(self.tree)- 1, self.tree[-1])


        def set_branch_data(this_branch, this_node, path):

            def set_terminal():
                this_branch['type'] = this_node.get('type')
                ### this_branch['terminal'] = this_node.get('tag')
                if this_branch.get('ignore', True) is False:
                    path.append(this_branch.get('tag'))
                this_branch['expr'] = '+'.join(path) if this_node.get('expr') is None else this_node.get('expr')

            def set_decision():
                this_branch['type'] = this_node.get('type')
                this_branch['forced_branch_idx'] = None
                this_branch['next_branches'] = []
                this_branch['max'] = this_node.get('max')
                if this_branch.get('ignore', True) is False:
                    path.append(this_branch.get('tag'))
                #
                for idx, (value, next_node) in enumerate(this_node.get('branches')):
                    #
                    next_branch_id, next_branch = new_branch()
                    this_branch['next_branches'].append(next_branch_id)
                    next_branch['ignore'] = this_node.get('ignore')
                    next_branch['tag'] = this_node.get('tag')
                    next_branch['value'] = value
                    #
                    set_branch_data(this_branch=next_branch,
                                    this_node=self.data[next_node],
                                    path=path.copy())

            def set_chance():
                this_branch['type'] = this_node.get('type')
                this_branch['forced_branch_idx'] = None
                this_branch['next_branches'] = []
                if this_branch.get('ignore', True) is False:
                    path.append(this_branch.get('tag'))
                #
                for idx, (prob, value, next_node) in enumerate(this_node.get('branches')):
                    #
                    next_branch_id, next_branch = new_branch()
                    this_branch['next_branches'].append(next_branch_id)
                    next_branch['ignore'] = this_node.get('ignore')
                    next_branch['tag'] = this_node.get('tag')
                    next_branch['value'] = value
                    next_branch['prob'] = prob
                    #
                    set_branch_data(this_branch=next_branch,
                                    this_node=self.data[next_node],
                                    path=path.copy())

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
        self.tree = []
        path = []
        _ , this_branch = new_branch()
        set_branch_data(this_branch=this_branch,
                        this_node=self.data[0],
                        path=path.copy())



    def display_tree(self, maxdeep=None, selected_strategy=False):
        """Prints the tree as text.
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
            if type == 'TERMINAL' and 'pathprob' in this_branch.keys():
                txt = "| PathProb={:1.2f}".format(this_branch['pathprob'])
                print(prefix + txt)

            if 'exp_val' in this_branch.keys() and this_branch['exp_val'] is not None:
                txt = "| ExpVal={:1.2f}".format(this_branch['exp_val'])
                print(prefix + txt)

            if 'risk_profile' in this_branch.keys() and type != 'TERMINAL':
                print(prefix + "| Risk Profile:")
                print(prefix + "|      Value  Prob")
                for key in sorted(this_branch['risk_profile']):
                    txt = "|   {:8.2f} {:5.2f}".format(key, this_branch['risk_profile'][key])
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




    def evaluate(self):
        """Evalute the tree. First, the cumulative probabilities in all nodes
        are calculated. Finally, the algorithm computes the expected values."""

        def compute_expected_values():
            """computes expected values.
            """
            def compute_branch_expvalue(this_branch):

                if this_branch.get('type') == 'DECISION':
                    if 'tag' in this_branch.keys():
                        self.globals[this_branch['tag']] = this_branch['value']
                    ismax = this_branch['max']
                    expval = None

                    for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                        compute_branch_expvalue(this_branch=self.tree[branch_id])
                        if this_branch['forced_branch_idx'] is None:
                            if expval is None:
                                expval = self.tree[branch_id].get('exp_val')
                                this_branch['opt_branch_idx'] = branch_idx
                            if ismax is True and expval < self.tree[branch_id].get('exp_val'):
                                expval = self.tree[branch_id].get('exp_val')
                                this_branch['opt_branch_idx'] = branch_idx
                            if ismax is False and expval > self.tree[branch_id].get('exp_val'):
                                expval = self.tree[branch_id].get('exp_val')
                                this_branch['opt_branch_idx'] = branch_idx
                        else:
                            if branch_idx == this_branch['forced_branch_idx']:
                                expval = self.tree[branch_id].get('exp_val')
                                this_branch['opt_branch_idx'] = branch_idx

                    this_branch['exp_val'] = expval


                if this_branch.get('type') == 'CHANCE':
                    self.globals[this_branch['tag']] = this_branch['value']
                    expval = 0
                    if this_branch['forced_branch_idx'] is None:
                        for branch_id in this_branch['next_branches']:
                            compute_branch_expvalue(this_branch=self.tree[branch_id])
                            expval += self.tree[branch_id].get('exp_val') * self.tree[branch_id].get('prob') / 100
                    else:
                        for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                            if branch_idx == this_branch['forced_branch_idx']:
                                compute_branch_expvalue(this_branch=self.tree[branch_id])
                                expval += self.tree[branch_id].get('exp_val')
                            else:
                                compute_branch_expvalue(this_branch=self.tree[branch_id])
                                expval += 0
                    this_branch['exp_val'] = expval

                if this_branch.get('type') == 'TERMINAL':
                    var = this_branch['tag']
                    value = this_branch['value']
                    self.globals[var] = value
                    this_branch['exp_val'] = eval(this_branch['expr'], self.globals.copy())

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
                    this_branch['pathprob'] = probability * 100
            #
            compute_branch_prob(this_branch=self.tree[0], probability=1.0, sel_strategy=True)

        self.cumvalue = 0
        compute_expected_values()
        compute_path_probabilities()



    def compute_risk_profile(self):
        """Computes the risk profile for the selected strategy.
        """

        def collect(this_branch):

            if this_branch['sel_strategy'] is False:
                return

            if this_branch['type'] == 'DECISION':
                for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                    collect(this_branch=self.tree[branch_id])
                next_opt_branch = this_branch['next_branches'][this_branch['opt_branch_idx']]
                this_branch['risk_profile'] = self.tree[next_opt_branch]['risk_profile']

            if this_branch['type'] == 'CHANCE':
                for branch_idx, branch_id in enumerate(this_branch['next_branches']):
                    collect(this_branch=self.tree[branch_id])
                this_branch['risk_profile'] = {}
                for branch_id in this_branch['next_branches']:
                    next_branch = self.tree[branch_id]['risk_profile']
                    for key in next_branch.keys():
                        if key in this_branch['risk_profile'].keys():
                            this_branch['risk_profile'][key] += next_branch[key]
                        else:
                            this_branch['risk_profile'][key] = next_branch[key]

            if this_branch['type'] == 'TERMINAL':
                this_branch['risk_profile'] = {this_branch['exp_val']: this_branch['pathprob']}


        collect(this_branch=self.tree[0])




if __name__ == "__main__":
    import doctest
    doctest.testmod()
