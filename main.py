import time
from itertools import product
import string

class GeneratePassword:
    def generate():
        print("Password should have at lesat 6 characters and max 12 characters")
        password = input("Write Your password:").lower()

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
                print(f"Tried {tries} passwords")
                return
        else:
            print(f"couldnt find password... tried {tries} passwords")

    def created_passwords(password):
        characters = string.ascii_lowercase
        tries = 0
        total = sum(26 ** i for i in range(6,8))
        for i in range(6, 8):
            
            for combination in product(characters, repeat=i):
                created_password = "".join(combination)
                tries += 1
                if tries % 100_000 == 0:
                    procent = (tries / total) * 100
                    print(f"\rProgress: {procent:.2f}%", end="", flush=True)
                if created_password == password:
                    print(f"Ditt lösenord är {i}")
                    print(f"Tried {tries} passwords")
                    return



def main():

    password = GeneratePassword.generate()
    start = time.perf_counter()
    print(password)
    password_list = ImportPasswords.lists_passwords()
    PasswordSolver.solver(password, password_list)
    PasswordSolver.created_passwords(password)
    end = time.perf_counter()
    execution_time = end - start
    print(f"Exekveringstid: {execution_time:.4f} sekunder")
    
main()

