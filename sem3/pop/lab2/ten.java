import java.util.*;
import java.io.*;

public class ten {
	public static void main(String args[]) {
		try {
			Scanner obj = new Scanner(new File("q.txt"));
			int count=0;
			while(obj.hasNextLine()) {
				obj.nextLine();
				count++;
			}
			System.out.println("Number of lines : "+count);
		}catch (FileNotFoundException e){
			System.out.println("File not found...");
		}
	}
}