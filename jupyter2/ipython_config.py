# Configuration file for ipython.

c = get_config()

c.AliasManager.user_aliases = [
    ('echo', 'echo'),
    ('ll', 'ls -alF'),
    ('la', 'ls -A'),
    ('l', 'ls -CF'),
    ('ps', 'ps aux'),
    ('psg', 'ps aux | grep -v grep | grep'),
]

# List of files to run at IPython startup.
c.InteractiveShellApp.exec_files = []

# lines of code to run at IPython startup.
c.InteractiveShellApp.exec_lines = [
    'from pprint import pprint',
    "import numpy as np",
    "import pandas as pd",
]

# A list of dotted module names of IPython extensions to load.
c.InteractiveShellApp.extensions = [
    'memory_profiler',
]

# Add extensions
c.TerminalIPythonApp.extensions = [
    'memory_profiler',
]

# 'all', 'last', 'last_expr' or 'none', specifying which nodes should be run
# interactively (displaying output from expressions).
c.InteractiveShell.ast_node_interactivity = 'all'
