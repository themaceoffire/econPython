import numpy as np
import numpy_financial as npf
import os

#TODO - investigate overall signage

###-----------Econ Logic-------------###

##---- Helper Functions -----###

#present value from future value F
def presentValuePfromF(i, n, F):
    i = i/100
    #F = -F
    print(f'If statement for present value activated')
    return(npf.pv(i, n, 0, F))

#future value from present value P
def futureValueFfromP(i, n, P):
    #P = -P
    i = i/100
    print(f'If statement for future value activated')
    return(npf.fv(i, n, 0, P))

#payment value A from P, A/P
def paymentValueAfromP(i, n, P):
    #P = -P
    i = i/100
    print("If statement for A/P activated")
    return(npf.pmt(i, n, P))

#present value P from A, P/A
def presentValuePfromA(i, n, A):
    i = i/100
    print("If statement for P/A activated")
    return(npf.pv(i, n, A))

#Payment value A from F, A/F
def paymentValueAfromF(i, n, F):
    i = i/100
    print("If statement for A/F activated")

    return(npf.pmt(i, n, 0, F))


#Future value from A, F/A
def futureValueFfromA(i, n, A):
    i = i/100
    print("if statement for F/A activated")

    return(npf.fv(i, n, A, 0))


#Number of periods with set amount & interest rate
def numPeriods(i, A, P, F):
    print(f'If statement for number of periods activated')
    i = i/100
    return(npf.nper(i, A, P, F))

### Calculate compound interest
    #Iterest rate for a loan per period
def compoundInterest(n, A, P):
    print(f'If statement for compound interest activated')

    #P = -P
    return(npf.rate(n, A, P, 0)*100)


#---------------- Single project Analysis Functions--------------$


#present worth analysis
def presentWorthAnalysis(P, A, F, n, i):
    print(" present worth function activated ")
    PW = P + presentValuePfromA(i, n, -A) + presentValuePfromF(i, n, -F)
    return(PW)
    
    

#future worth analysis
def futureWorthAnalysis(P, A, n, i):
    print(" Future worth analysis activated ")
    FW = futureValueFfromP(i, n, -P) + futureValueFfromA(i, n, -A)
    return(FW)

#TODO - single cycle annual worth analysis
def annualWorthAnalysis(P, F, A, n, i):
    print("annual worth analysis activated")

    AW = A + paymentValueAfromP(i, n, -P) + paymentValueAfromF(i, n, -F)

    return(AW)




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