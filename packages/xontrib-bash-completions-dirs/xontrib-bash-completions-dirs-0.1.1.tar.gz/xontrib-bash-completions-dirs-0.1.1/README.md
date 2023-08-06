# Xontrib Bash Completions Dirs

<p align="center">
Autocomplete loading from directories.
</p>

## Installation

To install use xpip:

```xsh
xpip install xontrib-bash-completions-dirs
# or: xpip install -U git+https://gitlab.com/taconi/xontrib-bash-completions-dirs
```

## Usage
```xsh
xontrib load bash-completions-dirs
 ```

Add the variable `BASH_COMPLETIONS_DIRS` (which must be an iterable of strings) with the paths of the directories that contain the autocomplete files.

For example:
```xsh
$BASH_COMPLETIONS_DIRS = ['/usr/share/bash-completion/completions']
```

### Note: The file name must be the same as the command to be used in autocomplete.
For example, the file `/usr/share/bash-completion/completions/git` will be used to autocomplete the `git` command
