import java.rmi.*;
import java.rmi.server.*;
interface Adder extends Remote{
   public int add(int x,int y) throws        RemoteException;
}

public class AdderRemote extends UnicastRemoteObject implements Adder{
   AdderRemote()throws RemoteException{
      super();
   }

public int add(int x,int y){
   return x+y;
   }
   public static void main(String args[]){
      try{
         Adder ob=new AdderRemote();
         Naming.rebind("rmi://localhost:6000/adder",ob);
      }catch(Exception e){
         System.out.println(e);
      }
   }
}
