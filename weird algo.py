def weird_algorithm(n):  #function we named as weird_Algo
  sequence = [n]  # Initialize the sequence with the initial value n empty list

  while n != 1:
    if n % 2 == 0:  # If n is even
      n //= 2
    else:  # If n is odd
      n = n * 3 + 1
    sequence.append(n)

  return sequence


# Take input from the user
n = int(input("Enter a positive integer: "))

# Call the function and print the sequence
sequence = weird_algorithm(n)
print("Sequence:", sequence)
