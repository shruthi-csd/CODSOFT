import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Prompt the user to specify the length of the password
    length = int(input("Enter the  length of the password: "))
    password = generate_password(length)
    print("Generated password:", password)
main()


/*OUTPUT:
Enter the length of the password: 5
Generated password: Z=p54 */



