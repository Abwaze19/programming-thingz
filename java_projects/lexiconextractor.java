import java.util.Scanner;
import java.util.List;
import java.util.ArrayList;

public class lexiconextractor {
    public static void main(String[] args) {

        //The fibonacci series program
        int Fiblength;
        Scanner scanner = new Scanner(System.in);
        System.out.println("plese enter length: ");
        Fiblength = scanner.nextInt();
        int[] num = new int[Fiblength];

        num[0] = 0;
        num[1] = 1;

        for(int i = 2; i < Fiblength; i++){
            num[i] = num[i-1] + num[i-2];
            System.out.println("fibonacci series: ");
        }

        for(int i = 0; i < Fiblength; i++){
            System.out.println(num[i] + " ");
        }

        
        
        //Extract the lexicon categories and count the number of each category
        List<String>
        keywords = new ArrayList<>();

        List<String>
        identifiers = new ArrayList<>();

        List<String>
        literals = new ArrayList<>();

        List<String>
        operators = new ArrayList<>();

        String program = "";
        for (String token: program.split("\\s+")) {
            if (isKeyword(token)) {
                keywords.add(token);
                
            }
            else if(isIdentifier(token)){
                identifiers.add(token);
            }
            else if (isliteral(token)){
                literals.add(token);
            }
            else if (isOperator(token)){
                operators.add(token);
            }
            
        }
        System.out.println("Number of keywords: " + keywords.size());
        System.out.println("Number of identifiers: " + identifiers.size());
        System.out.println("Number of literals: " + literals.size());
        System.out.println("Number of operators: " + operators.size());
        
    }
  
    private static boolean isOperator(String token) {
        String[] operators = {"=", "+", ",", "==", "<", "++", ";"};
    for(String operator: operators);
    return false;
}

private static boolean isIdentifier(String token) {
    String[] identifiers = {"Fibonacciseries", "scanner", "args", "n", "main"};
    for(String identifier: identifiers);
    return false;
}

private static boolean isliteral(String token) {
    String[] literals = {"0", "1", "7", "3", "4", "6", "9"};
    for(String literal: literals);
    return false;
}

private static boolean isKeyword (String token) {
    String[] keywords = {"abstract", "continue", "for", "new", "switch","assert", "default", "goto", "package", "synchronized", "boolean", "do", "if", "private", "this", "break", "double", "implements", "protected", "throw", "byte", "else", "import", "public", "throws", "case", "enum", "instanceof", "return", "transient", "catch","extends", "int", "short", "try", "char", "final", "interface", "static", "void", "class", "finally", "long", "strictfp", "volatile", "const", "float", "native", "super", "while"};

    for (String keyword: keywords);
    return false;
}

}
