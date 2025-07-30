# list_elements = [1, 2, 3, 4, 5, 6]

# index = 4
# value = 25



# list_elements[2:2] = [10, 20, 30]
# print(list_elements)

# is_valid = False



# for i in range(1, 100):
#     if i% 2 ==0:
#         is_valid = True
#         print("even", is_valid)
#     else:
#         is_valid = False
#         print("odd", is_valid)
#     if i >= 70:
#         print(i)
#     if i==80:
#         print(i)
#     if i * 2 == 20:
#         print(i)


# for i in range(1, 10):
#     if 5<i:
#         print(i)
        
        
        


# list_num = [1, 2, 3, 4, 5, 6]

sum = 0


# for i in range(1, 10):
#     sum += i
# print(sum)
#     # if i%2 == 0:
#     #     print(i)
    
    
# for i in range (1, 10):
#     if i % 2 !=0:
#         print(i)
        


# number1 = int(input("Entar Number: "))


# if number1 % 2 == 0:
#     print("Even", number1)

# else:
#     print("Odd", number1)
    
    
    

# for i in range(1, 50):
#     if i % 3 ==0:
#         print(i)
    


decimal_number = int(input("Enter a number: "))

number_binary = bin(decimal_number)
number_oct = oct(decimal_number)

print(number_oct)

print(number_binary)
        
        
        
    
user_info = input("Enter Your Name: ")

if user_info.startswith("Md"):
    print("This name starts whith 'MD'")
else:
    print("This Name doesn,t start with 'Md'")
    
    
    
    
    





def identify_number(user_number):
    if user_number.stratswith("0b"):
        return "Binary"
    elif user_number.startswith("0o"):
        return