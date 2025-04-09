#Write a program that takes a string input and converts it to uppercase using a string method,Text1="Hello world"
text1="Hello world"
text=text1.upper()
print(text)

#write a program that converts a given string to lower case
text2='PYTHON IS FUN'
word=text2.lower()
print(word)

#write a program that removes leading and trailing spaces from a string
text3="    python  "
word_strip=text3.strip()
print(word_strip)

#write a program that counts how many times a specific word appears in a sentence
text4="banana banana apple"
apperance=text4.count('banana')
print(apperance)

#write a program that finds **first index** of a substring inside a string 
text5="I love Python"
sub=text5.index("I")
print(sub)


#write a python program that replaces all occurance of one word with another "I love python",replace "love " with "like"
#"I love python",replace "love " with "like"
text6="I love python"
modify_text=text6.replace("love","like")
print(modify_text)

#write a python program that checks whether a string starts starts with a specific word "Hello, world!","Hello"
text7="Hello, world!"
specific_word=text7.startswith("Hello")
print(specific_word)


#Write a program that splits a sentence into a list of words
text8="python is amazing "
sentence_split=text8.split()
print(sentence_split)


#write a program that joins a list of words into a single string separated by hyphens(-)
text9=["apple","banana","cherry"]
string="-" .join(text9)
print(string)


#write  a program that checks if a given string only contains only numbers 
text10="12345"
numbers=text10.isdigit()
print(numbers)


#write a program that extracts dormain from an email address -sharlynemrc7@gmail.com
email='sharlynemrc7@gmail.com'
email_split=email.split("@")[-1]
print(email_split)