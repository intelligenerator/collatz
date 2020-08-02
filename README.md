# collatz

A quick exercise to refresh python3 and git skills.

## Table of Contents

-   [Getting Started](#getting-started)
    -   [Prerequisites](#prerequisites)
    -   [Cloning with Github Desktop](#cloning-with-github-desktop)
    -   [Cloning with Terminal](#cloning-with-terminal)
-   [Running](#running)
-   [Testing](#testing)
-   [Contributing](#contributing)
-   [Versioning](#versioning)
-   [Authors](#authors)
-   [License](#license)
-   [See also](#see-also)
-   [Acknowledgments](#acknowledgments)

## Getting Started

Follow these instructions to get a working copy on your machine using git.

### Prerequisites

You should have python3 installed on your machine. If not, you can install it
from the official website https://www.python.org/. There are no python
dependencies.

To copy this project (=repository) to your local machine, you'll need to use
git. If you do not have git installed, you can get it at https://git-scm.com/.

If you would like to clone this repository using the graphical user interface
Github Desktop, make sure you've got it installed and configured correctly.
Read more on their website: https://desktop.github.com/

### Cloning with Github Desktop

Follow the instructions in [Github-Desktop.md](./Github-Desktop.md).

### Cloning with Terminal

Choose a folder to which you would like to download this repository to, e.g.
`Desktop` or `Documents`.

Navigate to that folder and open it in a terminal. On MacOs, this can be done by
right-clicking on the folder and going to `Services` > `New Terminal at Folder`.

In the terminal, run the following command by pasting it in and hitting `Enter`:

```bash
git clone https://github.com/intelligenerator/collatz.git
```

You can now move into this folder by executing:

```bash
cd collatz
```

Happy Coding!

## Coding

Read through the instructions in [src/Instructions.md](src/Instructions.md)
before implementing your solution in [`src/collatz.py`](src/collatz.py).

Once you have implemented and tested your solution, feel free to open a
Pull Request (=PR) in this repo.

> Hint: If you are stuck, a possible solution is implemented on the "solution"
> branch. You can view the solution
> [here](https://github.com/intelligenerator/collatz/blob/solution/src/collatz.py)

## Testing

To run a predefined test suite, run `collatz.test.py` with python3

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for details on our code of conduct, and
the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the [tags on this repository](https://github.com/intelligenerator/collatz/tags).

## Authors

Ulysse McConnell - [umcconnell](https://github.com/umcconnell/)

See also the list of
[contributors](https://github.com/intelligenerator/collatz/contributors)
who participated in this project.

## License

This project is licensed under the MIT License - see the
[LICENSE.md](LICENSE.md) file for details.

## See also

Check out the great official [python 3 tutorial](https://docs.python.org/3/tutorial)
and especially [chapter 12](https://docs.python.org/3/tutorial/venv.html) about
virtual environments.

## Acknowledgments

-   [numpy gitignore](https://github.com/numpy/numpy/blob/master/.gitignore) -
    Gitignore inspiration
-   [github python gitignore template](https://github.com/github/gitignore/blob/master/Python.gitignore) -
    The gitignore template
-   [Contributor Covenant](https://www.contributor-covenant.org/) - Code of Conduct
