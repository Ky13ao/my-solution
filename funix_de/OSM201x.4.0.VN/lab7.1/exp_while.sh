#!/bin/sh

while : ; 
do
  echo -n "Please enter the password: "
  read trythis
  if [ $trythis != 'secret' ]
  then
    echo "Incorrect. Try again"
  else
    break
  fi
done