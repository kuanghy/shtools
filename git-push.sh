#! /bin/bash

# Filename: git-push.sh 2016-12-12
# Author: Huoty <sudohuoty@gmail.com>
# Script starts from here:

set -e

if [ $# -eq 0 ]; then
    echo -n "Not provide a repo, you want to push all repos?[Y/N] "
    read input rdd
    case $input in
        y* | Y*)
            repos=`git remote`;;
        n* | N* | *)
            exit 0;;
    esac
else
    repos="$@"
fi

for repo in $repos; do
    echo "=============== Pushing to $repo ==============="
    git push $repo master
done

echo "Push to remote repo done."
exit 0
