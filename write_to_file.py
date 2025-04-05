from command_parser import output

filename = "data.txt"
text = output

with open(filename, 'a') as file:
    file.write(text + "\n")
