#Password generator source code---
import string
import random

print(f"""-----:PASSWORD GENERATOR:-----
""")
try:
    while True:
        print("""
        Function Codes--->
        1 -> Generate Random Password
        2 -> Review other passwords (requires master-password)
        3 -> Search password by password-name (requires master-password)
        x -> Exit
        """)
        function_code = input("Function Code: ")
        if function_code == "1":

            char_length = int(input("Enter desired Password Length: "))
            def create_random_string(char_length, characters):
                random_string = ""
                for i in range(char_length):
                    random_string = random_string + random.choice(characters)
                return random_string
            numpunc = input("""
            Would you like include Numbers or Punctuations
            num -> include numbers
            punc -> inclde punctuations
            both -> include both
            >>>""")
            pass_name = input("Give your password a name: ").title()
            if numpunc.lower() == "num":
                characters = string.ascii_letters + string.ascii_uppercase + string.digits
            elif numpunc.lower() == "punc":
                characters = string.ascii_letters + string.ascii_uppercase + string.punctuation
            else:
                characters = string.ascii_letters + string.ascii_uppercase + string.digits + string.punctuation

            string = create_random_string(char_length, characters)

            print(f"Your randomly generated password: {string}")
            with open("PasswordGen-Database.txt", "a") as f:
                with open("PasswordGen-Database.txt", "r") as r:
                    lines = r.readlines()
                    lenlines = len(lines)
                    saved_line = lenlines + 1
                f.write(f"\n{saved_line} {pass_name} {string}")
                print(f"Password named {pass_name} was succesfully saved in 'PasswordGen-Database.txt' in line {saved_line}")
            pass
        elif function_code == "2":
            master_password = "MasterKeyPy"
            attempt = 0
            while attempt < 5:
                password_attempt = input("Enter Master-Password: ")
                attempt += 1
                if password_attempt == master_password:
                    with open("PasswordGen-Database.txt", "r") as p:
                        data = p.read()
                        print(data)
                    break
            else:
                print(f"Try again (you have {5 - attempt} tries left)")
            pass
        elif function_code == "3":
            master_password = "MasterKeyPy"
            attempt = 0
            while attempt < 5:
                password_attempt = input("Enter Master-Password: ")
                attempt += 1
                if password_attempt == master_password:
                    search_word = input("Search by name of the password: ")
                    with open("PasswordGen-Database.txt", "r") as f:
                        lines = f.readlines()
                        for line in lines:
                            words = line.split()
                            if search_word.title() in words:
                                print(f"""
                                RESULT :-
                                Search results based on {search_word.title()}
                                {line.split()[1]} -> {line.split()[2]}""")
                    break
                else:
                    print(f"Try again (you have {5 - attempt} tries left)")
                pass
        elif function_code == "x":
            print("PROGRAM: 'Password Generator.py' WAS SUCCESSFULLY CLOSED...")
            break
        else:
            print("Please enter a function code...")
            pass
except ValueError:
    print("Enter a valid function code")