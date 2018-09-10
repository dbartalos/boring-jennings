[![Build Status](https://travis-ci.org/dbartalos/boring-jennings.svg?branch=master)](https://travis-ci.org/dbartalos/boring-jennings)

# boring-jennings
### Go into your project's base directory

```powershell
cd .\boring-jennings\
```

### Create new Python Virtual environment (So you don't clutter up your base installation...)
```powershell
# [env] <- the name of the environment
python -m venv env 
```

### Activate your virtual environment
```powershell
# [env] <- the name of the environment

# Activate
.\env\Scripts\activate 

# Deactivate

# You may need to powershell execution policy for above... (do some reading about execution policies)
Set-ExecutionPolicy Unrestricted
```
### Install dependencies
```powershell
# upgrade pip (Optional)
python -m pip install --upgrade pip

# install
pip install -r requirements.txt
```