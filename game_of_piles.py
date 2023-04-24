import numpy as np
import argparse
from typing import List

def gameOfPiles(piles: List[int], k: int) -> str:
    n = len(piles)
    piles = np.array(piles)
    turn = 0
    
    while True:
        if np.count_nonzero(piles) == 0:
            if turn == 0:
                return f"Alex wins the game of {n} pile(s)."
            else:
                return f"Sam wins the game of {n} pile(s)."
        
        if turn == 0:
            idx = np.where(piles % k == 0)[0]
            if len(idx) == 0:
                idx = np.where(piles > k)[0]
            if len(idx) == 0:
                idx = np.where(piles > 0)[0]
            pile = np.random.choice(idx)
            remove = piles[pile] // k * k if piles[pile] >= k else np.random.randint(1, piles[pile]+1)
            piles[pile] -= remove
            turn = 1
        else:
            idx = np.where(piles % k == 0)[0]
            if len(idx) == 0:
                idx = np.where(piles > k)[0]
            if len(idx) == 0:
                idx = np.where(piles > 0)[0]
            pile = np.random.choice(idx)
            remove = piles[pile] // k * k if piles[pile] >= k else np.random.randint(1, piles[pile]+1)
            piles[pile] -= remove
            turn = 0
