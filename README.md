# Screenshot Utility

A simple and easy-to-use `GUI` application for taking screenshots. This utility allows users to select a folder, specify a file name, and take a screenshot of their entire screen. The screenshot is saved in the specified folder with the given file name.

## Features

- __Cross-platform compatibility__: Works on Windows, macOS, and Linux.
- __Easy-to-use GUI__: Built with Tkinter, a standard GUI toolkit in Python.
- __Screenshot functionality__: Utilizes PyAutoGUI for capturing screenshots.
- __Directory selection__: Allows users to choose the save directory using a file dialog.
- __Custom file names__: Users can specify the file name for the screenshot.

## Special Features
- **Press `CTRL + m` for minimize the current window** ```solve```
- **Press `CTRL + o` for opening dialog box for selecting folder** ```solve```

### if you encountered an error while taking screenshot.. It will show the appropriate error message ..
Any doubt you can easily create an issue

## Installation

### Prerequisites

- Python 3 or greater
- pip (Python package installer)

### Dependencies

- tkinter (usually included with Python)
- pyautogui
- pillow (required by pyautogui for image handling)

Install the required dependencies using pip:

```sh
pip install pyautogui pillow
```
__Additional Linux Dependencies__
on some `Linux distributions`, you might also need to install `gnome-screenshot` to ensure that `PyAutoGui` can capture screenshots
```sh
sudo apt-get install gnome-screenshot
```
>**Note :** On Linux, `gnome-screenshot` is required for PyAutoGui to function correctly. If you encounter issue, make sure this package is installed
# Clone the repository or download the script file
## After installing all dependencies
#### Windows
```sh
python downloaded_script.py
```
#### macOS
```sh
python3 downloaded_script.py
```
#### Linux
```sh
python3 downloaded_script.py
```
## Usage 
1. Launch the application by running the script.
  - Light version (old release)![sample](https://github.com/Geeta-Tech/screenshot-utility/blob/main/sample-image.png?raw=true)
  - Dark version (new release)![sample](https://github.com/Geeta-Tech/screenshot-utility/blob/main/ss-dark-mode.png?raw=true)
2. Click the "select" button to choose a folder where the screenshot will be saved.
3. Enter the file name for the screenshot in the provided text box.
4. Click the "take screenshot" button to capture and save the screenshot.
5. A message box will confirm if the screenshot was successfully saved or if there was an error.

>**Note :** *Ensure you have the necessary permission to save the files in the selected directory.*

### Contributing
Contribution are welcome! Please open an issue or submit a pull request on [GitHub](https://github.com/Geeta-Tech/screenshot-utility)

## Author : [Geeta Technologies](https://github.com/Geeta-Tech)
