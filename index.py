print("Array To Tree!")

# Function takes in an array and returns a tree

def array_to_tree(array, index=0):

	# If index out of range (exit code for reccursion)
	if index > len(array):
		return None

		