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
def decode(password):
    # Alessandro Giusti was here
    dict_pw_keys = {'3': '0', '4': '1', '5': '2', '6': '3',
                    '7': '4', '8': '5', '9': '6', '0': '7',
                    '1': '8', '2': '9'}

    password_list = list(password)
    encoded_password = ''

    for i in range(len(password_list)):
        password_list[i] = dict_pw_keys.get(password_list[i])
        encoded_password += ''.join(password_list[i])

    return encoded_password


def main():
    while True:
        # displays menu and gets user input
        print("\nMenu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        option = int(input("Please enter an option: "))

        # encode, decode, or quit
        if option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your Password has been encoded and stored!\n")
        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif option == 3:
            break
        else:
            continue


if __name__ == "__main__":
    main()
