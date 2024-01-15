import random
import string

def generate_code(length=8):
    characters = string.ascii_uppercase + string.digits  # alphabets and numbers
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

# Example: Generate a code with a length of 8 characters
# generated_code = generate_code(8)
# print("Generated Code:", generated_code)
