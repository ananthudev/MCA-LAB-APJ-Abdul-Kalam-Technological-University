y={'carl':40,'alan':2,'bob':1,'danny':3}
l=list(y.items())
dict=dict(l)
print("Dictionary",dict)
l.sort()
print('Ascending order is',l)
l=list(y.items())
l.sort(reverse=True)
print('Descending order is',l)
