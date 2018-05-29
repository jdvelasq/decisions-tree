"""
Functions in this Module
==============================================================================




"""
from hardDecisions.treenode import *

class DecisionTree:
    """Creates and evaluates a decision tree model. """

    def __init__(self):
        """Decision tree constructorself.
        """
        self.datatree = TreeNode('DMTREE')
        self.variables = new_node(parent=self.datatree, tag='VARS')
        self.treenodes = new_node(parent=self.datatree, tag='TREENODES')
        self.root = None
        self.globals = {}

    def terminal_node(self, name=None, expr=None):
        """Creates a decision tree's terminal node.
        """
        node = new_node(parent=self.variables,
                        tag=name,
                        attrib={'type':'TERMINAL', 'expr':expr})


    def chance_node(self, name=None, values=None):
        """Creates a decisions tree's internal chance node.
        """
        node = new_node(parent=self.variables,
                        tag=name,
                        attrib={'type':'CHANCE', 'values':values})


    def decision_node(self, name=None, values=None, max=True):
        """Creates a decisions tree's internal decision node.
        """
        node = new_node(parent=self.variables,
                        tag=name,
                        attrib={'type':'DECISION', 'values':values, 'max':max})


    def display_variables(self):
        """Display all the varibles in the decision tree.
        """
        txt = []
        for index, var in enumerate(self.variables):
            #
            txt.append('Node {:d}'.format(index))
            txt.append('    Name: ' + var.tag)
            txt.append('    Type: ' + var.get('type'))
            #
            if  var.get('type') == 'DECISION':
                #
                if  var.get('max') is True:
                    txt[-1] += ' - Maximum Payoff'
                else:
                    txt[-1] += ' - Minimum Payoff'
                txt.append('    Branches:')
                txt.append('                      Outcomes  Sucessor Var')
                for (value, next_node) in var.get('values'):
                    txt.append('                  {:12.3f}  {:d}'.format(value, next_node))
                txt.append('')
                #
            elif  var.get('type') == 'CHANCE':
                #
                txt.append('    Branches:')
                txt.append('          Chance       Outcome  Sucessor Var')
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
        """Builds the decision tree using the information in the variables.
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
        build_node(parent=parent, var=self.variables[0])


    def evaluate(self):
        """Evalute the tree. First, the cumulative probabilities in all nodes
        are calculated. Finally, the algorithm computes the expected values."""
        self.compute_prob()
        self.compute_values()

    def compute_prob(self):
        """Computes the probabilities in all tree branches.
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
        """Compute expectes values.
        """
        def compute_node_value(node):

            type = node.get(key='type')

            if type == 'DECISION':
                if 'var' in node.keys():
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
        self.compute_prob()
        self.compute_values()
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


    def display_tree(self, maxdeep=None, policy_suggestion=False):
        """Prints the tree as text.

        """

        def print_node(prefix, node, last_node):

            node_number = node.get(key='node_number')
            var = node.get(key='var')
            type = node.get(key='type')

            ## prints the name and value of the variable

            print(prefix + '|')



            if 'var' in node.keys():
                if 'value' in node.keys():
                    txt = "| " + var + "=" + str(node.get(key='value'))
                else:
                    txt = "| " + var
                print(prefix + txt)

            ## prints the probability
            if 'prob' in node.keys():
                txt = "| Prob={:1.2f}".format(node.get(key='prob'))
                print(prefix + txt)

            ## prints the cumulative probability
            if 'cprob' in node.keys():
                txt = "| CProb={:1.2f}".format(node.get(key='cprob'))
                print(prefix + txt)

            if 'expval' in node.keys() and node.get(key='expval') is not None:
                txt = "| ExpVal={:1.2f}".format(node.get(key='expval'))
                print(prefix + txt)

            if last_node:
                if type == 'DECISION':
                    txt = '+-------[D-{:d}] '.format(node_number)
                    txt = '\-------[D]'
                if type == 'CHANCE':
                    txt = '+-------[C-{:d}] '.format(node_number)
                    txt = '\-------[C]'
                if type == 'TERMINAL':
                    txt = '\-------[T] '
            else:
                if type == 'DECISION':
                    txt = '+-------[D-{:d}] '.format(node_number)
                    txt = '+-------[D]'
                if type == 'CHANCE':
                    txt = '+-------[C-{:d}] '.format(node_number)
                    txt = '+-------[C]'
                if type == 'TERMINAL':
                    txt = '+-------[T] '
            print(prefix + txt)

            next_node = node.get(key='next_node') if 'next_node' in node.keys() else None


            if maxdeep is not None and self.current_deep == maxdeep:
                return

            self.current_deep += 1

            if next_node is not None:

                if policy_suggestion is True and type == 'DECISION':
                    optbranch = node.get(key='optbranch')
                    # raise ValueError(optbranch.__repr__())
                    print_node(prefix + ' ' * 9, self.treenodes[next_node[optbranch]], last_node=True)
                else:
                    for index, node in enumerate(next_node):
                        is_last_node = True if index == len(next_node) - 1 else False
                        if last_node is True:
                            print_node(prefix + ' ' * 9, self.treenodes[node], last_node=is_last_node)
                        else:
                            print_node(prefix + '|' + ' ' * 8, self.treenodes[node], last_node=is_last_node)

            self.current_deep -= 1

        self.current_deep = 0
        print_node(prefix='', node=self.treenodes[0], last_node=True)





if __name__ == "__main__":
    import doctest
    doctest.testmod()
