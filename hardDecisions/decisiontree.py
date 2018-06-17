"""
Functions in this Module
==============================================================================


"""
from hardDecisions.treenode import *

class DecisionTree:
    """Creates and evaluates a decision tree model. """

    def __init__(self):
        """Decision tree constructor.
        """
        self.data = []
        self.tree = []
        self.globals = {}

    def terminal_node(self, name=None, expr=None):
        """Creates a decision tree's terminal node.
        """
        self.data.append({'tag':name,
                          'type':'TERMINAL',
                          'expr':expr})

    def chance_node(self, name=None, values=None, ignore=False):
        """Creates a decisions tree's internal chance node.
        """
        self.data.append({'tag':name,
                          'type':'CHANCE',
                          'values':values,
                          'ignore':ignore})

    def decision_node(self, name=None, values=None, max=True, ignore=False):
        """Creates a decisions tree's internal decision node.
        """
        self.data.append({'tag':name,
                          'type':'DECISION',
                          'values':values,
                          'max':max,
                          'ignore':ignore})

    def display_data(self):
        """Display all the varibles in the decision tree.
        """
        txt = []
        for index, node in enumerate(self.data):
            #
            txt.append('Node {:d}'.format(index))
            txt.append('    Name: ' + node.get('tag'))
            txt.append('    Type: ' + node.get('type'))
            #
            if  node.get('type') == 'DECISION':
                #
                txt[-1] += ' - Maximum Payoff' if node.get('max') is True else ' - Minimum Payoff'
                txt.append('    Branches:')
                txt.append('                      Outcomes  Sucessor Node')
                for (value, next_node) in node.get('values'):
                    txt.append('                  {:12.3f}  {:d}'.format(value, next_node))
                txt.append('')
                #
            elif  node.get('type') == 'CHANCE':
                #
                txt.append('    Branches:')
                txt.append('          Chance       Outcome  Sucessor Node')
                for (prob, value, next_node) in node.get('values'):
                    txt.append('           {:5.2f}  {:12.3f}  {:d}'.format(prob, value, next_node))
                txt.append('')
                #
            elif  node.get('type') == 'TERMINAL':
                #
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
                              'node_number':len(self.tree)})
            #
            return (len(self.tree)- 1, self.tree[-1])


        def set_branch_data(this_branch, node, path):

            def set_terminal():
                this_branch['type'] = node.get('type')
                this_branch['terminal'] = node.get('tag')
                if this_branch.get('ignore', True) is False:
                    path.append(this_branch.get('tag'))
                this_branch['expr'] = '+'.join(path) if node.get('expr') is None else node.get('expr')

            def set_decision():
                this_branch['type'] = node.get('type')
                this_branch['forced_branch'] = None
                this_branch['next_node'] = []
                this_branch['max'] = node.get('max')
                if this_branch.get('ignore', True) is False:
                    path.append(this_branch.get('tag'))
                #
                for i, (outcome, next_node) in enumerate(node.get('values')):
                    #
                    next_branch_index, next_branch = new_branch()
                    this_branch['next_node'].append(next_branch_index)
                    next_branch['ignore'] = node.get('ignore')
                    next_branch['tag'] = node.get('tag')
                    next_branch['value'] = outcome
                    #
                    set_branch_data(this_branch=next_branch,
                                 node=self.data[next_node],
                                 path=path.copy())

            def set_chance():
                this_branch['type'] = node.get('type')
                this_branch['forced_branch'] = None
                this_branch['next_node'] = []
                if this_branch.get('ignore', True) is False:
                    path.append(this_branch.get('tag'))
                #
                for index, (prob, outcome, next_node) in enumerate(node.get('values')):
                    #
                    branch_index, next_branch = new_branch()
                    this_branch['next_node'].append(branch_index)
                    next_branch['ignore'] = node.get('ignore')
                    next_branch['tag'] = node.get('tag')
                    next_branch['value'] = outcome
                    next_branch['prob'] = prob
                    #
                    set_branch_data(this_branch=next_branch,
                                 node=self.data[next_node],
                                 path=path.copy())

            ####
            if node.get('type') == 'DECISION':
                set_decision()
            elif node.get('type') == 'CHANCE':
                set_chance()
            elif node.get('type') == 'TERMINAL':
                set_terminal()
            else:
                pass
        ###
        self.tree = []
        path = []
        _ , this_branch = new_branch()
        set_branch_data(this_branch=this_branch,
                        node=self.data[0],
                        path=path.copy())



    def display_tree(self, maxdeep=None, selected_strategy=False):
        """Prints the tree as text.
        """

        def print_node(prefix, node, last_node):

            print(prefix + '|')

            type = node['type']
            if 'node_number' in node.keys():
                node_number = node['node_number']
                print(prefix + '| #' + str(node_number))


            ## prints the name and value of the variable
            if 'tag' in node.keys():
                var = node['tag']
                if 'value' in node.keys():
                    txt = "| " + var + "=" + str(node['value'])
                else:
                    txt = "| " + var
                print(prefix + txt)

            ## prints the probability
            if 'prob' in node.keys():
                txt = "| Prob={:1.2f}".format(node['prob'])
                print(prefix + txt)

            ## prints the cumulative probability
            if type == 'TERMINAL' and 'pathprob' in node.keys():
                txt = "| PathProb={:1.2f}".format(node['pathprob'])
                print(prefix + txt)

            if 'exp_val' in node.keys() and node['exp_val'] is not None:
                txt = "| ExpVal={:1.2f}".format(node['exp_val'])
                print(prefix + txt)

            if 'risk_profile' in node.keys() and type != 'TERMINAL':
                print(prefix + "| Risk Profile:")
                print(prefix + "|      Value  Prob")
                for key in sorted(node['risk_profile']):
                    txt = "|   {:8.2f} {:5.2f}".format(key, node['risk_profile'][key])
                    print(prefix + txt)

            if 'sel_strategy' in node.keys() and node['sel_strategy'] is True:
                txt = "| (selected strategy)"
                print(prefix + txt)

            if 'forced_branch' in node.keys() and node['forced_branch'] is not None:
                txt = "| (forced branch = {:1d})".format(node['forced_branch'])
                print(prefix + txt)


            next_node = node['next_node'] if 'next_node' in node.keys() else None

            if last_node:
                if type == 'DECISION':
                    txt = '\-------[D]'
                if type == 'CHANCE':
                    txt = '\-------[C]'
                if type == 'TERMINAL':
                    txt = '\-------[T] {:s}={:s}'.format(node['terminal'], node['expr'])
            else:
                if type == 'DECISION':
                    txt = '+-------[D]'
                if type == 'CHANCE':
                    txt = '+-------[C]'
                if type == 'TERMINAL':
                    txt = '+-------[T] {:s}={:s}'.format(node['terminal'], node['expr'])
            print(prefix + txt)

            if maxdeep is not None and self.current_deep == maxdeep:
                return

            self.current_deep += 1

            if next_node is not None:

                if selected_strategy is True and type == 'DECISION':
                    optbranch = node['opt_branch']
                    if last_node is True:
                        print_node(prefix + ' ' * 9, self.tree[next_node[optbranch]], last_node=True)
                    else:
                        print_node(prefix + '|' + ' ' * 8, self.tree[next_node[optbranch]], last_node=True)
                else:
                    for index, node in enumerate(next_node):
                        is_last_node = True if index == len(next_node) - 1 else False
                        if last_node is True:
                            print_node(prefix + ' ' * 9, self.tree[node], last_node=is_last_node)
                        else:
                            print_node(prefix + '|' + ' ' * 8, self.tree[node], last_node=is_last_node)

            self.current_deep -= 1

        self.current_deep = 0
        print_node(prefix='', node=self.tree[0], last_node=True)




    def evaluate(self):
        """Evalute the tree. First, the cumulative probabilities in all nodes
        are calculated. Finally, the algorithm computes the expected values."""

        def compute_values():
            """computes expected values.
            """
            def compute_node_value(node):

                type = node['type']

                if type == 'DECISION':
                    if 'tag' in node.keys():
                        var = node['tag']
                        value = node['value']
                        self.globals[var] = value
                    next_node = node['next_node']
                    ismax = node['max']
                    expval = None

                    for index, numnode in enumerate(next_node):
                        compute_node_value(node=self.tree[numnode])
                        if node['forced_branch'] is None:
                            if expval is None:
                                expval = self.tree[numnode].get('exp_val')
                                node['opt_branch'] = index
                            if ismax is True and expval < self.tree[numnode].get('exp_val'):
                                expval = self.tree[numnode].get('exp_val')
                                node['opt_branch'] = index
                            if ismax is False and expval > self.tree[numnode].get('exp_val'):
                                expval = self.tree[numnode].get('exp_val')
                                node['opt_branch'] = index
                        else:
                            if index == node['forced_branch']:
                                expval = self.tree[numnode].get('exp_val')
                                node['opt_branch'] = index

                    node['exp_val'] = expval


                if type == 'CHANCE':
                    var = node['tag']
                    value = node['value']
                    self.globals[var] = value
                    next_node = node['next_node']
                    expval = 0
                    if node['forced_branch'] is None:
                        for numnode in next_node:
                            compute_node_value(node=self.tree[numnode])
                            expval += self.tree[numnode].get('exp_val') * self.tree[numnode].get('prob') / 100
                    else:
                        for index, numnode in enumerate(next_node):
                            if index == node['forced_branch']:
                                compute_node_value(node=self.tree[numnode])
                                expval += self.tree[numnode].get('exp_val')
                            else:
                                compute_node_value(node=self.tree[numnode])
                                expval += 0
                    node['exp_val'] = expval

                if type == 'TERMINAL':
                    var = node['tag']
                    value = node['value']
                    self.globals[var] = value
                    node['exp_val'] = eval(node['expr'], self.globals.copy())

            compute_node_value(node=self.tree[0])


        def compute_prob():
            """Computes the probabilities in all tree branches.
            """
            def compute_node_prob(node, probability, sel_strategy):

                if node['type'] == 'DECISION':
                    node['sel_strategy'] = sel_strategy
                    if sel_strategy is True:
                        for index, numnode in enumerate(node['next_node']):
                            if index == node['opt_branch']:
                                compute_node_prob(node=self.tree[numnode],
                                                  probability=probability,
                                                  sel_strategy=True)
                            else:
                                compute_node_prob(node=self.tree[numnode],
                                                  probability=0,
                                                  sel_strategy=False)
                    else:
                        if sel_strategy is True:
                            current_prob = probability
                        else:
                            current_prob = 0
                        for numnode in node['next_node']:
                            compute_node_prob(node=self.tree[numnode],
                                              probability=current_prob,
                                              sel_strategy=False)
                if node['type'] == 'CHANCE':
                    node['sel_strategy'] = sel_strategy
                    if node['forced_branch'] is None:
                        for numnode in node['next_node']:
                            prob = self.tree[numnode]['prob']
                            compute_node_prob(node=self.tree[numnode],
                                              probability=probability * prob/100,
                                              sel_strategy = sel_strategy)
                    else:
                        for index, numnode in enumerate(node['next_node']):
                            if index == node['forced_branch']:
                                prob = self.tree[numnode]['prob']
                                prob = 100
                                compute_node_prob(node=self.tree[numnode],
                                                  probability=probability * prob/100,
                                                  sel_strategy = True)
                            else:
                                prob = self.tree[numnode]['prob']
                                prob = 0
                                compute_node_prob(node=self.tree[numnode],
                                                  probability=probability * prob/100,
                                                  sel_strategy = False)
                if node['type'] == 'TERMINAL':
                    node['sel_strategy'] = sel_strategy
                    node['pathprob'] = probability * 100
            #
            compute_node_prob(node=self.tree[0], probability=1.0, sel_strategy=True)

        self.cumvalue = 0
        compute_values()
        compute_prob()



    def compute_risk_profile(self):
        """Computes the risk profile for the selected strategy.
        """

        def collect(node):

            if node['sel_strategy'] is False:
                return

            if node['type'] == 'DECISION':
                for index, numnode in enumerate(node['next_node']):
                    collect(node=self.tree[numnode])
                next_opt_branch = node['next_node'][node['opt_branch']]
                node['risk_profile'] = self.tree[next_opt_branch]['risk_profile']

            if node['type'] == 'CHANCE':
                for index, numnode in enumerate(node['next_node']):
                    collect(node=self.tree[numnode])
                node['risk_profile'] = {}
                for numnode in node['next_node']:
                    dict = self.tree[numnode]['risk_profile']
                    for key in dict.keys():
                        if key in node['risk_profile'].keys():
                            node['risk_profile'][key] += dict[key]
                        else:
                            node['risk_profile'][key] = dict[key]


            if node['type'] == 'TERMINAL':
                node['risk_profile'] = {node['exp_val']: node['pathprob']}


        collect(node=self.tree[0])




if __name__ == "__main__":
    import doctest
    doctest.testmod()
