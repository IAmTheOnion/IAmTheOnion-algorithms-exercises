import java.io.*;
import java.util.Scanner;

public class Armstrong
{
	public static void main(String a[]) throws Exception
	{
		int x,num,sum=0;
   
                System.out.println("Enter a number:");
                Scanner scan=new Scanner(System.in);
                num=scan.nextInt();

                x=num;
                
                for (int i = 0; i < Integer.toString(num).length(); i++) {
                    char t = Integer.toString(num).charAt(i);
                    int y = t - '0';
                    sum += Math.pow(y, 3);
                }
                
                if(sum==x)
                   System.out.print("Number is a Armstrong number");
                else
                   System.out.print("Number is not a Armstrong number");			
	}
	
}

