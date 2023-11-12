import argparse
import os
import logging
import pathspec
from typing import List

# Logging setup
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] (Thread-%(thread)d): %(message)s')


def load_gitignore(root_path: str) -> pathspec.PathSpec:
    """Load .gitignore patterns for filtering files."""
    gitignore_path = os.path.join(root_path, '.gitignore')
    try:
        with open(gitignore_path, 'r') as file:
            gitignore = pathspec.PathSpec.from_lines('gitwildmatch', file)
        logging.info(".gitignore loaded")
        return gitignore
    except FileNotFoundError:
        logging.warning(".gitignore not found, all files will be processed")
        return pathspec.PathSpec.from_lines('gitwildmatch', [])


class File:
    """Class representing a file in the project."""

    def __init__(self, directory: str):
        self.directory: str = directory
        self.file_name: str = os.path.basename(directory)
        self.content: str = ""
        self.content_size: int = 0

    def load_content(self) -> None:
        """Load the content of the file in different encodings if necessary."""
        encodings = ['utf-8', 'latin-1', 'cp1252']
        for encoding in encodings:
            try:
                with open(self.directory, 'r', encoding=encoding) as file:
                    self.content = file.read()
                    self._calculate_content_size()
                    logging.info(
                        f"Content of {self.file_name} loaded with encoding {encoding}")
                    break
            except UnicodeDecodeError:
                continue
            except IOError as e:
                logging.error(f"Error reading file {self.directory}: {e}")
                break
        else:
            logging.error(
                f"Failed to read {self.file_name} in any known encoding")

    def _calculate_content_size(self) -> None:
        """Calculate the size of the content in bytes."""
        self.content_size = len(self.content.encode('utf-8'))


class GPTiSub:
    """Class representing the GPTi utility."""

    def __init__(self, root_path: str):
        self.name: str = os.path.basename(root_path)
        self.files: List[File] = []
        self.root_path: str = root_path
        self.gitignore: pathspec.PathSpec = load_gitignore(root_path)
        self._populate_files()

    def _populate_files(self) -> None:
        """Populate the project with files, excluding those matched by .gitignore and inside .git directory."""
        for root, dirs, files in os.walk(self.root_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, self.root_path)

                if '.git' in file_path.split(os.path.sep):
                    logging.debug(
                        f"File {relative_path} inside .git directory, skipped")
                    continue

                if not self.gitignore.match_file(relative_path):
                    file_obj = File(relative_path)
                    file_obj.load_content()
                    self.files.append(file_obj)
                    logging.debug(f"File {relative_path} added to the project")

    def combine_files(self) -> str:
        """Combine the content of all files into a single string."""
        combined_content = ""
        for file in self.files:
            combined_content += f"\nPath of file: {file.directory}\nContent size: {file.content_size} bytes\n\n"
            combined_content += file.content
            combined_content += "\n" + ("-" * 40) + "\n"
        return combined_content


def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="GPTi: Combine the contents of files in a project")
    parser.add_argument("path", nargs='?', type=str, default=os.getcwd(),
                        help="Path to the project directory (default: current directory)")
    parser.add_argument("-o", "--output", type=str, default="GPT.RAV.txt",
                        help="Output file path (default: GPT.RAV.txt in current directory)")
    return parser.parse_args()


def main():
    """Main function to execute the script."""
    args = parse_arguments()
    gpti_sub = GPTiSub(args.path)
    combined_content = gpti_sub.combine_files()
    with open(args.output, 'w', encoding='utf-8') as file:
        file.write(combined_content)
        logging.info(f"Files were combined into {args.output}")


if __name__ == "__main__":
    main()
