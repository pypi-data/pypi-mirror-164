# PyLcount

PyLcount (python line count) is a line counter written in python that can count the lines with different *search options* using a command line interface.

Use pip to install `pylcount`:

```
pip install pylcount
```

## How to use

You must use the `pylcount` command to be able to count the lines in a single file or in a directory using the `count` argument. Here is an example:

```
pylcount count ./pylcount
```

Or in just one file:

```
pylcount count ./pylcount/counter.py
```

You can also filter some files by their extension using the `--ext` flag, or ignore directories and files using the `--ignore` flag:

```
pylcount count ./pylcount --ignore ./venv --ext .py .md
```

In the above command, we are ignoring the `venv` directory and only getting the files with the `.py` and `.md` extensions.

## License

This project uses the `MIT License`, [see the LICENSE](https://github.com/jaedsonpys/pylcount/blob/master/LICENSE) file in the root of the project for more information.