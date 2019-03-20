import java.rmi.*;
import java.rmi.registry.*;
public class client{
    public static void main(String args[]){
        try {
	System.out.println("Connecting");
            Adder stub= (Adder) Naming.lookup("rmi://localhost:6000/adder");
            System.out.println("returned msg: " + stub.add(34,4));
        }catch(Exception e){    
            System.out.println(e);
        }
    }
}
