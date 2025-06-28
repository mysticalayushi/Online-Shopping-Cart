# 🛒 Online Shopping Cart – Console-Based Python Application

A comprehensive Python project simulating the core functionality of an online shopping cart system through the command line. This project demonstrates strong Object-Oriented Programming (OOP) principles, file handling for persistence, and an interactive product management system.

---

## 📖 Overview

This project is a part of the Semester 2 curriculum designed to implement real-world use cases using Python and OOPs. The application mimics an online shopping cart where users can browse products, add items to their cart, modify quantities, remove products, and view the final total.

The program also ensures data is saved between sessions using JSON files for the product catalog and cart state.

---

## 🚀 Features

- View available products (physical or digital)
- Add products to shopping cart
- Update product quantity in cart
- Remove items from cart
- View cart with subtotals and grand total
- Save/load catalog and cart data with JSON
- Catalog_Updater tool to dynamically manage product catalog

---

## 🧠 OOP Concepts Applied

| Concept           | Application                                                   |
| ----------------- | ------------------------------------------------------------- |
| **Encapsulation** | Used private-like attributes and property decorators          |
| **Inheritance**   | `PhysicalProduct` and `DigitalProduct` inherit from `Product` |
| **Polymorphism**  | Overridden `display_details()` method in child classes        |
| **Composition**   | `CartItem` contains a `Product` instance                      |
| **Magic Methods** | `__str__()` used in `CartItem` for readable output            |
| **Persistence**   | JSON file handling to save/load cart and product catalog      |

---

## 🗂️ Project Structure

```
OnlineShoppingCart/
├── product.py             # Product, PhysicalProduct, DigitalProduct classes
├── cart_item.py           # CartItem class (composition + subtotal logic)
├── shopping_cart.py       # Cart logic, JSON I/O, business operations
├── main.py                # Console interface for user interaction
├── Catalog_Updater.py     # Tool for adding products interactively
├── products.json          # Product catalog (persisted between runs)
├── cart.json              # Cart state (persisted between runs)
├── README.md              # Project documentation
└── report/                # Final submission documents (optional)
```

---

## ▶️ How to Run

### 1. Requirements

- Python 3.8 or higher
- No external libraries needed

### 2. Run Main App

```bash
python main.py
```

### 3. Add Products to Catalog

```bash
python Catalog_Updater.py
```

---

## 📄 File Descriptions

| File Name            | Purpose                                                 |
| -------------------- | ------------------------------------------------------- |
| `product.py`         | Base and derived product classes with polymorphism      |
| `cart_item.py`       | Class to wrap a product and quantity, handles subtotal  |
| `shopping_cart.py`   | Manages the cart and product catalog, handles all logic |
| `main.py`            | Console menu interface                                  |
| `Catalog_Updater.py` | Interactive tool to create/add products                 |
| `products.json`      | Persistent product catalog                              |
| `cart.json`          | Persistent cart data                                    |
| `README.md`          | Project documentation                                   |

---

## 🧪 Sample Data Files

### products.json

```json
[
  {
    "type": "physical",
    "product_id": "P001",
    "name": "Wireless Mouse",
    "price": 499.0,
    "quantity_available": 20,
    "weight": 0.2
  },
  {
    "type": "digital",
    "product_id": "D001",
    "name": "Online Course Access",
    "price": 999.0,
    "quantity_available": 100,
    "download_link": "https://example.com/course"
  }
]
```

### cart.json

```json
[]
```

---

## 👨‍💻 Developers

- **Chirayush Verma**
- **Ayushi Rai**

---

## 📝 Notes

- This project was designed to help students learn OOP in real-world scenarios.
- Easily extendable for GUI or web interface in the future.
- Clean and testable structure following modular programming practices.
