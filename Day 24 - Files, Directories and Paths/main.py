#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open(r"Day 24 - Files, Directories and Paths\Input\Letters\starting_letter.txt") as file1:
    letter = file1.read()

with open(r"Day 24 - Files, Directories and Paths\Input\Names\invited_names.txt") as file2:
    names = file2.readlines()

for name in names:
    name = name.strip()
    modified_letter = letter.replace("[name]", name)
    with open(f"Day 24 - Files, Directories and Paths\Output\ReadyToSend\letter_{name}.txt", "w") as file3:
        for line in modified_letter:
            file3.write(line)




    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp