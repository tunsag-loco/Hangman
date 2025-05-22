import random
import string

# Үгсийг агуулсан файл
WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Файлаас үгсийг ачааллаж байна...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print(len(wordlist), "үг ачааллаа.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

# ASCII дүрслэл: Hangman-ийн зургууд
HANGMAN_PICS = [
    """
     _______
    |/      |
    |
    |
    |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |
    |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |       |
    |       |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \|
    |       |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      /
    |
    |___
    """,
    """
     _______
    |/      |
    |      (_)
    |      \|/
    |       |
    |      / \\
    |
    |___
    """
]

def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    return guessed

def getAvailableLetters(lettersGuessed):
    remaining = [l for l in string.ascii_lowercase if l not in lettersGuessed]
    return ''.join(remaining)

def hangman(secretWord):
    print("Та Hangman тоглоомд тавтай морил!")
    print("Би", len(secretWord), "үсэгтэй үг бодлоо.")
    
    mistakesMade = 0
    lettersGuessed = []

    while mistakesMade < len(HANGMAN_PICS) - 1:
        print("-------------")
        print("Үлдсэн оролдлого:", (len(HANGMAN_PICS) - 1) - mistakesMade)
        print("Таасан үсгүүд:", ' '.join(lettersGuessed))
        print("Таагаагүй үсгүүд:", getAvailableLetters(lettersGuessed))
        print("Одоогийн байдал:", getGuessedWord(secretWord, lettersGuessed))
        print(HANGMAN_PICS[mistakesMade])

        guess = input("Нэг үсэг таана уу: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("❗ Зөвхөн нэг үсэг оруулна уу.")
            continue

        if guess in lettersGuessed:
            print("❗ Энэ үсгийг аль хэдийн таасан байна:", guess)
            continue

        lettersGuessed.append(guess)

        if guess in secretWord:
            print("✅ Сайн байна! Та зөв таалаа:", getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed):
                print("🎉 Баяр хүргэе! Та уг үгийг бүрэн таалаа:", secretWord)
                break
        else:
            mistakesMade += 1
            print("❌ Уучлаарай, энэ үсэг миний бодсон үгэнд байхгүй.")
            print(HANGMAN_PICS[mistakesMade])
    
    if not isWordGuessed(secretWord, lettersGuessed):
        print("-------------")
        print("😢 Та бүх оролдлогоо дуусгалаа.")
        print("Миний бодсон үг бол:", secretWord)
        print("Сүүлчийн дүрслэл:")
        print(HANGMAN_PICS[-1])

# Тоглоомыг эхлүүлэх хэсэг
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
