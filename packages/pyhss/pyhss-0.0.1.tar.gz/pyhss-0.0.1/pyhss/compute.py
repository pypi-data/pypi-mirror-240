import numpy as np
from dataclasses import dataclass
from .tree import tree


@dataclass
class treeG:
    leafnode : bool = False
    topnode : bool = False
    vbl : tree = None
    vbr : tree = None
    gl : tree = None
    gr : tree = None




def _down_sweep(trg, hsstree, f, x):
    if not hsstree.leafnode:
        if hsstree.topnode:
            fl = np.matmul(hsstree.Bu, trg.gr)
            fr = np.matmul(hsstree.Bl, trg.gl)
        else:
            fl = np.matmul(hsstree.Bu, trg.gr) + np.matmul(hsstree.RLeft, f)
            fr = np.matmul(hsstree.Bl, trg.gl) + np.matmul(hsstree.RRight, f)

        bl = _down_sweep(trg.vbl, hsstree.leftChild, fl, x[:hsstree.blocknLeft,:])
        br = _down_sweep(trg.vbr, hsstree.rightChild, fr, x[hsstree.blocknLeft:,:])

        b = np.vstack((bl, br))

    else:
        b = np.matmul(hsstree.D, x) + np.matmul(hsstree.U, f)
    return b




def _up_sweep(hsstree, x):
    trg = treeG()
    g = None

    if not hsstree.leafnode: 
        trg.vbl, trg.gl = _up_sweep(hsstree.leftChild, x[:hsstree.blocknLeft,:])
        trg.vbr, trg.gr = _up_sweep(hsstree.rightChild, x[hsstree.blocknLeft:,:])
        # trg.vbl, trg.gl, trg.vbr, trg.gr = vbl, gl, vbr, gr

        if not hsstree.topnode:
            g = np.matmul(hsstree.WLeft.T, trg.gl) + np.matmul(hsstree.WRight.T, trg.gr)    

    else:  
        g = np.matmul(hsstree.V.T, x)

    return trg, g





def hss_matmul(hsstree, x):
    if not hsstree.leafnode:           
        vb, _ = _up_sweep(hsstree, x)
        
        f = None
        b = _down_sweep(vb, hsstree, f, x)
    else:
        b = np.matmul(hsstree.D, x)
    return b
