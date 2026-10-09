


class GeneratePassword:
    def generate():
        print("Password should have at lesat 6 characters and max 12 characters")
        password = input("Write Your password:")

        if len(password) < 6 or len(password) > 12:
            print("Password should have at lesat 6 characters and max 12 characters")
            password = input("Write Your password:") 

        return password


        
class ImportPasswords:
    def lists_passwords():

        with open("rockyou.txt", "r", encoding="utf-8") as file:
            content = file.read()

        words = content.splitlines()
        password_list = []

        for i in words:
            password_list.append(i)

        return password_list

    
class PasswordSolver:
    def solver(password, password_list):
        tries = 0
        for i in password_list:
            tries += 1
            if i == password:
                print(f"Ditt lösenord är {i}")
                print(f"Tried {tries} pass")

        else:
            print(f"couldnt find password... tried {tries} passwords")



def main():
    password = GeneratePassword.generate()
    print(password)
    password_list = ImportPasswords.lists_passwords()
    PasswordSolver.solver(password, password_list)


main()