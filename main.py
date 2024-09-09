import random


MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1
#Defines a global variable (constant) 

ROWS = 3
COLS = 3
#3x3 grid for slot machine

symbolFrequency = {
    "A": 1,
    "B": 2,
    "C": 2,
    "D": 3,
    "E": 3
}
#Dictionary that indicates the frenqnecy of each symbol 

symbolMuliplyer = {
    "A": 7,
    "B": 5,
    "C": 4,
    "D": 3,
    "E": 1
}

def checkWinnings(columns, lines, bet, values):
    winnings = 0
    winningLines = []
    for line in range (lines):
        symbol = columns[0][line]
        for column in columns:
            symbolCheck = column[line]
            if symbol != symbolCheck:
                break
        else:
            winnings += values[symbol]*bet
            winningLines.append(line + 1)
        
    return winnings, winningLines



def slotMachineSpin(rows, cols, symbols):
    allSymbols = []
    for symbol, frequency in symbols.items():
        for _ in range (frequency):
            allSymbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        newSymbols = allSymbols[:]
        #colon makes a copy of dic not a refrence of it
        for row in range(rows):
            value = random.choice(newSymbols)
            newSymbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def printSlotMacnhine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(column) -1:
                print(column[row], end=" | ")
            else: 
                print (column[row], end="")
        
        print()



def deposit():
    while True:
        amount = input("Enter the amount you would like to deposit? $")
        if amount.isdigit():
            # returns true if string is a postive number 
            amount = int(amount)
            #type casting string digit into an int type
            if amount > 0:
                break
            else:
                print("You must enter a number greater than 0 to deposit.")
        else:
            print("You must enter a number")
    return amount

def getNumerOfLines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?")
        if lines.isdigit():
            # returns true if string is a postive number 
            lines = int(lines)
            #type casting string digit into an int type
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines")
        else:
            print("You must enter a number")
    return lines

def getBet():
    while True:
        amount = input("Enter the amount you would like to bet on each line? $")
        if amount.isdigit():
            # returns true if string is a postive number 
            amount = int(amount)
            #type casting string digit into an int type
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("You must enter a number between $" + str(MIN_BET) + "- $" + str(MAX_BET) + ".")
        else:
            print("You must enter a number")
    return amount

def spin(balance):
    lines = getNumerOfLines()
    while True:
        bet = getBet()
        totalBet = bet * lines
        if totalBet <= balance:
            break
        else:
            print("Insufficent Balance. Current Balance: $", balance)
    
    

    print("You are betting $"+ str(bet) + " on " + str(lines) + " lines. Total current bet is: $" + str(totalBet))

    slots = slotMachineSpin(ROWS, COLS, symbolFrequency)
    printSlotMacnhine(slots)
    winnings, winningLine = checkWinnings(slots, lines, bet, symbolMuliplyer)
    print("You won $", winnings)
    print("You won on lines: ", *winningLine)
    return winnings - totalBet

def main():  
# Defines main function
    balance = deposit()
    while True:
        print("Current balance is $", balance)
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    
    print("Ending balnce is now $", balance)
main()