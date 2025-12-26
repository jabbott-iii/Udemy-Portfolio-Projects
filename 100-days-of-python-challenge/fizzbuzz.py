# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

numbers = list(range(1, 101))

for number in numbers:
    if number % 5 == 0 and number % 3 == 0:
        print('fizzbuzz')
    elif number % 5 ==0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number)



