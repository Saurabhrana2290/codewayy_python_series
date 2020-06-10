'''Question-2: Write a program in Python in which you should display your following details:
    a. Full Name( String concatenation should be used)'''
first_name='Saurabh'
last_name='Rana'
full_name=first_name+' '+last_name           #String concatination
print("My name is {}.".format(full_name))

# b. College name with address (Use string concatenation)
college_name="DIT University"
address="Mussourie-Diversion Road, Dehradun\nUttarakhand-248009, India"
college_info=college_name+"\n"+address                                     #college_info contain college name and its full address
print(college_info)

# c.Initialize marks of  5 different subjects with good variable names.
chemistry=83
physics=82
hindi=85
english=79
maths=57

# d. Calculate and display the total marks, percentage.
total_marks_gain=chemistry+physics+hindi+english+maths
total=500
percentage=(total_marks_gain/total)*100
print("Total Marks: {0}\nPercentage: {1}".format(total_marks_gain,percentage))