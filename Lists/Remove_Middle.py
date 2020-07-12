#Write your function here
def remove_middle(lst,start,end):
  left_list = lst[:start];
  right_list = lst[end+1:];
  array_without_middle = left_list+right_list;
  return array_without_middle;

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))