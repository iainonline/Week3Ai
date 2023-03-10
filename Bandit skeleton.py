# -*- coding: utf-8 -*-
"""
Sample Stationary Bandit Skeleton.
Author: Dr. Collin F. Lynch

This code probides a basic skeleton for the 
stationary bandit code.  It should be adapted
by the students for their work.
"""


import csv, random

import pandas


class BanditSet(object):
    """
    This object represents a set of arms for a stationary multi-armed 
    bandit problem it will store a fixed set of arms from a set and
    will then maintain them over multiple iterations.
    """
    
    def __init__(self, DataRows, ArmNames, ExpRate,
                 DistribParam, DecayRate, RewardWeight):
        """
        This initializes the set of choices by acting as a factory
        class to create one arm instance for each of the choices.
        The names and the rows will come from the file that 
        is read in. 
        """

        # Store the Data for later use.
        self.Data = DataRows
        
        # Initialize the parameters.
        self.ExplorationRate       = ExpRate
        self.DistributionParameter = DistribParam
        self.DecayRate             = DecayRate
        self.RewardWeight          = RewardWeight

        # Store items for each of the arms.
        self.Names         = ArmNames

        # Store a list for the weights.
        self.Weights       = [-1 for I in range(len(ArmNames))]

        # Calculate the starting probability and add it.
        StartProb = 1 / float(len(ArmNames))
        self.Probabilities = [StartProb for I in range(len(ArmNames))]

        # And store the Cumulative Reward
        self.CumulativeReward = 0

    def handleRows(self):
        """
        Process each of the rows and update our running reward 
        and the basic probabilies for each one.
        """
        # We initialize the cumulative
        # Reward to be 0
        self.CumulativeReward = 0

        probabilities = self.Probabilities
        bandit_names = self.Names
        data = self.Data

        # Now iterate over the rows and make each
        # of the choices.

        for index, row in data.iterrows():
            col = random.choices(bandit_names, probabilities)
            colname = col[0]
            print(index)
            print(data.loc[index])
            print(colname)
            print(data.loc[index, colname])

            # Iain McIntosh - the above is working !

            # Get the reward value from the row.
            #selectedcolname = bandit_data.columns.values[selectedcol]
            #print(bandit_data.loc[CurrRow, selectedcolname])
            # Update the reward weight.
            # And update the probabilities.

        # Return the cumulative reward.
        return(self.CumulativeReward)
    

    def pickArmIndex(self):
        """
        Pick an index based upon the probabilities
        using the cumulative score approach based
        upon a random value.
        """
        pass


    def getReward(self, Index):
        """
        Use the Armnames to get the reward for the 
        chosen arm.
        """
        pass
        
    
    def updateWeight(self, Index, Reward):
        """
        Update the weight for the chosen index using 
        the parameters.
        """
        pass


    def updateProbability(self, Index):
        """
        Update the probability for the index from its weight.
        """
        pass


    def normalizeProbabilities(self, Index, Reward):
        """
        Normalize the probability values.
        """
        pass


def read_file(inFile, bandit_names):
    df = pandas.read_csv(inFile, header=0, names=bandit_names)
    return df

bandit_names = ['Sample A', 'Sample B','Sample C','Sample D']
inFile = "LargeBanditData.csv"
bandit_data = read_file(inFile, bandit_names)
print(bandit_data.head(10))

gamma = .3
epsilon = .1
beta = .6
nu = .9

bandit = BanditSet(bandit_data, bandit_names, gamma, epsilon, beta, nu)
print(bandit.Data.head())
bandit.handleRows()