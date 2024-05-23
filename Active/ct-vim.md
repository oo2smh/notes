<!---------------------->
# 📣 COMMANDS
<!---------------------->
## MODAL SHIFTS
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
# Can only enter the command mode from normal or visual mode
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
<none>: Operator Peding Mode (split moment when you type operator and comp is waiting for a motion)
<gh>: Select mode (created to make vim act more like conventional text editors. Avoid)

# in visual block mode <C-c> doesn't work as expected
```

## DIMENSIONAL SHIFTS
- Dimensions are the organizational nouns that exist within vim
- Windows, Buffers, Registers, Marks, Quick Fix List
```yaml
# WINDOWS
<C-w>(hjkl): Focus on window to left, down, right, up
<C-w>(c): Close the current window
(:vs): Vertical split
(:s): Horizontal split

# SPECIAL REGISTERS
=: Expression register
0: Yank register
": Unnamed register
*: System clipbaord
+: System Clipboard
```

## CURSOR SHIFTS (within a file)
```yaml
# A specific type of cursor shift is a motion. Motions are cursor shifts that
Motions are anything that moves the cursor. It can often be used with operator commands
# Used in Normal & Visual Modes
# Anatomy of a motion is (count)(motion)

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
# Relative movements in a line
0: beginning of line
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
H: High point of visual screen
M: Mid point of visual screen
L: Low point of visual screen
('mark): Jump to set mark
(m(char)): set mark with char name
(:num): go to line (num)
(numG): go to line (num)
gg: go to 1st line of file
G: go to last line of file

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

## COMMANDS
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
# separate selections used specifically as a range in place of a motion
# Anatomy: (range: ia)(selection)
# range refers to inner or around (including surrounding whitespace)
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
help [subject]: show help for a specific subject

## SPECIAL RANGE SPECIFICATIONS
(%): whole file
(.): current line
($): last line
(\): escape char
```

## INSERT MODE CMDS
```yaml
# Insert Mode Cursor Moves
<C-c>la:
<C-c>A: Move to end of line
<C-c>I: Move to beginning of line
<C-c>Bi: Move cursor to front of prev WORD

# OTHER INSERT MODE ACTIONS
<C-r>(reg): Paste from register
<C-r>(=): Perform an expression from a special register
<C-d>: Detab
<C-t>: Tab
```

## VISUAL MODE CMDS
```yaml
o: change cursor endpoint
gv: select last visual selection
```

<!---------------------->
# 👎 INCOMPATIBLE WITH CODERPAD
<!---------------------->
```yaml
# MOTIONS
H/M/L: High, Mid, Low
Ex cmds: Most ex cmds don't work
```
