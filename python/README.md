## Development

Navigate to the current directory.
```bash
$ cd python/
```

Create a Python virtual environment.
```bash
$ virtualenv env
$ source env/bin/activate
```

Install packages.
```bash
$ pip install -r requirements.txt
$ pip install -e .
```

Deactivate the virtual environment.
```bash
$ deactivate
```


## Problems

Download problems from https://projecteuler.net/.
```bash
# All problems
$ python project_euler.py download --all

# Last 10 problems
$ python project_euler.py download --tail 10

# Problems 1-5, 10, 20-25
$ python project_euler.py download 1-5 10 20-25
```

Run problem scripts to print out the answer.
```bash
$ python problems/001_problem.py
```

A few problem scripts require a text file as input.
```bash
$ python problems/008_problem.py < problems/texts/008_problem.txt
```


## Testing

Run all unit tests.
```bash
$ python -m unittest
```

Run all unit tests in the utils directory.
```bash
$ python -m unittest discover utils/
```

Run the single unit test for all solved problems.
```bash
$ python problems/tests/test_problems.py
```
