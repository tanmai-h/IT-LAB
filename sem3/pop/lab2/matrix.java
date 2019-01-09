import java.util.*;

class matrix{
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		System.out.print("enter nxn order");
		int n; n = sc.nextInt();

		int a[][] = new int[n][n];
		for(int i = 0; i < n; i++) 
			for(int j = 0; j < n; j++) a[i][j] = sc.nextInt();
		
	}
}

	
 