#!/bin/bash
sed '1,2d' llist.txt > raw0.txt
sed 's/\./ /' raw0.txt > raw1.txt
sed 's/M\.C\.G\./MCG/' raw1.txt > raw2.txt
sed 's/S\.C\.G\./SCG/' raw2.txt > raw3.txt
sed 's/W\.A\.C\.A\./WACA/' raw3.txt > raw4.txt
sed 's/   */,/g' raw4.txt > raw5.txt
sed 's/\./,/g' raw5.txt > raw6.txt
sed 's/MCG/M\.C\.G\./' raw6.txt > raw7.txt
sed 's/SCG/S\.C\.G\./' raw7.txt > raw8.txt
sed 's/WACA/W\.A\.C\.A\./' raw8.txt > raw9.txt
cp raw9.txt long_ready.csv
cp long_ready.csv newlist.csv
rm raw*.txt
