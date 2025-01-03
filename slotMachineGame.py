#slotMachineProgram3x3
import random

MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbols = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbolValue = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# To check whether a row/reel has matched or not and add-up the total score based on a win situation
def checkWinnings(value, lines, mainColumn, amount):
    winning = 0
    winningLines = [] #number of winning lines; not the number (th) of the won line
    for line in range(lines):
        symbol = mainColumn[0][line]

        for column in mainColumn: # As mainColumn is a 2D list, each iteration brings a 1D list
            symbolToCheck = column[line] #Here, an overlap occurs for the first element
            if symbol != symbolToCheck:
                break
        #it is a for-else loop, the else statement will execute only if the before (for) loop hasn't broken
        else:
            winning += amount * value[symbol]
            winningLines.append(line + 1)

    return winning, winningLines

def getSlotMachineSpin():
    allSymbol = []
    for symbol, symbol_count in symbols.items(): # returns A & 2 with each iteration/ as it is a dictionary, so we use two variables (symbol and symbol_count) to loop
        for _ in range(symbol_count): # loops through A, the number of times it is there in the dictionary, in case of A it loops 2 times
            allSymbol.append(symbol) # adds the value of A x2 times in the list

    mainColumn = [] # Mainly used for user display purposes or for combining the separate columns
    for _ in range(COLS): # _ is the anonymous operator, in loops it doesn't matter what we use
        column = []
        currentSymbols = allSymbol[:] # ":" is used for copying the dictionary without impacting the original dictionary/ currentSymbols is made a new copy everytime the above loops
        for _ in range(ROWS):
            value = random.choice(allSymbol)
            currentSymbols.remove(value)
            column.append(value) #The value is appended ROW-WISE, first iteration for 1st column-1st row, second iteration for 2nd row-1st column
        mainColumn.append(column)

    return mainColumn

# For making the list look like a real slot machine, For transposing the data from mainColumn
def printSlotMachine(mainColumn):
    for row in range(len(mainColumn[0])): #fixes the number of iterations/ range always starts from 0 by default
        #the below inner loop runs once for every column
        for i, column in enumerate(mainColumn): #enumerate returns the value of both index and its value; i takes the index and column takes the value
            if i != len(column) - 1:
                print(column[row], "| ", end="") #end tells what to end the line with, in this case with nothing
            else:
                print(column[row], end="")
        print("\n")

# For taking the user input for their current balance
def deposit():
    while True:
        amount = input("Enter your deposit: $")
        if amount.isdigit():
            amount = int(amount)

            if amount > 0:
                break
            else:
                print("Number must be positive")

        else:
            print("Please enter a number.")
    return amount

#For getting the number of lines user wants to bet upon
def getNumberOfLines():
    while True:
        lines = input("Enter the number of lines you would like to bet on(1 - " + str(MAX_LINES) +")? -> ")
        if lines.isdigit():
            lines = int(lines)

            if 1 <= lines <= 3:
                break
            else:
                print("Please a valid line amount")

        else:
            print("Please enter a number.")
    return lines

#For getting the amount the user wants to bet against each line
def getBetAmount():
    while True:
        amount = input("Enter your Bet Amount (must be within " + str(MIN_BET) + " - " + str(MAX_BET) + "): ")
        if amount.isdigit():
            amount = int(amount)

            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be within {MIN_BET} and {MAX_BET}")

        else:
            print("Please enter a number.")
    return amount

# A single game run
def spin(balance):
    while True:
        lineNum = getNumberOfLines()
        betAmount = getBetAmount()
        totalBet = lineNum * betAmount

        if totalBet > balance:
            print("You are low in cash. Bet something affordable.")
        else:
            break
    print(f"You are betting ${betAmount} on {lineNum} lines. Total Bet Amount: ${totalBet}")
    slots = getSlotMachineSpin()
    printSlotMachine(slots)
    win, wonLines = checkWinnings(symbolValue, lineNum, slots, betAmount)
    print(f"You win ${win} and on lines: ", *wonLines) # * is the splat operator, it is used to print the elements of list with space in between

    return win - totalBet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit)")
        if answer == "q" or balance == 0:
            break  #if the response is q, the function spin() is never called
        balance += spin(balance)

    print(f"You left with ${balance}")



main()