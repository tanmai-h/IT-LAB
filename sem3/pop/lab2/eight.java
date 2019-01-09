import java.util.*;

class eight{
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		System.out.print("enter sentence: ");
		String s = sc.nextLine();

		int l = 0;

		for(int i = 0; i < s.length(); i++) {
			if(s.charAt(i) != ' ') l++;
			else {
				System.out.print(l + " ");		
				l = 0;
			}
		}
		System.out.println(l + "");
	}
}


	