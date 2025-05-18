<!--==================-->
# Actions Overview
<!--==================-->
- these include other commonly actions (cut, copy, paste), screenshot, etc
- not comprehensive

<!--==================-->
# Bottom Row Essentials
<!--==================-->
```yaml
<C [cv]>: "[hypr, zen]: system clipboard copy, paste"
<C x>: "[!nvim]: system clipboard cut"
<C z>: "[!nvim]: undo"
```

<!--==================-->
# Other Keys
<!--==================-->
```yaml
<_QUICK_FIRE ['/y]>: "adjust volume"
<_QUICK_FIRE [u/#]>: "screenshot clipboard/file"

# Visual Change
<CTRL_ALT b>: "[hypr] toggle waybar"
<CTRL_ALT n>: "[hypr] toggle nightlight"
```

## VIDEO SPEED CONTROLLER
```yaml
(<): decrease speed
(>): increase (strengthen) speed
(v): view controller
(r): reset
(p): preferred speed (1.5)
```

<!--==================-->
# Text Edit (NVIM)
<!--==================-->
## GENERAL
```
- Delete Word (QMK)
  - Use CTRL_BSPC
  - Terminal/Nvim (Ctrl W)
- Delete Line (QMK <CTRL l> _ARROW_NUMPAD)
- BSPC
- TAB
```

## VIM DEFAULTS
```yaml
## BIG CHANGES
<i/I/a/A, v/V/<C-q>, :, ESC>: Mode Shifts
<dscrx>: Delete operations
<yY,pP,gpP>: "Yank and paste"
<:(range)s//g)>: "Ex substitute"
<:(range)norm (macro)>: "runs a macro over the range. Macros can be named (prefixed with @, ie: @t) or you can create an anonymous macro here"

## SMALL REFINEMENTS
<oO>: "Add a line"
<.>: "Repeat action"
<~, gu, gU>: "Captialization"
<C (xa)>: "Increment/decrement"
<J>: "Join line"
<gx>: "Open markdown link"
<gv>: "Select the last visual selection"

### BLOCK FORMATTING
<(<,>,=), (<C d>, <C t> normal_mode only) >: "Indentation"
<gw): "wrapping"
``

  ### Text Objects
- prefixed with i/a (in/around) `ie: iw, ap`
```yaml
w: word
s: sentence
p: paragraph
t: tag
('"[(}): delimiters
```

  ### SPECIAL EX RANGE SPECIFICATIONS
- use with substitution ln:45
```yaml
('<,'>): current visual selection
(%): whole file
(.): current line
($): last line
(\): escape char
```

## NVIM SPECIFIC CONFIGS
  ### Surround
```yaml
# SELECT line 1st, by default single word
<leader>(",',`,(,{,[)>: Surround word
```

  ### Other
```yaml
# INLINE INFO
<leader>gw: preview git hunk
<leader>dl: diagnostic line

# NICHE
<leader>r: rename function
<leader>fd: file diagnostic
<leader>mp: make pretty select lines
<S space>: treesitter incremental selection
<leader>j: jump to declaration
```

