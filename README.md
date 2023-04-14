[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10869820&assignment_repo_type=AssignmentRepo)
## Assignment
Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 

The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

## Starter Code
```python
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
```

## Desired Output
```
cwen@iupui.edu 5
```

## Test
Run `pytest` in the terminal when you think your code is complete!
