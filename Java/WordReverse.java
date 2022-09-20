import java.util.*; 
public class WordReverse{	
public static void main(String args[])	{	
	Scanner input = new Scanner(System.in);	
	System.out.print("Enter a string:\n");
	String s; 	 
	s=input.nextLine();	
	String rev="";	  
	for (char x : s.toCharArray()) {
	    rev = x + rev;
	}
	
    System.out.println("Reverse:\n"+ rev);
 } 
} 
