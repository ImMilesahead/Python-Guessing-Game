def find(first, last, guess):
    num = (last + first) // 2
    
    r = input("Guess: " + str(guess) + "\tyour number exactly, lower than, or higher than " + str(num) + ": ")
    
    if r == 'lower':
        last = num
    if r == 'higher':
        first = num
    if r == 'exact':
        return num, guess
    if last == first or last == first + 1 or last == first - 1:
        return 'Error'
    guess += 1
    return find(first, last, guess)
print("Hello User, Would you think of a number then press ENTER when you have decided")
input()
print("\n\n\n\nI will have 7 guesses to try and guess your number")
num, guesses = find(0, 100, 0)
print("Your number was: " + str(num))

toWrite = "Number: \t" + str(num) + "\nGuesses:\t" + str(guesses) + "\n\n"

with open('results.dll', 'a') as file:
    file.write(toWrite)

file.close()