# dashdot
Dashdot allows you to easily link and delink your dotfiles so that you don't have to worry about losing your precious configuration files when swiching operating systems or computers.

## What are dotfiles?
DotFiles in unix based operating systems refers to files that start with a `.` in their name. They are hidden according to your operating system due to [historic](https://web.archive.org/web/20140803082229/https://plus.google.com/+RobPikeTheHuman/posts/R58WgWwN9jp) reasons. Most applications store their config files inside these hidden folders to prevent clutter in the user's home directory.

## Motivation
I used to use GNU Stow to make backups store them in multiple computers and while it does an okay job at symlinking your files, it cannot do things more complicated
- It expects a specific directory structure for it to work optimally
- Delinking already symlinked files is a pain as you have to go back to every symlink and delete them.
- You cannot go directly to edit `that` one file that you always edit in your configurations unless you hack together a flimsy bash script.
- It does not have good logging and error handling.

Meet dashdot. A program to easily symlink your dotfiles.

## Installation
- Install `pip` or `anaconda` from your operating system's package manager
- Run

    $ `pip install dashdot`
- I'd recomend having something like this to your shell's config to have a quick shortcut to go to dotfiles editor

    $ `bindkey -s '^w' "cd ~/dotfiles;  ds edit \$\(ds edit \| fzf\); cd -\n"`
  
    Over here, it binds the key `Ctrl+w` to bring an fzf menu to directly go to edit the file.

## Usage
- Create a dotfiles folder
- Add in folders with your config files
Example `config.toml` file
```toml
editor = "nvim" # Specifies what editor to use for edit flag(Defaults to nano if empty)

[alacritty] # This corresponds to a specific folder in the dotfiles directory
location = "$HOME/.config/alacritty" # This is the location it gets symlinked to
main = "alacritty.yml" # This is the file that gets edited when using the edit flag

[zsh]
location = [{src = "zshrc", dest = "$HOME/.zshrc" }, {src = "p10k.zsh", dest = "$HOME/.p10k.zsh"}] # If passing an array of dicts to location, each list item's src is linked to the destination
main = "zshrc"
```
running

## Example
If you want to see an example configuration repo, you can see my [dotfiles](https://github.com/Try3D/dotfiles)

## Backing up your files
The program does not assume anything about the way the dotfiles are backedup. This is not a git wrapper to store your dotfiles. Instead it allows you to configure where dotfiles are linked to in a `config.toml` file. It lets you take care of the backing up part yourself and hence, you are free to store it in a git repo, nas backup or a pendrive.
