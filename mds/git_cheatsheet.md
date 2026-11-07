# Git Cheatsheet

## Basics
```bash
git init                    # initialize a repo
git status                  # show current branch and file states
git add <file>              # stage a file
git add .                   # stage all files
git commit -m "msg"         # commit staged changes
git commit -am "msg"        # stage all modified tracked files + commit
git log                     # show commit history
git log --oneline           # compact history
git log --oneline --graph --all   # visual branch history
```

## File States
```
All files
├── Not modified
│   ├── Already tracked → do nothing
│   └── Never tracked   → git add + git commit
└── Modified
    └── git add + git commit
```

## Branching
```bash
git branch                  # list branches (* = current)
git branch <name>           # create a branch
git checkout <name>         # switch to a branch
git checkout -b <name>      # create + switch in one step
git diff master feature-1   # see difference between two branches
```

## Merging
```bash
git checkout master         # switch to branch you merge INTO
git merge <branch>          # merge branch into current
git merge --no-edit <branch>  # merge and accept default message
```

### Conflict rules
- Same file, different lines → no conflict, auto merged
- Same file, same line, only one branch changed → no conflict, takes changed version
- Same file, same line, both branches changed → CONFLICT, you decide

### Resolving a conflict
1. Open conflicted file, edit out the markers, keep what you want
2. `git add <file>`
3. `git commit`

## Rebase
```bash
git rebase master           # replay current branch commits on top of master
```
- Rebase = move your commits to start from a newer point
- Result: straight line history, no merge commit
- Never rebase a branch others are using

## Undoing Things
```bash
git restore <file>                # discard file changes (not staged)
git restore --staged <file>       # unstage file (keep changes)
git reset HEAD~1                  # undo last commit, keep file changes
git reset --hard HEAD~1           # undo last commit, DELETE file changes
git revert <hash>                 # new commit that undoes a previous commit (safe for pushed)
git commit --amend -m "msg"       # fix last commit message
git commit --amend --no-edit      # add forgotten file to last commit
```

### Reset vs Revert
- Not pushed yet → use `git reset` (rewrite history freely)
- Already pushed → use `git revert` (safe, preserves history for teammates)

## Fixing Mistakes
```bash
# Wrong branch commit → move it to correct branch
git reset HEAD~1            # on wrong branch: undo commit, keep changes
git checkout correct-branch
git add <file> && git commit -m "msg"

# Lock file error
rm .git/index.lock          # remove stale lock file

# Always use && not & between git commands
git add <file> && git commit -m "msg"   # sequential (correct)
git add <file> & git commit -m "msg"    # parallel (wrong!)
```
