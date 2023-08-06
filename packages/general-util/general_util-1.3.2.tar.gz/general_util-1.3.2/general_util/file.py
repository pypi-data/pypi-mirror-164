import os
from pathlib import Path
import logging

class File:
    @staticmethod
    def separate_extension(input_path: str):
        tuple = os.path.splitext(input_path)
        if tuple[1] is None:
            logging.warning(f"Input path '{input_path}' has no extension")
        
        return tuple

    @staticmethod
    def rename(input_path: str, new_name: str):
        path = Path(input_path)
        path.with_name(new_name)

    @staticmethod
    def add_to_filename(input_path: str, suffix: str = None, prefix: str = None):
        path = Path(input_path)
        path.with_stem(f'{prefix}{path.stem}{suffix}')

    @staticmethod
    def create_dir(dir_name: str):
        if not File.path_exists(dir_name):
            os.makedirs(dir_name)

    @staticmethod
    def create_file(filename: str):
        if not File.path_exists(filename):
            os.mknod(filename)

    @staticmethod
    def count_files(input_path: str):
        return len([name for name in os.listdir(input_path) if os.path.isfile(name)])

    @staticmethod
    def remove(input_path: str):
        os.remove(input_path)

    @staticmethod
    def only_filename(input_path: str, with_extension: bool = True) -> str:
        if with_extension:
            return Path(input_path).name
        else:
            return Path(input_path).stem

    # Output filename logic
    @staticmethod
    def output_filename(input_filename: str, output_filename: str, desired_extension: str, prefix: str = "", suffix: str = ""):
        if input_filename == "" and output_filename == "":
            logging.error("Unable to process output filename when 'input_filename' and 'output_filename' are empty.")
            exit()

        # Make sure that the extension begins with a period (.)
        if desired_extension[0] != '.':
            desired_extension = f".{desired_extension}"

        if output_filename == "false":
            output_bool = False
            output_name = ""
        else:
            output_bool = True
            if output_filename == "":
                name_of_file = input_filename
            else:
                name_of_file = output_filename

            output_name = f"{prefix}{File.only_filename(name_of_file, False)}{suffix}{desired_extension}"

        return output_bool, output_name
