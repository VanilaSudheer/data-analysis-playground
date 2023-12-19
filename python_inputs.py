strnames = input('Enter the names separated by commas: ').title().split(',')
strassignments = input('enter missing assignment of each in order separated by commas: ').split(',')
strgrades= input('current grades separated by commas:').split(',')
assignments = [int(num) for num in strassignments]
grades = [int(num) for num in strgrades]
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"
for name,assignment,grade in zip(strnames,assignments,grades):
    potential = grade+assignment*2
    print(message.format(name,assignment,grades,potential))


