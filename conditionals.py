name1 = "Molly"
name2 = "Daniel"
if len(name1) > len(name2):
    print "My name is greater"
elif len (name1) < len(name2):
    print "Your name is greater"
else:
    print "Our names are equal"




date = 18
if date > 15:
    print "Oh we're halfway there!"
else:
    print "The month is still young"




today = "Wednesday"
if today == "Monday":
    print "Yaaas Monday! Here we go!"
elif today == "Tuesday":
    print "Sigh, it's only Tuesday"
elif today == "Wednesday":
    print "Humpday!"
elif today == "Thursday":
    print "#tbt"
elif today == "Friday":
    print "TGIF!"
else:
    print "Yeah it's the weekend"




age = 28
if age > 18:
    print "Yay! I can vote"




age = 28
if age > 18:
    print "Yay! I can vote"
else:
    print "Aww, I cannot vote"




age = 28
if age >= 18 and age >=21:
    print "I can vote and go to a bar"




age = 28
if age >= 21:
    print "I can go to a bar"
elif age >= 18 and age < 21:
    print "I can vote but I cannot go to a bar"
else:
    print "I cannot vote or go to a bar"




num = 8
if num / 2 == 4:
    print "The number 8 is even"
else:
    print "The number 8 is odd"




num = 8
if num / 2 != 4:
    print "The number 8 is odd"
else:
    print "The number 8 is even"




num1 = 8.0
num2 = 9.0
if num1 / 2 == 4 and num2 / 2 == 4:
    print "Both numbers are even"
else:
    print "Both numbers are not even"

num1 = 8.0
num2 = 9.0
if num1 / 2 == 4 and num2 / 2 == 4:
    print "Both numbers are even"
elif num1 / 2 >= 4 or num2 / 2 >= 4:
    print "8 is even and 9 is odd"
elif num1 / 2 <= 4 or num2 / 2 >= 4:
    print "8 is odd and 9 is even"
else:
    print "Both numbers are odd"




color = raw_input("What is your favorite color? ")
if color == "Blue":
    print "My favorite color is blue!"
else:
    print "My favorite color is not blue"




color = raw_input("What is your favorite color? ")
if color == "Blue" or "Yellow" or "Red":
    print "My favorite color is a primary color"
else:
    print "My favorite color is a secondary color"



