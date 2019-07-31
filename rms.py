import numpy

task = """Write a function, rms(), that finds the 
root-mean-square (square root of the mean of the squared values) of a numpy array."""


def rms(arr):
	x = ((numpy.sum(numpy.square(arr)))/len(arr))**0.5
	print(x)
	return x



def main():
	print("Hi RMS")

	# a = numpy.random.random(5)
	a = numpy.array([1,2,3,4,5,6])

	rms(a)



if __name__ == "__main__":
	main()