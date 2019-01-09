import java.util.*;

public class insertion {
	static void sort(int arr[]) {
		for(int i = 0; i < arr.length; i++) {
			
			int k = arr[i], j;

			for(j = i-1; j >= 0 && k < arr[j]; j--) {
				arr[j+1] = arr[j];
			}
			arr[j+1] = k;
		}		
	}
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n;
		System.out.print("n: "); n = sc.nextInt();
		int [] a = new int[n];
		for(int i =0; i < n; i++) a[i] = sc.nextInt();

		sort(a);
		for(int i = 0; i < n; i++) System.out.print(a[i] + " ");
	}
}