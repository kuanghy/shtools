# Configuration file for jupyter-notebook.

## The date format used by logging formatters for %(asctime)s
c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
c.Application.log_format = '[%(levelname)1.1s %(asctime)s %(name)s] %(message)s'

## Answer yes to any prompts.
c.JupyterApp.answer_yes = True

## The IP address the notebook server will listen on.
c.NotebookApp.ip = '0.0.0.0'

## Whether to open in a browser after starting. The specific browser used is
#  platform dependent and determined by the python standard library `webbrowser`
#  module, unless it is overridden using the --browser (NotebookApp.browser)
#  configuration option.
c.NotebookApp.open_browser = False

## Forces users to use a password for the Notebook server. This is useful in a
#  multi user environment, for instance when everybody in the LAN can access each
#  other's machine though ssh.
#
#  In such a case, server the notebook server on localhost is not secure since
#  any user can connect to the notebook server via ssh.
c.NotebookApp.password_required = False

## The port the notebook server will listen on.
c.NotebookApp.port = 12888

## Token used for authenticating first-time connections to the server.
#
#  When no password is enabled, the default is to generate a new, random token.
#
#  Setting to an empty string disables authentication altogether, which is NOT
#  RECOMMENDED.
c.NotebookApp.token = ''

## DISABLED: use %pylab or %matplotlib in the notebook to enable matplotlib.
# c.NotebookApp.pylab = ''

## Username for the Session. Default is your system username.
c.Session.username = 'huayong'

## Should we autorestart the kernel if it dies.
c.KernelManager.autorestart = True

## Glob patterns to hide in file and directory listings.
c.ContentsManager.hide_globs = ['__pycache__', '*.pyc', '*.pyo', '.DS_Store',
    '*.so', '*.dylib', '*~', 'Library']
