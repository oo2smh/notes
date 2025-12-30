# DOTFILES
- rofi
- nvim
- hypr
- foot
- .tmux
- waybar
- .bashrc
- qmk

# PACKAGES
## 🧱 System / Boot / Kernel / Drivers
- base-devel	Essential dev tools
- amd-ucode	AMD CPU microcode updates
- linux	Kernel
- linux-headers	Kernel headers
- dkms	Kernel module builder
- v4l2loopback-dkms	OBS Virtual camera module
- efibootmgr	EFI boot manager
- grub-btrfs	GRUB snapshot integration for Btrfs
- zram-generator	Creates compressed swap devices in RAM
- sof-firmware	Firmware for audio devices

## 🔌 Audio / Sound
- alsa-utils 🔊	ALSA audio tools
- pipewire	Audio server
- pipewire-alsa	ALSA backend for PipeWire
- pipewire-jack	JACK backend for PipeWire
- pipewire-pulse	PulseAudio backend for PipeWire
- pavucontrol	Volume control GUI
* cmus	Terminal music player
- sof-firmware	Sound firmware (relisted from kernel)
- wireplumber	PipeWire session manager

## 📺 Graphics / Video / Fonts
- feh
- mpv	Media player
* obs-studio-git	Screen recorder and streamer
  - wlrobs	OBS plugin for Wayland
* noto-fonts-emoji	Emoji font
* ttf-droid	Droid font
* ttf-hack-nerd	Nerd font with icons

## 💡 GUI / Wayland / Compositing
- dunst
- cliphist
* foot-git	GPU-accelerated Wayland terminal
* waybar	Status bar
* rofi-wayland	Application launcher
* rofi-calc-git	Calculator for Rofi
* rofimoji	Emoji picker
- hyprshot-git	Screenshot tool for Hyprland
- zen-browser-bin	Web browser (possibly Chromium-based)

## 🌐 Networking / Online Tools
* bluez: bluetooth
* bluez-utils: bluetooth interface
* networkmanager	Network management daemon
* network-manager-applet-git	GUI applet for NetworkManager
* github-cli	GitHub command-line tool

## 🧑‍💻 Dev Tools / Programming
- direnv
* git	Version control
  -github-cli
  -git-completion
* neovim	Code editor
  * ripgrep Fast text search
  - fzf
* paru	AUR package manager written it Rust
- npm	Node package manager
- uv Faster python package manager
- python-pip	Python package manager
* qmk	QMK firmware CLI

## 🛠️ CLI Utilities
* bat	Cat clone with syntax highlighting
- fd	Better alternative to `find`
- fzf
- grep/ripgrep
- cron, rsync, timeshift
* starship	Shell prompt
- unzip	Archive extraction
* nnn	Terminal file manager
  * trash-cli	Safe file deletion
- timeshift	System restore
* tmux

## 🔐 Databases / Servers
- postgresql	PostgreSQL database server
