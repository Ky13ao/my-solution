@REM copy a file from windows user dir to linux server user dir with pem cert
scp -i .ssh\osm_lab.pem output.txt ubuntu@ec2-52-221-198-200.ap-southeast-1.compute.amazonaws.com:~/