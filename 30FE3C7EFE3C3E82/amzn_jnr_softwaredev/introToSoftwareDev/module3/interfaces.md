# Interfaces
- helps implement multiple inheritence
- a type of class in java
- only have abstract methods (no code inside)
- name of interface must have -able at the end because of naming conventions

- **interfaces are used to force implementing classese to implement functionality**

```java
interface Flyable{
    int maxMetersPerHour = 240; //automatically is public static and final (constant)

    public void flying(); //declared but not implemented
}

class Duck implements Flyable{
    @Override
    public void flying(){

    }
}


class Duck extends Animal implements Flyable{

}

class Duck implements Flyable, Walkable{

}
```
- classes can only implement Interfaces
- class will define or give body to all methods within an interface
- class becomes abstract if you don't implement the methods declared within an interface

Inheritence with interface
```java
interface sonicSpeedFlyable extends Flyable{
    public void hyperSonicFlying();
}
```
- when class implements sonicSpeedFlyable then it must implement all methods declared between both 
the sub and super interface

```java
Flyable flyable = new Duck();
```
- can create an object of the interface but it must be an object of a class that
implements the interface
- can only use interface methods not the methods of the object you are referencing to.

- ensure consistent functionality across different parts of the program

- To check if a class is implementing an interface use the "instanceof" keyword