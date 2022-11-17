import functions as f

"""Setup for tests"""
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}
# Add Key to Dictionary
marks = {1: 10, 2: 20}


xy = f.add_key_to_dictionary(marks, 3, 30)
print(xy)

for elements in (dic1, dic2, dic3):
    dic4.update(elements)
print(dic4)

x = f.check_key_presence(dic4, 5)
y = f.check_key_presence(dic4, 9)

print(x)
print(y)