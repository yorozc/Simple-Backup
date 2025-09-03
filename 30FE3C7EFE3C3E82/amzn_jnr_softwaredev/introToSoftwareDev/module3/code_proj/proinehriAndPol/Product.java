public class Product {
    String name;
    double price;

    public Product(String name, double price){
        this.name = name;
        this.price = price;
    }

    public void productInfo(){
        System.out.println("Name of item: " + this.name + "\nPrice of item: " + this.price);
    }
}
