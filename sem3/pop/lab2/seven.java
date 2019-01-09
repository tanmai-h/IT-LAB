import java.util.*;

class price{
	int price; String s;

	price(String s, int n) {
		this.price = n;
		this.s = s;
	}
}

class seven {

	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		price [] arr = {new price("soap", 2),new price("bucket", 6),new price("mug", 8),new price("bed", 10)};

		System.out.println("prdts soap mug bucket bed");
		System.out.println("enter prdt qty");
		String s  = sc.next(); int n = sc.nextInt();

		for(int i = 0; i < 4; i++) {
			if(s.equals(arr[i].s)) {
				System.out.println("unitprice: " + arr[i].price + ",  totalprice: " + n*arr[i].price);
				return ;
			}
		}

		System.out.println("prdt not found");
	}
}

	
 