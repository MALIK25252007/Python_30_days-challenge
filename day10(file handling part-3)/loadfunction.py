#WAP to open th file Emp.dat created before , read the objects written in it and display them
import pickle
emp={ }
empfile=open('Emp.dat','rb')
try:
    while True:
        emp=pickle.load(empfile)
        print(emp)
except EOFError:
    empfile.close()
