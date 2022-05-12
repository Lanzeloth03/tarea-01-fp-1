package EstRepetitiva;

import java.util.Scanner;

/**
 * ejercicioL
*/
public class ejerciciosL {




public static void imprimirwhileN1_20() {
    int numInit=1;
     while (numInit<=20) {
        System.out.println(numInit);
        numInit=numInit+1;
     }
    }   
public static void imprimirDowhileN1_20(){
    int numInit=1;
    do {
        System.out.print(numInit);
        numInit++;
    } while (numInit<=1);
}

public static void imprimirForN1_20() {   
    for (int numInit = 1; numInit <= 20; numInit++){
        System.out.println(numInit);
    }
    
}
public static void nombreinvertida() {
    Scanner lt=new Scanner(System.in);
    System.out.println("ingrese su nombre:");
    String nombre=lt.next();
    for (int i = nombre.length()-1; i >=0; i--){
        System.out.println(nombre.charAt(i));
    }

}
 public static void main(String[] args) {

    /* System.out.println("imprime While:"); imprimirwhileN1_20();
     System.out.println("imprime Do while:"); imprimirDowhileN1_20();
     System.out.println("imprime for:"); imprimirForN1_20();*/
    
     nombreinvertida();
    }
}
