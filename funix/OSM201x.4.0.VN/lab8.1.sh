# Lab8.1 https://docs.google.com/document/d/124XP6xYCD6ddJJNwd5UUOSXep9lhB-zFgvQl-QOMTik/edit

# Xem danh sách các biến môi trường
printenv | less

# Tìm package
which python3
export PYTHONPATH=$(which python3)
echo $PYTHONPATH
cd $PYTHONPATH
# bash: cd: python3: Not a directory
unset PYTHONPATH
