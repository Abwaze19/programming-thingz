import java.util.Scanner;

public class program{
    static int keywordcount = 0;
    static int identifiercount = 0;
    static int literalcount = 0 ;

    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Enter the number of terms: ");
            int n = scanner.nextInt();
            int[] series = new int[n];

            series[0] = 0;
            series[1] = 1;

            for(int i = 2; i < n; i++){
                series[i] = series[i-1] + series[i-2];

                keywordcount++;
                identifiercount++;
                literalcount++;
            }

            System.out.print("Fibonacci series: ");

            for(int i = 0; i < n; i++){
                System.out.println(series[i] + "");
                keywordcount++;
                identifiercount++;
                literalcount++;
            }
        }
        System.out.println("keywords: " + keywordcount);
        System.out.println("identifiers: " + identifiercount);
        System.out.println("literals: " + literalcount);

    }


}