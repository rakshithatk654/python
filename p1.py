"""a={'a':10,'b':20}
print(a)"""

'''a={'a':[10,20],'b':40}
print(a['a'][-2])'''

'''a="rakshitha"
print(a[-2])
print(a[3])'''

'''a='hello'
print(a[0:4])'''

'''a={'a':[10,20,30],'b':40}
print(a['a'][-2])
print(a['b'])
print(a['a'][1])'''

'''a="good morning"
print(a[6:10])
print(a[-6:-2])'''

'''a="hello"
print(a[3:0:-1])
print(a[-2:-5:-1])'''

'''a="good morning"
print(a[1:5+1:2])
print(a[5::3])
print(a[5:11+1:3])
print(a[-7::3])
print(len(a[-2:-8-1:-3]))'''

'''a=eval(input("enter the value"))
print(type(a))'''

'''a=int(input("enter the value"))
if a%2==0:
    print("even")
else:
    print("odd")'''

'''a=eval(input("enter the value"))
if len(a)==5:
    print('yes')
else:
    print('no')'''

'''ch=input('enter:')
if "A"<=ch<="Z":
    print('upper')
elif"a"<=ch<='z':
    print('lower')
else:
    print('not an alpha')'''

'''un=input('enter:')
if un=='hero':
    print('correct username')
    pw=input("enter")
    if pw=='hi@123':
        print('succesfull login')
    else:
        print('incorrect pw')
else:
    print('incorrect un')'''

'''username=hero
password=he@123
un=input("enter the un")
if un==username:
    print('correct username')
    pw=input("enter the pw")
    if pw==password:
        print('succesfull login')
    else:
         print('incorrect pw')
else:
    print('incorrect un')'''

'''i=1
while i<=10:
    print(i)
    i+=1'''

'''i=1
while i<=10:
 if i%2==0:
    print(i)
 i+=1'''

'''print("hello")'''

'''n=int(input("enter num:"))
rev=0
while n>0:
    id=n%10
    n=n//10
    rev=rev*10+id
print(rev)'''

'''for i in range(1,100):
    print(i)'''

'''for i in range(1,100):
    if i%2==0:
        print(i,'even')'''

'''a=[10,20,30]
for i in a:
    print(i)'''

'''s=input("enter:")
out=''
for i in s:
    if "A"<=i<="Z":
        out+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        out+=chr(ord(i)-32)
    else:racchur
        out+=i
print(out)'''

'''s=input("enter:")
rev=''
for i in s:
    rev=i+rev
print(rev)'''


'''for i in range(1,6):
    for j in range(1,6):
        print('*',end='')
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('1',end=' ')
        else:
            print('@',end=' ')
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('1',end=' ')
        else:
            print('@',end=' ')
    print()'''

'''a='happy birthday'
'htr'
print(a[-4:-7:-1])'''

'''def convert(s):
    out=' '
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert(input('enter a string:')))'''

'''def convert(s,out):
    out=' '
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
convert(input('enter a string:'),' ')'''

'''def convert():
    s=input('enter:')
    out=' '
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    return out
print(convert())'''

'''class college:
    cname="goln"
    cloc='hoodi'
s1=college()
print(s1.cname,s1.cloc)
college.cloc='kr puram'
print(college.cloc)
print('changing loc wtrsp obj')
s1.cloc='hoodi'
print(s1.cloc)
print(college.cloc)

s1.name='racchu'
s1.phone=7894561235

s2=college()
s2.name='anu'
s2.phone=8974561234

print(s1.cloc)
s1.cloc='kr puram'
print('after chamging')
print(s1.cloc)
print(s2.cloc)
print(college.cloc)'''

'''class college:
    def __init__ (self,name,phone,usn):
        self.name=name
        self.phone=phone
        self.usn=usn
    def display(self):
        print(self.name,self.phone,self.usn)
    def change_name(self,new):
        self.name=new
s1=college('racchu',8954627635,'gyefde')
s2=college('anu',965854562,'dghty')
s1.display()
s2.display()
s1.change_name('acchu')
s1.display()'''