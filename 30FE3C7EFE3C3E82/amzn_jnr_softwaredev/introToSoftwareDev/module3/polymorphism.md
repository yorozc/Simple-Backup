# Polymorphism

## Method overloading
- create methods with the same name but different arguments

```java
//camera program

public class Camera{

    public void takePicture(String mode){
        System.out.println("Taking picture in " + mode + " mode");
    }

    public void takePicture(int resolution){
        System.out.println("Taking pictures in " + resolution + " megapixels.");
    }
    //cannot have both arguements take string types
    //if methods take same number of arguments, the arguments must be a different type
    public void takePicture(String mode, int resolution){
        System.out.println("Taking a " + resolution + " megapixels picture in " + mode + " mode." );
    }
}

public class Main{
    public static void main(String[] args){
        Camera favCam = new Camera();

        favCam.takePicture("Portrait");
        favCam.takePicture(12);
        favCam.takePicture("landscape", 24);
    }
}
```
Method overriding, subclasses can override methods to fit their needs (will be dealt with in the future)

## Overriding methods
- Allows a subclass to refine or enhance a method inherited from its superclass. 
- Useful when you want to adapt the inherited method's behavior to better suit the needs of the subclass

## Using Polymorphic design
- enables to keep code organized and manageable
