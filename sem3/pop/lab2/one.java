import java.util.Scanner;

class one{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("Enter one character");
		
		String j= input.nextLine();
		
		j = j.toLowerCase();
		
		switch(j){
				
			case "a":
			case "u":
			case "o":
			case "i":
			case "e":
				System.out.println("vowel");
			break;
			//if (Character.isLetter(j)) 
			case "q":
			case "w":
			case "r":
			case "t":
			case "y":
			case "s":
			case "d":
			case "f":
			case "g":
			case "h":
			case "j":
			case "k":
			case "l":
			case "z":
			case "x":
			case "c":
			case "v":
			case "b":
			case "n":
			case "m":
				System.out.println("consonent"); break;
			default :
				System.out.println("neither consonent nor vowel");
				
		}
	}
}