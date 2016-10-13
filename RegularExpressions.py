import re

# "." character is the place holder for ny character in regular expressions
x = re.search(r".at", "A cat and a rat can't be friends.")
print(x)

# Square brackets, "[" and "]", are used to include a character class. [xyz] means e.g. either an "x", an "y" or a "z".
x = re.search(r"[cr]at", "A cat and a rat can't be friends.")
print(x)

# To manage such such character classes the syntax of regular expressions supplies a metacharacter "-".
# [a-e] a simplified writing for [abcde] or [0-5] denotes [012345].
x = re.search(r"[A-Za-z]at", "A cat and a rat can't be friends.")
print(x)

# The expression [-az] is only the choice between the three characters "-", "a" and "z", but no other characters.
# The same is true for [az-]
x = re.search(r"[-a-z]at", "A cat and a -rat can't be friends.")
print(x)

# "^" is used directly after an opening sqare bracket, it negates the choice.
# [^0-9] denotes the choice "any character but a digit"
x = re.search(r"[^abc]at", "A cat and a bat can't be friends.")
print(x)

# Finds all the lines of the phone book, which contain a person with the surname "Neu" and a first name starting with J.
# fh = open("simpsons_phone_book.txt")
# for line in fh:
#    if re.search(r"J.*Neu", line):
#        print(line.rstrip())
# fh.close()

# The special sequences consist of "\\" and a character from the following list:
# \d	Matches any decimal digit; equivalent to the set [0-9].
# \D	The complement of \d. It matches any non-digit character; equivalent to the set [^0-9].
# \s	Matches any whitespace character; equivalent to [ \t\n\r\f\v].
# \S	The complement of \s. It matches any non-whitespace character; equiv. to [^ \t\n\r\f\v].
# \w	Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]. With LOCALE, it will match the set [a-zA-Z0-9_] plus characters defined as letters for the current locale.
# \W	Matches the complement of \w.
# \b	Matches the empty string, but only at the start or end of a word.
# \B	Matches the empty string, but not at the start or end of a word.
# \\	Matches a literal backslash.

# match(re_str, s) checks for a match of re_str merely at the beginning of the string
s1 = "Mayer is a very common Name"
s2 = "He is called Meyer but he isn't German."
print(re.search(r"M[ae][iy]er", s1))
print(re.search(r"M[ae][iy]er", s2))
print(re.match(r"M[ae][iy]er", s1))
print(re.match(r"M[ae][iy]er", s2))

# Now the string doesn't start with a Maier of any kind, but the name is following a newline character:
# The name hasn't been found, because only the beginning of the string is checked.
s = s2 + "\n" + s1
print(re.search(r"^M[ae][iy]er", s))

# We use the multiline mode. Multiline mode doesn't affect the match() method
print(re.search(r"^M[ae][iy]er", s, re.MULTILINE))
print(re.search(r"^M[ae][iy]er", s, re.M))
print(re.match(r"^M[ae][iy]er", s, re.M))

# The usage of the "$" character that shows the end of the string in the following example:
print(re.search(r"Python\.$", "I like Python."))
print(re.search(r"Python\.$", "I like Python and Perl."))
print(re.search(r"Python\.$", "I like Python.\nSome prefer Java or Perl."))
print(re.search(r"Python\.$", "I like Python.\nSome prefer Java or Perl.", re.M))

# A question mark declares that the preceding character or expression is optional.
# A subexpression is grouped by round brackets and a question mark following such a group means that this
# group may or may not exist. With the following expression we can match dates like "Feb 2011" or February 2011"
s1 = "Mayr is a very common Name"
print(re.search(r"M[ae][iy]e?r", s1))

# A regular expression which matches strings which starts with a sequence of digits - at least one digit -
# followed by a blank and after this arbitrary characters.
s3 = "9"
print(re.search(r"^[0-9][0-9]* ", s3))
s3 = "9 "
print(re.search(r"^[0-9][0-9]* ", s3))
s3 = "9 1"
print(re.search(r"^[0-9][0-9]* ", s3))
s3 = "91"
print(re.search(r"^[0-9][0-9]* ", s3))
s3 = "9 a"
print(re.search(r"^[0-9][0-9]* ", s3))


# Solution with the + quantifier
s3 = "9"
print(re.search(r"^[0-9]+ ", s3))
s3 = "9 "
print(re.search(r"^[0-9]+ ", s3))
s3 = "9 1"
print(re.search(r"^[0-9]+ ", s3))
s3 = "91"
print(re.search(r"^[0-9]+ ", s3))
s3 = "9 a"
print(re.search(r"^[0-9]+ ", s3))

# The general syntax is {from, to}: this means that the expression has to appear at least
# "from" times and not more than "to" times. {, to} is an abbreviated spelling for {0,to} and
# {from,} is an abbreviation for "at least from times but no upper limit"
# r"^[0-9]{4,5} [A-Z][a-z]{2,}"


# A match object contains the methods group(), span(), start() and end(), as can be seen in the following application:
mo = re.search("([0-9]+).*: (.*)", "Customer number: 232454, Date: February 12, 2011")
print mo.group()
# 232454, Date: February 12, 2011
print mo.span()
# (17, 48)
print mo.start()
# 17
print mo.end()
# 48
print mo.span()[0]
# 17
print mo.span()[1]
# 48
print mo.group(1)
# '232454'
print mo.group(2)
# 'February 12, 2011'
print mo.group(1,2)
# ('232454', 'February 12, 2011')

