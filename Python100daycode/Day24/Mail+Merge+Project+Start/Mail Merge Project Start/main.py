#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open("Python100daycode/Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt",mode="r") as file:
    names=file.readlines()
    

print(names)
    


with open("Python100daycode/Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt",mode="r") as file:
    starting_letter=file.read()

print(starting_letter)

print(starting_letter.replace("[name]",names[0].strip()))

for name in names:
    with open(f"Python100daycode/Day24/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/{name.strip()}.txt",mode="w") as file:
        file.write(starting_letter.replace("[name]",name.strip()))