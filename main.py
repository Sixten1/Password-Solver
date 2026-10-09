


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

        with open("10k-most-common.txt", "r", encoding="utf-8") as file:
            content = file.read()

        words = content.splitlines()
        password_list = []

        for i in words:
            password_list.append(i)

        return password_list

    
class PasswordSolver:
    pass



def main():
    password = GeneratePassword.generate()
    print(password)
    ImportPasswords.lists_passwords()

main()