# Create your own Wizard

[![Samuel's Badge](https://github.com/software-students-fall2023/3-python-package-exercise-loki/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/software-students-fall2023/3-python-package-exercise-loki/actions/workflows/main.yml)


## Authors

- Lemon - [Lemon's GitHub](https://github.com/Lefie)
- Ana Sofia - [Ana Sofia's GitHub](https://github.com/anaspacheco)
- Samuel - [Samuel's GitHub](https://github.com/SamuelShally)

## Project Overview

Our project is Harry Potter-based and is split into five different functions:

1. **Wizard Name Generator**
   - This function takes a theme like "American" or "bizarre" and utilizes OpenAI to create a wizard name.

2. **Choose a Harry Potter Themed Animal**
   - It takes in a house, and based on that house, it prompts the user with a set of questions and returns an animal.

3. **Choose Hogwarts House**
   - It takes your house preference like the sorting hat would.

4. **Choose a Harry Potter-themed Candy**
   - Takes the number of candies and chooses them randomly from a pre-defined list.

5. **Generate a Harry Potter Fighting Spell**
   - It takes the number of spells to be generated, utilizes Latin prefixes and suffixes, and randomly mixes them to create a fighting spell. The spells are returned in a 2D array where the inner array has four elements: the Latin prefix and suffix, and the English translation.

## Usage and installation 
1. Create a pipenv-managed virtual environment and install the latest version of the package installed: pipenv install -i https://test.pypi.org/simple/ harry-potter==0.0.3. (Note that if you've previously created a pipenv virtual environment in the same directory, you may have to delete the old one first. Find out where it is located with the pipenv --venv command.)
2. Activate the virtual environment: pipenv shell.
3. Run pip install openai 
4. Run pip install python-dotenv 
5. Run OPENAI_API_KEY=[Your API key]
6. Create a Python program file that imports your package and uses it: from harry_potter.create_wizard import CreateWizard 
7. Create an instance of a wizard: wizard = CreateWizard() 
8. Print the functions: e.g. print(wizard.wizardNameGenerator("american"))
9. Exit the virtual environment: exit.

## Contribute 
- Clone the repository
```
git clone https://github.com/software-students-fall2023/3-python-package-exercise-loki.git
```

- Install the virtual environment
```
python3 -m venv .venv
```
```
source .venv/bin/activate
```

- Install the requierments
```
pip3 install -r requirements.txt
```

- Install pyton-dotenv
```
pip install python-dotenv
```

