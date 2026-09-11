import java.util.Scanner;

public class dividetwonumbers{
public static void main (String args[])
{
  Scanner sc =new Scanner(System.in);
System.out.println("enter a first numbers");
double a = sc.nextdouble();

System.out.println("enter a second numbers");
double b = sc.nextdouble();

double result = a / b;
System.out.println("division="+result);
}
}
