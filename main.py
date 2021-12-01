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
        if input == "F" or "P" or "A":
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


            #TODO - compound interest
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

        if(problemType=="Future Value, F, from P"):
            self.ids.mutable1.hint_text = i
            self.ids.mutable2.hint_text = n
            self.ids.mutable3.hint_text = P

        if(problemType=="Present Value of a Series"):
            self.ids.mutable1.hint_text = i
            self.ids.mutable2.hint_text = n
            self.ids.mutable3.hint_text = P

        if(problemType=="Number of Periods"):
            self.ids.mutable1.hint_text = i
            self.ids.mutable2.hint_text = A
            self.ids.mutable3.hint_text = P
            self.ids.mutable4.hint_text = F

            self.ids.mutable4.size_hint_y = 0.1

        if(problemType=="Find Compound Interest"):
            self.ids.mutable1.hint_text = n
            self.ids.mutable2.hint_text = A
            self.ids.mutable3.hint_text = P


        #reseting contextual values
        if(problemType != "Number of Periods" and self.ids.mutable4.size_hint_y == 0.1):
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
        self.ids.table_selection_disp.text = f"{value}"

    def reset(self):
        print("reset called")
        self.ids.A0.text = ""
        self.ids.A0type.text = "..."
        self.ids.A1.text = ""
        self.ids.A1type.text = "..."
        self.ids.A2.text = ""
        self.ids.A2type.text = "..."
        self.ids.A3.text = ""
        self.ids.A3type.text = "..."
        self.ids.A4.text = ""
        self.ids.A4type.text = "..."
        self.ids.A5.text = ""
        self.ids.A5type.text = "..."
        self.ids.A6.text = ""
        self.ids.A6type.text = "..."
        self.ids.A7.text = ""
        self.ids.A7type.text = "..."
        self.ids.A8.text = ""
        self.ids.A8type.text = "..."
        self.ids.A9.text = ""
        self.ids.A9type.text = "..."
        self.ids.A10.text = ""
        self.ids.A10type.text = "..."
        self.ids.iRate.text = ""
        self.ids.answer_spot.text = ""

    def tableGo(self):

        #saving the values in the table to easier to handle variables
        # validating input & storing fields that have been filled
        if checkEmpty(self.ids.A0.text) and checkEmpty(self.ids.A0type.text):
            A0 = self.ids.A0.text
            A0type = self.ids.A0type.text
        else:
            A0 = False
            A0type = False

        if checkEmpty(self.ids.A1.text) and checkEmpty(self.ids.A1type.text):
            A1 = self.ids.A1.text
            A1type = self.ids.A1type.text
        else:
            A1 = False
            A1type = False

        if checkEmpty(self.ids.A2.text) and checkEmpty(self.ids.A2type.text):
            A2 = self.ids.A2.text
            A2type = self.ids.A2type.text
        else:
            A2 = False
            A2type = False

        if checkEmpty(self.ids.A3.text) and checkEmpty(self.ids.A3type.text):
            A3 = self.ids.A3.text
            A3type = self.ids.A3type.text
        else:
            A3 = False
            A3type = False

        if checkEmpty(self.ids.A4.text) and checkEmpty(self.ids.A4type.text):
            A4 = self.ids.A4.text
            A4type = self.ids.A4type.text
        else:
            A4 = False
            A4type = False
        
        if checkEmpty(self.ids.A5.text) and checkEmpty(self.ids.A5type.text):
            A5 = self.ids.A5.text
            A5type = self.ids.A5type.text
        else:
            A5 = False
            A5type = False

        if checkEmpty(self.ids.A6.text) and checkEmpty(self.ids.A6type.text):
            A6 = self.ids.A6.text
            A6type = self.ids.A6type.text
        else:
            A6 = False
            A6type = False

        if checkEmpty(self.ids.A7.text) and checkEmpty(self.ids.A7type.text):
            A7 = self.ids.A7.text
            A7type = self.ids.A7type.text
        else:
            A7 = False
            A7type = False

        if checkEmpty(self.ids.A8.text) and checkEmpty(self.ids.A8type.text):
            A8 = self.ids.A8.text
            A8type = self.ids.A8type.text
        else:
            A8 = False
            A8type = False

        if checkEmpty(self.ids.A9.text) and checkEmpty(self.ids.A9type.text):
            A9 = self.ids.A9.text
            A9type = self.ids.A9type.text
        else:
            A9 = False
            A9type = False

        if checkEmpty(self.ids.A10.text) and checkEmpty(self.ids.A10type.text):
            A10 = self.ids.A10.text
            A10type = self.ids.A10type.text
        else:
            A10 = False
            A10type = False

        iRate = self.ids.iRate.text


        try:
            tableType = self.ids.table_selection_id.text
            iRate = float(self.ids.iRate.text)
        except:
            self.ids.answer_spot.text = "Please make a problem type selection and ensure to enter an interest rate."
            return
        
        try:
            
            # expected tableInput structure
            # [{'n' : 0, 'value': 120000, 'type' : "F"}]
            #access syntax
            # a[0]['type']

            if tableType == "Present Worth Analysis":
                tableInput = []
                if A0 and A0type:
                    tableInput.append({'n' : 0, 'value' : float(A0), 'type' : A0type})

                if A1 and A1type:
                    tableInput.append({'n': 1, 'value' : float(A1), 'type' : A1type})

                if A2 and A2type:
                    tableInput.append({'n' : 2, 'value' : float(A2), 'type' : A2type})

                if A3 and A3type:
                    tableInput.append({'n' : 3, 'value' : float(A3), 'type' : A3type})

                if A4 and A4type:
                    tableInput.append({'n' : 4, 'value' : float(A4), 'type' : A4type})

                if A5 and A5type:
                    tableInput.append({'n' : 5, 'value' : float(A5), 'type' : A5type})

                if A6 and A6type:
                    tableInput.append({'n' : 6, 'value' : float(A6), 'type' : A6type})
                
                if A7 and A7type:
                    tableInput.append({'n' : 7, 'value' : float(A7), 'type' : A7type})

                if A8 and A8type:
                    tableInput.append({'n' : 8, 'value' : float(A8), 'type' : A8type})

                if A9 and A9type:
                    tableInput.append({'n' : 9, 'value' : float(A9), 'type' : A9type})

                if A10 and A10type:
                    tableInput.append({'n' : 10, 'value' : float(A10), 'type' : A10type})

                print(tableInput)
                econEngine.presentWorthAnalysis(tableInput, iRate)

            if tableType == "Future Worth Analysis":
                tableInput = []
                if A0 and A0type:
                    tableInput.append({'n' : 0, 'value' : float(A0), 'type' : A0type})

                if A1 and A1type:
                    tableInput.append({'n': 1, 'value' : float(A1), 'type' : A1type})

                if A2 and A2type:
                    tableInput.append({'n' : 2, 'value' : float(A2), 'type' : A2type})

                if A3 and A3type:
                    tableInput.append({'n' : 3, 'value' : float(A3), 'type' : A3type})

                if A4 and A4type:
                    tableInput.append({'n' : 4, 'value' : float(A4), 'type' : A4type})

                if A5 and A5type:
                    tableInput.append({'n' : 5, 'value' : float(A5), 'type' : A5type})

                if A6 and A6type:
                    tableInput.append({'n' : 6, 'value' : float(A6), 'type' : A6type})
                
                if A7 and A7type:
                    tableInput.append({'n' : 7, 'value' : float(A7), 'type' : A7type})

                if A8 and A8type:
                    tableInput.append({'n' : 8, 'value' : float(A8), 'type' : A8type})

                if A9 and A9type:
                    tableInput.append({'n' : 9, 'value' : float(A9), 'type' : A9type})

                if A10 and A10type:
                    tableInput.append({'n' : 10, 'value' : float(A10), 'type' : A10type})

                print(tableInput)

                econEngine.futureWorthAnalysis(tableInput, iRate)

            if tableType == "Annual Worth Analysis":
                tableInput = []
                if A0 and A0type:
                    tableInput.append({'n' : 0, 'value' : float(A0), 'type' : A0type})

                if A1 and A1type:
                    tableInput.append({'n': 1, 'value' : float(A1), 'type' : A1type})

                if A2 and A2type:
                    tableInput.append({'n' : 2, 'value' : float(A2), 'type' : A2type})

                if A3 and A3type:
                    tableInput.append({'n' : 3, 'value' : float(A3), 'type' : A3type})

                if A4 and A4type:
                    tableInput.append({'n' : 4, 'value' : float(A4), 'type' : A4type})

                if A5 and A5type:
                    tableInput.append({'n' : 5, 'value' : float(A5), 'type' : A5type})

                if A6 and A6type:
                    tableInput.append({'n' : 6, 'value' : float(A6), 'type' : A6type})
                
                if A7 and A7type:
                    tableInput.append({'n' : 7, 'value' : float(A7), 'type' : A7type})

                if A8 and A8type:
                    tableInput.append({'n' : 8, 'value' : float(A8), 'type' : A8type})

                if A9 and A9type:
                    tableInput.append({'n' : 9, 'value' : float(A9), 'type' : A9type})

                if A10 and A10type:
                    tableInput.append({'n' : 10, 'value' : float(A10), 'type' : A10type})

                print(tableInput)

                econEngine.annaualWorthAnalysis(tableInput, iRate)
            else:
                self.ids.answer_spot.text = "Please check that you made a problem type selection."
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