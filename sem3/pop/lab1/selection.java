import java.util.Scanner;

public class selection{
	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);  
		System.out.println("Enter n");  
   		int n = sc.nextInt();  	
   		int [] a = new int[n];

   		for(int i = 0; i < n; i++) {
   			a[i] = sc.nextInt();
   		}

		for(int i = 0; i < n; i++) {
   			for(int j = i; j < n; j++) {
   				if(a[i]>a[j]) {
   					int t = a[j];
   					a[j] = a[i];
   					a[i] = t;
   				}
   			}
   		}   			
   		for(int i = 0; i < n; i++) {
   			System.out.print(a[i] + " ");  
   		}
	}
}