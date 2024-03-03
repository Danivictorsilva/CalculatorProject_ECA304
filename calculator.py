import os
import cmath

def startCalculator(operations):
    optionSelection = ''
    infoMessage = ''
    while optionSelection != '0':
        os.system('clear')
        print('Welcome to Calculator Project v1.0!\nSelect the desired operation:\n')
        for key in operations: print(f'{key} - {operations[key]["name"].capitalize()}')
        print('0 - Return')
        if infoMessage != '': print('\n>>> ', infoMessage)
        optionSelection = input('\nInsert operation: ')
        if optionSelection in operations.keys():
            try:
                result = operations[optionSelection]['operator']()
                infoMessage = 'Result: ' + f'{result:.4f}'
            except:
                infoMessage = 'Something went wrong with operation. Try again'
        else: infoMessage = 'Invalid option'

def sumOperator():
    firstValue = complex(input('Insert first complex value: '))
    secondValue = complex(input('Insert second complex value: '))
    return firstValue + secondValue

def subtractionOperator():
    firstValue = complex(input('Insert first complex value: '))
    secondValue = complex(input('Insert second complex value: '))
    return firstValue - secondValue

def multiplicationOperator():
    firstValue = complex(input('Insert first complex value: '))
    secondValue = complex(input('Insert second complex value: '))
    return firstValue * secondValue

def divisionOperator():
    firstValue = complex(input('Insert first complex value: '))
    secondValue = complex(input('Insert second complex value: '))
    return firstValue / secondValue if secondValue != 0 else complex(cmath.inf) * firstValue

def sqrtOperator():
    value = complex(input('Insert complex value: '))
    return cmath.sqrt(value)

operations = {
    '1': {'name':'sum', 'operator': sumOperator},
    '2': {'name':'subtraction', 'operator': subtractionOperator},
    '3': {'name':'multiplication', 'operator': multiplicationOperator},
    '4': {'name':'division', 'operator': divisionOperator},
    '5': {'name':'square root', 'operator': sqrtOperator}
}

startCalculator(operations)
