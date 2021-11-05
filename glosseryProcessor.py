import json

def main():

    termsList = []
    problemTypeList = []

    with open('glossary.json') as glossary:
        data = json.load(glossary)


    termsObject = data['terms']
    problemTypeObject = data['problemTypes']

    print("I'm the glossary processor!")

    for terms in termsObject:
        term = terms['type'] + " - " + terms['def']
        termsList.append(term)
        

    for types in problemTypeObject:
        problemDef = types['cat']
        problemTypeList.append(problemDef)
    
    return(termsList, problemTypeList)

#TODO - figure out best data format for writing stuff to
    #   GUI glossary :)