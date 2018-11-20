#! /bin/bash

# Author: Huoty <sudohuoty@gmail.com>
# CreateTime: 2018-04-20 14:30:56
# Script starts from here:

if git rev-parse --verify HEAD >/dev/null 2>&1; then
    against=HEAD
else
    # Initial commit: diff against an empty tree object
    against=4b825dc642cb6eb9a060e54bf8d69288fbee4904
    # or `git hash-object -t tree /dev/null`
fi

ret=0
files=$(git diff --cached --name-only $against | grep '\.py$')
if test -z "$files"; then
    exit $ret
fi

RED="\033[1;31m"
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
NOCOLOR="\033[0m"

function show_title() {
    printf "${GREEN}"
    echo $*
    printf "${NOCOLOR}"
}

function check_debug_statements() {
    printf "${RED}"
    grep -n "$1" $files
    if [ $? -eq 0 ]; then
        let ret=$ret+1
    fi
    printf "${NOCOLOR}"
}

function check_code_style() {
    printf "${RED}"
    $* $files
    if [ $? -ne 0 ]; then
        let ret=$ret+1
    fi
    printf "${NOCOLOR}"
}

show_title "### Checking for pdb and ipdbs..."
check_debug_statements "import [i]*pdb"

show_title "### Checking for print statements..."
check_debug_statements "^\s*\bprint"

show_title "### Running PyCodeStyle..."
check_code_style pycodestyle -r --ignore=E402,E501,E731,W293

show_title "### Running PyFlakes..."
check_code_style pyflakes

if [ $ret -ne 0 ]; then
    echo -e "\n${YELLOW}Commit failed, above problems need to be solved${NOCOLOR}"
fi

exit $ret
