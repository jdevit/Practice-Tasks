import numpy

## Given two numpy arrays of the same length, one containing children's ages, and one containing their heights,
# sort their heights so that they are ordered by age.

def sortHeightByAge(age,height):
    agep = age.argsort()
    print("Age sorted:",age[agep])
    print("Height sorted (age):",height[agep])
    pass

def main():
    print("Helloo")

    age = numpy.array([11,10,12,13,8,9])
    height = numpy.array([153,151,149,133,160,170])
    print("Age:", age)
    print("Height:", height)

    sortHeightByAge(age,height)





if __name__=="__main__":
    main()