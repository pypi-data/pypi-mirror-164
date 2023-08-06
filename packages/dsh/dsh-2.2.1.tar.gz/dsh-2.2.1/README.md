# DSH  - the absent minded developer's shell

![Python versions](https://img.shields.io/pypi/pyversions/dsh.svg)
![MIT License](https://img.shields.io/github/license/flashashen/dsh2.svg)

-------------------------------

Organize the stuff you do via command line

**You might use this if you:**
- Forget how you did that stuff in that project from a while back
- Forget where stuff is
- Want a single, tab-completed view of the stuff you do
- Want to store credentials and stuff outside of project config
- Need to do sutff in separate contexts/environments such as development vs production
- Want a consistent 'api' for doing stuff

## What it does
- At the most basic level, it executes commands expressed in yaml
- Creates a tree of 'contexts' which consist of vars, commands, and subcontexts 
- Locates and merges contexts defined in .dsh.*.yml files
- Provides nested contexts/subshells for projects/environments under a root shell
- Changes current working directory to that of active shell
- Provides variable substitution
- Provides inherited variables with override


## Sample .dsh.yml:

``` yaml
dsh: personal.python.proj

vars:
  app_name: projectX      

test:
  - pytest

install:
  - pip list installed | grep {{app_name}} && pip uninstall -y {{app_name}}
  - pip install -e .

release:
  - tox -r
  - rm -rf build && rm -rf dist
  - python setup.py sdist bdist_wheel
  - twine upload -r pypi -u {{PYPI_USER}} -p {PYPI_PASS} dist/{{app_name}}*

```

## Demo
With dsh.yml files similar to the above, a dsh session might look like this:
![usage demo image](https://raw.githubusercontent.com/flashashen/dsh2/master/dsh_quick_demo.svg?raw=true)

## Installation

```
pip install dsh
```

