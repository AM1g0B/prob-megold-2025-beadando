def get_user_input():
    
    while True:
        num1 = input("Kérem az első számot: ")
        try:
            int(num1)
            break
        except ValueError:
            print("Kérlek egész számot adj meg.")
            
    while True:
        num2 = input("Kérem a második számot: ")
        try:
            int(num2)
            break
        except ValueError:
            print("Kérlek egész számot adj meg.")
            
    return num1, num2

def string_addition(num1: str, num2: str) -> str:
    return str(int(num1) + int(num2))

def string_subtraction(num1: str, num2: str) -> str:
    return str(int(num1) - int(num2))

def string_comparison(num1: str, num2: str) -> int:
    if int(num1) < int(num2):
        return 1
    elif int(num1) > int(num2):
        return -1
    else:
        return 0

def string_multiplication(num1: str, num2: str) -> str:
    return str(int(num1) * int(num2))

def main():
    while True:
        print("\nProblémamegoldások és algoritmusok projektfeladat")
        print("1. Összeadás")
        print("2. Kivonás")
        print("3. Összehasonlítás")
        print("4. Szorzás")
        print("5. Kilépés")
        
        choice = input("Kérem válasszon:")
        
        if choice == "1":
            num1, num2 = get_user_input()
            result = string_addition(num1, num2)
            print("Eredmény:", result)
        elif choice == "2":
            num1, num2 = get_user_input()
            result = string_subtraction(num1, num2)
            print("Eredmény:", result)
        elif choice == "3":
            num1, num2 = get_user_input()
            result = string_comparison(num1, num2)
            if result == 1:
                print("1")
            elif result == -1:
                print("-1")
            else:
                print("0")
        elif choice == "4":
            num1, num2 = get_user_input()
            result = string_multiplication(num1, num2)
            print("Eredmény:", result)
        elif choice == "5":
            print("Viszlát!")
            break
        else:
            print("Érvénytelen menüpont.")

if __name__ == "__main__":
    main()
