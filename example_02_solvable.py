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

    steaks = model.create_variable("steaks")
    potatoes = model.create_variable("potatoes")

    carbohydrates = 5*steaks + 15*potatoes
    protein = 20*steaks + 5*potatoes
    fats = 15*steaks + 2*potatoes

    model.add_constraint(carbohydrates >= 50)
    model.add_constraint(protein >= 40)
    model.add_constraint(fats <= 60)

    model.minimize(8*steaks + 4*potatoes)

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

    assert (solution.assignment(model) == [1.27, 2.91]), "Your algorithm found an incorrect solution!"

    logging.info("Congratulations! This solution seems to be alright :)")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s')
    run()
