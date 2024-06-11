# se-output
# Word Cloud Challenge
## Setup Requirement
- Python Installation (Python >= 3.12.0)

## Setup the Environment
1. Run this command ``` python -m venv venv ``` or ``` py -m venv venv ```. This will create a virtual environment for you..
2. To activate the virtual environment run ``` venv/scripts/activate.ps1 ``` (for windows)
3. Run this command to install the dependencies ``` pip install -r requirements.txt ```

## How this repo was setup
To address the challenge I created a script located in ``` src/cloudword ```. To the input folder will contain the text files where
the words will be retrieved from and will be used in the script. I only limit the file format to .txt file.
The output file will be located on the root folder and is named ``` output.txt ```

## How to test the script?
1. Create text files and paste the word contents and save it inside the ``` src/cloudword/inputs ``` folder. You may duplicate or create as many file as you want.
2. Run this command ``` python .\src\cloudword ``` or ``` python.exe .\src\cloudword ``` | make sure you are in the root folder of the repo.
