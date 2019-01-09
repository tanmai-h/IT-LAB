import java.util.*;
public class  four {
	public static void main(String args[]) {
		Scanner obj = new Scanner (System.in);
		Scanner obj1 = new Scanner (System.in);
		int m1,n1,m2,n2;
		System.out.print("Enter order of 1st matrix: ");
			m1 = obj.nextInt();
		System.out.print("Enter order of 2nd matrix: ");
			m2 = obj.nextInt();

		int a[][] = new int[m1][m1];
		int b[][] = new int[m2][m2];

		System.out.println("enter mat1");
		for(int i=0; i<m1; i++){
			String s = obj1.nextLine();
			Scanner st = new Scanner(s);
			for(int j=0;j<m1;j++)
				a[i][j]=st.nextInt();
		}
		System.out.println("enter mat2...");
		for(int i=0; i<m2; i++){
			String s = obj1.nextLine();
			Scanner st = new Scanner(s);
			for(int j=0;j<m2;j++)
				b[i][j]=st.nextInt();
		}
		if(m1==m2) {
			int sum[][] = new int[m1][m1];
			int sub[][] = new int[m2][m2];
			for(int i=0;i<m1;i++){
				for(int j=0; j<m1;j++){
					sum[i][j]=a[i][j]+b[i][j];
					sub[i][j]=a[i][j]-b[i][j];
				}
			}
			System.out.println("ADD");
			for(int i=0;i<m1;i++){
				for(int j=0; j<m1;j++){
					System.out.print(sum[i][j]+" ");
				}
				System.out.println();
			}

			System.out.println("SUBTRACT");
			for(int i=0;i<m1;i++){
				for(int j=0; j<m1;j++){
					System.out.print(sub[i][j]+" ");
				}
				System.out.println();
			}
		}
		else {
			System.out.println("\n\ncant add n subtract ");
		}

		System.out.print("\n\n\n");

		//b = new int[m1][m1];
		System.out.println("transpose matrix of A ");
		for(int i=0;i<m1;i++){
			for(int j=0; j<m1;j++){
				System.out.print(a[j][i]+" ");
			}
			System.out.println();
		}
		System.out.println("\n\n");

		System.out.print("Enter search element (searching in mat1): ");
		int search = obj.nextInt();
		int f = 0;
		for(int i=0;i<m1;i++){
			for(int j=0; j<m1;j++){
				if(a[i][j]==search){
					System.out.println("found at...");
					System.out.println("row : "+i+" col : "+j);
					f = 1;
					break;
				}
			}
		}

		if(f == 0) System.out.println("not found\n");
	}
}