a = input()
first = a[0]

if a.isalpha():
    if first == "a" or "e" or "i" or "o" or "u":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("invalid")
