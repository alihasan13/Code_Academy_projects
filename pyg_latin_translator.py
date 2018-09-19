
print ('Wellcome')
word= input("Enter your word: ")
if word != "" and word.isalpha():  #isalpha will prevent words containing digit/sympbols
    print ("you have entered: "+word)
    translate_pig= word[1:]+word[0]+"ay"
    print (translate_pig.lower())

else:
    print ("you have entered nothing or the word contains numbers/symbles")
