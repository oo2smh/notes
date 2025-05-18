<!--==================-->
# Commands
<!--==================-->
## _CORE LINUX_
```md
# File System
cd
ls
cp
mv
rm (-rf)
touch
mkdir
pwd

# Search & Info
man
cat
head/tail
find
grep

# Permissions
whoami: ls user
chown: change file ownership
chgwn: change group ownership
chmod (-ugo)(+/-[rwx]): change file permissions
sudo: super user do
ls -l

# Process Management
ps: display running ps
top: monitor sys ps in real dtime
kill: terminate a process
pkill: terminate ps based on name

# Network
curl

# Info
df: show disk space usage
free (-h): display memory usage info
uptime: show system uptime

# Redirection of Stout
pipe (|)
write (>)
append (>>)
```
## _USER ADDED_
```md
# Files/Folder
curl
bat
fd

# Package Manager
paru = searches AUR (arch user repo)
pacman = searches only the official arch supported pkgs
pip = python pkg manager
npm = node pkg manager

pacman -Q: query all packages (includes dependencies)
pacman -Qe: ls explictly installed pkgs
pacman -Qdt: ls unneeded pkgs
pacman -Syu: update everything
pacman -S <pkg>: install only
pacman -Rsu <pkg>: uninstall pkg along w/ dependencies
pactree <pkg>: dependencies of pkg
paru <pkg>
```

