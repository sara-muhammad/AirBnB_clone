AirBnB Clone
The goal of this project is to deploy on our server a simple copy of the AirBnB website.

We won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

Our application will be composed by:

A command interpreter to manipulate data without a visual interface, like in a Shell
A website that shows the final: static and dynamic
A database or files that store data
An API that provides a communication interface between the front-end and our data
Environment
Suite CRM terminal python Suite CRM Suite CRM git distributed version control system Github

Style guidelines:
pycodestyle (version 2.8.0)
PEP8
All the development and testing was runned over an operating system Ubuntu 20.04 LTS using programming language Python 3.8.3. The editors used were VIM 8.1.2269, VSCode 1.6.1 and Atom 1.58.0 . Control version using Git 2.25.1.

Installation
git clone https://github.com/aysuarex/AirBnB_clone.git
change to the AirBnb directory and run the command:

 ./console.py
Execution
In interactive mode

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
in Non-interactive mode

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
Testing
All the test are defined in the tests folder.

Documentation
Modules:
python3 -c 'print(__import__("my_module").__doc__)'
Classes:
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
Functions (inside and outside a class):
python3 -c 'print(__import__("my_module").my_function.__doc__)'
and

python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
Python Unit Tests
unittest module
File extension .py
Files and folders star with test_
Organization:for models/base.py, unit tests in: tests/test_models/test_base.py
Execution command: python3 -m unittest discover tests
or: python3 -m unittest tests/test_models/test_base.py
run test in interactive mode
echo "python3 -m unittest discover tests" | bash
run test in non-interactive mode
To run the tests in non-interactive mode, and discover all the test, you can use the command:

python3 -m unittest discover tests
Usage
Start the console in interactive mode:
$ ./console.py
(hbnb)
Use help to see the available commands:
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
Quit the console:
(hbnb) quit
$
Commands
The commands are displayed in the following format Command / usage / example with output

Create
Creates a new instance of a given class. The class' ID is printed and the instance is saved to the file file.json.

create <class>
(hbnb) create BaseModel
(hbnb)
Show
show <class> <id>
(hbnb) show BaseModel 
Destroy
Deletes an instance of a given class with a given ID. Update the file.json

(hbnb) create User
(hbnb) destroy User 
(hbnb) show User 
** no instance found **
(hbnb)
all
Prints all string representation of all instances of a given class. If no class is passed, all classes are printed.

(hbnb) create BaseModel
(hbnb) all BaseModel
count
Prints the number of instances of a given class.

(hbnb) create City
(hbnb) count City
update
Updates an instance based on the class name, id, and kwargs passed. Update the file.json

(hbnb) create User
(hbnb) update User 
(hbnb) show User