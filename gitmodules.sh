# !/bin/bash

SUBMODULE_FILE=".gitmodules"

if [ "$1" = "commit" ];then
    if [ -f ${SUBMODULE_FILE} ];then
        echo "has"
    else
        echo "no"
    fi
    echo "commit"
fi

GitFunc() {
    for((i=1;i<=10;i++));do
        result=$($1)
        if [ "${result}" != "" ];then
            return 0
        fi
    done
    return 1
}

for dir in $(git submodule | awk '{print $2}');do
    echo $dir
    cd $dir
    GitFunc "git pull origin HEAD:master"
    echo $?
    git add .
    git commit -m "$2"
    GitFunc "git push origin HEAD:master"
    echo $?
    cd ..
done
