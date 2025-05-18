<!--==================-->
# Main Apps
<!--==================-->
- HYPRLAND (hypr)
- ZEN (zen)
- TMUX (tmux)
  - NVIM (nvim)
    - Telescope (tele)
    - Harpoon
    - Neogit
    - NNN

<!--==================-->
# Windows and Views
<!--==================-->
## OPEN/CLOSE
```yaml
<SUPERMAN q>: "[hypr] exit"
<SUPER .>: "[hypr] close window"
<ALT .>: "[zen] close pane/tab "
<_TMUX .>: "[tmux] close pane"

<SUPER f>: "[hypr] open foot terminal"
<SUPER b>: "[hypr] open browser"
<ALT t>: "[zen] new tab"
<_TMUX c>: "[tmux] new pane"
<_TMUX s>: "[tmux] new wintab"

# NVIM
<CTRL g | :q>: "quit buffer (reg, nnn, telescope, neogit)"
<ALT x>: "delete window/view"
```

## SIZING
```yaml
<SUPER spc>: "[hypr] fullscreen"
<_TMUX a>: "[tmux] fullscreen"

<SUPER (khtn)>: "[hypr] resize (left,down,up,right)"
<_TMUX ('you)>: "[tmux] resize (left,down,up,right)"
```

## MOVING
```yaml
<$SUPERMAN (khtn)>: "[hypr] move workspace (1,2,ref,term)"
```

## FOCUSING (CURSOR SHIFT)
- focusing is changing the cursor focus on the on the main, often persistent windows

```yaml
<SUPER tab>: "[hypr] toggle main workspace 1/2"
<SUPERMAN bspc | _QUICKFIRE a>:" [hypr] toggle special:terminal"
<SUPERMAN tab> | _QUICKFIRE o>:" [hypr] toggle special:reference"

<SUPER bspc>: "[hypr] toggle windows"
<CTRL tab>: "[zen] toggle tab"
<CTRL/_TMUX (1-6)>: "[zen] go to tab"
<ALT tab>: "[zen] toggle alt structure (workspace, panes)"
```

## VIEWS
- views are focusing and exposing a special workspace or window
- usually togglable

```yaml
#HYPR
## UTILITY VIEWS
<ZX h | _QUICKFIRE c>: "[hypr] clipboard" #history
<ZX spc | _QUICKFIRE i>: "[hypr] rofi emoji"
<ZX tab | _QUICKFIRE a>: "[hypr] rofi run"

<ZX m>: "[hypr] calculator" # math
<ZX s>: "[hypr] pavu sound" # sound

#NVIM
## UTILITY VIEWS
<CTRL j>: "[nvim/neogit]"

<LEADER u>: "[tele] undo-history search"
<LEADER c>: "[tele] clipboard-register search"
<LEADER gw>: "[tele] git who to blame search"
<LEADER gh>: "[tele] git hunks"

## WARP VIEWS
<LEADER n>: "[nvim/nnn]"
<ALT HOME>: "[nvim/harpoon] view"
<_QUICKFIRE s>: "[nvim/harpoon] add"
<ALT (1-6)>: "[nvim/harpoon] go to #"
<SPC_SPC (1-6)>: "[nvim/harpoon] go to #"

<LEADER t>: "[tele] tele-main file search"
<LEADER b>: "[tele] buffers search"
<LEADER s>: "[tele] find symbols"
<LEADER d>: "[tele] diagnostic search"
```

## HISTORY
```yaml
<ALT (left,right) (_QUICKFIRE e/o)>: "[zen, nvim] back/next history"
```

<!--==================-->
# Scouting
<!--==================-->
- scouting refers to navigation within a file

## SCROLLING
```yaml
<ALT s>: "[zell] enter scroll mode"
<CTRL h,t>: "[zen, zell, nvim] scroll down/up"
```

```yaml
#zen
<CTRL l>: "[zen]: go to url"
<t>: "[vimium]: go-to link"
<T>: "[vimium]: go-to link in new tab"
<z>: "[vimium]: bookmarks tab"
```

## NVIM
- bottom right of status bar shows total `curr_line | total_lines | curr_char | total_line_chars`
```yaml
# HISTORICAL MOVEMENT
<CTRL o/i>: old/itself jumps (arrow movements don't count as jumps)
<''>: toggle between last 2 cursor positions
<ALT left/right>: prev/next buffers

# VERTICAL MOVEMENT
<H,L>: "high/low"
<zz>: "center screen"
<#(jk)>: "relative jumping"
<:#>: "absolute jumping"

# BLOCK MOVEMENT
<{}>: "Move to empty space between blocks"
<()>: "Move to first line/ ending space between blocks"
<%>: "Move to matching brace"

# HORIZONTAL MOVEMENT
# --NOTE: it's hard to use f and ; where it's mapped on my kybd. My plan is to
#   spam the repeat key
<(#)|>: "absolute horizontal move"
<_>: "first written char of line"
<gM>: "center of chars"
<HOME/END>: "absolute first/last of each line"
<CTRL (left/right)>: "move word"
<wW,eE>: "beginning/end of word/Word"
<b/B>: "back to prev word/Word"
<f,F>: "move cursor on char"
<t,T>: "move cursor to char"
<;/, | ALT j/k>: "move to next/preceding char"

# SEARCH MOVEMENT
</>: "search by term"
<*>: "search all instances of current word"
<n/N>: "toggle next/prev of search"
<CTRL l>: "drop highlights" -- disabled it by default
```

<!--==================-->
# File Navigation NNN
<!--==================-->
```yaml
[1234]: Move to cxt [1234]
n[fdsh]: New [file/directory/symbolic link/hard link]
x: Delete
p: Copy to destination
<CTRL G>: Quit
v: Move to destination
r: Rename
.: Toggle hidden
e: Edit file
b[cn]: Go to preset bookmarks
a: Select all
A: Inverse selection
```


