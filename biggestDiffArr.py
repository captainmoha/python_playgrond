# write a function that takes an array of numbers and returns the biggest
# difference that can be obtained from subtracting two of them


def biggestDiff(arr):
	currentDiff = 0
	bigDiff = 0

	for num1 in arr:
		for num2 in arr:
			currentDiff = num1 - num2
			if currentDiff >= bigDiff:
				bigDiff = currentDiff
	return bigDiff


def biggestDiff2(arr):
	arr.sort()
	return (arr[-1] - arr[0])


def biggestDiff3(arr):
	max_num = max(arr)
	min_num = min(arr)
	return max_num - min_num


def biggestDiff4(arr):
	max_num = arr[0]
	min_num = arr[0]

	for num in arr:
		if num > max_num:
			max_num = num
		elif num < min_num:
			min_num = num
	return max_num - min_num