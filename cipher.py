# ceasar cypher

#initilize variable and set shift value
shift_letter = 0
cipher_shift = 5
final_message =''

#user input message
starting_message = input('Please enter a sentence: ')

#encode
for character in starting_message:
    #check for special character
    if character.isalpha():
        shift_letter = ord(character.lower()) + cipher_shift
        if shift_letter > 122:
            shift_letter -=26
        #append to final output if letter
        final_message += chr(shift_letter)
    else:
        #append to final output if special character
        final_message += character

#Output result
print('The encrypted sentence is:',final_message)
