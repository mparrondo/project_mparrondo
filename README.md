# README.md

## Weekly Task \& Habit Tracker

### Project Description

This repository contains a **Weekly Task \& Habit Tracker** developed in Python as part of an ACENET academic project. The application allows users to manage and track their tasks and habits throughout the week, providing a functional and interactive tool to improve personal productivity.

### Key Features

The tracker enables users to:

- **Task Management**: Add tasks to specific days of the week and mark them as completed
- **Habit Tracking**: Add and track daily habits (exercise, water consumption, reading, etc.) and mark them as completed
- **Deletion**: Remove tasks or habits when they are no longer needed
- **Reports**: View progress reports for both tasks and habits on a weekly or daily basis


### Project Objectives

The main objectives include:

- Gain practical experience in developing Python applications with user input, loops, and conditionals
- Understand how to manage and manipulate data structures such as dictionaries and lists
- Learn to design and implement interactive user interfaces in command-line environments
- Develop deep understanding of code modularity and best practices


### Repository Structure

```
project_mparrondo/
├── Project_mparrondo.ipynb    # Main notebook with complete implementation
├── .gitignore                 # Git configuration file
└── README.md                  # This file
```


### Implemented Features

#### Part 1: Initial Setup

- List of days of the week
- Dictionary for habit tracking
- Dictionary for task storage by day


#### Part 2: Adding Tasks and Habits

- `add_tasks()` function: Allows adding tasks to specific days with input validation
- `add_habits()` function: Allows adding new habits with duplicate verification


#### Part 3: Mark as Completed

- `tasks_completed()` function: Marks tasks as completed with validation
- `habits_completed()` function: Marks habits as completed for specific days


#### Part 4: Deletion

- `remove_tasks()` function: Removes specific tasks from determined days
- `remove_habits()` function: Removes habits from the tracking system


#### Part 5: Reports

- `weekly_report()` function: Generates weekly summary of progress in tasks and habits
- `daily_report()` function: Shows specific activities for a day with visual indicators (✅/❌)


#### Part 6: Main Menu System

- Interactive main loop with 5 options:

1. Add Task or Habit
2. Mark as Completed
3. Remove Task or Habit
4. View Reports
5. Exit the program


### Technologies Used

- **Python 3**: Main programming language
- **Jupyter Notebook**: Interactive development environment
- **Git**: Version control
- **GitHub**: Remote repository and collaboration


### How to Use

1. **Clone the repository**:

```bash
git clone https://github.com/mparrondo/project_mparrondo.git
```

2. **Open the notebook**:
    - Run `Project_mparrondo.ipynb` in Jupyter Notebook or JupyterLab
    - Execute all cells sequentially
3. **Interact with the program**:
    - The system will display a main menu with numbered options
    - Follow the on-screen instructions to manage tasks and habits

### Evaluation Criteria

The project is evaluated based on:

- **Functionality**: Complete ability to add, remove, mark as completed, and generate reports
- **Code Organization**: Clear structure with meaningful variable names and appropriate use of functions
- **User Experience**: Ease of use with clear instructions, error handling, and appropriate feedback
- **Completeness**: Implementation of all described features without errors
- **Creativity**: User experience-oriented development with additional functionalities


### Version History

The project maintains version control with the following main commits:

- **Final submission version**: Complete final version of the project
- **Tasks 4, 5 and 6 completed**: Implementation of deletion, reports, and main menu
- **Create Project_mparrondo.ipynb**: Initial notebook creation
- **Initial commit**: Initial repository setup


### Contribution

This is an individual academic project developed by mparrondo as part of the ACENET program. The repository is configured as public for evaluation and demonstration purposes.

### License

Academic project - all rights reserved to the author.

---

*Developed as part of the ACENET project to demonstrate skills in Python programming and interactive application development.*

