import java.util.Stack;

public class PilaExample{
    public static void main(Strings[] args){
      Stack<Integer> pila = new Stack<>();
      
      pila.push(10);
      pila.push(20);
      pila.push(30);
      
      while (!pila.empty()){
        System.out.print(pila.peck()+" ");
        pila.pop();
      
      }    
    }
}
