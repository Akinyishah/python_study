#Clean up the following variable to give the clean version in lower case. Using inbuilt methods in the str class 
#name = “  JOHn  .“ to “john”

name= "   JOHn  ."
name=name.lower().replace('.','').strip()
print(name)

#Slice the below string to get you the resulting sentence:
#sentence_one = “The Dog Breed is German Shepherd” only display “Breed is German”
sentence_one="The Dog Breed is German Shepherd"
text=sentence_one[8:22+1]
print(text)
#sentence_two = “Defeats for the Clinton forces, this was her moment of triumph” only display “Clinton forces”
sentence_two ="Defeats for the Clinton forces, this was her moment of triumph"
text1="Defeats for the Clinton forces, this was her moment of triumph"
text1=sentence_two[16:29+1]
print(text1)

#Split the below sentence using a semicolon i.e ; And display length of the result. 
#“The lazy dog; ran so fast; it hit the wall.” 
sentence="The lazy dog; ran so fast; it hit the wall."
split_sentence=sentence.split(";")
print(split_sentence)
print(len(split_sentence))

#first_name="  Joh.n"  last_name="   Do,e" Clean up and display Full name i.e John Doe
first_name="  Joh.n"
last_name="   Do,e"
#cleaning first_name
first_name=first_name.replace('.','').strip()
#cleaning last_name
last_name=last_name.replace(',','').strip()
full_name=first_name+" "+last_name
print(full_name)

#Having the string r = '["E","W","C"]' #Manipulate it to display EWC
r = '["E","W","C"]'
r=r[1:12] #"E","W","C"
r=r.replace('"','').replace(',','')
print(r)


