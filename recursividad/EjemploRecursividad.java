/**
 * EjemploRecursividad
 */
public class EjemploRecursividad {
    public static int factotialR(int n) {
        if (n>1) {
            return factotialR(n-1)*n;
        }
        return 1;
    }

    public static int fibonaciR(int n) {
        if (n>1){
            return fibonaciR(n-1)+fibonaciR(n-2);
        }
        return n;
    }

    public static double potencia(int base, int exponente) {
        if (exponente ==0){
            return 1;
        }else if (exponente==1){

        }else if 
    }


    public static void main(String[] args) {
        System.out.println(factotialR(10));
        System.out.println("fibonacci");
        System.out.println(fibonaciR(6));
    }
}
