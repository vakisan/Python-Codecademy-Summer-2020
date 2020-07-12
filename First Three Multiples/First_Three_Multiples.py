# Write your first_three_multiples function here
def first_three_multiples(num):
    print("The first 3 multiples of " + str(num) + "are :")
    print(str(num*1) + str(num*2) + str(num*3));
    return num*3;

# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0
