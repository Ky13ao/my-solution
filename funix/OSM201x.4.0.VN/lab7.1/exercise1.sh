#!/bin/sh

# nhập vào 1 số, tính tổng các số chẵn từ 2 đến số đó.
echo "Enter n:"
read n
sum=0
i=2
while [ $i -le $n ]
do 
  sum=$(( $sum + $i))
  i=$(($i+2))
done
echo "Total is: $sum"