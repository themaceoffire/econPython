import numpy as np
import numpy_financial as npf
import os

###-----------Econ Logic-------------###

##---- Helper Functions -----###

#present value from future value F
def presentValuePfromF(i, n, F):
    i = i/100
    F = -F
    print(f'If statement for present value activated')
    return(npf.pv(i, n,0, F))

#future value from present value P
def futureValueFfromP(i, n, P):
    P = -P
    i = i/100
    print(f'If statement for future value activated')
    return(npf.fv(i, n, 0, P))

#Number of periods with set amount & interest rate
def numPeriods(i, A, P, F):
    #TODO - investige signs for this one
    print(f'If statement for number of periods activated')
    i = i/100
    return(npf.nper(i, A, P, F))

### TODO Calculate compound interest
    #Iterest rate for a loan per period
def compoundInterest(n, A, P):
    print(f'If statement for compound interest activated')

    P = -P
    return(npf.rate(n, A, P, 0)*100)


#---------------- Extended Analysis Functions--------------$

#TODO - dynamically handle different numbers of input for all following

#TODO - present worth analysis
def presentWorthAnalysis(input):
    print(" present worth function activated ")

#TODO - future worth analysis
def futureWorthAnalysis(input):
    print(" Future worth analysis activated ")

#TODO - annual worth analysis
def annaualWorthAnalysis(input):
    print("present worth analysis activated")






#         <3
#               <3
#    =/\    <3           /\=                    <3
#    / \'._   (\_/)   _.'/ \       (_      <3           _)
#   / .''._'--(^.^)--'_.''. \       /\          <3     /\
#  /.' _/ |`'=/ <3\='`| \_ `.\     / \'._   (\_/)   _.'/ \
# /` .' `\;-,'\___/',-;/` '. '\   /_.''._'--(^.^)--'_.''._\
#/.-' jgs   `\(---)/`       `-.\  | \_ / `;=/ <3\=;` \ _/ |
#             "   "               \/  `\__|`\___/`|__/`  \/
#                                  `       \(/ \)/       `
#                                           "   "
# M. Hurst