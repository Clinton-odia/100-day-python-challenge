#TODO: Create a letter using starting_letter.txt 
with open(file=r".\Input\Letters\starting_letter.txt") as start_letter:
    letter = start_letter.read()
print(letter)
#for each name in invited_names.txt
invited_name = open(file=r"Input\Names\invited_names.txt" )
names = invited_name.readlines()

print(names)
for name in names:
    new_name = name.rstrip()
    invite = letter.replace("[name]", f"{new_name}")
    with open(file=fr"Output\ReadyToSend\invitation_for_{new_name}", mode="w") as invitation:
        invitation.write(invite)

    print(invite)
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp