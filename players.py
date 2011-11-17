# -*- coding: utf-8 -*-
"""

pyNIRA firm and node classes

Created on Thu Nov 17 16:24:12 2011

@author: jamesz
"""


class NIRA_node:
    """
    
    Node class for defining nodes in NIRA.
    
    NIRA_node(name, generator, a, b)
    
        name: string or value identifier
        generator: 0/1 depending on generation status of node. 0 for demand-only
        a: linear inverse demand constant parameter
        b: linear inverse demand slope parameter
    """
    def __init__(self, name, generator, a, b):
        self.name = name
        self.generator = generator
        self.demd_const = a
        self.demd_grad = b
                        
    def inv_demand(self, q):
        """
        Calculate the price for a given quantity sold at this node.        
        """
        price = self.demd_const - self.demd_grad * q
        return price

    def cons_surp(self, q):
        """
        Calculate the consumer surplus for a given quantity sold at this node.        
        """
        cs = 0.5 * (self.demd_const - self.inv_demand(q)) * q
        return cs

class NIRA_firm:
    """
    
    Firm class for defining firms in NIRA.
    
    NIRA_firm(name, margcost, env_cost, nodes)
    
        name: string or value identifier
        marg_cost: value giving the constant marginal cost of the firm
        env_cost: array giving parametrisation of pollution function
        nodes: tuple of the nodes at which the firm sells
    """
    def __init__(self, name, margcost, nodes):
        self.name = name
        self.mc = margcost
        
    def profit(self, q, node):
        """
        Calculate the firms profits across al.        
        """