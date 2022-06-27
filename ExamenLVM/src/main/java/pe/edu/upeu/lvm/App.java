package pe.edu.upeu.lvm;

import java.util.Scanner;

import pe.edu.upeu.lvm.examen.ResolucionExamen;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
        Scanner leer=new Scanner(System.in);
        int n;
        System.out.println("Ingrese el numero de algoritmo(2-5):");
        n=leer.nextInt();
        switch (n) {
            case 2: new ResolucionExamen().examen02lvm(); break;
            case 3: new ResolucionExamen().examen03lvm(); break;
            case 4: new ResolucionExamen().examen04lvm(); break;
            case 5: new ResolucionExamen().examen05lvm(); break;
            default: System.err.println("Esa opcion no existe"); break;
        }
    }

}
