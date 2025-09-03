# Classes and Objects

## Methods
- methods are basically functions
- order matters in which they are called

## Classes and Objects
- acts like a blueprint 
- defines characteristics and actions
- objects are instances of the class
    - can change values within the class for each instance using the dot notation


## Grouping methods
- Building BMI calculator

```java
public class Main{
    public static void main(String[] args){
        double weightInPounds1 = 154.0;
        double heightInInches1 = 70.0;
        double bmi1 = weightInPounds1 / (heightInInches * heightInInches1) * 703;
        double weightInPounds2 = 187.0;
        double heightInInches2 = 74.0;
        double bmi2 = weightInPounds2 / (heightInInches2 * heightInInches2) * 703;
        System.out.println("BMI of USer 1: " + bmi1); 
    }
}
```
- this way of making a bmi calender is not very good
- Introducing grouping methods
    - recudes code repitition
    - improved readability
    - easier maintenance

```java
public class BMICalculator{
    public double calculateBmiImperial(double weightInPounds, double heightInInches){
        return weightInPounds / (heightInInches * heightInInches) * 703;
    }

    public double calculateBmiMetric(Double weightInKilos, double heightInMeters){
        return weightInKilos / (heightInMeters * heightInMeters);
    }
}

public class Main{
    public static void main(String[] args){
        BMICalculator bmiCalculator = new BMICalculator();

        double weightInPounds = 154.0;
        double heightInInches = 70.0
        double bmiImperial = bmiCalculator.calculateBmiImperial(weightInPounds, heightInInches);

        double weightInKilos = 70.0;
        double heightInMeters = 1.82;
        double bmiMetric = bmiCalculator.calculateBmiMetric(weightInKilos, heightInMeters);
    }
}
```

## Components of an object: Attributes and actions
- What is an object
    - object holds data that define its characteristics and methods that define its behavior

## Creating attributes and actions
- Start with class
- Then make your attributes
    - attributes describe a class, hold specific details
    also known as member variables
- By creating a new instance of a car, you can have many cars
```java
public class Main{
    public static void main(String[] args){
        Car colorado = new Car();
        //this is an instance of the car class
    }
}
```
- With the use of these instances you can make many unique cars who have differences among their variables that they all share. 

- Each class can have an action (functions/methods)

- **toString**: creating a toString() function is good so it can display the attributes to help with testing. 
    - make sure to have override 

## Constructors - Instantiatign objects with different states
- Initializes object's attribute values during creation

- Three types of constructors
    - Default constructors
        - when creating an instance of the class, the default constructor automatically assigns values to the attributes contained within the class
        - it makes strings null and numbers 0
    - **No-argument constructors**
        - allows you to take control of the starting state of the object
        ```java
        class Car{
            String make;
            String model;
            String color;

            public Car(){
                this.make = "Unknown";
                this.model = "Unknown";
                this.color = "Black";
            }
        }
        ```
        - as we can see in the code block above, default values are set
        - **this** keyword is used to refer to the current object being created
    - **Parameterized constructors**
        - Fine-tune the initial state
        ```java
        class Car{
            String make;
            String model;
            String color;

            public Car(String make, String model, String color){
                this.make = make;
                this.model = model;
                this.color = color;
            }
        }
        public class Main{
            public static void main(String[] args){
                Car toyota = new Car("Toyota", "Camery", "Black");
            }
        }
        ```
        - It is probably best to create one where there is no arguments but a default state
        - Then also have a constructor with parameterized constructors
         

