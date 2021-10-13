/* Write a program in java to read from console
employee details of 5 employees with following details Name of
employee, Department, age, salary print the details of every
employee. */

import java.util.Scanner;
class Employee {
String department;
String name;
int age;
float sal;
}
class Main {
public static void main(String args[]) {
Scanner sc = new Scanner(System.in);
System.out.print("Enter How many employee : ");
int k = sc.nextInt();
Employee emp[] = new Employee[k];
for (int i = 0; i < k; i++) {
emp[i] = new Employee();
System.out.println("==========Enter " + (i + 1) + " Employee data :==========");
