
lines=[]
with open('key.txt', 'r') as key_file:
    for line in key_file:
        lines.append(line.strip())

col_num, row_num = int(lines[0]),int(lines[1])

secret = ''
with open('secret.txt','r') as secret_file:
    for line in secret_file:
        secret += line.strip()

rows = []
for x in range(0,len(secret),col_num):
    bracket = (x, x+col_num)
    rows.append(bracket)

public_list = []
with open('public.txt','w') as public_file:
    for start, end in rows:
        public_list.append(secret[start:end])
    public_list_fixed = [item + '\n' for item in public_list]
    public_file.writelines(public_list_fixed)

