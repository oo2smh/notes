<!--==================-->
# tldr;
<!--==================-->
- file structure loosely based off the unix default folder/file structure

<!--==================-->
# Folder Structure
<!--==================-->
1. bin
  * big-pic executables
2. etc
  * systems and config
  - keyboard shortcuts
  - setups
3. lib
  * details and supports bin_notes
  - pics, dict(ionaries), anki, etc
4. var
  * variable data
  - logs, scratch, backup, tmp

- optional `zip` folder in bin and lib for archived notes

<!--==================-->
# Formatting
<!--==================-->
## HEADERS_
- Header 1 will be separated by a frame
- Header 2 will be in UPPERCASE
  - This is to add visual distinction when notes are viewed from Github
- Header 3+ will be indented

## FILE PREFIXES
- Files will be prefixed and followed by a `-`
- This is an indicator as to what type of file the note is
  - `_` persistent files
  - `@` action file (typing exercises, questions)
    - requires active participation with notes
  - `kc` keymaps, commands to memorize
  - `ls` list note (ie: a list of problems)

## _TEMPLATES_
  ### Bin Sections
  1. tldr;
  2. references
  3. keys
  4. syntax* (opt)
  5. quests* (opt)

  ### Lib File Names
  - `bin_name++.md`: for the additional details
  - `bin_name.csv`: for anki and glossary
  - `ls_name`: lists of stuff. might not be directly tied to a bin_note

  ```
  bin
    - git.md
  lib
    - git++.md
    - git.csv
  ```

  ### Lib File++ Sections
  1. tldr;
  2. references
  3. keys
  4. syntax*
  5. socrates*
  6. this and that*


