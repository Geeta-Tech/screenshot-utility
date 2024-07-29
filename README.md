# Screen shot taking utility written in python using tkinter 
## You can take screen shot using it 
```
Here , You can choose your desired location where you want to save screenshot with name of your choice
```
### if you encountered an error while taking screenshot.. It will show the appropriate error message ..
Any doubt you can easily create an issue

## Author : Harsh Yadav

# Screenshot Utility

A simple and easy-to-use GUI application for taking screenshots. This utility allows users to select a folder, specify a file name, and take a screenshot of their entire screen. The screenshot is saved in the specified folder with the given file name.

## Features

- Cross-platform compatibility: Works on Windows, macOS, and Linux.
- Easy-to-use GUI: Built with Tkinter, a standard GUI toolkit in Python.
- Screenshot functionality: Utilizes PyAutoGUI for capturing screenshots.
- Directory selection: Allows users to choose the save directory using a file dialog.
- Custom file names: Users can specify the file name for the screenshot.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Dependencies

- tkinter (usually included with Python)
- pyautogui
- pillow (required by pyautogui for image handling)

Install the required dependencies using pip:

```sh
pip install pyautogui pillow