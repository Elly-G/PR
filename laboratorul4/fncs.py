import random

def help_me():
    return help_description.encode('utf-8')

def hello(word):
    return word.encode('utf-8')
    
def is_prime(n):
    n = int(n)
    if n > 1:
        for i in range(2,n):
            if (n % i) == 0:
                ans = str(n) + " isn't a prime number!\n"
                ans = ans + str(i) + " * " + str(n//i) + " = " + str(n)
                break
            else:
                ans = str(n) + " is a prime number!\n"
    else:
        ans = str(n) + " isn't a prime number!\n"   
    return ans.encode('utf-8')
    
def answer():
    return random.choice(yn).encode('utf-8')
    
def joke():
    return random.choice(jokelist).encode('utf-8')
    
    
help_description = \
"""
===============
=== h e l p ===
===============
/help - displays this list of available commands
/hello <text> - returns the text that was sent as param
/prime <int> - tells if the given number is prime
/answer - responds to your most interested question with an 'yes' or 'no' 
/joke - tells awesome programming jokes 
/exit - closes connection
===============
"""

yn = ['yes','no']

jokelist = \
[
'Q: How many programmers does it take to change a light bulb? A: none, that is a hardware problem',
'Q: Whats the object-oriented way to become wealthy? A: Inheritance',
'Q: What did the Java code say to the C code? A: You have got no class.',
'Q: Why did the database administrator leave his wife? A: She had one-to-many relationships',
'Q: What do cats and programmers have in common? A: When either one is unusually happy and excited, an appropriate question would be, "did you find a bug?"',
'Q: Why did the programmer quit his job? A: Because he did not get arrays.',
'Yesterday I changed the name of my WiFi to "Hack me if you can". Today I found it named to "Challenge accepted".',
'There are 10 types of people in this world - those who understand binary, and those who do not.',
'Q: Why do python coders wear glasses? A: Because they cannot "C".'
]