n = int(input("Enter the number of terms: "))

a, b = 0, 1

print("Fibonacci Series of the number is :")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

print("\nProgram completed successfully!")