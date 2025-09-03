public class electronics extends Product{
    int warrantyPeriodInMonths;

    public electronics(String name, double price, int warrantyPeriodInMonths){
        super(name, price);
        this.warrantyPeriodInMonths = warrantyPeriodInMonths;
    }

    @Override
    public void productInfo(){
        super.productInfo();
        System.out.println("Warranty Period: " + this.warrantyPeriodInMonths);
    }
}
