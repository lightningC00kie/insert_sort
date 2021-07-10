i=0
A = []
num=0
while num != 'x':
    num = input('input number\n')
    if num == 'x':
        break
    A.append(num)
    i=i+1
for j in range(1, len(A)):
    key = A[j]
    i=j-1
    while i>-1 and A[i] < key:
        A[i+1] = A[i]
        i=i-1
    A[i+1] = key

print(A)