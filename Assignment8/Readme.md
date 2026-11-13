# Assignment 8: Streamlit Apps

A set of four beginner-friendly Streamlit exercises covering basic app elements, user input, simple calculations, forms, and a small sales dashboard.

## Apps in this folder

| File | What it does |
| --- | --- |
| `app_basic.py` | Displays a welcome title, asks for a name, and greets the user when **Greet Me** is clicked. |
| `app_discount.py` | Takes a product price and discount percentage, then shows the original and discounted prices. |
| `app_product_form.py` | Collects a product name, category, and price in the sidebar, then displays the submitted details. |
| `app_dashboard.py` | Shows monthly sales, lets you choose a month, and displays sales totals in a bar chart. |

## Requirements

- Python 3
- Streamlit

Install Streamlit if it is not already installed:

```bash
python -m pip install streamlit
```

## Run an app

Open a terminal in this folder and run one script at a time:

```bash
streamlit run app_basic.py
```

To launch another exercise, replace `app_basic.py` with `app_discount.py`, `app_product_form.py`, or `app_dashboard.py`. Streamlit will open the app in your browser.

## Notes

- The discount calculator limits the discount slider to 0–50%.
- The product form includes Electronics, Home, Clothing, Furniture, and Groceries as category options.
- The sales dashboard uses static sample data for January through April; it does not load sales from an external source.