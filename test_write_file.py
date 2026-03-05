from function.write_file_content import write_file


def main():

    print('write_file(".", "lorem.txt", "wait, this isnt lorem ipsum")')
    result = write_file(".", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    print()

    print('write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    print()

    print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed")')
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

    

if __name__ == "__main__":
    main()