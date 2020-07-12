#Write your function here
def middle_element(lst):
  length = len(lst);
  start_index = (length // 2);
  print(start_index)
  if length%2 == 0:
    start_index -= 1; 
    average = (lst[start_index] + lst[start_index + 1])/2;
    return average;
  else:
    return lst[start_index];
    
#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
print(middle_element([5, 2, -4, 4, 5]))