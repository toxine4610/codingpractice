# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 13:11:12 2018

@author: rvrikhye
"""

class SubArray(object):
    
    def __init__(self, array):
        self.A = array
        self.N = len(array)
        
    def isList(self, ls):
        if hasattr(ls,"__iter__") != 0:
            return True
        else:
            print('Input is not a list')
            return False
        
    '''
    max sum of a subarray
    '''
    
    def maxSumConsecutive(self):
        max_here = 0
        max_so_far = 0
        start = 0 
        end   = 0
        s = 0
        if self.isList(self.A) == False:
            return [0,0,0]
        else:
            for i in range(len(self.A)):
                max_here += self.A[i]
                if max_here < 0:
                    max_here = 0
                    s = i+1
                if max_here > max_so_far:
                    max_so_far = max_here
                    end = i
                    start = s
        self.MaxSumConsec = max_so_far
        self.MaxConsecArray = self.A[start:end+1]
        return [max_so_far, start, end]
    
    
    '''
    max sum of non consecutive elements
    '''
    
    def maxSumNonConsecutive(self):
        max_cons = 0       #<-- max sum including the previous element
        max_here = 0  #<-- max sum excluding previous element
        if self.isList(self.A) == False:
            self.MaxSumNonConsec = 0
        else:
            for i in range(len(self.A)):
                new_max_here = max( max_here, max_cons ) #<-- max sum including previous element
                max_cons = max_here + self.A[i] # <--- update the max sum
                max_here = new_max_here 
        self.MaxSumNonConsec = max(max_here, max_cons)
        return self.MaxSumNonConsec
    
    '''
    max product of a subarray
    '''
    def maxProductConsecutive(self):
        max_so_far = 1
        min_here = 1
        max_here = 1
        end = 0
        start = 0
        s = 0
        if self.isList(self.A) == False:
            return 0
        else:
            for i in range(self.N):
                if self.A[i] == 0:
                    s = i+1
                    max_here = 1
                    min_here = 1
                elif self.A[i] > 0:
                    max_here = max_here*self.A[i]
                    min_here = 1
                elif self.A[i] < 0:
                    max_here_temp = max_here
                    max_here = max( min_here*self.A[i], 1 ) # this will be > 1 if 2 consecutive negative values multiply
                    min_here = max_here_temp*self.A[i]
                    
                if max_here > max_so_far:
                    max_so_far = max_here
                    end = i
                    start = s
            self.MaxProduct = max_so_far
            self.MaxProdArray = self.A[start:end+1]
            return [max_so_far, start, end]
'''
test
'''

A =  [6, -3, -10, 0, 2]
s = SubArray(A)
max_so_far, start, end = s.maxSumConsecutive()
max_nonconsecutive = s.maxSumNonConsecutive()
max_product, startProd, endProd = s.maxProductConsecutive()