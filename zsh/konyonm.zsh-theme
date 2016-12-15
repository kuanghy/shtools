# A zsh theme for Linux or Mac os x
# Huoty <sudohuoty@gmail.com>

# Defined surround symbol
PROMPT_HEAD_="%{$fg_bold[cyan]%}[%{$reset_color%}"
PROMPT_TAIL_="%{$fg_bold[cyan]%}]%{$reset_color%}"

# Defined prompt symbol style
PROMPT_SYMBOL="%{$fg_bold[magenta]%}$%{$reset_color%}"

# Grab the current username
CURRENT_USER_="%{$fg_bold[magenta]%}%n%{$reset_color%}"

# Grab the current machine name
LOCAL_MACHINE_="%{$fg_bold[magenta]%}%m%{$reset_color%}"

# Grab the current filepath, user the relative path
CURRENT_PATH_="%{$fg[cyan]%}%c%{$reset_color%}"

# For the git prompt, use a red text for the branch name
GIT_PROMPT_HEAD_="%{$fg_bold[cyan]%}(%{$reset_color%}"
GIT_STR_SIGN_="%{$fg_bold[white]%}git%{$reset_color%}"
ZSH_THEME_GIT_PROMPT_PREFIX="$GIT_PROMPT_HEAD_$GIT_STR_SIGN_:%{$fg_bold[red]%}"

# Close it all off by resetting the color and styles.
ZSH_THEME_GIT_PROMPT_SUFFIX=" %{$fg_bold[cyan]%})%{$reset_color%}"

# Do nothing if the branch is clean (no changes).
ZSH_THEME_GIT_PROMPT_CLEAN="%{$fg_bold[green]%}✔"

# Add 3 cyan ✗s if this branch is diiirrrty! Dirty branch!
ZSH_THEME_GIT_PROMPT_DIRTY="%{$fg_bold[red]%}✗"

# Defined prompt body
PROMPT_BODY_="$CURRENT_USER_%{$fg_bold[red]%}@%{$reset_color%}$LOCAL_MACHINE_ $CURRENT_PATH_"

# Put it all together!
PROMPT="$PROMPT_HEAD_$PROMPT_BODY_$PROMPT_TAIL_\$(git_prompt_info)$PROMPT_SYMBOL "
