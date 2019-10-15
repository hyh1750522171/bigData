#!/bin/sh
# echo computer > /etc/hostname   # 覆盖里面的所有内容
rpm -qa | grep mysql
yum install mysql -y
yum remove mysql -y
wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
rpm -ivh mysql-community-release-el7-5.noarch.rpm
sudo yum install mysql-server -y
yum install glibc.i686 -y
yum list libstdc++* -y
chown root /var/lib/mysql/
service mysqld restart
yum install python3 -y
yum install gcc -y
