#*args and **kwargs
def function(normal,*args,**kwargs):
    print(normal)
    i=0
    for i in args:
        print(i)
    for key,value in (kwargs.items()):
        print(key,value)
        
lists=["ashish",34,56]
students={"ashish":23,"bhargav":34,"ashu":43,"vishu":78}
function("ashish is king",*lists,**students)