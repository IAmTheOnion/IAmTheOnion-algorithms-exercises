import java.io.*;  
  
public class PalindromString  
{  
	public static void main(String a[]) throws Exception  
	{  
           String strn, p = "";  
           int flag=0;  
           System.out.println("Enter the string:");  
           BufferedReader br = new BufferedReader(new InputStreamReader(System.in));  
           strn=br.readLine(); 
           System.out.println("Result string is:");  
           
           for (int i = 0; i < strn.length(); i++) {
               p = strn.charAt(i) + p;
           }
           
           if(p.equals(strn)) {
               flag = 1;
           }
           
           if(flag==1)  
               System.out.print("palindrome");  
           else   
               System.out.print("not a palindrome");  
  
        }  
}  
