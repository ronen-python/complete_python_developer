import re

string1 = 'search inside of this text please'
a = re.search('this', string1)


print(a.span())
print(a.start())
print(a.end())
print(a.group())


pattern=re.compile('this')
a = pattern.search(string1)
b = pattern.findall(string1)
c = pattern.fullmatch(string1)
d = pattern.match(string1)
print(d)


pattern=re.compile(r'([a-zA-Z]).([a])')
e = pattern.search(string1)
print(e.group())
print(e.group(1))

print(e.group(2))

# regex101


pattern = re.compile(r"^([a-zA-Z0-9$%#@.0-9]){7,}[0:9]")
password = 'retreter44i9a'
check = pattern.fullmatch(password)
print(check)

