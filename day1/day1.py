# DAY1
# input_file = open('input.txt','r')
# print(input_file.read())

with open('input.txt','r') as input_file:
  #calculate sum of frequency changes in input.txt
  freq_changes=[]
  for line in input_file.readlines():
    freq_changes.append(int(line))
  #answer: sum of frequency changes
  print('length of frequency changes = ', len(freq_changes))
  print('sum of frequency changes = ', sum(freq_changes))
  
  
  #determine first frequency that repeats
  i = 0
  freq = 0
  unique_freq = {freq}
  unique_flag = 1
  length_freq_changes = len(freq_changes)
  while unique_flag == 1:
    j = i % length_freq_changes
    i = i + 1
    freq = freq + freq_changes[j]
    if freq in unique_freq:
      unique_flag = 0
      #answer: first frequency to repeat
      print('total frequency changes until repeat = ', i)
      print('first frequency to repeat = ', freq)
    else:
      unique_freq.add(freq)
  
  #the following code didn't work because it only cycled through the frequency changes once (assuming the repeat happened in the first cycle)
  #cu_freq = []
  #length = len(freq_changes)
  #cu_freq=[sum(freq_changes[0:x+1]) for x in range(0, length)]
  #seen={}
  #dupes=[]
  #for x in cu_freq:
  #  if x not in seen:
  #    seen[x] = 1
  #  else:
  #    if seen[x] == 1:
  #      dupes.append(x)
  #    seen[x] += 1
  #print(seen)
  #print(dupes)

    
