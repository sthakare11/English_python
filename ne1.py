import texttable as tt
tab = tt.Texttable()
headings = ['Tenses','Simple','Continuous','Perfect','PerfectContinuos']
tab.header(headings)
tenses = ['Past','Present','Future']
simple = ['v2\n I played Cricket','v1\n I play Cricket','will+v1\n I will play cricket']
continuous = ['was/were+v1+ing\n  I was playing cricket','am/is/are+v1+ing\n I am playing cricket','will/shall+be+v1+ing\n I will be playing cricket' ]
perfect = ['had+v3\n I had played cricket','have/has+v3\n I have played cricket','will/shall+have+v3\n I will have played cricket']
perfectcontinuous  = ['had+been+v1+ing\n I had been playing cricket','have/has+v1+ing\n I have been playing cricket','will+have/has+been+v1+ing\n I will have been playing cricket ']

for row in zip(tenses,simple,continuous,perfect,perfectcontinuous):
    tab.add_row(row)

s = tab.draw()
print (s)

print("V1=FIRST FORM OF VERB\n v2=SECOND FORM OF VERB\n V3=THIRD FORM OF VERB\n")

b=input("1.Practice tenses rules\n 2.Change the tenses\n")
b=int(b)

if b == 1 :
    import os
    os.system('python3 tenserule.py')

else :
    import os 
    os.system('python3 Change.py')
 


