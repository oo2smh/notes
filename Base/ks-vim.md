<!--==================-->
# 📣 Shorthands
<!--==================-->
## _MODAL SHIFTS_
> [!Note]
> The main vim modes are `Insert` and `Normal`. In `Visual Block Mode` if you press `i` and make a change, it will make that change in all the lines the cursor is active. However, if you cancel with `<C-c>` in visual block mode, it will not do that. To escape out `Visual Block Mode` use the other 2 keyboard shortcuts instead (`Esc` or `<C-[>`.

```yaml
# TO NORMAL
<C-c>: Cancel
<Esc>: Cancel
<C-[>: Cancel

# TO INSERT
# Enter insert mode...
<i>: Before cursor
<I>: Beginning of line
<a>: After cursor
<A>: End of line

# TO COMMAND (:)
# Enter cmd mode from normal/visual
<:>: Type colon followed by command
</>: Used to search a phrase

# TO VISUAL MODE
v: Visual-char mode
<S-v>: Visual line
<C-v>: Visual block mode
<C-q>: Visual block mode

# OBSCURE MODES
<C-o>: Normal-insert mode
<S-r>: Replace mode
<none>: Operator Peding Mode
<gh>: Select mode
# in visual block mode <C-c> doesn't work as expected
```
## _DIMENSIONAL SHIFTS_
> `Dimensions` are the organizational nouns that exist within vim. This term isn't officially endorsed by vim, but I coined it to chunk together the different entities/nouns that exist within vim. Some of these include windows, buffers, registers, marks, and the quick-fix list.

```yaml
# WINDOWS
<C-w-[hljk]>: Focus on window to left, down, right, up
<C-w-c>: Close the current window
(:vs): Vertical split
(:s): Horizontal split

# SPECIAL REGISTERS
(=): Expression register
(0): Yank register
("): Unnamed register
(*): System clipbaord
(+): System Clipboard
```

## _CURSOR SHIFTS_
> Navigation is a big part of vim. It might be vim's biggest selling point. `Motions` is a loaded word defined slightly different depending on who you ask. I define it as anything that moves the cursor and can be used with operator commands. An anatomy of a motion is `(count)(motion)`. There are cursor shifts search as `Search` and `Scroll` actions which are not used with operators.

> [!Tip]
> The main types of navigation are horizontal and vertical movements. Try to be efficient and get as close to your target with the fewest amount of keystrokes. Using the count can be helpful as well, but might not be worth the mental overload. Generally, it's advisable to use the relative movements `0$gM` for horizontal or `HML` for vertical movements and then navigate to your code. If the code is outside of the visible screen use `<C-d>` `<C-u>` to scroll down. Alternatively, you can use marks, `*/#` and/or `/(searchWord)` to navigate out of the screen.

```yaml
# Used in Normal & Visual Modes

# SIMPLE MOTION (1 char movment)
h: left 1 ('hatchback')
j: down 1 ('judo')
k: up 1 ('kite')
l: right 1 ('lunge')

# WORD-WISE MOTIONS (horizontal movement)
w/W: beginning of next word/WORD
e/E: end of word/WORD
ge/gE: previous end of word/WORD
b/B: previous beginning of word/WORD
f/F: to next/prev char in line
t/T: to next/prev char before search-char in line
(;): next f/F or t/T match
(,): previous f/F or t/T match

# HORIZONTAL RELATIVE MOTIONS
(0): beginning of line
^: first non-space char of line
$: last char of line
g_: last non-space char of line
gM: middle of line with characters
gm: middle of screen total width if not, goes to end of char

# VERTICAL MOTIONS
(%): Jump to matching delimiter (cursor must be on delimiter)
(*): Jump to next cursor match
(#): Jump to previous cursor match
(n/<S-n>): jump to next/prev cursor match
<S-]>: next island gap (island = any text surround by blank line)
<S-[>: prev island gap
<S-)>: next sentence or (1st line of island and island end-gap)
<S-(>: prev sentence or (1st line of island and island end-gap)

# VERTICAL RELATIVE MOTIONS
H: High point of visual screen
M: Mid point of visual screen
L: Low point of visual screen
gg: go to 1st line of file
G: go to last line of file

# VERTICAL PRECISE MOVEMENTS
('mark): Jump to set mark
(m(char)): set mark with char name
(:num): go to line (num)
(numG): go to line (num)

# SCROLLS
<C-e>: Scroll 1 line down
<C-y>: Scroll 1 line up
<C-d>: Scroll 1 page down
<C-u>: Scroll 1 page up
<zt>: Shift current cursor position to top of visible screen
<zz>: Shift current cursor position to middle of visible screen
<zb>: Shift current cursor position to bottom of visible screen

# SEARCH
/(pattern): Jump to next word
n/<S-n>: Jump to next/prev highlighted word
```

## _COMMANDS_
> Other than inserting, commands are the way to perform actions in vim. Actions include text manipulation (deletion, replacing, adding lines, formatting, copying, etc). There are generally 3 types of commands avaiable. The first is a simple command which has the anatomy of `(count)(cmd)`. The next type of command is an operator with the anatomy of `(count)(cmd)(motion)`. Lastly, the ex commands are prefixed with a `:`. These are for long-range actions. Many if not all of the operations can be done file-wide.
<!--~~~~~~~~~~~~~~~~~~-->

```yaml
# SIMPLE
# Anatomy of simple commands is (count)(cmd)
<C-a>: Increment number by 1
<C-x>: Decrement number by 1
r: Replace
x: delete a char
.: repeat cmd
J: join line
o/O: Add a following/preceding line

# OPERATORS
# When you double an operator, it affects the line
# Anatomy: (count)(operator)(motion)
d: Delete
c: Change
y: Yank
p: Paste
gU: Uppercase
gu: Lowercase
=: auto-indent
gw: wrapping
~: Toggle Alphabet case
(<): Shift left
(<<): Indent left
(>): Shift right
(>>): Indent right

# TEXT OBJECTS
# can be used in place of a motion
# Anatomy: (range: ia)(selection)
# range refers to inner or around
# selections are listed below
w: word
s: sentence
p: paragraph
t: tag
B: block
('"}): delimiters

# EX
# all ex commands start with (:)
w: write
q: quit
q!: quit without saving changes
x: write changes and quit
s: substitute
m: move
e: open/edit a file
!(cmd): execute a shell cmd
set: set an option
set tw=0: set text-width = 0 (use in md files)
help [subject]: show help for a specific subject

## SPECIAL EX RANGE SPECIFICATIONS
(%): whole file
(.): current line
($): last line
(\): escape char
```

## _INSERT MODE CMDS_
> Sometimes instead of going out of `Insert Mode` to move the cursor or delete a char/word. Luckily, vim provides common actions you can take without having to leave insert mode. I also added certain combos that chain multiple vim commands for common actions. It's easier to think of these combos as its own chunk.

```yaml
# Insert Mode Cursor Moves
<C-c>la: Move cursor to the right 1 char
<C-c>A: Move to end of line
<C-c>I: Move to beginning of line
<C-c>Bi: Move cursor to front of prev WORD

# OTHER INSERT MODE ACTIONS
<C-r>(reg): Paste from register
<C-r>(=): Perform an expression from a special register
<C-d>: Detab
<C-t>: Tab
```

## _VISUAL MODE CMDS_
```yaml
o: change cursor endpoint
gv: select last visual selection
```

<!--==================-->
# 👎 Incompatible With Coderpad
<!--==================-->
```yaml
# MOTIONS
H/M/L: High, Mid, Low
i(C-w, C-h): Insert specific delete shorthands
Ex cmds: Most ex cmds don't work
```
