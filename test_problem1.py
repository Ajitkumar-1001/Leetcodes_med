import pytest
from problem1 import FoodRatingSystem


@pytest.fixture
def system():
    """LeetCode example setup."""
    foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
    cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
    ratings = [9, 12, 8, 15, 14, 7]
    return FoodRatingSystem(foods, ratings, cuisines)


def test_highest_rated_basic(system):
    assert system.highestRated("korean") == "kimchi"
    assert system.highestRated("japanese") == "ramen"
    assert system.highestRated("greek") == "moussaka"


def test_change_rating_and_query(system):
    system.changeRating("sushi", 16)
    assert system.highestRated("japanese") == "sushi"


def test_change_rating_tie_breaks_lexicographically(system):
    # After changing sushi to 16, change ramen to 16 as well
    system.changeRating("sushi", 16)
    system.changeRating("ramen", 16)
    # Tie at 16: "ramen" < "sushi" lexicographically
    assert system.highestRated("japanese") == "ramen"


def test_leetcode_example_full_sequence(system):
    # Step-by-step from the LeetCode example
    assert system.highestRated("korean") == "kimchi"
    assert system.highestRated("japanese") == "ramen"

    system.changeRating("sushi", 16)
    assert system.highestRated("japanese") == "sushi"

    system.changeRating("ramen", 16)
    assert system.highestRated("japanese") == "ramen"


def test_single_food():
    sys = FoodRatingSystem(["pizza"], [10], ["italian"])
    assert sys.highestRated("italian") == "pizza"


def test_change_rating_multiple_times():
    sys = FoodRatingSystem(["a", "b"], [5, 3], ["x", "x"])
    assert sys.highestRated("x") == "a"

    sys.changeRating("b", 10)
    assert sys.highestRated("x") == "b"

    sys.changeRating("b", 1)
    assert sys.highestRated("x") == "a"


def test_same_rating_lexicographic_order():
    sys = FoodRatingSystem(["banana", "apple"], [10, 10], ["fruit", "fruit"])
    # Both rated 10 — "apple" < "banana" lexicographically
    assert sys.highestRated("fruit") == "apple"


def test_many_cuisines_independent():
    foods = ["tacos", "pad_thai", "croissant"]
    cuisines = ["mexican", "thai", "french"]
    ratings = [8, 9, 7]
    sys = FoodRatingSystem(foods, ratings, cuisines)

    assert sys.highestRated("mexican") == "tacos"
    assert sys.highestRated("thai") == "pad_thai"
    assert sys.highestRated("french") == "croissant"

    # Changing one cuisine doesn't affect others
    sys.changeRating("croissant", 20)
    assert sys.highestRated("french") == "croissant"
    assert sys.highestRated("thai") == "pad_thai"
