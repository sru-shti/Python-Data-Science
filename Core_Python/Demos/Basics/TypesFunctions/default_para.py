# 1 . to make parameter optional
# 2 . Assign value to  parameter in function defination
# 3 . if we pass value to default parameter it takes passed value 
#     if we dont pass value to default para it takes default value 
# 4 . flow from right to left in formal parameter and left to right in actual parameter 

def emp(id,name="srushti",sal=1000 ,dept="computer"):
    print("ID: ",id)
    print("NAME: ",name)
    print("SALARY: ",sal)
    print("DEPARTMENT: ",dept)

emp(101,"abc",50000)
emp(102,"fdbfs",90000,"IT")
emp(103,"dnhsl")