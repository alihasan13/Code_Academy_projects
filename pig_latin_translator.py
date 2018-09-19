
word= input("Enter your word: ")
if word=="":
    print ("You have entered nothing.")
else:
    translate_pig= word[1:]+word[0]+"ay"
    print (translate_pig.lower())

