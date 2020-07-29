import random
print("EINSTEIN'S RIDDLE")
print(" ")
print("This is a tool to make a version of Einstein's Riddle.")
print(" ")
print("Please Choose Five People.")
p1 = input("Person 1: ")
p2 = input("Person 2: ")
p12 = p1, p2
psemis1and2 = random.choice(p12)
if psemis1and2 == p1:
    psemis1 = p1
    loser1 = p2
elif psemis1and2 == p2:
    psemis1 = p2
    loser1 = p1
p3 = input("Person 3: ")
p4 = input("Person 4: ")
p34 = p3, p4
psemis3and4 = random.choice(p34)
if psemis3and4 == p3:
    psemis2 = p3
    loser2 = p4
elif psemis3and4 == p4:
    psemis2 = p4
    loser2 = p3
p5 = input("Person 5: ")
quarter = loser2, p5
quarter1choice = random.choice(quarter)
if quarter1choice == p5:
    pgroup3 = p5
    loserquarter = loser2
elif quarter1choice == loser2:
    pgroup3 = loser2
    loserquarter= p5
fifthandfourth = loser1, loserquarter
fourthchoice = random.choice(fifthandfourth)
if fourthchoice == loser1:
    pgroup4 = loser1
    pgroup5 = loserquarter
elif fourthchoice == loserquarter:
    pgroup4 = loserquarter
    pgroup5 = loser1
psemis = psemis1, psemis2
psemiswin = random.choice(psemis)
if psemiswin == psemis1:
    pgroup1 = psemis1
    pgroup2 = psemis2
elif psemiswin == psemis2:
    pgroup1 = psemis2
    pgroup2 = psemis1
print("Please Choose Five Colors.")
c1 = input("Color 1: ")
c2 = input("Color 2: ")
c12 = c1, c2
csemis1and2 = random.choice(c12)
if csemis1and2 == c1:
    csemis1 = c1
    closer1 = c2
elif csemis1and2 == c2:
    csemis1 = c2
    closer1 = c1
c3 = input("Color 3: ")
c4 = input("Color 4: ")
c34 = c3, c4
csemis3and4 = random.choice(c34)
if csemis3and4 == c3:
    csemis2 = c3
    closer2 = c4
elif csemis3and4 == c4:
    csemis2 = c4
    closer2 = c3
c5 = input("Color 5: ")
cquarter = closer2, c5
cquarter1choice = random.choice(cquarter)
if cquarter1choice == c5:
    cgroup3 = c5
    closerquarter = closer2
elif cquarter1choice == closer2:
    cgroup3 = closer2
    closerquarter= c5
cfifthandfourth = closer1, closerquarter
cfourthchoice = random.choice(cfifthandfourth)
if cfourthchoice == closer1:
    cgroup4 = closer1
    cgroup5 = closerquarter
elif cfourthchoice == closerquarter:
    cgroup4 = closerquarter
    cgroup5 = closer1
csemis = csemis1, csemis2
csemiswin = random.choice(csemis)
if csemiswin == csemis1:
    cgroup1 = csemis1
    cgroup2 = csemis2
elif csemiswin == csemis2:
    cgroup1 = csemis2
    cgroup2 = csemis1
print("Please Choose Five Drinks.")
d1 = input("Drink 1: ")
d2 = input("Drink 2: ")
d12 = d1, d2
dsemis1and2 = random.choice(d12)
if dsemis1and2 == d1:
    dsemis1 = d1
    dloser1 = d2
elif dsemis1and2 == d2:
    dsemis1 = d2
    dloser1 = d1
d3 = input("Drink 3: ")
d4 = input("Drink 4: ")
d34 = d3, d4
dsemis3and4 = random.choice(d34)
if dsemis3and4 == d3:
    dsemis2 = d3
    dloser2 = d4
elif dsemis3and4 == d4:
    dsemis2 = d4
    dloser2 = d3
d5 = input("Drink 5: ")
dquarter = dloser2, d5
dquarter1choice = random.choice(dquarter)
if dquarter1choice == d5:
    dgroup3 = d5
    dloserquarter = dloser2
elif dquarter1choice == dloser2:
    dgroup3 = dloser2
    dloserquarter= d5
dfifthandfourth = dloser1, dloserquarter
dfourthchoice = random.choice(dfifthandfourth)
if dfourthchoice == dloser1:
    dgroup4 = dloser1
    dgroup5 = dloserquarter
elif dfourthchoice == dloserquarter:
    dgroup4 = dloserquarter
    dgroup5 = dloser1
dsemis = dsemis1, dsemis2
dsemiswin = random.choice(dsemis)
if dsemiswin == dsemis1:
    dgroup1 = dsemis1
    dgroup2 = dsemis2
elif dsemiswin == dsemis2:
    dgroup1 = dsemis2
    dgroup2 = dsemis1
print("Please Choose Five Sports.")
s1 = input("Sport 1: ")
s2 = input("Sport 2: ")
s12 = s1, s2
ssemis1and2 = random.choice(s12)
if ssemis1and2 == s1:
    ssemis1 = s1
    sloser1 = s2
elif ssemis1and2 == s2:
    ssemis1 = s2
    sloser1 = s1
s3 = input("Sport 3: ")
s4 = input("Sport 4: ")
s34 = s3, s4
ssemis3and4 = random.choice(s34)
if ssemis3and4 == s3:
    ssemis2 = s3
    sloser2 = s4
elif ssemis3and4 == s4:
    ssemis2 = s4
    sloser2 = s3
s5 = input("Sport 5: ")
squarter = sloser2, s5
squarter1choice = random.choice(squarter)
if squarter1choice == s5:
    sgroup3 = s5
    sloserquarter = sloser2
elif squarter1choice == sloser2:
    sgroup3 = sloser2
    sloserquarter= s5
sfifthandfourth = sloser1, sloserquarter
sfourthchoice = random.choice(sfifthandfourth)
if sfourthchoice == sloser1:
    sgroup4 = sloser1
    sgroup5 = sloserquarter
elif sfourthchoice == sloserquarter:
    sgroup4 = sloserquarter
    sgroup5 = sloser1
ssemis = ssemis1, ssemis2
ssemiswin = random.choice(ssemis)
if ssemiswin == ssemis1:
    sgroup1 = ssemis1
    sgroup2 = ssemis2
elif ssemiswin == ssemis2:
    sgroup1 = ssemis2
    sgroup2 = ssemis1
print("Please Choose Five Foods.")
f1 = input("Food 1: ")
f2 = input("Food 2: ")
f12 = f1, f2
fsemis1and2 = random.choice(f12)
if fsemis1and2 == f1:
    fsemis1 = f1
    floser1 = f2
elif fsemis1and2 == f2:
    fsemis1 = f2
    floser1 = f1
f3 = input("Food 3: ")
f4 = input("Food 4: ")
f34 = f3, f4
fsemis3and4 = random.choice(f34)
if fsemis3and4 == f3:
    fsemis2 = f3
    floser2 = f4
elif fsemis3and4 == f4:
    fsemis2 = f4
    floser2 = f3
f5 = input("Food 5: ")
fquarter = floser2, f5
fquarter1choice = random.choice(fquarter)
if fquarter1choice == f5:
    fgroup3 = f5
    floserquarter = floser2
elif fquarter1choice == floser2:
    fgroup3 = floser2
    floserquarter= f5
ffifthandfourth = floser1, floserquarter
ffourthchoice = random.choice(ffifthandfourth)
if ffourthchoice == floser1:
    fgroup4 = floser1
    fgroup5 = floserquarter
elif ffourthchoice == floserquarter:
    fgroup4 = floserquarter
    fgroup5 = floser1
fsemis = fsemis1, fsemis2
fsemiswin = random.choice(fsemis)
if fsemiswin == fsemis1:
    fgroup1 = fsemis1
    fgroup2 = fsemis2
elif fsemiswin == fsemis2:
    fgroup1 = fsemis2
    fgroup2 = fsemis1
allgroup1 = pgroup1, cgroup1, dgroup1, sgroup1, fgroup1
allgroup2 = pgroup2, cgroup2, dgroup2, sgroup2, fgroup2
allgroup3 = pgroup3, cgroup3, dgroup3, sgroup3, fgroup3
allgroup4 = pgroup4, cgroup4, dgroup4, sgroup4, fgroup4
allgroup5 = pgroup5, cgroup5, dgroup5, sgroup5, fgroup5
print(" ")
print("NOW FOR THE RIDDLE")
print("-There are 5 houses in five different colors.")
print("-In each house there lives five different people.")
print("-These five people drink a certain type of beverage, play a ceratian kind of sport, and eat a certain type of food.")
print("-No people play the same sport, eat the same food, or drink the same beverage.")
print(" ")
print("The question is who eats %s?" % (fgroup4))
print(" ")
print("HINTS")
print(" ")
print("-%s lives in the %s house" % (pgroup3, cgroup3))
print("-%s eats %s" % (pgroup5, fgroup5))
print("-%s drinks %s" % (pgroup2, dgroup2))
print("-The %s house is on the left of the %s house" % (cgroup4, cgroup5))
print("-The %s house owner drinks %s" % (cgroup4, dgroup4))
print("-The person who plays %s eats %s" % (sgroup3, fgroup3))
print("-The owner of the %s house plays %s" % (cgroup1, sgroup1))
print("-The person living in the center house drinks %s" % (dgroup3))
print("-%s lives in the first house" % (pgroup1))
print("-The person who plays %s lives next to the person who eats %s" % (sgroup2, fgroup1))
print("-The person who eats %s lives next to the person who plays %s" % (fgroup2, sgroup1))
print("-The owner who plays %s drinks %s" % (sgroup5, dgroup5))
print("-%s plays %s" % (pgroup4, sgroup4))
print("-The person who plays %s has a neighbor who drinks %s" % (sgroup2, dgroup1))
print("-%s lives next to the %s house" % (pgroup1, cgroup2))
egg = input("(PRESS ENTER)")
if egg == "cheat":
    print(allgroup1)
    print(allgroup2)
    print(allgroup3)
    print(allgroup4)
    print(allgroup5)
else:
    print(" ")
fa = input("So what's the answer? ")
if fa == pgroup4:
    print("CONGRATULATIONS, YOU HAVE COMPLETED THIS RIDDLE!!")
else:
    print("SORRY, TRY AGAIN.")
