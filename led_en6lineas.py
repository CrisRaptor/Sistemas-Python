numbers = (("###", "# #", "# #", "# #", "###"),("  #", "  #", "  #", "  #", "  #"),("###", "  #", "###", "#  ", "###"),("###", "  #", "###", "  #", "###"),("# #", "# #", "###", "  #", "  #"),("###", "#  ", "###", "  #", "###"),("###", "#  ", "###", "# #", "###"),("###", "  #", "  #", "  #", "  #"),("###", "# #", "###", "# #", "###"),("###", "# #", "###", "  #", "###"))
def print_number(number):
    print("\n".join(" ".join(numbers[int(d)][i] for d in str(number)) for i in range(5)))
while not (number_input := input("Enter a number: ")).isdigit():
    print("Invalid input. Please enter a number.")
print_number(int(number_input))

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

### Short print number function multiline
# def print_number(number):
#     print("\n".join(
#         " ".join(
#             numbers[int(d)][i] 
#             for d in str(number)
#             ) for i in range(5)))
# while not (number_input := 
#            input("Enter a number: ")
#            ).isdigit():
#     print("Invalid input. Please enter a number.")

# print_number(int(number_input))

### Short print number function
#    digits = [int(d) for d in str(number)]
#    for i in range(5):
#        print(" ".join(numbers[d][i] for d in digits))

### Original code
# def print_number(number):
#     digits = [int(d) for d in str(number)]
#     for i in range(5):
#         for d in digits:
#             print(numbers[d][i], end=" ")
#         print()
    
# number_input = input("Enter a number: ")
# while not number_input.isdigit():
#     print("Invalid input. Please enter a number.")
#     number_input = input("Enter a number: ")
# print_number(int(number_input))