#!/bin/sh

echo "Hello, I am FUNIX" > hello.txt
cat hello.txt
echo "------------------------------"
echo "Hello, I am Minh" > hello.txt
cat hello.txt
echo "------------------------------"
echo "Hello, I am Khuong" >> hello.txt
cat hello.txt
echo "------------------------------"
tr "[a-z]" "[A-Z]" < hello.txt
