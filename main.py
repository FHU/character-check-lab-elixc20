#Remove pass and complete the code
def check_character(word, index):
   if 0 < index < len(word):
      index_character = word[index]
   if index_character.isalpha():
      return "letter"
   if index_character.isspace():
      return "white space"
   if index_character.isdigit():
      return "digit"
   else:
      return "unknown"

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))