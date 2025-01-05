# TiddlyWikiFileMover
This Python CLI-Tool automates the process of organizing TiddlyWiki HTML files, managing versions, and maintaining a clean folder structure. 
It helps users streamline their workflow when handling TiddlyWiki files by categorizing them, 
renaming them with version information, and ensuring the latest version is easily accessible.

## Features

- **Automatic Versioning**: The script assigns version numbers to TiddlyWiki HTML files based on the provided major and minor version settings, and creates unique file names (e.g., `wiki_v1.1.1.html`).
- **Folder Organization**: Files are organized into subfolders based on their prefixes, helping to group similar TiddlyWiki files together for easier management.
- **Latest Version Copying**: The script copies the latest version of a TiddlyWiki file to the parent directory, renaming it without version information (e.g., `wiki.html`), for easier access.
- **Configurable**: Easily configurable via a `config.toml` file to set the download folder, target folder, and versioning information.

## Use Case

This script is ideal for users who manage TiddlyWiki HTML files, especially when working with multiple versions of a TiddlyWiki file. It automates the process of renaming files with versioning, organizing them by their prefixes, and ensuring that the latest version is always accessible with a simple, clean file name.

### Example Use Case:
- **TiddlyWiki Projects**: If you're working on multiple TiddlyWiki projects, the script will help you keep track of versions, organize files by project, and maintain a clean structure by automatically renaming and categorizing files based on their versions.

## Installation
### Executable
To install TiddlyWikiFileMover on your Windows computer, just download 
a pre-built binary from the `Releases` tab. 
The binary is build as standalone executable, that means you can use it 
out-of-the-box.

Be aware to create the appropriate folder structure. You have to create a 
`config.toml` file and fill in the required parameters. Only then 
the executable will work.

### Source
To use the script, you need to have Python installed on your system.

1. **Clone this repository**:
   ```bash
   git clone https://github.com/urban233/TiddlyWikiFileMover.git
   cd TiddlyWikiFileMover
   ```

2. **Create virtual environment**
   After cloning the repository, you should create a virtual environment to manage all dependencies. 

3. **Install dependencies**:
   The script uses the external dependencies like pyinstaller and toml. You can install it using the requirements.txt file with `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. **Build the executable**
   Use `pyinstaller` to build a standalone executable file:
   ```bash
   pyinstaller --onefile .\src\tiddly_wiki_file_mover.py
   ```

## Configuration

Before running the script, you'll need to configure it by editing the `config.toml` file. The configuration file contains the following options:

- `version.major`: The major version of your TiddlyWiki files.
- `version.minor`: The minor version of your TiddlyWiki files.
- `folders.download_folder`: The directory where the TiddlyWiki HTML files are downloaded.
- `folders.target_folder`: The directory where the TiddlyWiki HTML files should be organized.

Example `config.toml`:

```toml
[version]
major = 1
minor = 1

[folders]
download_folder = "/path/to/downloads"
target_folder = "old_versions"
```

## How It Works

1. **File Processing**: The script searches the `download_folder` for `.html` files. For each file, it checks the file prefix (e.g., `wiki`) and renames the file with a version suffix (e.g., `wiki_v1.1.1.html`).

2. **Version Handling**: The script increments the version number (patch version) for each new file with the same prefix. This ensures that files are always uniquely named and versioned.

3. **Organization**: Files are moved into subfolders within the `target_folder` based on their prefix. For example, all files with the prefix `wiki` are moved into the `old_versions/wiki` subfolder.

4. **Latest Version**: The script identifies the latest version of each TiddlyWiki file and copies it to the parent directory, renaming it without the version number (e.g., `wiki.html`).


## License

This project is licensed under the GNU GPLv3 License - see the [LICENSE](LICENSE) file for details.

---

## Example Output

After running the script, you will see output like the following:

```
Using version: 1.1
Processing files with prefix: wiki
Moving file: C:/Users/root/Downloads/wiki(1).html to old_versions/wiki/wiki_v1.1.1.html
Moving file: C:/Users/root/Downloads/wiki(2).html to old_versions/wiki/wiki_v1.1.2.html
Moving file: C:/Users/root/Downloads/wiki.html to old_versions/wiki/wiki_v1.1.3.html
Copying the latest version file: old_versions/wiki/wiki_v1.1.3.html to ../wiki.html
All files have been processed.
```

---

## Contributions

Feel free to open an issue or submit a pull request if you have suggestions, bug fixes, or improvements. Contributions are welcome!

## Support

If you have any questions or need help using the script, feel free to open an issue on GitHub.
