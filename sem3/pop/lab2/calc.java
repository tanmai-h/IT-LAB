import java.util.Scanner;

class calc{
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		System.out.println("Enter  2 numbers");
		int i= input.nextInt();
		int j= input.nextInt();
		System.out.println("Now enter the operation");
		System.out.println(" addition 1 \n substraction 2 \n multiplication 3\n division 4 \n moduli 5 ");
		int k = input.nextInt();
		switch(k){
			
			case 1:
			System.out.println(i+j);
			break;
			case 2:
			System.out.println(i-j);
			break;
			case 3:
			System.out.println(i*j);
			break;
			case 4:
			System.out.println(i/j);
			break;
			case 5:
			System.out.println(i%j);
			break;
			default :
			
			System.out.println("entered wrong no.");
			
		}
	}
}