def emp(**data):
    for val in data:
        print(val)
print()

emp(id=102,name='abc',sal=123244,dept='IT')
def emp(**data):
    for key,val in data.items():
        print(key,":",val)

emp(id=102,name='abc',sal=123244,dept='IT')