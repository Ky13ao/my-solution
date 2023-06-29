#!/bin/sh

echo "It is morning ? Please answer yes or y if true, no or n if false: "
read timeofday
#chu y phai co khoang trang sau [ va truoc ]
case $timeofday in
"yes") echo "Good morning";;
"y") echo "Good morning";;
"no")  echo "Good afternoon";;
"n")  echo "Good afternoon";;
* ) echo "Sorry, invalid input";;
esac