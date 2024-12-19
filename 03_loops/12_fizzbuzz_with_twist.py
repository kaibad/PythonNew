# Problem: Print numbers from 1 to 50, but: - Print "Fizz" for multiples of 3. - Print "Buzz" for multiples of 5. - Print "FizzBuzz" for multiples of both 3 and 5. - Skip numbers that are divisible by 7.

i = 1
while i < 51:
    # Skip numbers divisible by 7
    if i % 7 == 0:
        i += 1
        continue
    
    # Check for multiples of both 3 and 5 (FizzBuzz)
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Check for multiples of 3
    elif i % 3 == 0:
        print("Fizz")
    # Check for multiples of 5
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    
    i += 1


# Check for numbers divisible by 7 (to skip them):

# Reason: Numbers divisible by 7 should be skipped immediately, so this check is done first.
# Check for "FizzBuzz" (divisible by both 3 and 5):

# Reason: Numbers divisible by both 3 and 5 should print "FizzBuzz", so we handle this case before checking for "Fizz" or "Buzz" individually.
# Check for "Fizz" (divisible by 3):

# Reason: If a number is divisible by 3 but not 5, we print "Fizz". This is checked after "FizzBuzz".
# Check for "Buzz" (divisible by 5):

# Reason: Finally, check for numbers divisible by 5. These will print "Buzz" if they are not also divisible by 3.
