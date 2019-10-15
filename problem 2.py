tup_list = [('John', ('Physics', 80)), ('Mark', ('Social', 95)), (' Daniel', ('Science', 90)), ('John', ('Science', 95)),
             ('Mark', ('Maths', 100)), ('Daniel', ('History', 75))]
gdict = dict()


for t in tup_list:
    if not (t[0] in gdict):
        gdict[t[0]] = list()
        gdict[t[0]].append(t[1])
    else:
        gdict[t[0]].append(t[1])
    gdict[t[0]] = sorted(gdict[t[0]])

for k in gdict:
    print(k, gdict.get(k))
