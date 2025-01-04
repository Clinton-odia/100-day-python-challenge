
with open(file=r".\Input\Letters\starting_letter.txt") as start_letter:
    letter = start_letter.read()
print(letter)

invited_name = open(file=r"Input\Names\invited_names.txt" )
names = invited_name.readlines()

print(names)
for name in names:
    new_name = name.rstrip()
    invite = letter.replace("[name]", f"{new_name}")
    with open(file=fr"Output\ReadyToSend\invitation_for_{new_name}", mode="w") as invitation:
        invitation.write(invite)

