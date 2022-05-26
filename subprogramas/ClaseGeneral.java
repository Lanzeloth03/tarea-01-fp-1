
    //import Subprogramas.aritmetica

public class ClaseGeneral {
    
    public static void main(String[] args) {
        aritmetica a=new aritmetica();
        
        int resultado=a.sumar(5, 3);
        System.out.println("Suma: "+resultado);

        aritmetica obj=new aritmetica(5, 3);
        resultado=obj.multiplicar();
        System.out.println("multiplicacion: "+resultado);
    }
}
