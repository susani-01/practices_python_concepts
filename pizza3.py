def make_pizza(*toppings):
    """make a list with any toppings """
    print("\nmake a pizza with the following topping: ")
    for topping in toppings:
        print(f"-{topping}")

make_pizza("pepperon",)
make_pizza("mushrooms","pepperon","kimchi")