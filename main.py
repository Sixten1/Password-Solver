import time
from itertools import product
import string

class GeneratePassword:
    def generate():
        print("Password should have at least 2 characters and max 6 characters")
        password = input("Write Your password:").lower()

        while len(password) < 2 or len(password) > 6:
            print("Password should have at least 6 characters and max 12 characters")
            password = input("Write Your password:").lower()

        return password


        
class ImportPasswords:
    def lists_passwords():
        
        with open("rockyou.txt", "r", encoding="utf-8") as file:
            password_list = file.read().splitlines()

        return password_list

    
class PasswordSolver:
    def solver(password, password_list):
        tries = 0
        for i in password_list:
            tries += 1
            if i == password:
                print(f"Your passcode is {i}")
                print(f"Tried {tries} passwords")
                return True
        else:
            print(f"couldnt find password... tried {tries} passwords")
            return False

    def created_passwords(password):
        characters = string.ascii_lowercase + string.digits
        tries = 0
        total = sum(len(characters) ** i for i in range(2, 7))
        next_update = 1_000_000
        for i in range(2, 7):
            
            for combination in product(characters, repeat=i):
                created_password = "".join(combination)
                tries += 1
                if tries % next_update == 0:
                    procent = (tries / total) * 100
                    print(f"\rProgress: {procent:.2f}%", end="", flush=True)
                if created_password == password:
                    print(f"\nDitt lösenord är {created_password}")
                    print(f"Tried {tries} passwords")
                    return



def main():

    password = GeneratePassword.generate()
    start = time.perf_counter()
    print(password)
    password_list = ImportPasswords.lists_passwords()
    find_password = PasswordSolver.solver(password, password_list)
    if find_password == False:
        PasswordSolver.created_passwords(password)
    end = time.perf_counter()
    execution_time = end - start
    print(f"Exekveringstid: {execution_time:.4f} sekunder")
    
main()

