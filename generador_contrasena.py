import random

secure_number_generator = random.SystemRandom()
upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
special_characters = ['*','+','#','@','_','-','&','%','$','!','/','?']
characters = upper_case + lower_case + numbers + special_characters

def generate_password():
    password = ""
    for i in range(15):
        password += secure_number_generator.choice(characters)
    return password

def main():
    print("password generator")
    print("genereting password...")
    print("This is your password: " + generate_password())
    print("finished")
    

if __name__ == "__main__":
    main()