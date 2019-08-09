import numpy

'''Given a numpy array of runners' marathon completion times, 
generate another array with the corresponding place that each runner took in the final results'''


def getRacePlace(times):
    a = numpy.argsort(times)
    return a+1



def main():
    print("Hello")

    times = numpy.array([5.14, 4.22, 6.89, 3.08, 4.71])
    print(times)

    places = getRacePlace(times)
    print(places)

if __name__=="__main__":
    main()