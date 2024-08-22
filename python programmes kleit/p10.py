#Program to check if the alphabet is Vowel or Consonant
alphabet = input("Enter an alphabet: ").lower()
if alphabet in ('a', 'e', 'i', 'o', 'u'):
    print(f"{alphabet} is a vowel.")
else:
    print(f"{alphabet} is a consonant.")