import java.util.Scanner;

class arm {
    public static void main(String args[]) {
        int s;
        Scanner sc = new Scanner(System.in);  
        s = sc.nextInt();
        //int []ar = new int[26];
        int t = s, sum = 0;
        while(s > 0 ) {
            int d = s%10;
            sum += d*d*d;
            s = s/10;
        }
        if(sum == t)
            System.out.println("armstrong");
        else
        System.out.println("not armstrong");
    }
}