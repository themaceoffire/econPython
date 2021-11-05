import json

def main():

    termsList = []
    termsDesc = []
    problemTypeList = []
    typeDesc = []

    with open('glossary.json') as glossary:
        data = json.load(glossary)


    termsObject = data['terms']
    problemTypeObject = data['problemTypes']

    print("I'm the glossary processor!")

    for terms in termsObject:
        term = terms['term'] + " - " + terms['def']
        termsList.append(term)
        termsDesc.append(terms['description'])
        

    for types in problemTypeObject:
        typeDef = types['fullName'] + " - " + types['meaning']
        problemTypeList.append(types['type'])
        typeDesc.append(typeDef)
    
    return(termsList, termsDesc, problemTypeList, typeDesc)

#TODO - figure out best data format for writing stuff to
    #   GUI glossary :)