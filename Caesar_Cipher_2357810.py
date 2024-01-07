import os

def welcome():
  '''This function will give the welcome message to the user'''
  print("Welcome to the Caesar Cipher")
  print("This program encrypts and decrypts text using Caesar Cipher.")

def enter_message():
  '''This function takes the input of the user,
      choose_mode allows user to choose either the message encrypt or decrypt, 
      message allows user to input the message for the encryption or decryption and change the message into uppercase,
       shift allows user how many times the message want to shift,
        and return the choose_mode, message,shift '''
  choose_mode = input("Would you like to encrypt (e) or decrypt (d): ")
  while choose_mode not in ["e", "d"]:
    print("Invalid Mode")
    choose_mode = input("Would you like to encrypt (e) or decrypt (d): ")
  message = input("What message would you like to {}: ".format(choose_mode))
  message = message.upper()
  shift = int(input("What is the shift number: "))
  return choose_mode, message, shift

def encrypt(message, shift):
  '''This function is used for the encryption.
  it encrypt the text with the help of given shift value.
  ord(letter): convert letter into its ASCII Value
    chr(encrypted_value): Converts ASCII Value Into its Character
      return gives the stored value in encrypted_message   '''
  Encrypted_message = ""
  for letter in message:
    if letter.isalpha():
      encrypted_letter = (ord(letter) + shift - 65) % 26 + 65
      Encrypted_message += chr(encrypted_letter)
    else:
      Encrypted_message += letter
  return Encrypted_message

def decrypt(message, shift):
  '''This function is used for the decryption.
  it decrypt the text with the help of given shift value.
  ord(letter): convert letter into its ASCII Value
    chr(encrypted_value): Converts ASCII Value Into its Character
      return gives the stored value in decrypted_message   '''
  decrypted_message = ""
  for letter in message:
    if letter.isalpha():
      decrypted_letter = (ord(letter) - 65 - shift) % 26 + 65
      decrypted_message += chr(decrypted_letter)
    else:
      decrypted_message += letter
  return decrypted_message
  

def process_file(filename, shift):
  '''process_file needs two arguments filename and mode.
  open(filename, "r") reads the text inside the file
  f.readlines() reads the text line by line
  .append add the content in the empty list encrypted_messages'''
  with open(filename, "r") as f:
      messages = f.readlines()
  Encrypted_messages = []
  for message in messages:
    encrypted_message = encrypt(message, shift)
    Encrypted_messages.append(encrypted_message)
  return Encrypted_messages

def write_messages(messages):
  '''This function helps to encrypt or decrypt the file given by the user and give the output in results.txt'''
  with open("results.txt", "w") as f:
    for message in messages:
      f.write(message )

def is_file(filename):
  '''This function check either the file is exists or not'''
  try:
    os.path.isfile(filename)
    return True
  except FileNotFoundError: # display the filenotfounderror to the user
    return False

def message_or_file():
  '''This function is responsible for interacting with user either they use text file or console for the encryption and decryption '''
  choose_mode = input("Would you like to encrypt (e) or decrypt (d): ")
  while choose_mode not in ["e", "d"]:
    print("Invalid Mode")
    choose_mode = input("Would you like to encrypt (e) or decrypt (d): ")
  read_file = input("Would you like to read from a file (f) or the console (c)? ")
  while read_file not in ["f", "c"]:
    print("Invalid Input")
    read_file = input("Would you like to read from a file (f) or the console (c)? ")
  if read_file == "f":
    filename = input("Enter a filename: ")
    while not is_file(filename):
      print("Invalid Filename")
      filename = input("Enter a filename: ")
    shift = int(input("What is the shift number: "))
    return choose_mode, None, filename,shift
  else:
    message = input("What message would you like to {}: ".format(choose_mode))
    message = message.upper()
    shift = int(input("What is the shift number: "))
    return choose_mode, message, None, shift

def main():
  '''This fuction is used to call the other previous function '''
  welcome()
  while True:
    choose_mode, message, filename, shift = message_or_file()
    if choose_mode == "e":
      if filename is None:
        Encrypted_message = encrypt(message, shift)
        print(Encrypted_message)
      else:
        Encrypted_messages = process_file(filename, shift)
        write_messages(Encrypted_messages)
        print("Output written to results.txt")
    else:
      if filename is None:
        Decrypted_message = decrypt(message, shift)
        print(Decrypted_message)
      else:
        Decrypted_messages = process_file(filename, shift)
        write_messages(Decrypted_messages)
        print("Output written to results.txt")
    next_message = input("Would you like to encrypt or decrypt another message? (y/n): ") # ask user to encrypt or decrypt the text file or text again
    if next_message == "n":
      print("Thanks For using this program, goodbye!") 
      break #terminates the loop

if __name__ == "__main__":
  main()
