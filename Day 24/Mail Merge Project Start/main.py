#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
from importlib.metadata import Lookup
from tempfile import template


#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

def main():
    name_list = create_list_of_names()
    template = read_template()
    replace_name_and_create_file(name_list, template)

#Global variable
#--empty

#Function
def create_list_of_names():
    name_list = []
    with open("./Input/Names/invited_names.txt", mode='r') as names:
        for line in names: #Loops through number of lines in the file
            name_list.append(line.strip()) #strip(), removes whitespaces and \n
        return name_list

def read_template():
    with open("./Input/Letters/starting_letter.txt") as file:
        return file.read()

def replace_name_and_create_file(name_list, template):
    for name in name_list:
        new_letter = template.replace("[name]", name)
        file_name = "./Output/ReadyToSend/" + name + "_invitation_letter.txt"
        with open(file_name, mode='w') as file:
            file.write(new_letter)

#Call
main()