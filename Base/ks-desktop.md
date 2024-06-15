<!--==================-->
# 🔑 COMMANDS
<!--==================-->
> W = Super Key, A = Alt, C = Ctrl, S = Shift. `[abc]` = Char class shorthand syntax. For instance <C-[abc]> means <C-a>, <C-b> and <C-c> are all valid commands

## HYPR
```yaml
<CS-[hjkl]>: Move window focus (left/down/up/right)
<AS-[hjkl]>: Move window (left/down/up/right)
<W-Q>: Close Window
<WS-[hl]: Resize window (left/right)
<W-F>: Toggle fullscreen

<CS-[qweas]>: Go to workspace [q=1, w=2, e=3, a=4, s=5]
<AS-[12345]>: Move window to workspace [12345]

# SCRATCHPADS
<W-Space>: Toggle terminal scratchpad
<W-0>: Toggle reference scratchpad

# SCREENSHOTS
<WS-3>: Screenshot region and save to clipboard only
<AS-3>: Screenshot region and save to file
<WS-2>: Screenshot region and open annotation screen

# NEW INSTANCE
<WA-B>: Open Browser
<WA-Space>: Open Terminal
<WA-n>: Oven pavucontrol(sound/noise gui) #n = noise

# MISC
<CS-X>: Toggle app launcher
<CS-9>: Toggle clipboard history
<CS-7>: Toggle hyprshade
<WA-d>: Close dunst(notification daemon) popup
```

## TERMINAL
These are the default terminal shortcuts regardless of which terminal emulator you chooose to use

```yaml
<C-l>: Clear screen
<C-a>: Go to beginning
<C-e>: Go to end
<C-c>: Cancel
<C-u>: Clear current line
<C-h>: Delete char
<C-w>: Delete from cursor the word beginning
!!: Repeat last command
Tab: Show autocomplete options (Tab to cycle between options)
```

## ZELLIJ
The main modifier for zellij is `ALT`. As others have noted using `CTRL` conflicts with some of the vim keybindings. Although zellij is feature rich, I will only use a small subset of the commands to reduce mental overhead. Commands listed here aren't comprehensive, but simply list the most used commands.

I will use zellij with 3 main modes. Normal (default), Lock (to turn off zellij keybindings in case of keybinding conflicts), scroll

> [!Tip]
> You can create `panes` in zellij which in essence functions the same as a desktop window. I have a separate keyboard shortcut mapped to creating a new pane, however, it feels redundant to use both windows and panes. Prefer windows over panes as it's less things to remember. When you want to create a new terminal window, you can use <WC-Space>. Or better yet, you can use <CS-n> to create a new instance window of whatever window you're focused on at the moment. The only downside to this is that the newer window is not saved into that session, but as a separate session. This is a tradeoff that I am willing to live with since at the moment I don't use sessions that much.

```yaml
# GENERAL
<C-d>: Closes terminal instance/window
<A-z>: Lock mode
<A-a>: Normal mode
<A-s>: Scroll mode
<A-f>: Toggle Float

<A-n>: New pane
<A-t>: New tab

<A-w>: Closes window (<C-d> alternative)
<A-[hjkl]>: Focus [left/down/up/right]
<A-[1234]>: Go to tab [1234]
<A-[=-]>: Resize [right/left]

# SCROLL
<C-d>: (In Scroll mode) Scroll down 1/2 page
<C-u>: (In Scroll mode) Scroll up 1/2 page
<C-e>: (In Scroll mode) Scroll down 1 line
<C-y>: (In Scroll mode) Scroll up 1 line

# SESSION
<A-o>: Session/Owl mode
<d>: Detach
<w>: Session Manager
```

## NNN
```yaml
[hjkl]: [left,down,up,right]
[1234]: Move to cxt [1234]
n[fdsh]: New [file/directory/symbolic link/hard link]
x: Delete
p: Copy here
v: Move here
r: rename
.: Toggle hidden
e: Edit file
Space: Select
a: Select all
A: Inverse selection
```

