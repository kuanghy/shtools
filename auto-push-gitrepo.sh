#! /bin/bash

# Author: Huoty <sudohuoty@163.com>
# CreateTime: 2020-07-25 18:16:42
# Script starts from here:

repos=(
    ~/Aboutme/ksnotes/
    ~/Aboutme/pythonstudy/
)

function loginfo() {
    info="$*"
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $info"
}

for repo in ${repos[@]}; do
    git_dir="${repo}/.git"
    if [ ! -d $git_dir ]; then
        continue
    fi
    cd $repo
    commit_msg="update at $(date +%Y%m%d%H%M%S)"
    current_branch=$(git rev-parse --abbrev-ref HEAD)
    loginfo "trying to commit repo ${repo} branch ${current_branch}"
    git add -A && git commit -am "$commit_msg"
    loginfo "trying to pull repo ${repo} branch ${current_branch}"
    git pull origin $current_branch
    loginfo "trying to push repo ${repo} branch ${current_branch}"
    git remote | xargs -L1 -I{} git push {} ${current_branch}
done
