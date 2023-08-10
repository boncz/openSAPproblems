alphabet = 'abcdefghijklmnopqrstuvwxyz'

#determine the shift based on a letter in the keyword
def calculate_shifts(letter):
    return alphabet.find(letter)

#encrypt each letter in the message:
#take as input each character from the message, and each letter from the keyword
def encrypt_letter(char, key):
    #first we find the index of the letter that needs to be encrypted
    index = alphabet.index(char)
    #the new index for the encrypted letter will be the current index, plus the shift
    new_index = (index + calculate_shifts(key)) % 26
    new_char = alphabet[new_index]
    #return the encrypted character
    return new_char


#function to encrypt the entire message:
def encrypt_message(text = input("Please enter the text to encode: "), keyword = input("Please enter the keyword: ")):
    #ensure that the keyword given only contains letters:
    if keyword.isalpha():
        count = 0
        encrypted_message = ''
        #move through each character in the message:
        for char in text.lower():
            #check if the character is a letter:
            if char in alphabet:
                new_char = encrypt_letter(char, keyword[count])
                encrypted_message += new_char
                #make sure count doesn't exceed length of keyword:
                if count < len(keyword):
                    count += 0
                else:
                    count = 0
            #keep all other spaces and punctuation as they are
            else:
                encrypted_message += char
    #allows user to change the keyword to fit the parameters:
    else:
        keyword = input("keyword must only include letters. please try again: ")
        return encrypt_message(text, keyword)
    return encrypted_message

print(encrypt_message())