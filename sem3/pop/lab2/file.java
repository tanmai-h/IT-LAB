import java.util.*;
class Student {
	private int id;
	private String name;
	public int getId() { return id;}
	public String getName() {return name;}
	public void setId(int id) {this.id=id;}
	public void setName(String name) {this.name=name;}
}
class six {
	public static void main(String args[]) {
		Scanner obj = new Scanner(System.in);
		Scanner obj1 = new Scanner(System.in);
		System.out.print("Enter n : ");
		int n = obj.nextInt();
		Student a[] = new Student[n];
		for(int i=0;i<n;i++){
			System.out.print("Enter id : ");
			int id = obj.nextInt();
			System.out.print("Enter name : ");
			String name = obj1.nextLine();	
			a[i] = new Student();
			a[i].setId(id);
			a[i].setName(name);
		}
		System.out.print("Enter name to search : ");
		String name = obj1.nextLine();
		System.out.println("");
		for(int i=0;i<n;i++) {
			if(name.equals(a[i].getName())) {
				
				System.out.println("Student id : "+a[i].getId());
				System.out.println("Student name : "+a[i].getName());
				break;
			}
		}
	}
}
