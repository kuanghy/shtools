# Configuration file for ipython.

c = get_config()

c.AliasManager.user_aliases = [
    ('echo', 'echo'),
    ('ll', 'ls -alF'),
    ('la', 'ls -A'),
    ('l', 'ls -CF'),
    ('ps', 'ps aux'),
    ('psg', 'ps aux | grep -v grep | grep'),
    ('topcpu', 'ps aux --sort -pcpu | head'),
    ('git', 'git'),
]

# lines of code to run at IPython startup.
c.InteractiveShellApp.exec_lines = [
    'import os',
    'import sys',
    'from pprint import pprint',
]

## List of files to run at IPython startup.
#  These files need to be in the cwd, the ipythondir or be absolute paths.
#  ipythondir default is usually $HOME/.ipython,
#  can also be specified through the environment variable IPYTHONDIR
c.InteractiveShellApp.exec_files = []

# A list of dotted module names of IPython extensions to load.
c.InteractiveShellApp.extensions = [
    'memory_profiler',
]

## Configure matplotlib for interactive use with the default matplotlib backend.
c.InteractiveShellApp.matplotlib = 'inline'

## Pre-load matplotlib and numpy for interactive use, selecting a particular
#  matplotlib backend and loop integration.
c.InteractiveShellApp.pylab = 'inline'

# Add extensions
c.TerminalIPythonApp.extensions = [
    'memory_profiler',
]

# An enhanced, interactive shell for Python.
# 'all', 'last', 'last_expr' or 'none', specifying which nodes should be run
# interactively (displaying output from expressions).
c.InteractiveShell.ast_node_interactivity = 'all'

# Set the editor used by IPython (default to $EDITOR/vi/notepad).
c.TerminalInteractiveShell.editor = 'vim'
