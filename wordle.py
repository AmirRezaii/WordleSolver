def showGuess(guess: str, guess_count: int):
    print(f"Guess {guess_count}: {guess.upper()}")


def firstGuess() -> str:
    return "tales".upper()

def getColors() -> str | None :
    colors = input("Input colors: ")
    
    if colors == "" or colors == "exit":
        exit(0)
    if len(colors) != 5:
        print(f"ERROR: Invalid number of colors. Expected 5, but got {len(colors)}!")
        return None
    for color in colors:
        if not color in ['b', 'y', 'g']:
            print(f"ERROR: Invalid color. Color should be 'b' or 'y' or 'g', But got {color}")
            return None
    return colors

def filterWords(words: list, word: str, colors: str) -> list:
    res = []

    blacked_letters = [] 
    yellow_letters = []
    green_letters = []

    for i, color in enumerate(colors):
        if color == 'b':
            blacked_letters.append((i, word[i]))
        elif color == 'y':
            yellow_letters.append((i, word[i]))
        else:
            green_letters.append((i, word[i]))

    for w in words:
        black = False
        for l in blacked_letters:
            if l[1] in w:
                black = True
                break
        if black == True:
            continue


        include = True
        for y in yellow_letters:
            if y[1] in w:
                if w[y[0]] == y[1]:
                    include = False
                    break
            else:
                include = False

        for g in green_letters:
            if g[1] not in w:
                include = False
            else:
                if w[g[0]] != g[1]:
                    include = False

        if include:
            res.append(w)

    return res

    
def nextGuess(words: list) -> str:
    letters_freq = ['E', 'T', 'A', 'O', 'I', 'S', 'R', 'N', 'H', 'L', 'D', 'Y', 'W', 'U', 'M', 'G', 'F', 'C', 'P', 'B', 'Z', 'X', 'V', 'Q', 'K', 'J']

    res = ""
    least = float('inf')
    for word in words:
        score = 0
        for letter in word:
            score += letters_freq.index(letter)

        if score < least:
            least = score
            res = word

    return res


def main():
    guess_count = 1
    guess = ""

    words = []
    
    with open("word.txt", "r") as f:
        words_string = f.read()
        words = words_string.splitlines()

    guess = firstGuess()

    showGuess(guess, guess_count)

    while guess_count <= 5:
        colors = getColors()
        if colors == None:
            continue

        words  = filterWords(words, guess, colors)
        print(words)
        guess = nextGuess(words)
        showGuess(guess, guess_count)
        guess_count += 1

try:
    main()
except KeyboardInterrupt:
    print("\nProgram interrupted by the user.")
