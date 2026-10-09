class GeneratePassword:
    def generate():
        print("Password should have at lesat 6 characters and max 12 characters")
        password = input("Write Your password:")

        if len(password) < 6 or len(password) > 12:
            print("Password should have at lesat 6 characters and max 12 characters")
            password = input("Write Your password:") 

        return password


        
class ImportPasswords:
    pass

class PasswordSolver:
    pass



def main():
    password = GeneratePassword.generate()
    print(password)

main()