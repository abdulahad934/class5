def Even_Odd_cheker(number):
    
    
    
    if number % 2 == 0:
        print(f"Even Number: {number}")
    else:
        print(f"Odd Number: {number}")
    return number
    

number = int(input("Enter Even or Odd Number cheker: "))

result = Even_Odd_cheker(number)

print(result)    