n =int( input("Enter a integer: "))
sum=0
print("Calculating sum from 1 to" ,n,"...")
for num in range(1, n + 1):
    sum += num
print(f"The total sum of numbers from 1 to {n} is: {sum}")