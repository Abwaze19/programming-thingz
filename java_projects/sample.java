import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class sample {
    public static void main(String[] args) {
        String program = "";
                         int FibLength;
                         Scanner sc = new Scanner(System.in);
                         System.out.print("Please enter length: ");
                         FibLength = sc.nextInt();
                         int[] num = new int[FibLength];
                         num[0] = 0;
                         num[1] = 1;

                         for (int i = 2; i < FibLength; i++) {
                             num[i] = num[i - 1] + num[i - 2];
                             System.out.println("Fibonacci Series: ");
                         }
                         for (int i = 0; i < FibLength; i++) {
                         System.out.print(num[i] );
                         }
        int keywordsCount = 0;
        int  identifiersCount = 0;
        int constantsCount = 0;
        int operatorsCount = 0;

        // keywords
        String keywordsRegex = ("import|public|static|void|int|new|for|System|out|println|print");
        Pattern keywordsPattern = Pattern.compile(keywordsRegex);
        Matcher keywordsMatcher = keywordsPattern.matcher(program);
        while (keywordsMatcher.find()) {
            keywordsCount++;
        }

        // identifiers
        String identifiersRegex = ("[a-zA-Z_$][a-zA-Z\\d_$]");
        Pattern identifiersPattern = Pattern.compile(identifiersRegex);
        Matcher identifiersMatcher = identifiersPattern.matcher(program);
        while (identifiersMatcher.find()) {
            String identifier = identifiersMatcher.group();
            // exclude keywords
            if (!identifier.matches(keywordsRegex)) {
                identifiersCount++;
            }
        }

        // constants
        String constantsRegex = ("d+");
        Pattern constantsPattern = Pattern.compile(constantsRegex);
        Matcher constantsMatcher = constantsPattern.matcher(program);
        while (constantsMatcher.find()) {
            constantsCount++;
        }

        // operators
        String operatorsRegex = "[+\\-*/%=<>!&|^]";
        Pattern operatorsPattern = Pattern.compile(operatorsRegex);
        Matcher operatorsMatcher = 

operatorsPattern.matcher(program);
        while (operatorsMatcher.find()) {
            operatorsCount++;
        }

        System.out.println("Keywords: " + keywordsCount);
        System.out.println("identifiers: " + identifiersCount);
        System.out.println("constants: " + constantsCount);
        System.out.println("operators: " + operatorsCount);


    }
    
}
