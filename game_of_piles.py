def gameOfPiles(piles, k):
    """
    Determines the winner of the game of piles.
    Args:
        piles (list): An array of integers, where piles[i] represents the number of stones in the i-th pile.
        k (int): An integer representing the multiplier for the number of stones that can be removed.
    Returns:
        str: A string indicating the winner of the game.
    """
    # Determine the total number of stones in all the piles
    total_stones = sum(piles)
    
    # Check if the total number of stones is divisible by k
    if total_stones % k == 0:
        # If so, Alex wins
        return "Alex wins the game of {} pile(s).".format(len(piles))
    else:
        # Otherwise, Sam wins
        return "Sam wins the game of {} pile(s).".format(len(piles))


# Example usage
piles = [3, 5, 7]
k = 2
print(gameOfPiles(piles, k))  # Output: Sam wins the game of 3 pile(s).
