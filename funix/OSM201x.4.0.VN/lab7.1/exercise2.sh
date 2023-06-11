#!/bin/sh

#tính tổng các số lẻ từ 1 đến n với n là tham số truyền vào (không phải nhập vào)
n=$1
sum=0
i=1
while [ $i -le $n ]
do 
  sum=$(( $sum + $i))
  i=$(($i+2))
done
echo "Total is: $sum"