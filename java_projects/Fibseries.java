import java.util.HashMap;
import java.util.Scanner;

public class Fibseries{
    public static void main(String[] args) {
        // Create a HashMap to store the lexicon categories and their count
        HashMap<Integer, Integer> lexiconCategories = new HashMap<>();
        int FibLength;

        Scanner sc = new Scanner(System.in); //create object
        System.out.print("Please enter length: ");
        FibLength = sc.nextInt();
        int[] num = new int[FibLength];
        //initialized first element to 0
        num[0] = 0;

        //initialized second element to 1
        num[1] = 1;
        //New number should be the sum of the last two numbers of the series.
        for (int i = 2; i < FibLength; i++) {
            num[i] = num[i - 1] + num[i - 2];
        }
        //Print Fibonacci Series
        System.out.println("Fibonacci Series: ");
        for (int i = 0; i < FibLength; i++) {
            System.out.print(num[i] + " ");

            // Check the lexicon category of each element
            for (char c : Integer.toString(num[i]).toCharArray()) {
                int category = Character.getType(c);
                if (lexiconCategories.containsKey(category)) {

                    lexiconCategories.put(category, lexiconCategories.get(category) + 1);
                } else {
                    lexiconCategories.put(category, 1);
                }
            }
        }
        // Print out the lexicon categories and their count
        System.out.println("\nLexicon Categories: ");
        for (int category : lexiconCategories.keySet()) {
            System.out.println(category + ": " + lexiconCategories.get(category));
        }
    }
}
