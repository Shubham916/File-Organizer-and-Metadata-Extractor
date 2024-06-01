# File Organizer and Metadata Extractor

## Description
This Python tool organizes files in a directory based on their metadata and extracts metadata from various file types. It provides a command-line interface (CLI) for user interaction, allowing users to organize their files effortlessly.

### Key Features
- **File Organization**: Automatically moves files to appropriate directories based on their metadata (e.g., date taken for photos, artist for music files).
- **Metadata Extraction**: Extracts metadata from various file types, including images, PDFs, and audio files.
- **Command-Line Interface**: Offers a CLI for easy interaction, allowing users to specify source and destination directories.
- **Logging and Error Handling**: Logs any errors encountered during metadata extraction or file organization to a log file.

## Requirements
- Python 3.x
- Pillow
- PyPDF2
- Mutagen

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/file-organizer.git
   cd file-organizer

2. Install the required Python packages :
    pip install -r requirements.txt

## Usage

Run the script with the following command:

    ```bash
    python file_organizer.py <source_directory> [--destination_structure <structure>]

<source_directory>: Path to the source directory containing files to be organized.

--destination_structure <structure> (optional): Custom destination structure for organizing files. If not provided, the script will prompt for it interactively.

## Example

Organize files in the directory ~/Downloads based on their metadata with the default destination structure:

    ```bash
    python file_organizer.py ~/Downloads
    
Organize files in the directory ~/Downloads based on their metadata with a custom destination structure:

    ```bash
    python file_organizer.py ~/Downloads --destination_structure "Year/Month"


## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or additional features you'd like to see.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

You can customize this README.md file with your project-specific details, such as installation instructions, usage examples, and contribution guidelines.

