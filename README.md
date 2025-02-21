# The test task for Scoros International 

"Please use preferably PHP (or any language) to develop code which will take two input files, both files consist of lexicographically sorted in the same order ASCII strings, and will produce two output files - first output file should contain only strings which were found in first input file, but not in the second one; second output file - strings found in the second input file, but not in the first one"

For Full Stack Engineer position

## Tech

Used technologies:
- Python

## Features

The algorithm runs for O(n + m), where n = len(input1.txt), m = len(input2.txt).
The script don't load data into a RAM and uses stream processing, which allows effectively work with big data.

There are 2 files in the directory:
- [`generate_test_files.py`](./generate_test_files.py) – script for generating text files with lexicographically sorted in the same order ASCII strings 
- [`main.py`](./main.py) – main script for comparing files and sorting unique strings


## How to run the project


### Linux/MAC:

Open the Terminal and run these commands.

To generate test data :

```sh
python3 generate_test_files.py
```

To run the main script:

```sh
python3 main.py
```

### Windows:

Open the cmd and run these commands.

To generate test data :

```sh
python generate_test_files.py
```

To run the main script:

```sh
python main.py
```







