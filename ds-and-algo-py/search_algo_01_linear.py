from jovian.pythondsa import evaluate_test_case, evaluate_test_cases
from core.test_cases import test, tests, large_test

"""
Linear Search
"""


def locate_card(cards, query):
    position = 0  # create a variable position with the value 0
    while position < len(cards):  # set up a loop for repetion
        if cards[position] == query:  # check if element at the current position match the query
            return position  # Answer found! Return and exit..
        position += 1  # increment the position
    return -1

# evaluate_test_case(locate_card, test)
# evaluate_test_cases(locate_card, tests)


result, passed, runtime = evaluate_test_case(
    locate_card, large_test, display=False)
print("==========================================================")
print({"Result": result, "Passed": passed, "Execution Time": f"{runtime} ms"})
print("==========================================================")
