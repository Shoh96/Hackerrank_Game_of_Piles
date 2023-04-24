import gameOfPiles

def test_gameOfPiles_sam_wins():
    # Sam should win with these inputs
    piles = [3, 5, 7]
    k = 2
    assert gameOfPiles.gameOfPiles(piles, k) == "Sam wins the game of 3 pile(s)."

def test_gameOfPiles_alex_wins():
    # Alex should win with these inputs
    piles = [4, 6]
    k = 2
    assert gameOfPiles.gameOfPiles(piles, k) == "Alex wins the game of 2 pile(s)."

def test_gameOfPiles_empty_piles():
    # The function should return an error message if the piles array is empty
    piles = []
    k = 3
    assert gameOfPiles.gameOfPiles(piles, k) == "Error: Piles array is empty."

def test_gameOfPiles_negative_k():
    # The function should return an error message if k is negative
    piles = [5, 8, 10]
    k = -2
    assert gameOfPiles.gameOfPiles(piles, k) == "Error: k must be a positive integer."

def test_gameOfPiles_zero_stones():
    # The function should return a message if all piles have zero stones
    piles = [0, 0, 0]
    k = 2
    assert gameOfPiles.gameOfPiles(piles, k) == "All piles have zero stones. The game is over."
