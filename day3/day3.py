#open file and strip out box IDs into a list
with open('input.txt','r') as input_file:
  #create claims matrix
  claims=[]
  #create fabric matrix (NOTE: python index starts at zero by default and doesn't include last index in range)
  fabric = [[0 for i in range(1000)] for j in range(1000)]
  for line in input_file.readlines():
    claim_num = int(line[line.find('#')+1:line.find('@')].strip())
    claim_col = int(line[line.find('@')+1:line.find(',')].strip())
    claim_row = int(line[line.find(',')+1:line.find(':')].strip())
    claim_width = int(line[line.find(':')+1:line.find('x')].strip())
    claim_height = int(line[line.find('x')+1:-1].strip())
    claims.append([claim_num, claim_row, claim_col, claim_height, claim_width])
    for i in range(claim_row,claim_row+claim_height):
      for j in range(claim_col,claim_col+claim_width):
        fabric[i][j] += 1
  #calculate total square inches with overlapping claims
  sqin_overlap = 0
  for i in range(1000):
    for j in range(1000):
      if fabric[i][j] > 1:
        sqin_overlap += 1
  print(claims[0:5])
  print('Max row inch in fabric (check it is below 1000) =', max([j[1] + j[3] for j in claims[0:len(claims)]]))
  print('Max column inch in fabric (check it is below 1000) =', max([j[2] + j[4] for j in claims[0:len(claims)]]))
  #answer for total square inches with overlapping claims
  print('Square inch overlap = ', sqin_overlap)
  
  #find a claim with no overlapping claims
  flag = 0
  claim_index = 0
  while flag == 0:
    claim = claims[claim_index]
    claim_flag = 0
    #check if claim has any overlapping claims, if it doesn't it's the answer
    for i in range(claim[1],claim[1]+claim[3]):
      for j in range(claim[2],claim[2]+claim[4]):
        if fabric[i][j] > 1:
          claim_flag = 1
    if claim_flag == 0:
      flag = 1
    claim_index += 1
  #answer for claim number that does not have overlapping claims
  print('The claim# that has no overlapping claims is ', claim_index)
    