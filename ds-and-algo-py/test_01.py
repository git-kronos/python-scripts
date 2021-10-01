from jovian.pythondsa import evaluate_test_case, evaluate_test_cases
from core.test_cases import test, tests, large_test

"""
Binary Search
"""
question = [0, 2, 3, 4, 5, 6, 9]
output = [5, 6, 9, 0, 2, 3, 4]

nums = []

test = {
    'input': {
        'nums': [19, 25, 29, 3, 5, 6, 7, 9, 11, 14]
    },
    'output': 3
}


def count_rotations(nums):
    pass


if __name__ == "__main__":
    print("==========================================================")
    nums0 = test['input']["nums"]
    output0 = test['input']["nums"]
    result0 = count_rotations(nums0)
    print(result0, result0 == output0)

    # evaluate_test_cases(count_rotations, tests)
    print("==========================================================")
