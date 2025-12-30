# 🐧 Tldr
- **WHAT**: interface to use the _shell_ (program used to talk with OS)
  - resources manager
    - memory, processes
  - pkg management (install, delete, manage dependencies)
  - file and folder
- **WHY**: GUIs exist, but text-based interfaces (ie: terminal) are faster and more powerful
- **HOW**: Shell is a program like any other. It lives in `/usr/bin/bash`. Terminal simply provides a way to connect to the shell.

# 🔑 Keywords
## _BACKBONE_
- Background Info
- Language Basics
- File systems
- Permissions

## _BACKGROUND_
- interface
  - GUI (ui/visuals based)
  - terminal (text-based)
  - REPL
  - terminal emulator
- shell (program that uses the terminal to talk with os)
- sessions
- compiled vs interpreted
- UNIX philosophy
  - each program does 1 thing only
  - KISS
- pkg and pkg manager

## _LANGUAGE BASICS_
### Variables
  - prefixed with $
    - $PATH, $HOME, $USER, $SHELL, $PS1/2, $? (exit status var)

  ### Similar DNA?
  - shell uses a basic language (bash), however it has the basic structure of other prog lang
    - ctrl flow (conditionals, looping)
    - functions
    - arrays
    - error manangement

  ### Persistent Config
  - .bashrc
    - aliases
    - environment var
  - scripts
    - shebang (`#!`): special line at the top of a script that tells your shell which program to use to execute the file

  ### Cmd Anatomy
  - program [options] <args>
    - options have 2 forms
      * boolean on/off options = flags
      1. abbrev (-l)
      2. long form (--long)
    - args are positional. Order matters!

  ### I/O: Data Streams
  - Stream? Ephemeral data that exists only for the lifetime of a cmd
    - `STDIN (0)`, `STDOUT (1)`, `STDERR (2)`
  - most cmds expect an input (stdin)
  - most cmds output to `STDOUT`
    - usually this is simply echoed to the terminal
    * but you can redirect the output to another cmd (chaining)
  - error codes (0 = success, !0 = error (ie: 1 = general err))
    - last error code

  ### Redirection
  - most cmds, produce an output and an error code
    - typically, the output is echoed
    - errors are attached to numbers. And if there's an error, the msg is raised (!0)
  - However, you can REDIRECT the output
    - To a file (OUT: `>, >>`, ERR: `2>, 2>>`)
    - To another cmd (`|`)

## _FILE SYSTEMS_
- root (/)
- home (~)
- relative (. ..) vs absolute
- executables (file type)
- Default (out-of-the-box)
  - Executables binaries
    - /bin (symbolic)
    - /sbin (symbolic)
    - /usr/bin (hard)
    - /usr/sbin (symbolic)
  - Startup and core
    - /boot
    - /dev (devices)
    - /proc
  - Other
    - /etc
    - /var
    - /tmp

## Permissions
- rwx
- users
  - root, group, others

# 👊🏻 Syntax
## _RESOURCES MANAGEMENT_
- ps
  - kill
- top (mem , cpu-usage)

## _INFO_
- man
- which
- echo
- cat
- history
- less

## _FILES/DIRECTORIES_
  ### Manipulation
  - touch
  - mkdir
  - cp
  - rm
  - mv

  ### Navigation
  - ls
  - cd

  ### Search
  - find
  - grep

  ### _PERMISSIONS
  - ls -l
  - chown
  - chmod
  - sudo

## _OTHER_
- sed
- awk
- ssh
- curl
