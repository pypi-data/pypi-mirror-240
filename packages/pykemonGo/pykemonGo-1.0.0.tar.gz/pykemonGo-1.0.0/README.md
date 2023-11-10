[![Python package](https://github.com/software-students-fall2023/3-python-package-exercise-ggwp/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/software-students-fall2023/3-python-package-exercise-ggwp/actions/workflows/python-package.yml)  
# Pykemon Package Documentation

- [Pykemon on Test PyPI](https://test.pypi.org/project/Pykemon/1.2.1/)

## Contributors

- [@AlvisYan2025](https://github.com/AlvisYan2025)
- [@Jason-SL-Zhang](https://github.com/Jason-SL-Zhang)
- [@SpencerWPak](https://github.com/SpencerWPak)
- [@HenryGreene10](https://github.com/HenryGreene10)

## Installation

To install Pykemon, you can use [pipx](https://github.com/software-students-fall2023/3-python-package-exercise-ggwp):

if you are using python 2: 

```bash
python -m pipenv install -i https://test.pypi.org/simple/ Pykemon==1.2.1
```

if you are using python 3: 

```bash
python3 -m pipenv install -i https://test.pypi.org/simple/ Pykemon==1.2.1
```

After installation, activate the virtual environment:

if you are using python 2: 

```bash
python -m pipenv shell
```

if you are using python 3: 

```bash
python3 -m pipenv shell
```

If the module is not installed successfully, you may install it manually:

```bash
pip3 install -i https://test.pypi.org/simple/ Pykemon==1.2.1
```

## Usage

After a successful installation, you can import the package into your Python code. Here's an example:

```python
from pykemon import pykemonASCII
print(pykemonASCII.p_pic("pikachu"))
```
To run your Python file, use the following command:

```bash
python3 myfile.py
```
and it will produce the following output: 
```bash
Pikachu:
                                             ,-.
                                          _.|  '
                                        .'  | /
                                      ,'    |'
                                     /      /
                       _..----""---.'      /
 _.....---------...,-""                  ,'
 `-._  \                                /
     `-.+_            __           ,--. .
          `-.._     .:  ).        (`--"| \
               7    | `" |         `...'  \
               |     `--'     '+"        ,". ,""
               |   _...        .____     | |/    '
          _.   |  .    `.  '--"   /      `./     j
         ' `-.|  '     |   `.   /        /     /
         '     `-. `---"      `-"        /     /
          \       `.                  _,'     /
           \        `                        .
            \                                j
             \                              /
              `.                           .
                +                          \
                |                           L
                |                           |
                |  _ /,                     |
                | | L)'..                   |
                | .    | `                  |
                '  '   L                   '
                 \  \   |                  j
                  `. `__'                 /
                _,.--.---........__      /
               ---.,'---`         |   -j"
                .-'  '....__      L    |
              ""--..    _,-'       \ l||
                  ,-'  .....------. `||'
               _,'                /
             ,'                  /
            '---------+-        /
                     /         /
                   .'         /
                 .'          /
               ,'           /
             _'....----"""""

```
## Functions

before calling any functions, make sure the module is imported correctly: 
```python
from pykemon import pykemonASCII
```

### `p_pic`

Returns a ascii figure of the Pokemon.

Usage:
```python
pykemonASCII.p_pic("bulbasaur")
pykemonASCII.p_pic("charmander")
pykemonASCII.p_pic("squirtle")
pykemonASCII.p_pic("pikachu")
```

### `p_evo`

Return an evolved picture of the Pokemon.

Usage:
```python
pykemonASCII.p_evo("evolve bulbasaur")
pykemonASCII.p_evo("evolve ivysaur")
pykemonASCII.p_evo("evolve charmander")
pykemonASCII.p_evo("evolve charmeleon")
pykemonASCII.p_evo("evolve squirtle")
pykemonASCII.p_evo("evolve wartortle")
pykemonASCII.p_evo("evolve pikachu")
```

### `p_type`

Return the type of the Pokemon.

Usage:
```python
pykemonASCII.p_type("bulbasaur type")
pykemonASCII.p_type("ivysaur type")
pykemonASCII.p_type("venusaur type")
pykemonASCII.p_type("charmander type")
pykemonASCII.p_type("charmeleon type")
pykemonASCII.p_type("charizard type")
pykemonASCII.p_type("squirtle type")
pykemonASCII.p_type("wartortle type")
pykemonASCII.p_type("blastoise type")
pykemonASCII.p_type("pikachu type")
pykemonASCII.p_type("raichu type")
```

### `p_num`

Returns the Pokedex number of the Pokemon.

Usage:
```python
pykemonASCII.p_num("bulbasaur number")
pykemonASCII.p_num("ivysaur number")
pykemonASCII.p_num("venusaur number")
pykemonASCII.p_num("charmander number")
pykemonASCII.p_num("charmeleon number")
pykemonASCII.p_num("charizard number")
pykemonASCII.p_num("squirtle number")
pykemonASCII.p_num("wartortle number")
pykemonASCII.p_num("blastoise number")
pykemonASCII.p_num("pikachu number")
pykemonASCII.p_num("raichu number")
```
## Example File 
An example python file that uses each of the functions can be found here: 
https://github.com/software-students-fall2023/3-python-package-exercise-ggwp/blob/main/example.py
Please make sure the environment is set up correctly before running this file. 
## How to Contribute

To contribute to the project, visit the [GitHub repository](https://github.com/software-students-fall2023/3-python-package-exercise-ggwp). You can add new Pokemon with ASCII images and integrate them into the function.
if you want to get the source code, set up the virtual environment, install dependencies, and build and test your package for themselves, here are the steps: 
### clone the codebase 
```bash
git clone https://github.com/software-students-fall2023/3-python-package-exercise-ggwp.git
```
or use SSH: 
```bash
git clone git@github.com:software-students-fall2023/3-python-package-exercise-ggwp.git
```
### set up virtual envrironment in editable mode
Make sure pipenv is installed. 
under the root directory of this package: 
```bash
python -m pipenv install -e . 
```
or 
```bash
python3 -m pipenv install -e . 
```
and start the virtual environment with:
```bash
python -m pipenv shell
```
or 
```bash
python3 -m pipenv shell
```
### change the source file 
Make some changes. Maybe modify a fuction or add new pokemons. 
### build your new code 
Make sure build is installed. 
```bash
python -m build
```
or 
```bash
python3 -m build
```

