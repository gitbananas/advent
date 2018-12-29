#open file and strip out box IDs into a list
with open('input.txt','r') as input_file:
  claims=[]
  for line in input_file.readlines():
    claim_num = int(line[line.find('#')+1:line.find('@')].strip())
    claim_col = int(line[line.find('@')+1:line.find(',')].strip()) + 1
    claim_row = int(line[line.find(',')+1:line.find(':')].strip()) + 1
    claim_width = int(line[line.find(':')+1:line.find('x')].strip())
    claim_height = int(line[line.find('x')+1:-1].strip())
    claims.append([claim_num, claim_row, claim_col, claim_width, claim_height])
  print(claims)
  print(len(claims))