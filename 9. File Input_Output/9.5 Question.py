# # wap to find in which line of the file does the word "learning" occur first. Print -1 if word not found.

# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1


# with open ("practice.txt", "r") as f:
#     while data :
#         data = f.readline()
#         if(word in data):
#             print(line_no):
#             line_no += 1
#         return -1


def create_practice_file():
    # Define the content to be written to the file
    content = """This is a practice file.
    It contains some text for testing purposes.
    We will search for the word 'learning' in this file."""

    # Open the file in write mode
    with open("practice.txt", "w") as file:
        # Write the content to the file
        file.write(content)

# Call the function to create the file
create_practice_file()

print("File 'practice.txt' has been created successfully.")



def find_word_in_line():
    # Define the word to search for
    word = "learning"
    # Initialize a variable to track if data exists in the file
    data_exists = True
    # Initialize line number
    line_no = 1

    # Open the file in read mode
    with open("practice.txt", "r") as file:
        # Loop through each line in the file
        while data_exists:
            # Read a line from the file
            line = file.readline()
            # Check if line is not empty
            if line:
                # Check if the word exists in the line
                if word in line:
                    # Print the line number where the word is found
                    print("The word '{}' is found in line {}".format(word, line_no))
                    # Return the line number where the word is found
                    return line_no
                # Increment line number
                line_no += 1
            else:
                # If end of file is reached and word is not found, return -1
                return -1

# Call the function to find the word in the file
result = find_word_in_line()

# Check if the word was not found
if result == -1:
    print("The word '{}' was not found in the file.".format("learning"))
