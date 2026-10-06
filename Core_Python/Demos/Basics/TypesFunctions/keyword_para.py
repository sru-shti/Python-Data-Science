# 1. To neglect positional parameter concept
# 2. Assign value to parameter in function callable
# 3. NAme of para in function call and function defination shpuld be same 
# 4. Flow from right to left

def employee(id , name , dept, sal):
    return f'ID: {id}\nNAME: {name}\nDEPARTMENT: {dept}\nSALARY: {sal}\n'

res=employee(name='abc', sal=3405940, dept='computer',id=241)
print(res)