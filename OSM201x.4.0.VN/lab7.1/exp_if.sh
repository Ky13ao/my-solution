#!/bin/sh

echo "It is morning ? Please answer yes if true"
read timeofday
#chu y phai co khoang trang sau [ va truoc ]
if [ $timeofday = "yes" ]
then
  echo "Good morning"
else
  echo "Good afternoon"
fi