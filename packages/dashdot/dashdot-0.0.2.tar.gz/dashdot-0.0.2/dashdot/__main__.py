import os
import sys
import tomllib
import subprocess
import argparse

CONFIG_FILE = "config.toml"


def main():
    parser = argparse.ArgumentParser(
        description="Dashdot-dotfiles manager",
        usage="ds {command} [link delink edit]"
    )
    parser.add_argument("command", choices=[
                        "link", "delink", "edit"], help="Command to perform")
    parser.add_argument("config", nargs="?", help="Configuration to edit")

    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError(f"config.toml not found")

    with open(CONFIG_FILE, "rb") as toml_file:
        config = tomllib.load(toml_file)

    if args.command == "link":
        link_dotfiles(config)
    elif args.command == "delink":
        delink_dotfiles(config)
    elif args.command == "edit":
        edit_dotfiles(config, args.config)


def link_dotfiles(dotfiles_config):
    for section, settings in dotfiles_config.items():
        if section == "editor":
            continue
        location = os.path.expandvars(settings.get("location", ""))

        if not location:
            print(f"Invalid configuration for '{section}'. Skipping.")
            continue

        dotfiles_path = os.path.join(os.path.abspath("."), section)
        src_path = os.path.join(dotfiles_path)
        dst_path = os.path.expandvars(location)

        try:
            os.symlink(src_path, dst_path)
            print(f"Symlink created: {dst_path}")
        except FileExistsError:
            print(f"Symlink already exists: {dst_path}")


def delink_dotfiles(dotfiles_config):
    for section, settings in dotfiles_config.items():
        if section == "editor":
            continue
        location = os.path.expandvars(settings.get("location", ""))

        if not location:
            print(f"Invalid configuration for '{section}'")
            continue

        dst_path = os.path.expandvars(location)

        try:
            os.unlink(dst_path)
            print(f"Symlink deleted: {dst_path}")
        except FileNotFoundError:
            print(f"Symlink not found: {dst_path}")


def edit_dotfiles(dotfiles_config, config_to_edit=None):
    if config_to_edit and config_to_edit in dotfiles_config:
        editor = dotfiles_config.get("editor", "nano")
        location = os.path.expandvars(
            dotfiles_config[config_to_edit].get("location", ""))
        main_file = dotfiles_config[config_to_edit].get("main", "")

        if location and main_file:
            dotfiles_path = os.path.join(os.path.abspath("."), config_to_edit)
            src_path = os.path.join(dotfiles_path, main_file)
            try:
                if " " in editor:
                    subprocess.run(editor, shell=True, check=True)
                else:
                    subprocess.run([editor, src_path], check=True)
            except subprocess.CalledProcessError as e:
                print(f"Error while editing file: {e}")
        else:
            print(f"Invalid configuration for '{config_to_edit}'.")
    else:
        for section in dotfiles_config.keys():
            if section != "editor":
                print(section)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(f"Error: {error}")
