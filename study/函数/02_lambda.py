student = [
    {'name':'Tom','age':18},
    {'name':'Lay','age':20},
    {'name':'Jerry','age':7}
]
student.sort(key=lambda x:x['age'])
print(student)