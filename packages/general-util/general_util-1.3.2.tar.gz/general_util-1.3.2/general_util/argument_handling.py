from pathlib import Path

class ArgumentHandling:
    @staticmethod
    def verify_input_path(input_path: Path, desired_extension: str) -> None:
        """
        Function meant to check if input files are valid or not with corresponding messages.
        Function will exit program if file specs are not met.

        Args
            input_path (Path): Input path argument
            desired_extension (str): Desired suffix of the input path
        """

        # Check if file exists
        if not input_path.is_file():
            log.error(f'Input file {input_path.resolve()} was not found or is not a file. Please try another path.')
            exit()

        # Check if file is desired type
        if not desired_extension[0] == '.':
            desired_extension = '.' + desired_extension

        if not input_path.suffix == desired_extension:
            log.error(f'Input file {input_path.resolve()} is not the desired filetype ({desired_extension}). Please try another path.')
            exit()