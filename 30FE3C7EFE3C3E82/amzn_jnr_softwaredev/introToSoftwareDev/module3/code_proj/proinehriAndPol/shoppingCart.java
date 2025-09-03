import java.util.*;

public class shoppingCart {

    List<String> cartItems = new ArrayList<String>();

    public void addItem(Product item){
        System.out.println("Item " + item.name + " has been added to the cart");
        item.productInfo();
        cartItems.add(item.name);

    }

    public void displayItems(){
        System.out.println(cartItems.toString());
    }
}
