import java.util.Scanner;

public class Main{
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        int result = 0;

        System.out.println("Enter the 1st number:");
        int num1 = keyboard.nextInt();

        System.out.println("Enter the operation +, -, *, /, %");
        
        if(keyboard.hasNextLine()){
            keyboard.nextLine();
        }
        String operation = keyboard.nextLine();

        System.out.println("Enter the 2nd number");
        int num2 = keyboard.nextInt();

        switch (operation) {
            case "+":
                result = num1 + num2;
                break;
            case "-":
                result = num1 - num2;
                break;
            case "*":
                result = num1 * num2;
                break;
            case "/":
                result = num1 / num2;
                break;
        
            default:
                System.out.println("Ineligible Operation");
                System.exit(0);
        }
        System.out.println(num1 + " " + operation + " " + num2 + " = " + result);
    }
}