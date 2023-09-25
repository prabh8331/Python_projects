from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(input_text,shift_amount,which_direction):
    output_text=""
    if which_direction == "decode":
          shift_amount*=-1
    
    for letter in input_text:
            if letter not in alphabet:
                output_text+=letter
            else:
                position=alphabet.index(letter)
                new_position=position+shift_amount
                if new_position > 25 or new_position < 0:
                    # multiple=(new_position+1)//26
                    # new_position=new_position-26*multiple
                    new_position=new_position%26
                output_text+=alphabet[new_position]
    
    if which_direction in ["encode","decode"]:
        print(f"The {which_direction}d text is {output_text}")
    else:
        print("Wrong Input, Try again!")



rerun=True

while rerun:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    ask=input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if ask != "yes":
         rerun=False

