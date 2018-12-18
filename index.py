print("Array To Tree!")

# Function takes in an array and returns a tree

def array_to_tree(array, index=0):

	# If index out of range (exit code for reccursion)
	if index > len(array):
		return None

	# Define and initialize left and right children nodes
	left = (index * 2) + 1

	right = left + 1	

	# Return tree using reccursion
	return {

		value: array[index],

		left: array_to_tree(array, left),

		right: array_to_tree(array, right)
	}

		