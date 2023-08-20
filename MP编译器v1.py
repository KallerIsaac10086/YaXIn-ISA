# Define a dictionary that maps Micro-Py keywords to YaXin-ISA instructions
keywords = {
    "if": "pureE",
    "else": "PC_jump",
    "for": "PC_jump",
    "while": "pureE",
    "print": "load Cache-Screen0"
}

# Define a function that reads a txt file and returns a list of lines
def read_file(filename):
    lines = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip() # Remove whitespace
            if line: # Ignore empty lines
                lines.append(line)
    return lines

# Define a function that parses a line of Micro-Py code and returns a list of tokens
def parse_line(line):
    tokens = []
    # Split the line by spaces and parentheses
    for token in line.split():
        if "(" in token:
            tokens.append(token[:token.index("(")])
            tokens.append("(")
            tokens.append(token[token.index("(")+1:])
        elif ")" in token:
            tokens.append(token[:token.index(")")])
            tokens.append(")")
        else:
            tokens.append(token)
    return tokens

# Define a function that converts a list of tokens to a list of assembly instructions
def convert_tokens(tokens):
    instructions = []
    # Check the first token to determine the type of statement
    if tokens[0] == "if":
        # If statement: pureE La XB Xp; PC_jump Xp; PC_jump Xj; ...
        instructions.append(keywords["if"] + " La XB Xp")
        instructions.append(keywords["else"] + " Xp")
        instructions.append(keywords["else"] + " Xj")
        # Convert the rest of the tokens recursively
        instructions.extend(convert_tokens(tokens[2:]))
    elif tokens[0] == "else":
        # Else statement: load Cache-Screen0(...); ...
        instructions.append(keywords["print"] + "(" + tokens[2] + ")")
        # Convert the rest of the tokens recursively
        instructions.extend(convert_tokens(tokens[4:]))
    elif tokens[0] == "for":
        # For statement: PC_jump Xj; load Cache-Screen0(...); ...
        instructions.append(keywords["for"] + " Xj")
        instructions.append(keywords["print"] + "(" + tokens[4] + ")")
        # Convert the rest of the tokens recursively
        instructions.extend(convert_tokens(tokens[6:]))
    elif tokens[0] == "while":
        # While statement: pureE La XB Xp; PC_jump Xp; PC_jump Xj; ...
        instructions.append(keywords["while"] + " La XB Xp")
        instructions.append(keywords["else"] + " Xp")
        instructions.append(keywords["else"] + " Xj")
        # Convert the rest of the tokens recursively
        instructions.extend(convert_tokens(tokens[2:]))
    elif tokens[0] == "print":
        # Print statement: load Cache-Screen0(...)
        instructions.append(keywords["print"] + "(" + tokens[2] + ")")
    else:
        # Other statements: assume they are already in assembly format
        instructions.append(" ".join(tokens))
    return instructions

# Define a function that compiles a txt file of Micro-Py code to a txt file of YaXin-ISA assembly code
def compile_file(source, target):
    # Read the source file and get the lines of code
    lines = read_file(source)
    # Open the target file for writing
    with open(target, "w") as f:
        # Loop through each line of code
        for line in lines:
            # Parse the line into tokens
            tokens = parse_line(line)
            # Convert the tokens into assembly instructions
            instructions = convert_tokens(tokens)
            # Write each instruction to the target file on a new line
            for instruction in instructions:
                f.write(instruction + "\n")

# Example usage: compile_file("source.txt", "target.txt")
