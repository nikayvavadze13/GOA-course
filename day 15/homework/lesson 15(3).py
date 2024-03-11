
def starts_with_G(input_string):
    # Check if the string is not empty
    if input_string:
        # Compare the first character with "G" (case-sensitive)
        return input_string[0] == "G"
    else:
        # If the string is empty, return False
        return True

# Example usage:
input_str = input("Enter a string: ")
result = starts_with_G(input_str)
print(result)
  
