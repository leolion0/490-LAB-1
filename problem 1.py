f = open("p1.txt", 'r')
conts = f.read()
bad_chars = ['(', ')', ',', '?', '!', '=', ':', ';', '.']
for i in bad_chars:
    conts = conts.replace(i, ' ')
conts = " ".join(conts.split())

c_list = list()
outstr = ''
for c in conts:
    if c == ' ':
        outstr += c
        continue
    if c not in c_list:
        c_list.append(c)
        outstr += c
outstr = " ".join(outstr.split())
print(outstr)