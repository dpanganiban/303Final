x=0
score=0

print("How well do you know the Warriors?")
# Question 1
print ("On March 12,2007, the Golden State Warriors Snapped which team's 17 game winning streak?")
answer_1= input("(a) Spurs\n(b) Pistons\n(c) Suns\n(d) Mavericks\n:")
if answer_1.lower()== "d" or answer_1.lower()== "Mavericks":
	print("Correct")
	x = x + 1
else:
	print("Incorrect, the answer is Mavericks")	
# Question 2
print("What was the first year the Warriors played under the Golden State name in the NBA?")
answer_2= input("(a) 1954\n(b) 1949\n(c) 1962\n(d) 1971\n:")
if answer_2.lower()== "d" or answer_2.lower()=="1971":
	print("Correct")
	x = x + 1
else:
	print("Incorrect, the answer is 1971")
# Question 3
print("How many games did the Golden State Warriors win during the 2007 NBA playoffs?")
answer_3= input("(a) 4\n(b) 6\n(c) 5\n(d) 7\n:")
if answer_3.lower()== "c" or answer_3.lower()=="5":
	print("Correct")
	x = x + 1
else:
	print("Incorrect, the answer is 5")
# Question 4
print("In the 2015 playoffs, Steph Curry broke the record for the most three-pointers in  a single post season. Whose record did he break?")
answer_4= input("(a) Reggier Miller\n(b) Ray Allen\n(c) Paul George\n(d) Danny Green\n:")
if answer_4.lower()== "a" or answer_4=="Reggie Miller":
	print("Correct")
	x = x + 1
else:
	print("Incorrect, the answer is Reggie Miller ")
# Question 5
print("Steph Curry was named as the NBA MVP for a second consecutive season in 2015-2016. Who finished second in the voting?")
answer_5= input("(a)James Harden\n(b) Lebron James\n(c) Kawahi Leonard\n(d) Kevin Durant\n:")
if answer_5.lower()== "c" or answer_5=="Kawahi Leonard":
	print("Correct")
	x = x + 1
else:
	print("Incorrect, the answer is Kawahi Leonard")
# Question 6
print("Which of these players failed to lead the Warriors in scoring in any of their 2015-16 playoff games?")
answer_6= input("(a) Draymond Green\n(b) Andre Iguolda\n(c) Stephen Curry\n(d) Klay Thompson\n:")
if answer_6.lower()== "b" or answer_6=="Andre Iguolda":
	print("Correct")
	x = x + 1
else:
	print("Incorrect, the answer is Andre Iguolda")
# Question 7
print("Which player featured in the most regular season games for the Warriors in the 2017-18 season?")
answer_7= input("(a) Kevin Durant\n(b) Nick Young\n(c) Draymond Green\n(d) Ian Clark\n:")
if answer_7.lower()== "d" or answer_7=="Ian Clark":
	print("Correct")
	x = x + 1
else: 
	print("Incorrect, the answer is Ian Clark")
# Question 8
print("On May 11,2017 Baron Davis had one of his biggest dunk of his carrer. Who did he dunk on?")
answer_8= input("(a) Deron Williams\n(b) Andrei Kirilenko\n(c) Cj Miles\n(d) Derek Fisher\n:")
if answer_8.lower()== "b" or answer_8=="Andrei Kirilenko":
	print("Correct")
	x = x + 1
else:
	print("Incorrect, the answer is Andrei Kirilenko")
# Question 9
print("When did Jason Richardson win his first dunk contest?")
answer_9= input("(a) 2004\n(b) 2005\n(c) 2001\n(d) 2002\n:")
if answer_9.lower()== "d" or answer_9=="2002":
	print("Correct")
	x = x + 1
else:
	print("Incorrect, the answer is 2002 ")
# Question 10
print("What year did Stephen Curry get draftd into the NBA?")
answer_10= input("(a) 2006\n(b) 2007\n(c) 2008\n(d) 2009\n:")
if answer_10.lower()== "d" or answer_10=="2009":
	print("Correct")
	x = x + 1
else:
	print("Incorrect, the answer is 2009")


score = float(x / 10) * 100
print(x,"out of 10, that is",score, "%")