# Write your function here
def divisible_by_ten(nums):
    list_divisible_by_ten = [num for num in nums if num % 10 == 0]
    return len(list_divisible_by_ten)


# Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
