# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:11:38 2015

@author: uwe
"""


class electrical_demand():
    '''
    '''
    def __init__(self, **kwargs):
        self.annual_demand = kwargs.get('annual_elec_demand')
        if self.annual_demand is None:
            self.annual_demand = self.calculate_annual_demand()
        self.year = 2010  # temporarily
        self.profile = kwargs.get('profile')['deu_' + str(self.year)]
        self.elec_demand = self.scale_profile()

    def scale_profile(self):
        '''
        scale a given profile to a given annual demand, which is the sum
        of the single profile values
        '''
        self.elec_demand = (self.profile /
                            self.profile.sum() *
                            self.annual_demand)
        return self.elec_demand

    def calculate_annual_demand(self):
        '''
        calculate annual demand from statistic data
        '''
        self.annual_demand = 50 + 50
        return self.annual_demand


class heat_demand():
    # Das Gebäudeprofil kommt aus der Datenbank einer Datei oder einer anderen
    # Funktion.
    pass
