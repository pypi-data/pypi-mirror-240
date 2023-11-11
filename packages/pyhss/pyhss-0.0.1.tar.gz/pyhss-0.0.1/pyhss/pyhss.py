import numpy as np
from .factor import *
from .tree import tree


def _allExept(block, nmax):
    return np.concatenate((np.arange(block[0], dtype=int), 
                           np.arange(block[-1]+1, nmax, dtype=int)), axis=None)    


def _hss_build_iter(A, tol, maxdepth, p=1, depth=0, blockm=None, blockn=None, U=None, V=None, lk_approx='svd', n_oversamples=10, random_state=0):
    depth = depth + 1
    seed = np.random.uniform(0, 1, 1)
    parentNode = len(blockm)>2 and len(blockn)>2 and p>seed and depth<maxdepth

    if parentNode:
        hsstree = tree(leafnode=False, topnode=False,
                       blockmLeft=int(np.floor((blockm[-1] - blockm[0]+1)/2)),
                       blockmRight=int(np.ceil((blockm[-1] - blockm[0]+1)/2)),
                       blocknLeft=int(np.floor((blockn[-1] - blockn[0]+1)/2)),
                       blocknRight=int(np.ceil((blockn[-1] - blockn[0]+1)/2))
                    )
        
        blockmLeft = np.arange(blockm[0], blockm[0]+hsstree.blockmLeft)
        blockmRight = np.arange(blockm[0]+hsstree.blockmLeft, blockm[-1]+1)
        blocknLeft = np.arange(blockn[0], blockn[0]+hsstree.blocknLeft)
        blocknRight = np.arange(blockn[0]+hsstree.blocknLeft, blockn[-1]+1)
        
        removeblockmLeft = _allExept(blockmLeft, A.shape[0])
        removeblockmRight = _allExept(blockmRight, A.shape[0])
        removeblocknLeft = _allExept(blocknLeft, A.shape[1])
        removeblocknRight = _allExept(blocknRight, A.shape[1])

        if lk_approx == 'randsvd':
            ULeft, _, _ = rand_svd(A[blockmLeft][:, removeblocknLeft], tol, n_oversamples, random_state)
            URight, _, _  = rand_svd(A[blockmRight][:, removeblocknRight], tol, n_oversamples, random_state)
            U12, S3, VLeft = rand_svd(A[removeblockmLeft][:, blocknLeft], tol, n_oversamples, random_state)
            U21, S4, VRight = rand_svd(A[removeblockmRight][:, blocknRight], tol, n_oversamples, random_state)

        else:
            ULeft, _, _ = tsvd(A[blockmLeft][:, removeblocknLeft], tol)
            URight, _, _  = tsvd(A[blockmRight][:, removeblocknRight], tol)
            U12, S3, VLeft = tsvd(A[removeblockmLeft][:, blocknLeft], tol)
            U21, S4, VRight = tsvd(A[removeblockmRight][:, blocknRight], tol)

        U12Ind = np.arange(blockm[0], blockm[0] + URight.shape[0])
        U21Ind = np.arange(blockm[0], blockm[0] + ULeft.shape[0])
        Bl = np.matmul(np.matmul(URight.T, U12[U12Ind]), np.diag(S3))
        Bu = np.matmul(np.matmul(ULeft.T, U21[U21Ind]), np.diag(S4))
        
        hsstree.Bl=Bl
        hsstree.Bu=Bu

        hsstree.leftChild = _hss_build_iter(A, tol, maxdepth, p, depth, blockmLeft, blocknLeft, ULeft, VLeft, n_oversamples, random_state)
        hsstree.rightChild = _hss_build_iter(A, tol, maxdepth, p, depth, blockmRight, blocknRight, URight, VRight, n_oversamples, random_state)

        if depth != 1:
            hsstree.RLeft = np.linalg.solve(ULeft, U[:hsstree.blockmLeft,:])
            hsstree.RRight = np.linalg.solve(URight, U[hsstree.blockmLeft:,:])

            hsstree.WLeft = np.linalg.solve(VLeft, V[:hsstree.blocknLeft,:])
            hsstree.WRight = np.linalg.solve(VRight, V[hsstree.blocknLeft:,:])
        else:
            hsstree.topnode = True

    else:
        hsstree = tree(leafnode=True, topnode=False)
        if depth != 1:
            hsstree.U = U
            hsstree.V = V
        else:
            hsstree.topnode=True
        
        hsstree.D = A[blockm][:, blockn]

    return hsstree


class hss(object):

    def __init__(self, tol=0, maxdepth=np.inf, p=1, lk_approx='svd', n_oversamples=10, random_state=0):
        self.tol = tol
        self.maxdepth = maxdepth
        self.p = p
        self.lk_approx = lk_approx
        self.n_oversamples = n_oversamples
        self.random_state = random_state

    def build(self, A):
        m, n = A.shape
        blockm = np.arange(m)
        blockn = np.arange(n)

        return _hss_build_iter(A, 
                               tol=self.tol,
                               maxdepth=self.maxdepth, 
                               p=self.p, 
                               blockm=blockm, 
                               blockn=blockn,
                               lk_approx=self.lk_approx, 
                               n_oversamples=self.n_oversamples,
                               random_state=self.random_state
                               )


    

 