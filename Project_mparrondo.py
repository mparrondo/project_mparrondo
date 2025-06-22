# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Insert your weekly report function
# Ensure the function takes 3 pieces of input - the task dictionary,
# habit dictionary, and file name to read the data.

def report_week(tasks, track_habits, file_name):
    print(f"Weekly progress for {file_name}")
    # Habits
    if not track_habits:
        print("No habits found")
    else:
        print("Habits progress:")
        for habit, days_dict in track_habits.items():
            completed_days = sum(1 for status in days_dict.values() if status)
            print(f"{habit}: {completed_days}/7 days completed")
    # Tasks
    completed_tasks = []
    uncompleted_tasks = []
    tasks_exist = any(tasks[day] for day in days)
    if not tasks_exist:
        print("No tasks found")
    else:
        for day in days:
            for task, done in tasks[day].items():
                entry = f"{task} ({day})"
                if done:
                    completed_tasks.append(entry)
                else:
                    uncompleted_tasks.append(entry)
        print("Tasks completed:")
        if completed_tasks:
            for t in completed_tasks:
                print(f" {t}")
        else:
            print("None")
        print("Tasks not completed:")
        if uncompleted_tasks:
            for t in uncompleted_tasks:
                print(f" {t}")
        else:
            print("None")
    print()

# Provide the list of files to process.
# The dictionaries.txt files each contain a list of
# two dictionaries, the first being for habits and
# the second for tasks. 
#
# Note that the files and this python script should be in the
# same directory when you run it.
file_list = [
    'dictionaries_1.txt', 'dictionaries_2.txt', 'dictionaries_3.txt',
    'dictionaries_4.txt', 'dictionaries_5.txt', 'dictionaries_6.txt',
    'dictionaries_7.txt', 'dictionaries_8.txt', 'dictionaries_9.txt',
    'dictionaries_10.txt'
]

# This section will loop through the files in the list above, and 
# run the report_week() function for each file. 
#
# The use of the ast library allows you to read text files
# that contain Python structures, in this case a list of dictionaries
#
# This code loops through each file, assigns the list of dictionaries
# as the variable 'data', then gives the report_week() function
# the appropriate input.
#
# Ensure you edit the final line so it matches your function name,
# and supply the appropriate input.
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        report_week(data[1], data[0], file_name)
