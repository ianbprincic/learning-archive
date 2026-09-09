## Git Documentation
- Available at git-scm.com
    - Find the Documentation section. 
- Might be helpful to have these sometime. 

## Keeing Your Commit Atomic
- When possible, a commit should encompass a single feature, change, or fix. 
    - In other words, try to keep each commit focused on a single thing. 
- This makes it much easier to undo or rollback changes later on. It also makes your code or project easier to review. 
- People will appreciate this. 

## Writing Commit Messages
- Use present-tense imperative style.
    - Describe your changes in imperative mood, e.g. "make xyzzy do 'this thing'" instead of "'This patch' makes xyzzy do 'this thing'".
        - As if you are giving orders to the codebase to change its behavior. 
- Sometimes it makes sense to say it in the past tense. Follow repo conventions. 
- Make sure first line is a brief summary and anything else is separated by a return. 

## Deeper Look At Git Logs
- `git log --abrev-commit` - Makes the commit hash much shorter in your git logs. 
- `git log --oneline` - Makes your abbreviated hash and commit messages on a single line. 
    - Much easier to read and nice way to look at the history. 

## Fixing Mistakes With Amend
- This only works for amending your last commit. 
- Supposed you just made a commit and then realized you forgot to include a file. 
- Or, maybe you made a typo in the commit message that you want to correct. 
- Rather than making a brand new separate commit, you can "redo" the previous commit using the `--amend` option. 
- Ex
    - `git commit -m "some commit"`
    - `git add forgotten_file`
    - `git commit --amend` <-- opens up the previous commit message where you can edit it in your IDE
        - Make your change, save, and close. 

## Ignoring Files with .gitignore
- We can tell git which files and directories to ignore in a given repository, using a .gitignore file. 
- This is useful for files you NEVER want to commit, including:
    - Secrets, API keys, credentials, etc. 
    - Operating System files (.DS_Store on Mac)
    - Log files
    - Dependencies and Packages. 
- Create a file called .gitignore in the root of a git repository. Inside the file, we can write patterns to tell git which files & folders to ignore:
    - .DS_Store will ignore files named .DS_Store
    - folderName/ will ignore an entire directory
    - *.log will ignore any files with the .log extension. 



