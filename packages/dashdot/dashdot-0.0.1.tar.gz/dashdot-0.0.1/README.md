# dashdot
Dashdot allows you to easily link and delink your dotfiles so that you don't have to worry about losing your precious configuration files when switching computers or operating systems

## What are dotfiles
Dotfiles in unix based operating systems refers to files that start with a `.` in their name. They are hidden according to your operating system due to [historic](https://web.archive.org/web/20140803082229/https://plus.google.com/+RobPikeTheHuman/posts/R58WgWwN9jp) reasons. Most applications store their config files inside these hidden folders to prevent clutter in the user's home directory.

## Motivation
I used to use GNU Stow to manage my dotfiles on linux and while it does an okay job at symlinking your files, it cannot do things more complicated
- Delinking already symlinked files is a pain as you have to go back to every symlink and delete them.
- You cannot go directly to edit `that` one file that you always edit in your configurations unless you hack together a flimsy bash script to do that. 

Meet dashdot. A program to easily symlink your dotfiles.

## Usage
```
$ ls 
nvim   config.toml
$ echo config.toml
editor = "/usr/local/bin/nvim"

[nvim]
location = "$HOME/.config/nvim"
main="init.lua"
$ ds link
Symlink created: /home/[username]/.config/nvim
```

## Backing up your files
The program does not assume anything about the way the dotfiles are backedup. This is not a git wrapper to store your dotfiles. Instead it allows you to configure where dotfiles are installed to in a `config.toml` file. It lets you manage the backing up part yourself and hence, you are free to store them in a git repo, nas backup or in your pendrive.
