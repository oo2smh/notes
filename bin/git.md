# 🐧 Tldr
- **What**: Version control system that takes snapshots. Undo tree.
- **Why**: Manage history. Undo past work. Safety net against unwanted changes.
- **How**: Internal plumbing cmds which are abstracted into porcelain cmds.It stores data as objects and creates a unique SHA-1 identifier (commit id). All of the changes are linked to the unique SHA-1 hash and saved.

# 📘 References
- [Boot.Dev](https://www.boot.dev/tracks/backend)
- [States of Files](https://www.boot.dev/lessons/f330368c-734c-4708-971b-2ad33b4b7f52)
# 🔑 Keywords
## _.GIT STRUCTURE_
~~~ md
.git/
├── HEAD
├── config
├── worktrees
├── index
├── .gitignore
├── COMMIT_EDITMSG
├── FETCH_HEAD
├── ORIG_HEAD
├── hooks/
├── info/
│   └── exclude
├── logs/
│   ├── HEAD                # Tracks `HEAD` movements (current branch history)
│   ├── refs/
│   │   ├── heads/
│   │   │   ├── main       # Tracks commits to the `main` branch
│   │   │   ├── feature    # Tracks commits to the `feature` branch
│   │   ├── remotes/
│   │   │   ├── origin/
│   │   │   │   ├── main   # Tracks remote `origin/main` history
│   │   │   ├── upstream/
│   │   ├── reflog          # Records all reference changes (HEAD, branches)
│   ├── .gitignore          # Ignores specific logs if necessary
├── objects/
│   ├── info/   #
│   └── pack/   # storage of git objects in a compressed format
├── refs/
│   ├── heads/
│   ├── tags/
│   └── remotes/
└── packed-refs
~~~

## _CHANGE LIFECYCLE_
- working directory
- index (file)
- commit (stored in 📁 objects)

## _FILES/FOLDER STATE_
> Both staged/unstaged files will have a prefix descriptor of A or M describing if it had been 1st added or modified

- untracked
- tracked (??)
  - unstaged
  - staged
  * descriptors
    - added (tracking for 1st time) (A)
    - modified (contents changed)(M)
- committed

## _REMOTE_
- fork
- upstream (branch)
- merge conflict
- base commit
- parent commit

## _CMD MODES_
- normal mode
- merge, rebase, stash, bisect

# 👊🏻 Syntax
> All cmds should be prefixed with git

## _PLUMBING CMDS_
- cat-file [-p]
- hash-object
- apply
- commit-tree

## _SETUP AND CONFIG_
- init
- config [-l(ist), --add, --unset, --unset-all]

## _CMDS:INFO_
- man
- status [-s(hort), -v(erbose)]
- show
- log
- reflog
- diff
- tag [-a, -m]

## _CMDS:BRANCHING_
- branch (-d)
- switch (-c)

## _CMDS:GRAFTING_
- merge
- rebase
- checkout (--ours/--theirs)

## _CMDS:HISTORIAN_
- revert
- reset (--soft, --hard [--mixed])
- restore (--staged)
- rebase -i

## _CMDS:REMOTE_
- remote
- clone
- push
- pull
- forking
- upstream

## _CMDS:PLUCKING_
- cherry-pick
- stash
- bisect
