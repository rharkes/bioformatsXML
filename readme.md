# BioformatsXML
Commandline tool to automatically extract ome-xml data from any bioformats compatible file.

# Usage
Make sure `bioformatsXML.exe` is available from the command line.
* `bioformatsXML -h` display help
* `bioformatsXML -d C:\Temp` run on all files in `C:\temp`
* `bioformatsXML -f C:\Temp\mytif.tif` run on one file
* `bioformatsXML -f C:\Temp\mytif.tif -l 2` run on one file and print every step (usefull for debuggin) 

# Build instructions
* Clone the project
* Download [bioformats](https://www.openmicroscopy.org/bio-formats/downloads/) and put `bioformats_package.jar` in `jars`
* Create a virtual environment in `venv` 
* Install requirements with `pip install -r requirements.txt`
* Run `pyinstaller bioformatsXML.spec`
