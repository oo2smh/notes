<!--==================-->
# 🔑 Keywords
<!--==================-->
## _BIGGER CXT_
```md
- Interface
  - Nested interface: Node repl inside of a terminal emulator
- Boot Program
- OS
- Kernel
- Shell
- Terminal
- Terminal Emulator
```
## _PERMISSIONS_
```md
0. root
1. user
2. group
3. other
- rwx
```
## _ENVIRONMENT_
```md
- Variables
  - PATH
- Executables
```

## _REPL_
```
- Repl
  - python repl
  - node repl
  - mysql repl
```

## _FILE SYSTEM_
```
- File System
- Absolute Path
- Relative Path
- Root Folder
- Home Folder
- Superuser
  - sudo
```

## _PROGRAMS_
```
- compiled
- interpreted
- stdout
- stdin
- stderr
- shebang
- packages
- package manager
- dependencies
- exit codes
```

<!--==================-->
# 📗 Dictionary
<!--==================-->
## _BIGGER CXT_
- *Interface* = General term referring to the mechanism in which to ctrl a given input. It also refers to what is available to the public versus what is made private. The public methods which are meant to be used is the interface. Private methods are abstracted away.
  - Cmd-line interface: Text-based interface
  - GUI: Graphical user interface. Mainly controlled with the mouse
  - TUI: Terminal user interface. Hybrid of 2. Attempt to bring simple graphics (boxes) into the terminal emulator
  - Voice-UI: Interface for programs like SIRI. Not as common as the other interfaces
- *Boot Program* = 1st program that boots/starts a computer
- *Operating System* = software that manages all other programs in the computer. Software that is connected o the hardware (memory). It is composed of the kernel, bootloader, and all other tools needed to manage the CPU
  - *Bootloader*: Program that starts the computer
  - *Kernel*: the heart of an OS. A program within the OS that has complete ctrl. 1st program to be run after the bootloader. Program that controls the resources of a computer and allocates it.
    - Peripheral management/connection
    - Network management
    - Memory management
    - CPU usage management
    - Processes (manages ps conflicts)
  - *Unix* = OP created in the 1970s and written in C
    - *Linux* = Unix-like OS. Open Source
    - *Mac OS* = Unix-like OS. Proprietary
  - *Windows*: = Microsoft Gui-based OS. Proprietary
  - *Mobile OS*: = OS for mobile phones
- *Shell*: Program that interprets/runs commands from your terminal/terminal emulator.
  - *sh*: The original shell program by Unix
  - *BASH*: Bourne-again shell. Improvement over sh
  - *ZSH*: Another flavor of a shell used by Mac OS

## _TERMINAL_
- *Terminal*: A physical computer/station connected to the hardware.Historically, the word "terminal" meant a physical device that you could type commands into, essentially a keyboard and a screen.
  - *TTY*: teletypewriter. devices that enable typing from a distance. Essentially these were what early terminals were.
- *Terminal emulators*: Hardware improvements have made physical terminals obsolete. Terminal emulators are softwares that emulate physical terminals. It allows for the control of the OS and other programs with keyboard cmds. Each instance of a terminal is called a tty.
- *Executables* = Programs that can be ran directly by your OS. Typically these files end in sh. Put the path of executables into your `PATH` env variable to allow these executables to be available globally. This means the executables can be ran regardless of where you are in the folder hierarchy.
- *Terminal Environment*: List of settings that can be referenced by programs
  - *PATH*: Variables are part of a terminal environment. PATH is a useful variable where the shell will look when you run an executable.
- *REPL*: A type of program that can read, evaluate, print and loop. The shell (bash, zsh) are repls. Many languages also provide REPLS such as the node, python, mysql repls.

## _FILE SYSTEM_
- *File System*: Way to manage/organize texts, programs in a hierarchy.
  - *File Path*: The address of each file/directory
    - Absolute: Exact coordinates starting from root (/)
    - Relative: Location determined relative to current position
- *Special Directories*
  - *Root directory*: (`/`)Topmost, global directory
  - *Home directory*: (`~`) Where personal files of each user lives. Each user has their own home directory
  - *bin*: binaries or scripts that can be ran
  - *sbin*: system binaries
  - *etc*: extra files that don't belong elsewhere
  - *tmp*: temporary files meant to be deleted
  - *usr*: refers to programs meant to be used by all users
  - *usr/local/bin*: binaries local to that specifric user


## _PROGRAMS_
> A program only understands 1s and 0s. 1s and 0s don't make much sense for humans. So humans created programming languages. The code that humans write in programming languages is called source code. The code that machines understand is called machine code. There are different ways to go from source --> machine code. Your computer's CPU hardware has been designed to execute machine code.
  - *Compiled*: A compiled program is a program that has been compiled from source to machine code. Source code is converted to machine code in its entirety by a program called the compiler. Compiled programs do not rely on any other program to be able to run/execute. Compiling = translating source code into machine code.
    - Languages like Go, C and Rust are compiled languages that produce compiled programs
  - *Interpreted*: An interpreted program is executed by another program called an interpreter and not directly by the CPU. The code is read by the interpreter as it's being ran.
    - Languages like JS, Python, sh are all interpreted languages.
    - [Compiled vs Interpreted](https://www.youtube.com/watch?v=KWsnpBsLV30)
- *Shebang*: Special line at top of scripts that tell your shell which program to use for execution
- *Exit Codes*: Programs return an exit code in the terminal to signify if they ran successfully or not. 0 means successfully ran. Any numerical code above 0 means there was an error.
- *STDOUT*: Standard output is the default place where programs print their output.
- *Standard Error*: Same as STDOUT, but for errors. Its stream is separate from stdout.
- *Standard Input*: Default place where programs read their input. Stream of data that programs can read as they run
- *Package*: 2 or more programs bundled together to perform some function.
- *Package Manager*: software that helps you manage packages (install, delete, update, manage dependencies)
  - brew (mac), pacman (arch), apt (ubuntu)
- *Dependencies*: Programs/other packages that are needed for your package to function properly

