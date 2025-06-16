def calculator():
    print("Simple Calculator")
    print("Enter 'exit' to quit")
    
    while True:
        expression = input("Enter an operation (e.g., 5 + 3): ")
        
        if expression.lower() == 'exit':
            print("Goodbye!")
            break
        
        try:
            result = eval(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

calculator()

