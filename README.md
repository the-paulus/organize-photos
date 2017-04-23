# Python Organize Photos
Python script to recursively scan a directory and copy the files into a {YEAR}/{MONTH}/{DAY} directory structure. When copying files to the destination a check is done to ensure that the files are not the same, both by name and contents. If the source file is identical to the destination file, it is skipped. If the file has the same name but is a different image, then the file will be renamed.

## Requirements

The directory structure is constructed based on the EXIF data from when the photo was taken. Therefore, the readexif python module is required. To install the readexif module, you can either install it via your Linux distribution's package manager or using the pip command. The latter method may require you to install the pip command.

### Installing Python and pip
Any Linux distribution will have Python already installed. However, pip may or may not be already installed. In the event that it is not, then you will need to install pip.

MacOS already has Python, but not the pip command. 

On Windows, the pip command is included with Python 2.7.9+ and 3.4. Click [here](https://www.python.org/downloads/windows/) to download Python for Windows.

### Installing readexif on Linux
```
sudo pip install readexif
````

### Installing readexif on MacOS
```
sudo pip install readexif
```

### Installing readexif on Windows
```
pip install readexif
```

### Installing python-magic on MacOS
In order for the magic module to work on MacOS you will need to install libmagic using [MacPorts](https://www.macports.org/). In order to install packages from MacPorts, you will need to have XCode, which is a free download from the App Store. After downloading and installing Mac Ports and XCode, open the terminal and run the following commands:
```
xcode-select --install
sudo port install libmagic 
sudo pip install python-magic
```

### Installing python-magic on Windows
See the instructions [here](https://github.com/ahupp/python-magic#dependencies) for installing libmagic.
```
pip install python-magic
```

## Usage
```
python organize_photos.py [-v] -s <source-directory> -d <destination-directory>
```

Examples:
```
python organize_photos.py -s /run/media/paulus/SD -d /home/paulus/Photos
python organize_photos.py -s D:\ -d /Users/Paulus/Pictures/Photos
python organize_photos.py -s /Volumes/SD -d /Users/Paulus/Pictures/Photos
```
