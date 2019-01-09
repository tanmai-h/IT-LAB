import java.util.*;

class oddeve {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int a [] = new int[5];
		System.out.print("enter 5 ele");
		for(int i = 0; i < 5; i++) a[i] = sc.nextInt();

		for(int i = 0; i < 5; i++) {if(a[i]%2 == 0) a[i] = 0; else a[i]=1; System.out.print(a[i] + " ");}
	}
}