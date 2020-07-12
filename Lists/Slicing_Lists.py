suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4];
length = len(suitcase);
even = 0;
if length%2 == 0:
  even = 2;
middle_index = int(length/2)
middle = suitcase[middle_index:even + middle_index]
print(beginning);
print(middle);
