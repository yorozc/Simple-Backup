# Encapsulation and data hiding
- User does not need to know how things work which is what encapsulation is

- Restricts direct access to object's elements
- declare variables or methods within a class as private to prevent change coming outside the class
- Can use getters and setters
- getters read values
- setters allow the change of a value

- Using private instead of public is how you prevent methods or variables from being accessed outside the class. 
- Private methods will still execute but they won't be accessible
- protected
    - accessible by a child class and others in the family group
    - protected property is allowed access from outside the class via objects of the class

## Access modifiers
- determines who sees and uses parts of a program
- public, private, and protected are the access modifiers
- they don't change how the method works but they change the only area they are accessible from
- **Packages**
    - math class java.util
    - java.lang contains strings and others
- Default packages exist

## abstract classes
- identify common properties between both objects you are creating
- moving the common properties to a common class 
    - just holds the properties
    - abstract classes hold the common code for the different objects
    - prevents an object being made of the useless skeletion that makes up other objects
- Placeholder for common code
- Implement method in child class
- if you inherit from abstract class, that means you have to implement the methods in the subclasses so java doesn't think the subclasses are also an abstract class

```java
public class abstract Robot{
    private int batteryCharge;
    private int modeOfOperation;
    //other common code like setters and getters

    public abstract void setChoice();
    public abstract void takeAction();
}
```