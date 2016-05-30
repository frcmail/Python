#!/usr/bin/python




info = 'This var will be printed out ...'
name=raw_input('Please input you name:')
age=raw_input('age:')
job=raw_input('job:')
salary=raw_input('salary:')

real_age =29


for i in range(10):
	age= input('age:')
  if age>29:
	  print 'think smaller'
  elif age=29:
	  print 'GOOD!'
	break
  else:
	  print 'think bigger!'
print 'you still got %s shots'%(9-i)



if age>40:
	  msg ='you are too old!'
	elif age>30:
	  msg='you still have a few years to xx up'
	else:
	  msg ='you are still quite young,go hook up some girls!'

print'''
personal information of %s:
	Name: %s
	Age : %s
	Job : %s
	Salary:%s
	----------------
%s
	''' % (name,name,age,job,salary,msg)
print type(age)

