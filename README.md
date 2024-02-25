git basics
==
Follow the videos at: https://git-scm.com/doc
You should end up with a repository, and files in it.

Cloning a repository
==
Clone a repository. I recommend *one* of:
- https://github.com/songlab-cal/tape
- https://github.com/molstar/pdbe-molstar

Can you see the commit history (with git log)?
Can you see the changes from a given commit (for example the last commit, with `git show -p HEAD`)?
can you open one of the notebooks ? (N.B. you may not be able to run them, depending on the packages used in the notebook)


Write a project: numbers_summer
==

Your task today is to write a full project, that fulfills the following task: sum the numbers in a file.
The way in which you accomplish the task is up to you, although I ask you to use git to keep track of changes you make

At the end you should have:
- a script that take in a file (of the users choice) and output the sum of the numbers written in said file.
- failure conditions, and how to respond to them, are left up to you: what happens if the file does not exist, or does not contain numbers?
- a data folder with a file that can be used to successfully run your program
- at least one test (preferrably more!)
- a git log that reflects the changes you made to accomplish the task.

Additional task: push this repository online.

N.B.: if you want to attempt a different / more ambitious task, you may do so, but I encourage you to do this first.

If you are stuck on how to get started, start with a simpler problem:
- write a program that print a file name, and attempts to open the file
- then change the program so that after opening the file, read the content, and count the number of characters
- then attempt to convert the file content to numbers
- finally, sum those numbers as you go. You are done!


Your own coursework project
==

Start organising the project based on what we have seen in today's class.
How will you answer the question? Where will you store the data?

As above, start with a minimal working example.
It doesn't need to do it all at the start!

Also, you could already write some tests!
What tests would need to pass for the project to be complete?