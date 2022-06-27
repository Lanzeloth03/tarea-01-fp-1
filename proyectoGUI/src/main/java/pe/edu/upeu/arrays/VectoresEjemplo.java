package pe.edu.upeu.arrays;

/**
 * VectoresEjemplo
 */
public class VectoresEjemplo {

    public void vectoresx() {
        int edades[]=new int[10];//forma uno 
        edades=new int[12];
        edades[0]=20;
        edades[1]=18;
        edades[11]=30;
        System.out.println("Edades");
        System.out.println("Indice 0:"+edades[0]);
        System.out.println("Indice 11:"+edades[11]);
        //forma dos 
        System.out.println("forma dos");
        int edadesx[]={20,18,30,40,16};
        System.out.println(edadesx.length);
        System.out.println("indice 0:"+edadesx[0]);
        System.out.println("indice 4:"+edadesx[4]);

    }

    public void vectorobjetos() {
        Persona[] p=new Persona[27];
        p[0].codigo="200410564";
        p[0].nombres="David Mamani";
        p[0].asistencia=true;
        Persona[] pp={
            new Persona(Codigo:"", nombre:"", true) };
    }

    public static void main(String[] args) {
        VectoresEjemplo objx=new VectoresEjemplo();
        objx.vectoresx();

    }
}