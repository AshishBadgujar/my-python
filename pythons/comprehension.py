#list comprehension
list=[1,23,34,45,65,567,4,75,7,65,5,45]
print([i for i in list if i%3==0])

#dictionary
dict={"a":23,"b":24,"A":45}
print({i.lower():dict.get(i.lower(),0)+dict.get(i.upper(),0) for i in dict.keys()})

#set
sqr={i**2 for i in [1,2,2,3,3,4,4]}
print(sqr)

#generator
gen=(i for i in range(56))
print(gen)