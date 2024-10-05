import os  # Import the OS module to interact with the operating system

# Get folder path and keyword from the user
folder_to_search = input("Enter the path to search in: ")  # Prompt user input the folder path
keyword = input("Enter the keyword to search for: ")  # Prompt user to input the keyword

# Ensure the folder exists
if not os.path.exists(folder_to_search):
    print(f"Error: The folder '{folder_to_search}' does not exist.")  # Display an error if the folder doesn't exist
else:
    print(f"Searching for '{keyword}' in folder: {folder_to_search}")  # Debug print to confirm folder exists
    found_anything = False  # Track if any keyword was found

    # Search through all .txt files in the folder
    for filename in os.listdir(folder_to_search):  # List all files in the folder
        if filename.endswith('.txt'):  # Only process files that end with '.txt'
            file_path = os.path.join(folder_to_search, filename)  # Build the full file path
            print(f"Checking file: {filename}")  # Debug print to confirm file is being processed

            # Open and read the contents of the file
            with open(file_path, 'r') as file:
                lines = file.readlines()  # Read all lines in the file

                # Loop through each line to check for the keyword
                for line_num, line in enumerate(lines, start=1):  # Loop through lines with line numbers starting at 1
                    if keyword in line:  # Check if the keyword is in the current line
                        print(f"Found '{keyword}' in {filename} on line {line_num}: {line.strip()}")  # Print result
                        found_anything = True  # Update if keyword is found

    if not found_anything:
        print(f"Keyword '{keyword}' not found in any .txt files.")  # If no matches are found
