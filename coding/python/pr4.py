PROBLEM STATEMENT:
Python program in number right angled triangle
Enter number 5

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1


SOLUTION:
rows = int(input("enter number of rows "))
for i in range(0, rows + 1):
	for j in range(rows - i, 0, -1):
		print(j, end=' ')
print()
