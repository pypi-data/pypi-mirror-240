from dataclasses import dataclass
import numpy as np

@dataclass
class tree:
    leafnode: bool = False
    topnode: bool = False
    blockmLeft: int = -1
    blockmRight: int = -1
    blocknLeft: int = -1
    blocknRight: int = -1
    Bl : np.ndarray = None
    Bu : np.ndarray = None
    leftChild : object = None
    rightChild : object = None
    RLeft : np.ndarray = None
    RRight : np.ndarray = None
    WLeft : np.ndarray = None
    WRight : np.ndarray = None
    U : np.ndarray = None
    V : np.ndarray = None
    D : np.ndarray = None
