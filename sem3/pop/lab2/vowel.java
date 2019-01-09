import java.util.Scanner;

class vowel{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("Enter one character");
		
		String j= input.nextLine();
		
		j=j.toLowerCase();
		
		switch(j){
				
			case "a":
			case "u":
			case "o":
			case "i":
			case "e":
			System.out.println("vowel");
			break;
			
			default :
			System.out.println("consonent");
				
		}
	}
}