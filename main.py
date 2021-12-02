#don't forget virtual enviornment!!
#       py -m pip install --upgrade pip setuptools virtualenv
#       py -m virtualenv kivy_venv
#       kivy_venv\Scripts\activate


from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
import econEngine
import sys
import traceback
import glosseryProcessor
from kivy.uix.screenmanager import ScreenManager, Screen

#helper constants
i = "Interest rate (%)"
n = "Number of compounding periods (n)"
A = "Reoccuring regular amount (A)"
P = "Present value (P)"
F = "Future Value (F)"

#helper functions
def checkEmpty(input):
    if input:
        if input == "...":
            return False
        if input == "F" or "P":
            return True
        
        try:
            float(input)
        except:
            return False
    
    else:
        return False

#defining screens & window manager
class LandingScreen(Screen):
    pass


#ultimately handles comms between the mainscreen GUI and data elements
#within python logic
class MainScreen(Screen):
    
    #initialize infinite keywords & write glossary data
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MainScreen, self).__init__(**kwargs)


        #handles writing glossary data to GUI
        termsList, termDefs, problemTypesList, typeDefs = glosseryProcessor.main()
        
    #    self.ids.problemTypes_id.values = problemTypesList



    #passes data from GUI to econEngine class functions
    def press(self):
        print("button pressed")
        problemType = self.ids.selection_id.text

        try:
            #present value P from F
            if(problemType=="Present Value, P, from F"):
                    iVal = float(self.ids.mutable1.text)
                    nVal = float(self.ids.mutable2.text)
                    fVal = float(self.ids.mutable3.text)

                    answer = econEngine.presentValuePfromF(iVal, nVal, fVal)
                    answer = str(format(answer, '.2f'))
                    answer = "${:}".format(answer)
                    answer = f'The answer is: {answer}'

                    self.ids.selection_disp.text = answer

            #future value F from P
            if(problemType=="Future Value, F, from P"):
                iVal = float(self.ids.mutable1.text)
                nVal = float(self.ids.mutable2.text)
                aVal = float(self.ids.mutable3.text)

                answer = econEngine.futureValueFfromP(iVal, nVal, aVal)
                answer = str(format(answer, '.2f'))
                answer = "${:}".format(answer)
                answer = f'The answer is: {answer}'

                self.ids.selection_disp.text = answer

            #payment value A from P, A/P
            if(problemType == "Payment Value, A, from P"):
                iVal = float(self.ids.mutable1.text)
                nVal = float(self.ids.mutable2.text)
                pVal = float(self.ids.mutable3.text)

                answer = econEngine.paymentValueAfromP(iVal, nVal, pVal)
                answer = str(format(answer, '.2f'))
                answer = "${:}".format(answer)
                answer = f'The answer is: {answer}'

                self.ids.selection_disp.text = answer



            #present value P from A, P/A
            if(problemType == "Present Value, P, from A"):
                iVal = float(self.ids.mutable1.text)
                nVal = float(self.ids.mutable2.text)
                aVal = float(self.ids.mutable3.text)

                answer = econEngine.presentValuePfromA(iVal, nVal, aVal)
                answer = str(format(answer, '.2f'))
                answer = "${:}".format(answer)
                answer = f'The answer is: {answer}'

                self.ids.selection_disp.text = answer

            #Payment value A from F, A/F
            if(problemType == "Payment Value, A, from F"):
                iVal = float(self.ids.mutable1.text)
                nVal = float(self.ids.mutable2.text)
                fVal = float(self.ids.mutable3.text)
            
                answer = econEngine.paymentValueAfromF(iVal, nVal, fVal)
                answer = str(format(answer, '.2f'))
                answer = "${:}".format(answer)
                answer = f'The answer is: {answer}'

                self.ids.selection_disp.text = answer

            #Future value F from A, F/A
            if(problemType == "Future Value, F, from A"):
                iVal = float(self.ids.mutable1.text)
                nVal = float(self.ids.mutable2.text)
                aVal = float(self.ids.mutable3.text)

                answer = econEngine.futureValueFfromA(iVal, nVal, aVal)
                answer = str(format(answer, '.2f'))
                answer = "${:}".format(answer)
                answer = f'The answer is: {answer}'

                self.ids.selection_disp.text = answer


            #number of periods based on i, A, P & F values (N/(A,P,F))
            if(problemType=="Number of Periods"):
                iVal = float(self.ids.mutable1.text)
                aVal = float(self.ids.mutable2.text)
                pVal = float(self.ids.mutable3.text)
                fVal = float(self.ids.mutable4.text)

                answer = econEngine.numPeriods(iVal, aVal, pVal, fVal)
                answer = str(format(answer, '.2f'))
                answer = "${:}".format(answer)
                answer = f'The answer is: {answer}'

                self.ids.selection_disp.text = answer


            #- compound interest
            if(problemType=="Find Compound Interest"):
                nVal = float(self.ids.mutable1.text)
                aVal = float(self.ids.mutable2.text)
                pVal = float(self.ids.mutable3.text)

                answer = econEngine.compoundInterest(nVal, aVal, pVal)
                answer = str(format(answer, '.2f'))
                answer = "{:}%".format(answer)
                answer = f'The answer is: {answer}'

                self.ids.selection_disp.text = answer


            #TODO - APY vs APR

        #TODO - figure out how to do present worth analysis
        #TODO - annual worth analysis
        
        except:
            self.ids.selection_disp.text = "Please check your input."
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback)

    #selection made here - logic for contextual changes here also
    def spinner_click(self, value):
        self.ids.selection_disp.text = f'You selected {value}'

        problemType = value

        #handels contextual input
        if(problemType=="Present Value, P, from F"):
            self.ids.mutable1.hint_text = i
            self.ids.mutable2.hint_text = n
            self.ids.mutable3.hint_text = F
            self.ids.mutable4.size_hint_y = 0

        if(problemType=="Future Value, F, from P"):
            self.ids.mutable1.hint_text = i
            self.ids.mutable2.hint_text = n
            self.ids.mutable3.hint_text = P
            self.ids.mutable4.size_hint_y = 0

        if(problemType == "Payment Value, A, from P"):
            self.ids.mutable1.hint_text = i
            self.ids.mutable2.hint_text = n
            self.ids.mutable3.hint_text = P
            self.ids.mutable4.size_hint_y = 0

        if(problemType == "Present Value, P, from A"):
            self.ids.mutable1.hint_text = i
            self.ids.mutable2.hint_text = n
            self.ids.mutable3.hint_text = A
            self.ids.mutable4.size_hint_y = 0

        if(problemType == "Payment Value, A, from F"):
            self.ids.mutable1.hint_text = i
            self.ids.mutable2.hint_text = n
            self.ids.mutable3.hint_text = F
            self.ids.mutable4.size_hint_y = 0

        if(problemType=="Present Value of a Series"):
            self.ids.mutable1.hint_text = i
            self.ids.mutable2.hint_text = n
            self.ids.mutable3.hint_text = P
            self.ids.mutable4.size_hint_y = 0

        if(problemType=="Future Value, F, from A"):
            self.ids.mutable1.hint_text = i
            self.ids.mutable2.hint_text = n
            self.ids.mutable3.hint_text = A
            self.ids.mutable4.size_hint_y = 0

        if(problemType=="Number of Periods"):
            self.ids.mutable1.hint_text = i
            self.ids.mutable2.hint_text = A
            self.ids.mutable3.hint_text = P
            self.ids.mutable4.hint_text = F

            self.ids.mutable4.size_hint_y = 0.3

        if(problemType=="Find Compound Interest"):
            self.ids.mutable1.hint_text = n
            self.ids.mutable2.hint_text = A
            self.ids.mutable3.hint_text = P
            self.ids.mutable4.size_hint_y = 0


        #reseting contextual values
        if(problemType != "Number of Periods" and self.ids.mutable4.size_hint_y == 0.1):
            self.ids.mutable4.size_hint_y = 0

    def main_reset(self):
        self.ids.selection_id.text = "Please make a selection"
        self.ids.mutable1.text = ""
        self.ids.mutable2.text = ""
        self.ids.mutable3.text = ""
        self.ids.mutable4.text = ""
        self.ids.mutable4.size_hint_y = 0

#TODO - see if possible: iterate through glossary to display definitions
#       of whatever kinda value on right hand side

    pass

class TableScreen(Screen):
    
    #initialize infinite keywords & write glossary data
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(TableScreen, self).__init__(**kwargs)

    def table_spinner_click(self, value):
        #table_selection_disp
        problemType = str(value)
        self.ids.table_selection_disp.text = f"{value}"

        if problemType == "Present Worth Analysis":
            self.ids.mutableType1.text = "Initial P:"
            self.ids.mutableType2.text = "AOC: "
            self.ids.mutableType3.text = "Salvage: "
            self.ids.mutableInput3.disabled = False

        if problemType == "Future Worth Analysis":
            self.ids.mutableType1.text = "Initial P: "
            self.ids.mutableType2.text = "AOC: "
            self.ids.mutableType3.text = "Final year: "
            self.ids.mutableInput3.disabled = True

        if problemType == "Annual Worth Analysis":
            self.ids.mutableType1.text = "Initial P: "
            self.ids.mutableType2.text = "AOC: "
            self.ids.mutableType3.text = "Salvage Value:"
            self.ids.mutableInput3.disabled = False

        

        

    def reset(self):
        print("reset called")
        self.ids.mutableType1.text = ""
        self.ids.mutableType2.text = ""
        self.ids.mutableType3.text = ""
        self.ids.mutableInput3.text = ""
        self.ids.mutableInput2.text = ""
        self.ids.mutableInput1.text = ""
        self.ids.input3year.text = ""
        self.ids.mutableInput3.disabled = False
        self.ids.iRate.text = ""
        self.ids.answer_spot.text = ""

    def tableGo(self):

        #saving the values in the table to easier to handle variables
        # validating input & storing fields that have been filled
        
        iRate = self.ids.iRate.text


        try:
            tableType = self.ids.table_selection_id.text
            iRate = float(self.ids.iRate.text)
        except:
            self.ids.answer_spot.text = "Please make a problem type selection and ensure to enter an interest rate."
            return
        
        try:
            
            # expected tableInput structure
            # [{'n' : 0, 'value': 120000}]
            #access syntax
            # a[0]['type']

            if tableType == "Present Worth Analysis":

                pVal = float(self.ids.mutableInput1.text)
                aVal = float(self.ids.mutableInput2.text)
                fVal = float(self.ids.mutableInput3.text)
                nVal = float(self.ids.input3year.text)
                
                answer = econEngine.presentWorthAnalysis(pVal, aVal, fVal, nVal, iRate)
                answer = str(format(answer, '.2f'))
                answer = "${:}".format(answer)
                answer = f'The answer is: {answer}'

                self.ids.answer_spot.text = answer

            if tableType == "Future Worth Analysis":
                pVal = float(self.ids.mutableInput1.text)
                aVal = float(self.ids.mutableInput2.text)
                nVal = float(self.ids.input3year.text)

                answer = econEngine.futureWorthAnalysis(pVal, aVal, nVal, iRate)
                answer = str(format(answer, '.2f'))
                answer = "${:}".format(answer)
                answer = f'The answer is: {answer}'

                self.ids.answer_spot.text = answer

            if tableType == "Annual Worth Analysis":
                pVal = float(self.ids.mutableInput1.text)
                aVal = float(self.ids.mutableInput2.text)
                fVal = float(self.ids.mutableInput3.text)
                nVal = float(self.ids.input3year.text)

                answer = econEngine.annualWorthAnalysis(pVal, fVal, aVal, nVal, iRate)
                answer = str(format(answer, '.2f'))
                answer = "${:}".format(answer)
                answer = f'The answer is: {answer}'

                self.ids.answer_spot.text = answer
        except:
                self.ids.answer_spot.text = "Please check that you made a problem type selection, and that your input is valid."
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback.print_exception(exc_type, exc_value, exc_traceback)


    pass

class WindowManager(ScreenManager):
    pass


#loading specific kivy file :)
kv = Builder.load_file('engine.kv')

class MyApp(App):
    def build(self):
        return kv

if __name__ == '__main__':
    MyApp().run()


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