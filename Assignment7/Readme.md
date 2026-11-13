# Python Object-Oriented Programming Tasks

A Jupyter notebook of hands-on Python exercises that introduce object-oriented programming (OOP). The examples build from simple product objects to inheritance, polymorphism, abstract payment methods, operator overloading, and a small inventory/store model.

## Notebook contents

The notebook contains seven tasks:

1. **Classes and objects** — define a `Product` with a name, price, and category; display product details and calculate a discounted price.
2. **Constructors and encapsulation** — store a product price as `__price` and access or update it with getter and setter methods.
3. **Single inheritance** — extend `Product` with `ElectronicProduct`, add warranty years, and override `get_info()`.
4. **Polymorphism** — define `Laptop` and `Mobile` product subclasses and call their `get_info()` methods through a shared loop.
5. **Abstraction** — define an abstract `Payment` class and implement credit-card and UPI payment methods.
6. **Magic methods and operator overloading** — make products printable with `__str__` and combine two products with `__add__`.
7. **Mini project: inventory system** — manage products in a store, list items, remove a product by name, calculate inventory value, show a summary, and combine two products.

## Libraries and requirements

- Python 3 (the notebook metadata records Python 3.13.16)
- Jupyter Notebook or JupyterLab to run the `.ipynb` file
- Python standard library only; the notebook imports `ABC` and `abstractmethod` from `abc`. No third-party packages are required.

## Run the notebook

1. Open `Tasks(2).ipynb` in Jupyter Notebook, JupyterLab, or another notebook-compatible environment.
2. Run the cells from top to bottom. The notebook redefines `Product` in later tasks, so running cells out of order may produce different behavior.

## Example outputs in the notebook

- A 15% discount on a $500 chair is displayed as **$425.00**.
- The encapsulation example changes a mobile product’s price from **$1,000** to **$1,200**.
- An electronic product displays a **2-year warranty**.
- Credit-card and UPI payment examples display amounts of **$1,000** and **$5,000**.
- Combining Pepsi ($2) and Sprite ($3) produces a combined product priced at **$5**.
- The Avengers Store example contains **3 products** with a displayed total value of **$2,250,000**.

## Notes on the current implementations

- `apply_discount()` prints the discounted amount; although its task prompt says it should return that amount, the current method does not return a value.
- `set_price()` rejects negative prices but currently allows a price of zero, while the exercise asks for a value greater than zero.
- In the mini project, `Store` inherits from `Inventory`, and `add_new_product()` accepts an already-created `Product` object. It does not prompt for product details as described in the task prompt.
- The task prompt names `get_total_value()`; the implemented inventory method is named `total_price()`.

## Learning goals

By working through the notebook, learners can practice defining classes, initializing object state, using name-mangled attributes, validating updates, extending and overriding classes, satisfying abstract methods, and customizing Python operators.