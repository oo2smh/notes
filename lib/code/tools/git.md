# 🐧 Tldr
- **What**: VCS that takes snapshots. Undo-tree.
- **Why**: To manage history. Track history. Safety-net against disastrous changes.
- **How**: Internal plumbing cmds which are abstracted into porcelain cmds.It stores data as objects and creates a unique SHA-1 identifier (commit id). All the changes are linked to the unique SHA-1 hash and saved.

## *SUMMARY*
Git is a vcs system that tracks history through `SHA`. SHA creates a unique id that lets you reference each snapshot. Many actions can be taken such as saving, viewing, altering, and rearranging snapshots.

# 🫧 Analogy
> 👷🏻 This is you! Your 🏢 (company) has given you a 👨🏻‍💼 (secretary) to help you track your work/be more organized! 👨🏻‍💼 is called Git. Git sets up a station in your office 🗄️ (`.git`)
- Your workstation is a table called a `worktree` 🌲
- Once you are satisfied with some of your work, you put the changes to the `index` tray 📤. Then stamp it to `commit`
  - 👨🏻‍💼 Git grabs the commit, creates a unique identifier through SHA, and sticks the SHA id onto the changes.
  - 👨🏻‍💼 It then stores the commits into the `objects` drawer of the filing cabinet
- Occasionally, you want to `branch` and work on a new idea. You need working space. Both your table and `index` tray must be empty! Solutions?
  1. Stash changes! Take a picture of your worktree. And put files onto a stash folder. After your current work is done, look at the picture and put table the way it was before
  2. Work on the other changes on a new worktree (aka table and 📤)
- This system allows you to view, change, rearrange past history. It also keeps a historical log of your changes
- 👨🏻‍💼 visits table and compares changes to previous commit. You can tell Git not to track a file. This is the file state (tracked vs untracked). You can also tell Git to completely ignore certain files on your worktree `.gitignore`.

# 📘 References
- [Boot.Dev](https://www.boot.dev/tracks/backend)
- [States of Files](https://www.boot.dev/lessons/f330368c-734c-4708-971b-2ad33b4b7f52)
# 🔑 Keywords
## _.GIT FILE STRUCTURE_
~~~python
.git/
├─ ORIG_HEAD # prev head pointer before major change
├─ HEAD # 🚧 current pointer
├─ config
├─ worktrees
├─ index # 📤
├─ COMMIT_EDITMSG # latest commit message
├─ FETCH_HEAD # reference file that records what was last fetched
├─ hooks/ # scripts to run pre/post certain git actions
├─ .gitignore
├─ info/
│   └── exclude # personal gitignore
├── logs/ # 📜 historical log
│   ├─ HEAD                # Tracks `HEAD` movements (current branch history)
│   ├─ refs/
│   │   ├── heads/
│   │   │   ├── main       # Tracks commits to the `main` branch
│   │   │   ├── feature    # Tracks commits to the `feature` branch
│   │   ├── remotes/
│   │   │   ├── origin/
│   │   │   │   ├── main   # Tracks remote `origin/main` history
│   │   │   ├── upstream/
│   │   ├── reflog          # Records all reference changes (HEAD, branches)
│   ├─ .gitignore
├─ objects/ # stores delta of files here, also commits
│   ├─ info/
│   └─ pack/   # storage of git objects in a compressed format
├─ refs/
│   ├─ heads/
│   ├─ tags/
│   └─ remotes/
└─ packed-refs # way to optimize storing refs by "packing them"
~~~

## _CHANGE LIFECYCLE_
- working directory
- index (file)
- commit (stored in 📁 objects)

## _FILES STATE_
> Both staged/unstaged files will have a prefix descriptor of A or M describing if it had been 1st added or modified

- untracked ❌
- tracked (??) ✅
  - unstaged 🦨
  - staged 💄
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

# 🥊 Syntax
> All cmds should be prefixed with git

## _PLUMBING CMDS_
```yaml
- cat-file [-p]
- hash-object
- apply
- commit-tree
```

## _SETUP AND CONFIG_
```yaml
- init
- config [-l(ist), --add, --unset, --unset-all]
```

## _CMDS:INFO_
```yaml
- man
- status [-s(hort), -v(erbose)]
- show
- log
- reflog
- diff
- tag [-a, -m]
```

## _CMDS:BRANCHING_
```yaml
- branch (-d)
- switch (-c)
```

## _CMDS:GRAFTING_
```yaml
- merge
- rebase
- checkout (--ours/--theirs)
```

## _CMDS:HISTORIAN_
```yaml
- revert
- reset (--soft, --hard [--mixed])
- restore (--staged)
- rebase -i
```

## _CMDS:REMOTE_
```yaml
- remote
- clone
- push
- pull
- forking
- upstream
```

## _CMDS:PLUCKING_
```yaml
- cherry-pick
- stash
- bisect
```
