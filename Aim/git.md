<!--==================-->
# Git
<!--==================-->
- `noautocmd w`

## _GIT CONFIG_
- [Git Config Defaults](https://spin.atomicobject.com/git-configurations-default/)

## _GIT MERGE_
- Call this cmd on the branch you want the other to be merged into (typically main)
  - Bring in the changes from the other to me (specified branch)

  ### Merge Conflicts
  - when you attempt to merge and fail, you remain in the merge state
  - `git status` gives you which files are conflicting
  - When you enter the file, it will be partitioned into 2.
  - `git merge (their section)`
    - Our section (refers to the branch you're on)
    - Their section (refers to branch being merged)
  - You can resolve conflicts 2 ways.
    1. go into the files with the conflicts and keep one source of truth, or if they are not conflicting, use both
      - commit while in the merging state
    2. Use the shorthand git checkout --(theirs/ours) (path to file with conflict)
      - this tells git to go inside the file and accept either their or your change(s)


## _GIT REBASE_
- Call this on the offshoots, the branches
- You are rebasing (changing the base) of these branches
  to something more modern

## _PULL REQUESTS_
- When working on a team, and you're requesting for your changes (usually on a branch) to be pulled into the main sacred timeline.
  - Pull not push. From your perspective, it's pushing. But pushing implies coercion and force. Pulling is a voluntary choice to accept which is more fitting in the cxt of a pull request.

## _GIT RESET_
- `git reset` undos
  - changes in idx (staging area)
  - past commmit(s)
  - worktree (unstaged, uncommitted)
- `--soft` flag
  - lets you keep your changes
  - committed -> becomes staged
  - uncommitted -> retains their staged/unstaged status
- `--hard` flag
  - deletes

- 🧪 `git reset --hard`
  - deletes all the changes in staging area to the last commit
- 🧪 `git reset --soft`
  - unstages all changes (but keeps changes in worktree)

* if you don't specify a [commit hash] as an argument, it uses the last commit by default

## _GIT REMOTE_
- In git, another repo is called a "remote." The standard convention is that when you're treating the remote as the "authoritative source of truth" (such as GitHub) you would name it the "origin".

By "authoritative source of truth" we mean that it's the one you and your team treat as the "true" repo. It's the one that contains the most up-to-date version of the accepted code.
