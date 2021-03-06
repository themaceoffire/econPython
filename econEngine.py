import numpy as np
import numpy_financial as npf
import os

###-----------Econ Logic-------------###

##---- Helper Functions -----###

#present value from future value F
def presentValuePfromF(i, n, F):
    i = i/100
    print(f'If statement for present value activated')
    return(npf.pv(i, n,0, F))

#future value from present value P
def futureValueFfromP(i, n, P):
    i = i/100
    print(f'If statement for future value activated')
    return(npf.fv(i, n, 0, P))

#Number of periods with set amount & interest rate
def numPeriods(i, A, P, F):
    print(f'If statement for number of periods activated')
    i = i/100
    return(npf.nper(i, A, P, F))

### TODO Calculate compound interest
    #Iterest rate for a loan per period
def compoundInterest(n, A, P):
    print(f'If statement for compound interest activated')






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