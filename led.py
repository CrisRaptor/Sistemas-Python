numbers = (("###", "# #", "# #", "# #", "###"),
            ("  #", "  #", "  #", "  #", "  #"),
            ("###", "  #", "###", "#  ", "###"),
            ("###", "  #", "###", "  #", "###"),
            ("# #", "# #", "###", "  #", "  #"),
            ("###", "#  ", "###", "  #", "###"),
            ("###", "#  ", "###", "# #", "###"),
            ("###", "  #", "  #", "  #", "  #"),
            ("###", "# #", "###", "# #", "###"),
            ("###", "# #", "###", "  #", "###"))

def print_number(number):
    digits = [int(caracter) for caracter in str(number)]
    for line in range(5):
        for digit in digits:
            print(numbers[digit][line], end=" ")
        print()

number_input = input("Enter a number: ")
while not number_input.isdigit():
    print("Invalid input. Please enter a number.")
    number_input = input("Enter a number: ")
print_number(int(number_input))