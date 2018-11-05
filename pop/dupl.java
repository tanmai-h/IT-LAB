import java.util.Scanner;

class dupl {
    public static void main(String args[]) {
        String s;
        Scanner sc = new Scanner(System.in);  
        s = sc.nextLine();
        int []ar = new int[26];

        
        for (int i = 0; i < s.length(); i++){
            ar[(int)s.charAt(i) - (int)'a']++;
        }
        for(int i = 0; i < 26; i++) {
            if(ar[i] >= 2)
                System.out.print((char)(i + (int)('a')));
        }
    }
}