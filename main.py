import random

lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["*", "!", "@", "#", "$", "%", "^", "&", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", ";", ":", "'", '"', ",", ".", "<", ">", "/", "?", "\\", "|"]

length = int(input("Lunghezza della password? "))
lower_count = int(input("Quante lettere minuscole? "))
upper_count = int(input("Quante lettere maiuscole? "))
while lower_count + upper_count > length:
    print("Il totale delle lettere non può superare la lunghezza.")
    lower_count = int(input("Quante lettere minuscole? "))
    upper_count = int(input("Quante lettere maiuscole? "))

include_symbols = input("Vuoi includere simboli? (s/n): ")
include_word = input("Vuoi includere una parola? (s/n): ")

password = []
lower_in_word = 0
upper_in_word = 0
if include_word.lower() == "s":
    word = input("Inserisci la parola: ")
    for character in word:
        if len(password) == length - lower_count - upper_count:
            break
        if character in lowercase and lower_in_word < lower_count:
            password.append(character)
            lower_in_word += 1
        elif character in uppercase and upper_in_word < upper_count:
            password.append(character)
            upper_in_word += 1
    if len(password) < len(word):
        print("La parola è stata abbreviata.")

for i in range(lower_count - lower_in_word):
    password.append(random.choice(lowercase))
for i in range(upper_count - upper_in_word):
    password.append(random.choice(uppercase))

characters = numbers + (symbols if include_symbols.lower() == "s" else [])
while len(password) < length:
    password.append(random.choice(characters))

random.shuffle(password)
print("".join(password))
