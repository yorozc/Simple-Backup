# Module 2

## User input for conditional statements
- Java scanner library
```Java
Scanner keyboard = new Scanner(System.in);
int age = keyboard.nextInt(); //scans number from keyboard
float money = keyboard.nextFloat();
String name = keyboard.nextLine();

//Switch Statement

switch(variableThatIsCompared){
    case compare1:

        default: 
}

Scanner keyboard = new Scanner(System.in);

System.out.println("Enter flavor");
String iceCreamFlavor = keyboard.nextLine();

switch(icecreamFlavor){
    case "Strawberry";
        System.out.println("Strawberry yum");
        break;
    
    case "Oreo":
        System.out.println("Oreo Yum");
        break;

    case "Chicken":
        System.out.println("wtf");
        break;
    
    default:
        System.out.println("I'll just drink water");
        break;
}
```