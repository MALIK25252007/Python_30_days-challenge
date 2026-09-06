#WAP to a binary file calledemp.dat and write into it the employee details of some employees,available in the form of dictionaries
import pickle
emp1={'empNo':1, 'Nmae': 'Tarun', 'age':19, 'Salary': 99000}
emp2={'empNo':2, 'Nmae': 'Varun', 'age':22, 'Salary': 69000}
emp3={'empNo':3, 'Nmae': 'Karan', 'age':32, 'Salary': 89000}
emp4={'empNo':4, 'Nmae': 'Vishnu', 'age':21, 'Salary': 99090}
empfile=open('Emp.dat','wb')
pickle.dump(emp1,empfile)
pickle.dump(emp2,empfile)
pickle.dump(emp3,empfile)
pickle.dump(emp4,empfile)

empfile.close()
