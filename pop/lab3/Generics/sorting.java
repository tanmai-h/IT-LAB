
public class sorting<E>{
	public static <E extends Comparable<? super E>> void sortArray(E arr[]) {
		E t;
		for(int i=0;i<arr.length-1;i++) {
			int minIn=i;
			for(int j=i+1;j<arr.length;j++) {
				if(arr[j].compareTo(arr[minIn])<0) {
					minIn=j;
				}
			}
			t=arr[i];
			arr[i]=arr[minIn];
			arr[minIn]=t;
		}
		for(E ele:arr) {
			System.out.print(ele + " ");
			
		}
		System.out.println();
	}
	public static void main(String[] args) {
		sorting<Integer> obj1=new sorting<Integer>();
		sorting<String> obj2=new sorting<String>();
		Integer [] a={9423,3,22,-1,0};
		String [] b= {"pop","x","l"};
		obj1.sortArray(a);
		obj2.sortArray(b);
	}

}
