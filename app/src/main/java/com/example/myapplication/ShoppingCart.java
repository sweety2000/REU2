package com.example.myapplication;

import java.util.ArrayList;
import java.util.List;

public class ShoppingCart {

    private List<ShoppingItem> shopping_cart;

    ShoppingCart() {
        this.shopping_cart = new ArrayList<>();
    }

    public List<ShoppingItem> getShopping_cart() {
        return shopping_cart;
    }

    public void setShopping_cart(List<ShoppingItem> shopping_cart) {
        this.shopping_cart = shopping_cart;
    }

    public boolean addItem(ShoppingItem item) {
        if (!shopping_cart.contains(item)) {
            shopping_cart.add(item);
            return true;
        } else {
            return false;
        }
    }

    public boolean removeItem(String name) {
        for (ShoppingItem item : shopping_cart) {
            if (item.getName().equalsIgnoreCase(name)) {
                shopping_cart.remove(item);
                return true;
            }
        }
        return false;
    }
}
