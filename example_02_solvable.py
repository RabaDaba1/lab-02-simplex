import logging
from saport.simplex.model import Model


def create_model() -> Model:
    model = Model(__file__)

    # TODO:
    # fill missing test based on the example_01_solvable.py
    # to make the test a bit more interesting:
    # * minimize the objective (so the solver would have to normalize it)
    # * make some ">=" constraints (GE)
    # * the model still has to be solvable by the basix simplex withour artificial var

    p1 = model.create_variable("p1")
    p2 = model.create_variable("p2")
    p3 = model.create_variable("p3")
    p4 = model.create_variable("p4")

    s1 = 0.8*p1 + 2.4*p2 + 0.9*p3 + 0.4*p4
    s2 = 0.6*p1 + 0.6*p2 + 0.3*p3 + 0.3*p4

    model.add_constraint(s1 >= 1200)
    model.add_constraint(s2 >= 600)

    model.minimize(9.6*p1 + 14.4*p2 + 10.8*p3 + 7.2*p4)

    return model


def run():
    model = create_model()
    # TODO:
    # add a test "assert something" based on the example_01_solvable.py
    # TIP: you may use other solvers (e.g. https://online-optimizer.appspot.com)
    #      to find the correct solution
    try:
        solution = model.solve()
    except:
        raise AssertionError("This problem has a solution and your algorithm hasn't found it!")

    logging.info(solution)

    assert (solution.assignment(model) == [750, 250, 0, 0]), "Your algorithm found an incorrect solution!"

    logging.info("Congratulations! This solution seems to be alright :)")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    run()
