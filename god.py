import random
def godsort(array):
	for i in range(len(array)):
		s = findMin(array,i)
		array[s],array[i] = array[i],array[s]
	return array
		
def findMin(array,i):
	return random.randint(i,len(array)-1)
	
# Assumes array is already sorted
# O(1) sorting algorithm, give me the nobel prize already
def bestsort(array):
	return array

print(godsort([5,6,8,13,2,1,2,5,6,2]))
