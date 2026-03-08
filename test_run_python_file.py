from function.run_python_file import run_python_file


def main():

    print('run_python_file("calculator", "main.py")')
    result = run_python_file("calculator", "main.py")
    print(result)
    print()

    print('run_python_file("calculator", "tests.py")')
    result = run_python_file("calculator", "tests.py")
    print(result)
    print()

    print("run_python_file('calculator','../main.py')")
    result = run_python_file('calculator','../main.py')
    print(result)
    print()

    print('run_python_file("calculator", "nonexistent.py") ')
    result = run_python_file("calculator", "nonexistent.py") 
    print(result)
    print()

    print('run_python_file("calculator", "lorem.txt")')
    result = run_python_file(".", "lorem.txt")
    print(result)
    print()



if __name__ == "__main__":
    main()