# def sum(num):
#     if num==1:
#      return 1
#     return num + sum(num-1)
# c=3
# s=sum(c)
# print("The sum of first",c,"numbers is: ",str(s))

# with open('abc.txt', 'w') as f:
#      print(f.write('hello i am coder'))
# with open("abc.txt",'r') as f:
#     print(f.read())

# f=open('abc.txt','w')
# f.write('Hello I am working on python')
# f.close()

# with open('abc.txt','r') as f:
#     t=f.read()
# if 'boss' in t:
#     print("Yes")
# else:
#     print("No")

# def search_element(arr,n,x):
#     for i in range(0, n):
#         if arr[i] == x:
#             return i
#     return -1

# arr = [2,45,67,89,12,34]
# n = len(arr)
# x = 12
# result = search_element(arr,n,x)
# if result != -1:
#     print(f"Element is present at index",{result})
# else:
#     print("Element is not present in array")

#for i in range(2,21):
#   with open(f'tables/table_of_{i}.txt','w') as f:
#         for j in range(1,11):
#             f.write(str(i)+'X'+str(j)+'='+str(i*j)+'\n')

# with open('abc.txt','r') as f:
#     cont= f.read()
# cont=cont.replace('code','###')
# with open('abc.txt','w') as f:
#     f.write(cont)

# n = int(input("Enter the number of elements in the array: "))
# arr = []
# for i in range(n):
#     element = input(f"Enter element {i+1}: ")
#     arr.append(element)
# print("Array:", arr)
 
