from jovian.pythondsa import evaluate_test_case

def binarySearch(arr, key):
	s, e = 0, len(arr) - 1
	while(s <= e):
		mid = s + (e-s)//2
		if (arr[mid] == key): return mid
		elif (key < arr[mid]): 	e = mid - 1
		elif (key > arr[mid]): s = mid+1
		else: raise Exception
	return -1
		
#Even length
test1 = {
	"input": {
		"arr": [2,3,6,31,56,577],
	    "key": 56
    },
	"output": 4
}

#Odd length
test2 = {
	"input": {
		"arr": [2,10,58,231,321,556,5377],
	    "key": 2
    },
	"output": 0
}

#Item not presenst
test3 = {
	"input": {
		"arr": [2,10,58,231,321,556,5377],
	    "key": 40
    },
	"output": -1
}

tests = [variable for variable in ["test1", "test2", "test3"]]

evaluate_test_case(binarySearch, test2)