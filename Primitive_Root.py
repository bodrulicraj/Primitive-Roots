from math import gcd
def checkPrime(number): 
    counter = 0
    if (number <= 1): 
        return False    
    if (number <= 2): 
        return True
    for i in range(2, number):
        if (number % i) == 0:
            counter = counter + 1
    if counter == 0:
        return True
    else:
        counter = 0
        return False
		
def primitiveRoots(primeNum):
    possible_set = {num for num in range(1, primeNum) if gcd(num, primeNum) }
    root_list = [base for base in range(1, primeNum) if possible_set == {pow(base, power, primeNum) for power in range(1, primeNum)}]
    return root_list
	
if __name__ == '__main__':
    print('Enter a prime number: ')
    number = int(input())
    error = str(number) + ' is not a Prime Number!'
    if (checkPrime(number)):
        print('Primitive Roots of ' + str(number) + " are: ")
        roots = primitiveRoots(number)
        print(roots)
        print("Number of Roots: " + str(len(roots)))
    else :
        print(error)