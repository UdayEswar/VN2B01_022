print("--------String Functions---------")

a="uday"
b=a.capitalize()        #Upper case the first letter in this sentence
print("1.",b)

a="HI ALL THIS IS UDAY"
b=a.casefold()          #Make the string lower case
print("2.",b)

a="This Is Center"
b=a.center(50)          #Returns a centered string
print("3.",b)

a="This_Is_Count"
b=a.count('s')          #Returns the number of times a specified value occurs in a string
print("4.",b)

b=a.encode()            #Returns an encoded version of the string
print("5.",b)

b=a.endswith('t')       #Returns true if the string ends with the specified value
print("6.",b)

a="This_Is_E\txp\tandtabs"
b=a.expandtabs(1)        #Sets the tab size of the string
print("7.",b)

b=a.find('E')
print("8.",b)           #Searches the string for a specified value and returns the position of where it was found

b=a.format()
print("9.",b)           #Formats specified values in a string

b=a.index("is")
print("10.",b)          #Searches the string for a specified value and returns the position of where it was found

a="ThisIsisalnum46"
b=a.isalnum()           #Check if all the characters in the text are alphanumeric:
print("11.",b)

a="ThisIsisalnum"
b=a.isalpha()           #Check if all the characters in the text are letters:
print("12.",b)

b=a.isascii()
print("13.",b)          #Returns True if all characters in the string are ascii characters

a='\u0033'
b=a.isdecimal()
print("14.",b)          #Returns True if all characters in the string are decimals

a=('6666')
b=a.isdigit()           #Returns True if all characters in the string are digits
print("15.",b)

a="Video"
b=a.isidentifier()      #Returns True if the string is an identifier
print("16.",b)

a="uday"
b=a.islower()           #Check if all the characters in the text are in lower case:
print("17.",b)

a="55555"
b=a.isnumeric()         #Check if all the characters in the text are numeric:
print("18.",b)

a="Hii This is Uday #@1!"
b=a.isprintable()       #Check if all the characters in the text are printable:
print("19.",b)

a=" "
b=a.isspace()           #Check if all the characters in the text are whitespaces:
print("20.",b)

a="Hi Everyone This Is Uday"
b=a.istitle()           #Returns True if the string follows the rules of a title
print("21.",b)

a="HI EVERYONE THIS IS UDAY"
b=a.isupper()           #Returns True if all characters in the string are upper case
print("22.",b)

a=("Uday","Vasudev","SunithaDev")
b= ' '.join(a)          #Join all items in a tuple into a string, using a hash character as separator:
print("23.",b)

a="Uday"
b=a.ljust(10)           #Return a 10 characters long, left justified version of the word "Uday":
print("24.",b,"Is a Gud Person")

a="Vasudev MY HEARTTOUCH"
b=a.lower()             #Converts a string into lower case
print("25.",b)

a="     Uday      "
b=a.lstrip()            #Returns a left trim version of the string
print("26. He Is ",b,"And He Is A Friendly Guy")

a="Hello Uday"
b=a.maketrans("U","D")  #Create a mapping table, and use it in the translate() method to replace any "U" characters with a "D" character:
print("27.",a.translate(b))

a="Only Uday Knows How To Behaviour"
b=a.partition("Uday")   #Returns a tuple where the string is parted into three parts
print("28.",b)

a="Uday is Uday"
b=a.replace("Uday","Vasudev")
print("29.",b)          #Returns a string where a specified value is replaced with a specified value

a="Uday, Have Redmik20."
b=a.rfind("Have")       #Where in the text is the last occurrence of the string "Have"?:
print("30.",b)

b=a.rindex("Redmik20")
print("31.",b)

a="Only Uday Knows How To Behaviour"
b=a.rpartition("Behaviour")
print("32.",b)          #Returns a tuple where the string is parted into three parts

a="Only, Uday, Knows, How To Behaviour"
b=a.rsplit(", ")        #Splits the string at the specified separator, and returns a list
print("33.",b)

a="Only Uday Knows How To Behaviour"
b=a.rstrip()            #Remove any white spaces at the end of the string:
print("34.  Only Uday",b,'Knows How To Behaviour')

a="Welcome To Vasudevs World"
b=a.split()             #Split a string into a list where each word is a list item:
print("35.",b)

a="Only Uday Knows\How To Behaviour"
b=a.splitlines()        #Splits the string at line breaks and returns a list
print("36.",b)

b=a.startswith("Only")  #Returns true if the string starts with the specified value
print("37.",b)

a="     Knows      "
b=a.strip()             #Remove spaces at the beginning and at the end of the string:
print("38. Only Uday",b,"How To Behaviour")

a="Only Uday Knows How To Behaviour"
b=a.swapcase()          #Make the lower case letters upper case and the upper case letters lower case:
print("39.",b)

a="Welcome To My World"
b=a.title()             #Make the first letter in each word upper case:
print("40.",b)

a= {85:68}
b= "Hello Uday.!"       #Replace any "S" characters with a "P" character:
print ("41.",b.translate(a))

a="50"
b=a.zfill(5)            #Fill the string with zeros until it is 10 characters long:
print("42.",b)

a="Uday"
b=a.upper()             #Upper case the string:
print("43.",b)

