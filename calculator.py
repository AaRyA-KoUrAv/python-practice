#  ----------- CALCULATOR ------------ # 
while True :
    num_1 = int(input("Enter a number : "))
    operators = input("Choose Operator ('+','-','*','//','/','%','**') Or 'exit' to quit ")
    operators = operators.strip().lower()
    if operators == 'exit':
        break
    num_2 = int(input("Enter a number : "))
    if operators == '+':
        result = num_1 + num_2
    elif operators == '-':
        result = num_1 - num_2
    elif operators == '*':
        result = num_1 * num_2
    elif operators == '**':
        result = num_1 ** num_2
    elif operators == '//':
        if num_2 == 0:
            print("Error : Denominator can't be zero")
            continue 
        result = num_1 // num_2
    elif operators == '/':
        if num_2 == 0:
            print("Error : Denominator can't be zero")
            continue 
        result = num_1 / num_2
    elif operators == '%':
        if num_2 == 0:
            print("Error : Denominator can't be zero")
            continue 
        result = num_1 % num_2
    else:
        print('Invalid')
        continue
    print(f"{num_1} {operators} {num_2} = {result}")
