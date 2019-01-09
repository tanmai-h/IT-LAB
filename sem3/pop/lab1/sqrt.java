import java.util.Scanner;
import java.*;

public class sqrt{
	static double fu(double x) {
		return x*x;
	}
	static double derv(double x) {
		return 2*x;
	}

	static double sqrt(float a) {
		int n = 1000;
		double E = 0.0001;

		double xn = a/2;
		
		double h = fu(xn) / derv(xn);
		while(Math.abs(h) > E) {
			h = fu(xn) / derv(xn);
			xn = xn - h;
		}

		return xn;
	}
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		System.out.println(Math.sqrt(n));
		System.out.println(sqrt(n));
	}
}