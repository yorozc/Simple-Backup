# Class hierarchy

## Designing a class hierarchy

## Understanding the importance of class design
- Designing fake racing game
- identifying concrete and abstract classes
- lets players race cars, trucks, other vehicles
    - common things
    - abstract class makes sense
- concrete classes are your objects that inherit from the abstract class
- IS-A and HAS-A relationship
vehicle (IS-A)
|
\--------- car
|
------------Truck
|
------------Motorcycle

Car (HAS-A) (Known as COMPOSITION)
|
----------------Engine class

CAR (IS-A)
|
---------SUV
|
---------SEDAN
|
----------SPORTS CAR

```java
abstract class Vehicle {

    Vehicle(String regNo, Engine engine){
        this.registrationNo = regNo;
        this.engine = engine;
    }

    public abstract void startEngine(); //abstract method, must be defined in subclass

}

class Engine{

    String engineType;
    double capacity;

    void getEngineDetails(){
        System.out.println("Type: " + this.engineType);
    }
}

abstract class Car extends Vehicle{
    String make;
    String model;
    String color;
    int year;

    Car(String make, String model, String color, int year){
        super(regNo, engine);
        this.make = make;
        this.model = model;
        this.color = color;
    }

    abstract String getColor();
    abstract String getModel();
    abstract String getMake();
    public void getYear(int year){
        this.year = yeaar;
    }

    public String getDetails(){
        return "Car with " + this.registrationNo+"model: "+this.model+"year of Mfg: "+this.year;
    }
}

class Sedan extends Car{
    int doors;

    Sedan(int doors){
        super(make, model, color, year);
    }

    @Override
    String getColor(){
        return this.color;
    }

    @Override 
    String getModel(){
        return this.make;
    }

    @Override
    public String getDetails(){

    }

    @Override
    String getMake(){

    }
}
```

```java
abstract class Person{
    String name;
    Date dob;
    abstract void getDetails();
}

class Date{
    int date;
    int month;
    int year;
    Date(int d, int m, int y){
        this.date = d;
        this.month = m;
        this.year = y;
    }
    String getDate(){
        return this.date+"-"+this.month+"-"+this.year;
    }

}

class Student extends Person{
    String subject;
    Teacher teacher;

    Student(String name, Date date, String subject, Teacher teacher){
        this.name = name;
        this.dob = date;
        this.teacher = teacher;
        this.subject = subject;
        }

    @Override
    void getDetails(){
        System.out.println("Name of Student: " + this.name);
        System.out.println("Date of Birth: " + this.dob.getDate());
        System.out.println("Subject: " + this.subject);
        System.out.println("Teacher: " + this.teacher.name);
    }
}

abstract class Employee extends Person{
    date dateOfAppointment;
    int salary;
    abstract void setSalary();
    abstract int getSalary();
}

class Teacher extends Employee{
    String qualification;
    String subject;
    Teacher(String name, Date dob, Date dateOfAppointment, int salary, String qual, String subject){
        this.name = name;
        this.dob = dob;
        this.dateOfAppointment = dateOfAppointment;
        this.salary = salary;
        this.qualification = qual;
        this.subject = subject;
    }

    @Override
    void setSalary(){
        this.salary = 50000;
    }

    @Override
    int getSalary(){
        return this.salary;
    }
}

public class Main{
    public static void main(String[] args){
        Date date1 = new Date(1,1,2005) ;//dob of teacher
        Date date2 = new Date(1,4,2024);

        Teach teacher = new Teacher("Madhavan", date1, date2, "Mtech", "electronics");
    }
}

```