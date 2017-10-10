print "T O  -  D O   A p p\n"

todo_list =[]
todo_dictionary = {}

while True:
    task = raw_input("What we have 2 do?")
    todo_list.append(task)

    complete = raw_input("Is this task done already? (yes / no):")
    if complete.lower() == "yes":
        todo_dictionary[task] = True
    else:
        todo_dictionary[task] = False

    print "Your very important task is: " + task
    newTask = raw_input(" Want to add another task? (yes / no)")
    if newTask.lower() == "no":
        break

todo_file = open("file_name.txt", "w+")
todo_file.write ("Task DONE: \n")
for task in todo_dictionary:
    if todo_dictionary[task]:
        print task
        todo_file.write("- " + task + "\n")
todo_file.write ("Task NOT DONE: \n")
for task in todo_dictionary:
    if not todo_dictionary[task]:
        print task
        todo_file.write("- " + task + "\n")

print "\nE N D"
