import java.util.concurrent.atomic.AtomicReference;

public class ECUACION2FGENERAL {

    // Variables globales para compartir resultados entre hilos utilizando AtomicReference para manejar la concurrencia
    private static AtomicReference<Double> resultado_b2 = new AtomicReference<>(null);  // Almacena el valor de b^2
    private static AtomicReference<Double> resultado_4ac = new AtomicReference<>(null); // Almacena el valor de 4*a*c
    private static AtomicReference<Double> resultado_raiz = new AtomicReference<>(null); // Almacena el valor de la raíz de (b^2 - 4*a*c)
    private static AtomicReference<Double> resultado_x1 = new AtomicReference<>(null);  // Almacena la solución x1 de la ecuación
    private static AtomicReference<Double> resultado_x2 = new AtomicReference<>(null);  // Almacena la solución x2 de la ecuación

    // Hilo para calcular b^2
    static class CalcularB2 extends Thread {
        private final double b;  // Almacena el valor del coeficiente b

        public CalcularB2(double b) {
            this.b = b;  // Constructor que inicializa b
        }

        @Override
        public void run() {
            // Calcula b^2 y lo guarda en resultado_b2
            resultado_b2.set(b * b);
            System.out.println("Proceso 1: Calculando b^2 = " + resultado_b2.get());
        }
    }

    // Hilo para calcular 4*a*c
    static class Calcular4ac extends Thread {
        private final double a, c;  // Almacena los coeficientes a y c

        public Calcular4ac(double a, double c) {
            this.a = a;  // Constructor que inicializa a
            this.c = c;  // Constructor que inicializa c
        }

        @Override
        public void run() {
            // Calcula 4*a*c y lo guarda en resultado_4ac
            resultado_4ac.set(4 * a * c);
            System.out.println("Proceso 2: Calculando 4*a*c = " + resultado_4ac.get());
        }
    }

    // Hilo para calcular la raíz cuadrada de (b^2 - 4*a*c)
    static class CalcularRaiz extends Thread {

        @Override
        public void run() {
            // Espera activa hasta que se hayan calculado b^2 y 4*a*c
            while (resultado_b2.get() == null || resultado_4ac.get() == null) {
                Thread.yield(); // Cede el control del procesador
            }
            // Calcula el discriminante b^2 - 4*a*c
            double discriminante = resultado_b2.get() - resultado_4ac.get();
            if (discriminante >= 0) {  // Verifica si el discriminante es no negativo (hay soluciones reales)
                // Calcula la raíz cuadrada del discriminante y lo guarda en resultado_raiz
                resultado_raiz.set(Math.sqrt(discriminante));
                System.out.println("Proceso 3: Calculando la raíz de " + discriminante + " = " + resultado_raiz.get());
            } else {
                // No hay soluciones reales si el discriminante es negativo
                System.out.println("Proceso 3: Discriminante negativo, no hay soluciones reales.");
            }
        }
    }

    // Hilo para calcular las dos soluciones de la ecuación
    static class CalcularSoluciones extends Thread {
        private final double a, b;  // Almacena los coeficientes a y b

        public CalcularSoluciones(double a, double b) {
            this.a = a;  // Constructor que inicializa a
            this.b = b;  // Constructor que inicializa b
        }

        @Override
        public void run() {
            // Espera activa hasta que se haya calculado la raíz cuadrada
            while (resultado_raiz.get() == null) {
                Thread.yield(); // Cede el control del procesador
            }
            // Calcula la primera solución de la ecuación cuadrática
            resultado_x1.set((-b + resultado_raiz.get()) / (2 * a));
            // Calcula la segunda solución de la ecuación cuadrática
            resultado_x2.set((-b - resultado_raiz.get()) / (2 * a));
            System.out.println("Proceso 4: Calculando x1 = " + resultado_x1.get());
            System.out.println("Proceso 5: Calculando x2 = " + resultado_x2.get());
        }
    }

    // Método principal para resolver la ecuación usando hilos
    public static void resolverEcuacion(double a, double b, double c) {
        System.out.println("Resolviendo ecuación " + a + "x^2 + " + b + "x + " + c + " = 0");

        // Crear los hilos para cada cálculo
        Thread hilo_b2 = new CalcularB2(b);  // Crea el hilo para calcular b^2
        Thread hilo_4ac = new Calcular4ac(a, c);  // Crea el hilo para calcular 4*a*c
        Thread hilo_raiz = new CalcularRaiz();  // Crea el hilo para calcular la raíz
        Thread hilo_soluciones = new CalcularSoluciones(a, b);  // Crea el hilo para calcular las soluciones

        // Iniciar los hilos
        hilo_b2.start();  // Inicia el hilo para calcular b^2
        hilo_4ac.start();  // Inicia el hilo para calcular 4*a*c
        hilo_raiz.start();  // Inicia el hilo para calcular la raíz
        hilo_soluciones.start();  // Inicia el hilo para calcular las soluciones

        // Espera a que todos los hilos terminen su ejecución
        try {
            hilo_b2.join();  // Espera a que termine el hilo que calcula b^2
            hilo_4ac.join();  // Espera a que termine el hilo que calcula 4*a*c
            hilo_raiz.join();  // Espera a que termine el hilo que calcula la raíz
            hilo_soluciones.join();  // Espera a que termine el hilo que calcula las soluciones
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("Ecuación resuelta.");
    }

    // Método principal del programa
    public static void main(String[] args) {
        double a = 1;  // Coeficiente de x^2
        double b = -3; // Coeficiente de x
        double c = 2;  // Término independiente

        // Resolver la ecuación cuadrática
        resolverEcuacion(a, b, c);
    }
}
