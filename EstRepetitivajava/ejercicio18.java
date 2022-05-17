package EstRepetitiva;
import java.util.Scanner;
/**
 * ejercicio18
 */
public class ejercicio18 {
    static Scanner lt=new Scanner(System.in);

    public static void impuestoVehiculo() {
        //Definir Variables 
        String cateV="";
        int cantidad=0;
        double costV; impUnit=0; impTotal=0; totalImpV=0;
        //Datos de entrada y proceso y salida
        for (int i = 0; i < 3; i++){
            System.out.println("Ingrese Cantidad Vehiculos de Categotia" + (i+1)+": ");
            cantidad=lt.nextInt();
            System.out.println("Ingrese el precio de la categoria "+(i+1)+":");
            costV=lt.nextDouble();
            if(i==0){
                impUnit=costV*0.10;
            }else if(i==1){
                impUnit=costV*0.07;
            }else{
                impUnit=costV*0.05;
            }
            impTotal=impUnit*cantidad;
            System.out.println("Impuesto de Categoria "+(i=1)+" es:"+impUnit);
            System.out.println("Impuesto Total de Categoria "+(i+1)+"es:"+impTotal);
            totalImpV=totalImpV+impTotal;
        }
        System.out.println("Impuesto Total de los Vehiculos:"+impTotal);
    }
    public static void main(String[] args) {
        impuestoVehiculo18();
    }
}
