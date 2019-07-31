
task = """In python, you have a list of values n elements long called value_list. 
Create a second list that is the reverse of the first, starting at the last element, 
and counting  down to the first."""

def reverseList(list1):
	newlist = []
	n=0
	while n<len(list1):
		newlist.append(list1[len(list1)-1])
		list1.pop(len(list1)-1)
	return newlist

def main():
	print("Hello reverse py")

	value_list = []
	n = 12
	for a in range(n):
		value_list.append(a)

	x = reverseList(value_list)
	print(x)


if __name__=="__main__":
	main()