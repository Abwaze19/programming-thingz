import java.util.Scanner;

public class FibonacciSeries{
    public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Enter the number of terms in the fibonacci series: ");
            int n = scanner.nextInt();
            int a = 0,b = 1, c;

            System.out.println("Fibonacci series: " + a + "" + b + "");
            for (int i = 2; i < n; i++) {
                c = a + b;
                System.out.println(c + "");

                a = b;
                b = c;
                
            }
        
    }
}