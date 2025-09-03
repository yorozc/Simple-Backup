public class main {
    public static void main(String[] args){
        Product apple = new Product("Apple", 120);
        apple.productInfo();

        System.out.println("++++++++++++++++++++++++++++++++++++++++++++++++++++++++");

        electronics phone = new electronics("mPhone23", 2000, 12);
        phone.productInfo();

        System.out.println("++++++++++++++++++++++++++++++++++++++++++++++++++++++++");

        clothing brandedTshirt = new clothing("T-Shirt", 121, "Vans");
        brandedTshirt.productInfo();

        System.out.println("++++++++++++++++++++++++++++++++++++++++++++++++++++++++");

        shoppingCart firstCart = new shoppingCart();
        firstCart.addItem(apple);
        firstCart.addItem(brandedTshirt);
        firstCart.addItem(phone);
        System.out.print("Cart: ");
        firstCart.displayItems();
    }

}
