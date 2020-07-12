#Write your function here
def append_size(lst):
    size = len(lst);
    lst.append(size);
    return lst;

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))