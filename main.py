def encode():
    global original_password
    global encoded_password

    original_password = str(input(("Please enter your password to encode: ")))

    product = []
    for character in original_password:
        if character == "0":
            product.append(0)
        elif character == "1":
            product.append(1)
        elif character == "2":
            product.append(2)
        elif character == "3":
            product.append(3)
        elif character == "4":
            product.append(4)
        elif character == "5":
            product.append(5)
        elif character == "6":
            product.append(6)
        elif character == "7":
            product.append(7)
        elif character == "8":
            product.append(8)
        elif character == "9":
            product.append(9)

    for i in range(len(product)):
        if product[i] == 0:
            product[i] = "3"
        elif product[i] == 1:
            product[i] = "4"
        elif product[i] == 2:
            product[i] = "5"
        elif product[i] == 3:
            product[i] = "6"
        elif product[i] == 4:
            product[i] = "7"
        elif product[i] == 5:
            product[i] = "8"
        elif product[i] == 6:
            product[i] = "9"
        elif product[i] == 7:
            product[i] = "0"
        elif product[i] == 8:
            product[i] = "1"
        elif product[i] == 9:
            product[i] = "2"

    gap = ""
    encoded_password = gap.join(product)

    print("Your password has been encoded and stored!")

def decode():
    decoded_product = []
    for character in encoded_password:
        if character == "0":
            decoded_product.append(0)
        elif character == "1":
            decoded_product.append(1)
        elif character == "2":
            decoded_product.append(2)
        elif character == "3":
            decoded_product.append(3)
        elif character == "4":
            decoded_product.append(4)
        elif character == "5":
            decoded_product.append(5)
        elif character == "6":
            decoded_product.append(6)
        elif character == "7":
            decoded_product.append(7)
        elif character == "8":
            decoded_product.append(8)
        elif character == "9":
            decoded_product.append(9)

        for i in range(len(decoded_product)):
            if decoded_product[i] == 0:
                decoded_product[i] = "7"
            elif decoded_product[i] == 1:
                decoded_product[i] = "8"
            elif decoded_product[i] == 2:
                decoded_product[i] = "9"
            elif decoded_product[i] == 3:
                decoded_product[i] = "0"
            elif decoded_product[i] == 4:
                decoded_product[i] = "1"
            elif decoded_product[i] == 5:
                decoded_product[i] = "2"
            elif decoded_product[i] == 6:
                decoded_product[i] = "3"
            elif decoded_product[i] == 7:
                decoded_product[i] = "4"
            elif decoded_product[i] == 8:
                decoded_product[i] = "5"
            elif decoded_product[i] == 9:
                decoded_product[i] = "6"
    gap = ""
    decoded_password = gap.join(decoded_product)

    print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")

while True:
    print("\n")
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")

    option = int(input("Please enter an option: "))
    if option == 3:
        exit()
    elif option == 1:
        encode()
    elif option == 2:
        decode()

