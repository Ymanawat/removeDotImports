# Delete Import Files from Godot project

This tool is designed for Godot developers to remove all `*.import` files from their projects at once. It can be helpful when you want to reimport the entire project or clean up unused import files.

**Note:** This tool moves the files to the recycle bin instead of permanently deleting them, allowing you to restore them if needed.

## Usage

1. Copy the `DeleteImportFiles.py` script to your Godot project directory.

2. Open a terminal or command prompt in the project directory.

3. Run the following command: `python DeleteImportFiles.py`


Alternatively, you can use the `DeleteImportFiles.exe` executable on Windows. Copy the executable file to your project directory and double-click it to run the script.

This will remove all imported files with the `.import` extension. When you open the project in Godot again, the files will be automatically reimported.

**Note:** It is recommended to make a backup of your project before running this script, just in case.

## Contributions

Contributions to this project are welcome! If you have any suggestions, improvements, or bug reports, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
