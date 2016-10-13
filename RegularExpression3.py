import re

# 1. Regular Expression "findall" method
courses = "Python Training Course for Beginners: 15/Aug/2011 - 19/Aug/2011;Python Training Course Intermediate: " \
          "12/Dec/2011 - 16/Dec/2011;Python Text Processing Course:31/Oct/2011 - 4/Nov/2011"
items = re.findall("[^:]*:[^;]*;?", courses)
print(items)
# ['Python Training Course for Beginners: 15/Aug/2011 - 19/Aug/2011;', 'Python Training Course Intermediate: '
#                '12/Dec/2011 - 16/Dec/2011;', 'Python Text Processing Course:31/Oct/2011 - 4/Nov/2011']
items = re.findall("([^:]*):([^;]*;?)", courses)
print(items)
# [('Python Training Course for Beginners', ' 15/Aug/2011 - 19/Aug/2011;'), ('Python Training Course Intermediate',
#                 ' 12/Dec/2011 - 16/Dec/2011;'), ('Python Text Processing Course', '31/Oct/2011 - 4/Nov/2011')]


# 2. Regular expressions alternation
str = "Course location is London or Paris!"
mo = re.search(r"location.*(London|Paris|Zurich|Strasbourg)", str)
if mo: print(mo.group())
# location is London or Paris


# 3. Regular Expression "split" method
lines = ["surname: Obama, prename: Barack, profession: president",
         "surname: Merkel, prename: Angela, profession: chancellor"]
for line in lines:
    # var = re.split(",* *\w*: ", line)[0:]
    var = re.split(r",* *\w*:", line)[0:]
    print(var)
# ['Obama', 'Barack', 'president']
# ['Merkel', 'Angela', 'chancellor']


# 4. String substitution with regular expressions
str = "yes I said yes I will Yes."
res = re.sub("[yY]es", "no", str)
print(res)
# no I said no I will no.
