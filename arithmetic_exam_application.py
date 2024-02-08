import random

def generate_task(difficulty_level):
    if difficulty_level == 1:
        num1 = random.randint(2, 9)
        num2 = random.randint(2, 9)
        operations = ["+", "-", "*"]
        operation = random.choice(operations)
        expression = f"{num1} {operation} {num2}"
        return expression, str(eval(expression))
    elif difficulty_level == 2:
        num = random.randint(11, 29)
        expression = str(num)
        return expression, str(num ** 2)

def save_result(name, level, correct_answers):
    with open("results.txt", "a") as file:
        file.write(f"{name}: {correct_answers}/5 in level {level} (")
        if level == 1:
            file.write("simple operations with numbers 2-9)\n")
        elif level == 2:
            file.write("integral squares of 11-29)\n")

def main():
    while True:
        difficulty_level = input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n> ")
        if difficulty_level in ['1', '2']:
            difficulty_level = int(difficulty_level)
            break
        else:
            print("Incorrect format.")

    correct_answers = 0
    for _ in range(5):
        expression, result = generate_task(difficulty_level)
        print(expression)
        while True:
            answer = input().strip()

            try:
                if float(answer) == float(result):
                    print("Right!")
                    correct_answers += 1
                    break
                else:
                    print("Wrong!")
                    break
            except ValueError:
                print("Incorrect format.")
                continue
    
    print(f"Your mark is {correct_answers}/5. Would you like to save the result? Enter yes or no.")
    save_choice = input("> ").lower()
    if save_choice in ['yes', 'y']:
        name = input("What is your name?\n> ")
        save_result(name, difficulty_level, correct_answers)
        print("The results are saved in \"results.txt\".")
    else:
        print("Exiting the program.")

if __name__ == "__main__":
    main()
