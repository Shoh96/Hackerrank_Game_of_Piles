import pytest
from game_of_piles import gameOfPiles

def test_gameOfPiles():
    # Test case 1
    piles = [2, 2, 2, 1]
    k = 2
    assert gameOfPiles(piles, k) == "Alex wins the game of 4 pile(s)."

    # Test case 2
    piles = [5, 7, 9]
    k = 2
    assert gameOfPiles(piles, k) == "Alex wins the game of 3 pile(s)."

    # Test case 3
    piles = [5, 7, 9]
    k = 3
    assert gameOfPiles(piles, k) == "Sam wins the game of 3 pile(s)."

    # Test case 4
    piles = [1, 1, 1]
    k = 2
    assert gameOfPiles(piles, k) == "Sam wins the game of 3 pile(s)."

    # Test case 5
    piles = [10, 20, 30, 40]
    k = 3
    assert gameOfPiles(piles, k) == "Alex wins the game of 4 pile(s)."
