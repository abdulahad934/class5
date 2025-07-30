def Even_Odd_cheker(number):
    
    
    
    if number % 2 == 0:
        print(f"Even Number: {number}")
    else:
        print(f"Odd Number: {number}")
    return number
    

number = int(input("Enter Even or Odd Number cheker: "))

result = Even_Odd_cheker(number)

print(result)



def Even_Odd_Cheker(number):
    Even = []
    Odd = []
    for i in number:
        if i % 2 ==0:
            Even +=  [i]
            
            print(f"Number is Even: {Even}")
        else:
            Odd += [i]
            print(f"number is Odd: {Odd}")
        
    return number

number = [1, 2, 3, 4, 5, 6, 6, 7]

result = Even_Odd_Cheker(number)
print(number)
