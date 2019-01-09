import java.util.Scanner;

public class strcp{
	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);  
		System.out.println("enter 2 strings") ;

		String a = sc.next(), b = sc.next();

		b = a;
		System.out.println("copied first to second\n" + a+" "+b)		;		
	}
}
