numbers = [1, 3, 12, 7, 15, 20, 24, 30, 33, 35, 37, 41, 45, 48, 60 ]

def determiner(num_array):
    for num in num_array:
        if(num % 3 == 0 and num % 5 == 0):
            print("fizzBuzz")
        elif(num % 3 == 0):
            print("fizz")
        elif(num % 5 == 0):
            print("buzz")
        else:
            print("not divisible by 3 or 5 or both")

determiner(numbers)

