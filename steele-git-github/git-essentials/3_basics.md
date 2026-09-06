## High-Level Conceptual Overview
- Repository (Repo) - A workspace that tracks and manages files within a folder. 
    - Does not happen on its own. It has to be initiated. 

## Our First Commands
- `git status` - Gives information on teh current status of a git repository and its contents. 
- `git init` - Creates a new git repository wherever you are in your terminal. 
    - You do this once per project in the top-level folder containing your project. 
## The Mysterious .git Directory
- This directory is hidden in your tracked folder. 
    - `ls -Force` - Shows all of the elements of a directory, hidden or not. 
- It is possible to delete this folder. 
    - Don't unless you absolutely need to. 

## A Common Early Git Mistake
- Need to understand: Git tracks a directory and all nested subdirectories. 
- Even if you are cd'ed into one of the nested folders, a `git status` will say that you are within that folder. 
- DO NOT INIT A REPO INSIDE OF A REPO!
    - If you are going to use `git init` make sure you are not within a repo already with `git status`. 
- Rule of Thumb: Make a folder for a project then do `git init` inside that folder. 
    - One repo per project. 

# Committing Workflow Overview
- `git commit` - A checkpoint in time of a repository that will have a message attached to it. 
    - Can go back to them, undo them, and much more. 
- A commit is not the same thing as saving a file. 
    - This has nothing to do with git. 
    - A save is just saving a single file, while a commit is saving a packages of changes within a repo. 

## The basic Git Workflow
- Work on project - Make new files, edit files, delete files, etc. 
- Add the changes (staging) - Group specific changes together, in preparation of committing. 
- Commit - Commit everything that was previously added. 

# Staging Changes With Git Add
 - Once you are done, you stage your changes to be commited by adding them. 
 - Working Directory - The place where you are actually working on your project. 
    - (learning-archive for our purposes.) 
- Staging Area - Where you add your changes to before you make a commit. 
- Repository - The contents inside the .git folder. This is where your commits are kept. 
- <b>Reminder</b>: `git status` to see what changes you have made. 
- `git add file1 file 2 etc` - Use git add to add specific files to the staging area. Separate files with spaces to add multiple at once. 

# How It Looks In Practice
- Work on your project
- `git add <file names (. = all files changed)>`
- Files from `git add` are in staging area.
- `git commit -m "message"` - Commits the files to the repository.
- Files are now in the repository. 

# Git Commit
- We use the `git commit` command to actually commit changes fromt he staging area. 
    - When making a commit, we need to provide a message that summarizes the changes and work snapshotted in the commit. 
- `git commit -m "message" <-- this is the syntax for committing. 
    - The -m flag allows us to pass in an inline commit message, rather than launching a text editor. 