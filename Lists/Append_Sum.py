#Write your function here
def append_sum(lst):
    sum = lst[-1] + lst[-2];
    lst.append(sum);
    sum = lst[-1] + lst[-2];
    lst.append(sum);
    sum = lst[-1] + lst[-2];
    lst.append(sum);
    return lst
    
#Uncomment the line below when your function is done

print(append_sum([1, 1, 2]))