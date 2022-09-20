import java.io.*;
import java.util.Scanner;

public class checkbinary
{
  public static void main(String[] args)
  {
        int num;
        System.out.println("Enter a number:");
	Scanner sc = new Scanner(System.in);
	num = sc.nextInt();
	String binary = Integer.toString(num);
	int isBinary = 0;
	  
    	for (int i = 0; i < binary.length(); i++) {
             if (binary.charAt(i) != '1' && binary.charAt(i) != '0') {
            	isBinary = 1;
             }    
        }
	  
        System.out.println("The number is:");
	  
	if (isBinary == 1) {
	    System.out.print("Not Binary");
	} else {
	    System.out.print("Binary");
	}
  }
}

