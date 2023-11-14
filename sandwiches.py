def make_sandwiche(*toppings):
    """make a list of the items needed to make a sandwiches."""
    print("\nitems required to make a sandwiches: ")
    for topping in toppings:
        print(f"- {topping}")

make_sandwiche("meat","snacks","pork","chill")
make_sandwiche("kimchi")
make_sandwiche("fish","soju")