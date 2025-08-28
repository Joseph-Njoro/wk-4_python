def main():

    input_filename = input("Enter the name of the file to read: ")
    output_filename = input("Enter the name for the new modified file: ")
    
    try:
        with open(input_filename, 'r') as file:
            content = file.read()
        
        print(f"Successfully read '{input_filename}'")

        modified_content = content.upper()

        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Successfully created '{output_filename}'")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")    
    except PermissionError:
        print(f"Error: You don't have permission to read '{input_filename}'.")
    except IsADirectoryError:
        print(f"Error: '{input_filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
