import java.io.*;
import java.util.Scanner;
public class statement_reverse {
    public static void main(String a[]) throws Exception {
        String strarr[]; //array which will hold splitted strings of the statement
        String st, result = ""; //contains user input statement 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Enter the Statement:");
        st = br.readLine();
        String split[] = st.split(" ", 0);
        for (String x: split) {
            result = x + " " + result;
        }
        System.out.println("The reverse is: " + result);
    }

}
   
 


