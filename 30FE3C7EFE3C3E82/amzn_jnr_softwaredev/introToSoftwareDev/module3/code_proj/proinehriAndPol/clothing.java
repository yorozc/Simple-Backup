public class clothing extends Product{
    String brand;

    public clothing(String name, double price, String brand){
        super(name, price);
        this.brand = brand;
    }

    @Override
    public void productInfo(){
        super.productInfo();
        System.out.println("Brand: " + brand);
    }
}
