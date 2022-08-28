lst = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
  
    lst.append(ele)
      
print("list1=",lst)


for num in lst:
    if num >= 0:
       print(num, end = " ")
