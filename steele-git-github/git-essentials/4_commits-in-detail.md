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


## Ignoring Files with .gitignore



