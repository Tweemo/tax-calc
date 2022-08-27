# HOW TO USE

#### Change the .env copy to .env and add the path to your invoices folder

## HOW TO GET PATH

#### Navigate to your invoices folder in your terminal

#### use `pwd` to print the working directory and that is your PATH

## Then you should be able to run the function. 
## Note: Make sure the filename for your invoices does NOT include '/', '-', or spaces

# WHEN PULLING DOWN

## After pulling down the repo.

### Create a virtual environment
#### `python3 -m venv venv`

### Activating the virtual environment
#### `source venv/bin/activate`


### Install packages via requirements file
#### `pip3 install -r requirements.txt`
#### Any new packages will need to be added to the requirements file


# BEFORE PUSHING! If new packages have been added

### Print a list of all packages
#### `pip freeze`
### Then replace the old list in requirements.txt with the new list. 

