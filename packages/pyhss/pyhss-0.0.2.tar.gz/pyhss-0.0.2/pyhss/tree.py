import numpy as np
from dataclasses import dataclass

class tree:
    def __init__(self,
                leafnode: bool = False,
                topnode: bool = False,
                blockmLeft: int = -1,
                blockmRight: int = -1,
                blocknLeft: int = -1,
                blocknRight: int = -1,
                Bl : np.ndarray = None,
                Bu : np.ndarray = None,
                leftChild : object = None,
                rightChild : object = None,
                RLeft : np.ndarray = None,
                RRight : np.ndarray = None,
                WLeft : np.ndarray = None,
                WRight : np.ndarray = None,
                U : np.ndarray = None,
                V : np.ndarray = None,
                D : np.ndarray = None,
                depth : int = None
        ):

        self.leafnode = leafnode
        self.topnode = topnode
        self.blockmLeft = blockmLeft
        self.blockmRight = blockmRight
        self.blocknLeft = blocknLeft
        self.blocknRight = blocknRight
        self.Bl = Bl
        self.Bu = Bu
        self.leftChild = leftChild
        self.rightChild = rightChild
        self.RLeft = RLeft
        self.RRight = RRight
        self.WLeft = WLeft
        self.WRight = WRight
        self.U = U
        self.V = V
        self.D = D
        self.depth = depth

    def show(self):
        if self.topnode:
            return hsstree(
                    leafnode = self.leafnode,
                    topnode = self.topnode,
                    blockmLeft = self.blockmLeft,
                    blockmRight = self.blockmRight,
                    blocknLeft = self.blocknLeft,
                    blocknRight = self.blocknRight,
                    Bl = self.Bl.shape,
                    Bu = self.Bu.shape,
                    leftChild = self.leftChild != None,
                    rightChild = self.rightChild != None,
                    depth = self.depth
                )
        
        elif not self.topnode and not self.leafnode:
            return hsstree(
                    leafnode = self.leafnode,
                    topnode = self.topnode,
                    blockmLeft = self.blockmLeft,
                    blockmRight = self.blockmRight,
                    blocknLeft = self.blocknLeft,
                    blocknRight = self.blocknRight,
                    Bl = self.Bl.shape,
                    Bu = self.Bu.shape,
                    leftChild = self.leftChild != None,
                    rightChild = self.rightChild != None,
                    RLeft = self.RLeft.shape,
                    RRight = self.RRight.shape,
                    WLeft = self.WLeft.shape,
                    WRight = self.WRight.shape,
                    depth = self.depth
                )

        elif self.leafnode:
            return hsstree(
                    leafnode = self.leafnode,
                    topnode = self.topnode,
                    blockmLeft = self.blockmLeft,
                    blockmRight = self.blockmRight,
                    blocknLeft = self.blocknLeft,
                    blocknRight = self.blocknRight,
                    leftChild = self.leftChild != None,
                    rightChild = self.rightChild != None,
                    U = self.U.shape,
                    V = self.V.shape,
                    D = self.D.shape,
                    depth = self.depth
                )

@dataclass
class hsstree:
    leafnode: bool = False
    topnode: bool = False
    blockmLeft: int = -1
    blockmRight: int = -1
    blocknLeft: int = -1
    blocknRight: int = -1
    Bl : tuple = None
    Bu : tuple = None
    leftChild : bool = False
    rightChild : bool = False
    RLeft : tuple = None
    RRight : tuple = None
    WLeft : tuple = None
    WRight : tuple = None
    U : tuple = None
    V : tuple = None
    D : tuple = None
    depth : int = None