import java.util.*;

class palin{
   public static void main(String[] args){
		Scanner sc=new Scanner(System.in);  
		System.out.println("Enter string");  
		
		String name = sc.next();
		
		int f = 1;
			
		for(int x =0;x < name.length(); x++) {
			if( name.charAt(x) != name.charAt(name.length()-x-1)){
				f = 0;
				break;
		  	}
		}

		if(f == 1) System.out.println("palindrome");  
		else System.out.println("not palindrome");  
	}
}
