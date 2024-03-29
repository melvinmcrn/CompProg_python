def string2list(s):
    s = s.strip()
    if s == '[]':
        return []
    if s.find('[') < 0:
        return int(s)
    count = 0
    ans = []
    start = 1
    for i in range(1, len(s)-1):
        if s[i] == '[':
            count+=1
        elif s[i] == ']':
            count-=1
        elif s[i] == ',' and count == 0:
            ans.append(string2list(s[start:i]))
            start = i+1
    ans.append(string2list(s[start:len(s)-1]))
    return ans

#-----------------------------------------------------------------
def isinlist(mylist, x):

    for c in mylist:
        if type(c) is list:
            if isinlist(c,x):
                return True
        else:
            if x == c:
                return True

    return False

#main=============================================================
mylist = string2list(input().strip())
x = int(input().strip())
if isinlist(mylist, x):
    print('Found')
else:
    print('Not Found')
