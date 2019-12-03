import mc


generator = mc.StringGenerator(
    samples=["hello world", "world of cuties"],
    order=2,  # You can set any order for the Markov model (https://en.wikipedia.org/wiki/Variable-order_Markov_model)
)
