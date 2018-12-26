# DAY2
num2 = 0
num3 = 0
#open file and strip out box IDs into a list
with open('input.txt','r') as input_file:
  box_IDs=[]
  for line in input_file.readlines():
    box_IDs.append(line.strip())
  
  #iterate over box IDs and count letters in each, count those with 2 and 3 repeats
  for i, box in enumerate(box_IDs):
    char_count={char:box.count(char) for char in box}
    if 2 in list(char_count.values()):
      num2 = num2 + 1
    if 3 in list(char_count.values()):
      num3 = num3 + 1
  print('Number of boxes with 2 repeated letters = ', num2)
  print('Number of boxes with 3 repeated letters = ', num3)
  print('Checksum = ', num2*num3)