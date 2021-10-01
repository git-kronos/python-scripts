from jovian.pythondsa import evaluate_test_case, evaluate_test_cases
from core.test_cases import test, tests, large_test

"""
Binary Search
"""


def binary_search(lo, hi, condition):
    while lo <= hi:  # 5 <= 7
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == "found":
            return mid
        elif result == "left":
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


"""
card issue
"""


def locate_card(cards, query):
    def condition(mid):
        if cards[mid] == query:
            if mid > 0 and cards[mid - 1] == query:
                return "left"
            else:
                return "found"
        elif cards[mid] < query:
            return "left"
        else:
            return "right"
    return binary_search(0, len(cards) - 1, condition)


"""
first and last position of list of numbers
"""


def first_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] == target:
                return "left"
            else:
                return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums) - 1, condition)


def last_position(nums, target):
    def condition(mid):
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] == target:
                return "left"
            return "found"
        elif nums[mid] < target:
            return "right"
        else:
            return "left"
    return binary_search(0, len(nums) - 1, condition)


def first_and_last_position(nums, target):
    return first_position(nums, target), last_position(nums, target)


if __name__ == "__main__":
    print("==========================================================")
    print(first_and_last_position(
        tests[0]['input']['cards'], tests[0]['input']['query']))
    print("==========================================================")
    result, passed, runtime = evaluate_test_case(
        locate_card, large_test, display=False)
    print({"Result": result, "Passed": passed, "Execution Time": f"{runtime} ms"})
    print("==========================================================")
