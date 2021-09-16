#formate function
students=["ashish","ashu","bhargav","vishu"]
marks=["100","34","23","56"]
for i in range (0,len(students)):
    template="{} has got {} marks"
    print(template.format(students[i],marks[i]))