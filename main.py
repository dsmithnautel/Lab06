# Derek Smith Nautel

# Encodes the password
def encode(password):
    encoded_password = ''
    list_password = list(password)
    int_password = map(int, list_password)
    list_int_password = list(int_password)
    for num in list_int_password:
        encoded_num = num + 3
        encoded_password += str(encoded_num)
    return encoded_password


# Decodes the password
# def decode(password):
    # decode function here


def main():
    while True:
        # displays menu and gets user input
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")
        option = int(input("Please enter an option: "))
        password = input("Please enter your password to encode: ")
        print("Your Password has been encoded and stored\n")
        # encode, decode, or quit
        if option == 1:
            encode(password)
        elif option == 2:
            decode(password)
        elif option == 3:
            break
        else:
            continue


if __name__ == "__main__":
    main()
