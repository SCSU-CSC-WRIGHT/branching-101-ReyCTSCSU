"""There are 3 errors in this code. Please use your own ability to find them all. Consider this a Python refresher."""
#Taking inputs to calculate the sum
def addNum ():
    total = 0
    for i in range(5):
        number = input("Enter a number: ")
        total += int(number)
    return total

#Calls upon the function addNum and executes it
def main():
    print("The running total is: ",  addNum())

if __name__ == "__main__":
    main()
