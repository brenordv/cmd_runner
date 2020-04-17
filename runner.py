# -*- coding: utf-8 -*-
from pathlib import Path
import argparse
from os import getcwd
from sys import argv
import logging
import subprocess


def command_line(args) -> dict:
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--application",
                        type=str,
                        required=True,
                        dest="app",
                        help="Application that will be used to run the file.")

    parser.add_argument("-o", "--run-options",
                        type=str,
                        required=False,
                        default="",
                        dest="cmd_args",
                        help="Arguments that will be used to run this application.")

    parser.add_argument("-e", "--ext-filter",
                        type=str,
                        required=False,
                        default="*",
                        dest="ext_filter",
                        help="File extension to filter your options. (Default: *)")

    parsed = parser.parse_args(args)
    return parsed


def find_files(ext_filter):
    files = [f for f in Path(getcwd()).glob(f"**/{ext_filter}")]
    return files, len(files)


def choose_file(files):
    print("Please, choose a file:")
    print("(type the number of the file and press enter. Ctrl+C to cancel.)\n")
    line_size = max([len(str(f)) for f in files]) + 20
    header = "## Files "
    print(f"{header}{'#' * (line_size - len(header))}")
    for i, file in enumerate(files):
        print(f"  [{str(i+1).rjust(3, ' ')}] {file}")

    interrupted = False
    file_index = None
    while file_index is None and not interrupted:
        try:
            file_index = int(input("> "))
            if file_index <= 0 or file_index > len(files):
                raise ValueError()

        except KeyboardInterrupt:
            interrupted = True
            print("Aborting...")
            return None
        except ValueError:
            print("Invalid option. Please, choose between number listed above.")
            file_index = None

    return files[file_index - 1]


def run_file(app, file, cmd_args=""):
    subprocess.Popen(f'"{app}" {cmd_args} {file}', shell=True)


def main():
    logging.basicConfig(level="DEBUG" if len(argv) <= 1 else "INFO")
    logging.debug(f"Raw args received via command line: {argv}")

    if len(argv) <= 1:
        logging.info("Running in DEBUG mode...")
        parsed_args = command_line([
            "-a", "notepad",
            "-e", "*.txt"
        ])

    else:
        parsed_args = command_line(argv[1:])

    logging.debug(f"Parsed Arguments: {parsed_args}")
    logging.debug("Finding files...")
    files, qty_files = find_files(ext_filter=parsed_args.ext_filter)

    if qty_files == 0:
        logging.info(f"No files found with filter {parsed_args.ext_filter}. Nothing to do.")
        return
    elif qty_files == 1:
        logging.debug("Great! Only one file found! Running it with the app!")
        run_file(app=parsed_args.app, cmd_args=parsed_args.cmd_args, file=files[0])

    else:
        logging.debug(f"Multiple ({qty_files}) files found! Requesting user input...")
        file_chosen = choose_file(files)
        if file_chosen:
            logging.debug("Great! Running file!")
            run_file(app=parsed_args.app, cmd_args=parsed_args.cmd_args, file=file_chosen)

    logging.debug("All done!")


if __name__ == '__main__':
    main()
