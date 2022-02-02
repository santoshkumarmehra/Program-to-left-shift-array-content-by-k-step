def lshift(arr,lshift):
	lshift=int(input("enter the l_step value = "))
	for count in range(lshift):
		x=arr[0]
		for i in range(1,len(arr)):
			arr[i-1]=arr[i]
		arr[-1]=x
	print("after shifting = ",arr)

arr=[]
sizeofarr=int(input("enter the size of array = "))
for i in range(sizeofarr):
	val=int(input("enter the value of array = "))
	arr.append(val)
print("old arr = ",arr)

lshift(arr,lshift)


