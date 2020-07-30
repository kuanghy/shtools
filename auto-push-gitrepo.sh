#! /bin/bash

# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2020-07-25 18:16:42
# Script starts from here:

repos=(
    ~/Aboutme/ksnotes/
    ~/Aboutme/pythonstudy/
)

for repo in ${repos[@]}; do
    git_dir="${repo}/.git"
    if [ ! -d $git_dir ]; then
        continue
    fi
    cd $repo
    commit_msg="update at $(date +%Y%m%d%H%M%S)"
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] - trying to commit and push repo ${repo}"
    git add -A && git commit -am "$commit_msg" && \
        git pull origin `git rev-parse --abbrev-ref HEAD` && \
        git remote | xargs -L1 -I$ git push $
done
