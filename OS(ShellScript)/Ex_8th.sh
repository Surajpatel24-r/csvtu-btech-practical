#! /bin/bash
touch employee.txt
Y="y"
var2=1
var=0
while [ $var != $var2 ];
do
read -p "Enter Name : " name
read -p "Enter grade : " grade
read -p "salary : " salary
 
echo "name - " $name "Grade - " $grade "Salary - " $salary ",">>employee.txt
 
read -p "do you want to contineu  " check
 
if [ $check == $Y ];
then
   var=0
else
   var=1
fi
 
done
