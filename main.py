#don't forget virtual enviornment!!
#       py -m pip install --upgrade pip setuptools virtualenv
#       py -m virtualenv kivy_venv
#       kivy_venv\Scripts\activate


from kivy.app import App
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.widget import Widget
from kivy.lang import Builder
import json
import econEngine

#helper constants
i = "Interest rate (%)"
n = "Number of compounding periods (n)"
A = "Reoccuring regular amount (A)"
P = "Present value (P)"
F = "Future Value (F)"

#loading specific kivy file :)
Builder.load_file('engine.kv')

#ultimately handles comms between the GUI and data elements
#within python logic
class MyBoxLayout(Widget):

    #initialize infinite keywords
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyBoxLayout, self).__init__(**kwargs)


    #passes data from GUI to econEngine class functions
    def press(self):
        print("button pressed")
        problemType = self.ids.selection_id.text

        #present value P from F
        if(problemType=="Present Value, P, from F"):
                iVal = float(self.ids.mutable1.text)
                nVal = float(self.ids.mutable2.text)
                fVal = float(self.ids.mutable3.text)

                answer = econEngine.presentValuePfromF(iVal, nVal, fVal)
                answer = str(format(answer, '.2f'))
                answer = f'The answer is: {answer}'

                self.ids.selection_disp.text = answer

        #future value F from P
        if(problemType=="Future Value, F, from P"):
            iVal = float(self.ids.mutable1.text)
            nVal = float(self.ids.mutable2.text)
            aVal = float(self.ids.mutable3.text)

            answer = econEngine.futureValueFfromP(iVal, nVal, aVal)
            answer = str(format(answer, '.2f'))
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
            answer = f'The answer is: {answer}'

            self.ids.selection_disp.text = answer


        #TODO - compound interest
        if(problemType=="Find Compound Interest"):
            pass

        #TODO - APY vs APR

    #TODO - figure out how to do present worth analysis

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

#TODO - iterate through glossary to display definitions
#       of whatever kinda value on right hand side


class MyApp(App):
    def build(self):
        return MyBoxLayout()

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