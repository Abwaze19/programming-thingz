
namespace guessingame
{
    class Program
    {
        static void Main(string[] args)
        {
         Random random = new Random();
         bool PlayAgain = true;
         int min = 1;
         int max = 100;
         int guess = 0;
         int number = random.next(min, max + 1);;
         int guesses = 0;
         string response;

         while (PlayAgain)
         {
            response = "";
            
            while (guess != number)
                
                guess++;
            
                 Console.WriteLine("guess a number between " + min + "-" + max);
                 
                 guess = convert.Toint32(Console.ReadLine());
                 Console.WriteLine("Guess: " + guess);

                 if (guess > number)
                 {
                    Console.WriteLine(guess +" is too HIGH");
                    
                 }
                 else if (guess < number)
                 {
                    Console.WriteLine(guess + " is too LOW");
                 }
            }

            Console.WriteLine("Number: " + number);
            Console.WriteLine("you WIN");
            Console.WriteLine("Guesses: " + guesses);

            Console.WriteLine("would you like to playagain (Y/N)");
            response = Console.ReadLine();
            response = response.Toupper();

            if (response = "Y")
            {
                PlayAgain  = true;
            }
            else
            {
                PlayAgain = false;
            }
             Console.WriteLine("thanks for playing!.....i guess");
         }

    }
}