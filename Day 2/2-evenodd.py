# #output:
# #even numbers: 
# odd numbers:
# sum of even numbers:

nums = []
for i in range(1, 6):
    inp = int(input("Enter a number: "))
    nums.append(inp)
even_num = []
odd_num = []

for num in nums:
    if num%2==0:
        even_num.append(num)
    else:
        odd_num.append(num)
oddsum = sum(odd_num)
evensum = sum(even_num)
if len(even_num) < 0:
    print("cant find the average of numbers")
else:
    avg_even = evensum/len(even_num)
    
if len(odd_num) < 0:
    print("cant find the average of numbers")
else:
    avg_odd = oddsum/len(odd_num)


print(f"Even numbers: {even_num}")
print(f"Odd numbers: {odd_num}")
print(f"Sum of even numbers: {sum(even_num)}")
print(f"Sum of odd numbers: {sum(odd_num)}")
print(f"Average of even numbers: {avg_even}")
print(f"Average of odd numbers: {avg_odd}")
print(f"Total odd numbers: {len(odd_num)}")