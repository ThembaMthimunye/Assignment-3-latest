#Student Name:Mthimunye Themba
#Student no:218634567
#Date:Feb 2023
#Assignment 3:Python


s="fullstackslp"
#"f"
print(s[0])

#"p"
print(s[-1])

#"stack"
print(s[4:9])

#"slp"
print(s[9:])

#"stack"
print(s[7:10])




########################
#Probelm 2

d1={"simple_key":"hello"}
print(d1["simple_key"])

d2={"k1":{"k2":"hello"}}
print(d2["k1"]["k2"])

d3={"k1":[{"nest_key":["ti is deep",["hello"]]}]}
print(d3["k1"][0]["nest_key"][1][0])

 
###########################################
#problem 4

mylist=[1,1,1,1,1,2,2,2,2,3,3,3,3]
s=set()
s.add(1)
s.add(1)
s.add(1)
s.add(1)
s.add(2)
s.add(2)
s.add(2)
s.add(2)
s.add(3)
s.add(3)
s.add(3)
s.add(3)
print(s)


#Probelem 5
age=45
name="kyle"

print("hello my dog's name is {} and he looks {} years old".format(name,age))