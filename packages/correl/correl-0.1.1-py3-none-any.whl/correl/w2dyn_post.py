"""
Python module for easier handling of the generalized
susceptibility matrices generated from
'w2dynamics' DMFT calculations
"""

import numpy as np
import scipy as sp
import scipy.integrate as integ
import h5py
import re
import matplotlib as mpl

class read(object):
    def __init__(self, file, iter=-1):
        self.file = file
        self.iter = iter
        self.iter_str = self.get_iter()
        try:
            self.iter_str2p = self.get_iter(twp=True)
        except IndexError:
            self.iter_str2p = ''

    def get(self, string):
        f = h5py.File(self.file,"r")
        data = f[string]
        return data

    def get_iter(self, twp=False):
        if self.iter==-1:
            if twp:
                iterpat = re.compile(r"^(?:stat-001|worm-001)+$")
            else:
                iterpat = re.compile(r"^(?:dmft-last|stat-001|worm-001)+$")
            f = h5py.File(self.file,"r")
            iters = sorted([k for k in f.keys() if iterpat.match(k)])
            return iters[0]
        else:
            if twp:
                iterpat = re.compile(r"^(?:stat|worm)-\d+$")
            else:
                iterpat = re.compile(r"^(?:dmft|stat|worm)-\d+$")
            f = h5py.File(self.file,"r") 
            iters = sorted([k for k in f.keys() if iterpat.match(k)])
            return iters[self.iter]

    def beta(self):
        beta = self.get(".config").attrs["general.beta"]
        return beta

    def U(self,atom=1):
        U = self.get(".config").attrs["atoms."+str(atom)+".udd"]
        return U

    def mu(self):
        mu = self.get(".config").attrs["general.mu"]
        return mu

    def occ(self,atom=1):
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        occ = np.array(self.get(strg+"/occ/value"))
        return occ

    def magn(self,atom=1):
        """
        n_up - n_down
        """
        occ = self.occ(atom)
        magn = occ[:,0,:,0] - occ[:,1,:,1]
        return magn

    def iw(self):
        return self.get(".axes/iw")[:]

    def giw(self,atom=1):
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        giw = np.array(self.get(strg+"/giw/value"))
        return giw

    def g0iw(self,atom=1):
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        g0iw = np.array(self.get(strg+"/g0iw/value"))
        return g0iw

    def siw(self,atom=1):
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        siw = np.array(self.get(strg+"/siw/value"))
        return siw
    
    def fiw(self,atom=1):
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        fiw = np.array(self.get(strg+"/fiw/value"))
        return fiw
     
    def gkiw(self,ek,atom=1,biw=0):
        iW = 1j*2*np.pi*biw
        kdim = np.ones(ek.ndim,dtype=int)
        siw = self.siw(atom)
        mu = self.mu()
        iw = 1j*np.array(self.get(".axes/iw")).reshape(1,1,-1,*kdim)
        gkiw = np.zeros((*siw.shape, *ek.shape),dtype='complex')
        gkiw = 1/(iw + iW + mu -ek.reshape(1,1,1,*ek.shape) \
                  - siw.reshape(*siw.shape,*kdim))
        return gkiw

    def bubble(self, atom=1, other_giw=None ,worm=False, iw4f=True):
        giw = self.giw(atom) if other_giw is None else other_giw
        if iw4f:
            g4iw  = self.g4iw_worm(atom) if worm  else self.g4iw(atom)
            niw = giw.shape[-1]
            niw4f = g4iw.shape[-2]
            i_start = (niw-niw4f)//2
            iw4f_slice = slice(i_start, i_start+niw4f)
            giw = giw[..., iw4f_slice]
        return - self.beta()*giw*giw
    
    def bubble_q(self, ek,ekq,atom=1, worm=False, iw4f=True):
        sum_ax = np.arange(-ek.ndim,0,dtype=int)
        giw = self.gkiw(ek)
        giw_q = self.gkiw(ekq)
        if iw4f:
            g4iw  = self.g4iw_worm(atom) if worm  else self.g4iw(atom)
            niw = giw.shape[2]
            niw4f = g4iw.shape[-2]
            i_start = (niw-niw4f)//2
            iw4f_slice = slice(i_start, i_start+niw4f)
            giw = giw[:, :, iw4f_slice,:]
            giw_q = giw_q[:, :, iw4f_slice,:]
        return - self.beta()*np.sum(giw*giw_q,axis=tuple(sum_ax))/ek.size

    def g4iw(self,atom=1):
        strg = self.iter_str2p+"/ineq-"+str(atom).zfill(3)
        g4iw = np.array(self.get(strg+"/g4iw/value"))
        return g4iw

    def g4iw_worm(self,atom=1):
        strg = self.iter_str2p+"/ineq-"+str(atom).zfill(3)
        g4iw_uu = np.array(self.get(strg+"/g4iw-worm/00001/value")) #0000 uuuu
        g4iw_ud = np.array(self.get(strg+"/g4iw-worm/00004/value")) #0001 uudd
        g4iw_dd = np.array(self.get(strg+"/g4iw-worm/00016/value")) #0101 dddd
        g4iw_du = np.array(self.get(strg+"/g4iw-worm/00013/value")) #0100 dduu
        g4iw = np.zeros((1,2,1,2,*g4iw_uu.shape),dtype=complex)
        g4iw[0,0,0,0,:] = g4iw_uu
        g4iw[0,0,0,1,:] = g4iw_ud
        g4iw[0,1,0,1,:] = g4iw_dd
        g4iw[0,1,0,0,:] = g4iw_du
        return g4iw 

    def g4iw_bar_worm(self,atom=1):
        strg = self.iter_str2p+"/ineq-"+str(atom).zfill(3)
        g4iw_barud = np.array(self.get(strg+"/g4iw-worm/00007/value")) #     udud
        g4iw_bardu = np.array(self.get(strg+"/g4iw-worm/00010/value")) #     dudu
        g4iw_bar = np.zeros((1,2,1,2,*g4iw_barud.shape),dtype=complex)
        g4iw_bar[0,0,0,0,:] = g4iw_barud
        g4iw_bar[0,1,0,1,:] = g4iw_bardu
        return g4iw_bar

    def g4iw_pp(self,atom=1):
        strg = self.iter_str2p+"/ineq-"+str(atom).zfill(3)
        g4iw_pp = np.array(self.get(strg+"/g4iw-pp/value"))
        return g4iw_pp

    def g4iw_pp_worm(self,atom=1):
        strg = self.iter_str2p+"/ineq-"+str(atom).zfill(3)
        g4iw_pp_uu = np.array(self.get(strg+"/g4iwpp-worm/00001/value")) #0000
        g4iw_pp_ud = np.array(self.get(strg+"/g4iwpp-worm/00004/value")) #0001
        g4iw_pp_dd = np.array(self.get(strg+"/g4iwpp-worm/00016/value")) #0101
        g4iw_pp_du = np.array(self.get(strg+"/g4iwpp-worm/00013/value")) #0100
        g4iw_pp = np.zeros((1,2,1,2,*g4iw_pp_uu.shape),dtype=complex)
        g4iw_pp[0,0,0,0,:] = g4iw_pp_uu
        g4iw_pp[0,0,0,1,:] = g4iw_pp_ud
        g4iw_pp[0,1,0,1,:] = g4iw_pp_dd
        g4iw_pp[0,1,0,0,:] = g4iw_pp_du
        return g4iw_pp

    def chi_ph(self, atom=1, other_giw=None, worm=False):
        def get_ggstraight_ph(giw, niw4f):
            """ taken from w2dyn/auxilaries/postporcessing.py
            Helper function for getting the straight part from GG
            The "straight" disconnected part of the two-particle Green's function is
            given by:
            GG_AB(iv, iv', iw) = G_A(iv) G_B(iv') delta(iw,0)
            and is returned as six-dimensional array GG(A,B,iv,iv'), omitting the
            bosonic frequency for brevity.
            """
            nband, nspin, niw = giw.shape
            startidx = (niw-niw4f)//2
            iw4f_slice = slice(startidx, startidx+niw4f)
            giw = giw.reshape(-1, niw)[:, iw4f_slice]
            gg_straight = np.tensordot(giw, giw, ((),()))  # i,iv,j,iv'
            gg_straight = gg_straight.transpose(0, 2, 1, 3)
            return gg_straight.reshape(nband, nspin, nband, nspin, niw4f, niw4f) 

        giw = self.giw(atom) if other_giw is None else other_giw
        g4iw  = self.g4iw_worm(atom) if worm  else self.g4iw(atom)

        iw4b0 = g4iw.shape[-1]//2
        chi = g4iw.copy()
        chi[..., iw4b0] -= get_ggstraight_ph(giw, g4iw.shape[-2])
        chi *= self.beta()
        return chi

    def chi_ph_bar(self, atom=1, other_giw=None):
        g4iw  = self.g4iw_bar_worm(atom) 

        iw4b0 = g4iw.shape[-1]//2
        chi = g4iw.copy()
        chi *= self.beta()
        return chi

    def chi_pp(self, atom=1, other_giw=None, worm=False):
        """ taken from w2dyn/auxilaries/postporcessing.py
        generalised susceptibility (particle-particle channel)
        """
        def get_ggstraight_pp(giw, g4iw_pp_shape):
            """ taken from w2dyn/auxilaries/postporcessing.py
            Computes GG = G(iv)G(iv')delta(iw',-iv-iv')
            """
            #print giw.shape, g4iw_pp_shape
            assert giw.shape[-3:] == g4iw_pp_shape[-5:-2], "Shape mismatch"
            dotnot = ((),())
            nneq = g4iw_pp_shape[0]
            N = g4iw_pp_shape[-3]
            K = g4iw_pp_shape[-1]
            KhpNm1 = + K//2 - N + 1
            # TODO slow
            chi0_pp = np.zeros(shape=g4iw_pp_shape, dtype=complex)
            #chi0_pp[...] = np.nan
            for m in range(N):
                for n in range(N):
                    ktarg = KhpNm1 + m + n
                    if 0 <= ktarg < K:
                        chi0_pp[...,m,n,ktarg] = \
                                   np.tensordot(giw[...,m], giw[...,n], dotnot)
            return chi0_pp

        giw = self.giw(atom) if other_giw is None else other_giw
        g4iw_pp  = self.g4iw_pp_worm(atom) if worm  else self.g4iw_pp(atom)
        
        iw4st = (giw.shape[-1] - g4iw_pp.shape[-2])//2
        iw4sl = slice(iw4st, -iw4st)
        chi0_pp = get_ggstraight_pp(giw[...,iw4sl], g4iw_pp.shape)
        return g4iw_pp - chi0_pp

    def chi_stat(self,atom=1,worm=False,other_giw=None,asymp=False):
        chi_ph = self.chi_ph(atom, other_giw, worm)
        iw4b0 = chi_ph.shape[-1]//2

        if asymp:
            x0 = self.bubble(atom, other_giw ,worm, iw4f=False)
            niw4f = chi_ph.shape[-2]
            niw = x0.shape[-1]
            i_start = (niw-niw4f)//2
            iw4f_slice = slice(i_start, i_start+niw4f)

            x_uu = np.diag(x0[0,0,:])
            x_uu[iw4f_slice,iw4f_slice] = chi_ph[0,0,0,0,...,iw4b0]
            x_ud = np.zeros((niw,niw),dtype='complex')
            x_ud[iw4f_slice,iw4f_slice] = chi_ph[0,0,0,1,...,iw4b0]
            x_dd = np.diag(x0[0,1,:])
            x_dd[iw4f_slice,iw4f_slice] = chi_ph[0,1,0,1,...,iw4b0]
            x_du = np.zeros((niw,niw),dtype='complex')
            x_du[iw4f_slice,iw4f_slice] = chi_ph[0,1,0,0,...,iw4b0]

            return susz(self.beta(),self.U(atom),self.mu(),
                    x_uu,
                    x_ud,
                    x_dd,
                    x_du)
        else:
            return susz(self.beta(),self.U(atom),self.mu(),
                        chi_ph[0,0,0,0,...,iw4b0],
                        chi_ph[0,0,0,1,...,iw4b0],
                        chi_ph[0,1,0,1,...,iw4b0],
                        chi_ph[0,1,0,0,...,iw4b0])

    def chi_stat_pp(self,atom=1,worm=False,other_giw=None):
        chi_ph = self.chi_pp(atom, other_giw, worm)
        iw4b0 = chi_ph.shape[-1]//2
        return susz(self.beta(),self.U(atom),self.mu(),
                    chi_ph[0,0,0,0,...,iw4b0],
                    chi_ph[0,0,0,1,...,iw4b0],
                    chi_ph[0,1,0,1,...,iw4b0],
                    chi_ph[0,1,0,0,...,iw4b0])

    def chi_stat_bar(self,atom=1, other_giw=None):
        """ worm only """
        chi_ph = self.chi_ph_bar(atom, other_giw,)
        iw4b0 = chi_ph.shape[-1]//2
        return susz(self.beta(),self.U(atom),self.mu(),
                chi_ph[0,0,0,0,...,iw4b0],
                chi_ph[0,0,0,1,...,iw4b0],
                chi_ph[0,1,0,1,...,iw4b0],
                chi_ph[0,1,0,0,...,iw4b0])
    
    def chi_phys(self, atom=1):
        """
        returns tuple of local physical Xs, Xc
        """
        strg = self.iter_str+"/ineq-"+str(atom).zfill(3)
        dat_ntn0 = np.array(self.get(strg+"/ntau-n0/value"))
        dat_tausus = np.array(self.get(".axes/tausus"))
        dat_occ =  np.array(self.get(strg+"/occ/value"))
        occ = dat_occ[0,0,0,0] + dat_occ[0,1,0,1]
        magn = dat_occ[0,0,0,0] - dat_occ[0,1,0,1]
        dtau = dat_tausus[1] - dat_tausus[0]
        print('# delta_tau =', dtau)
        chi_tau_charge = dat_ntn0[0,1,0,1,:] + dat_ntn0[0,1,0,0,:] + dat_ntn0[0,0,0,1,:] + dat_ntn0[0,0,0,0,:] - occ**2
        chi_tau_magn = dat_ntn0[0,1,0,1,:] - dat_ntn0[0,1,0,0,:] - dat_ntn0[0,0,0,1,:] + dat_ntn0[0,0,0,0,:] - magn**2

        chi_phys_charge = 1/2.*integ.simps(chi_tau_charge, dx = dtau)
        chi_phys_spin = 1/2.*integ.simps(chi_tau_magn, dx = dtau)
        return  chi_phys_spin, chi_phys_charge


class susz(object):
    def __init__(self,beta,U,mu,uu,ud,dd,du):
        assert uu.shape == ud.shape == dd.shape == du.shape \
            ,"shape of spin components must be equal"
        assert uu.ndim == 2, "dimension 2 for spin components expected"
        self.beta   = float(beta)
        self.U      = float(U)
        self.mu      = float(mu)
        self.Niwf   = int(uu.shape[0]//2) 
        self.uu     = np.array(uu)
        self.ud     = np.array(ud)
        self.dd     = np.array(dd)
        self.du     = np.array(du)
        self.c     = 0.5 * (self.uu + self.dd + self.ud + self.du)
        self.s     = 0.5 * (self.uu + self.dd - self.ud - self.du)
        self.sc    = 0.5 * (- self.uu + self.dd - self.ud + self.du)
        self.cs    = 0.5 * (- self.uu + self.dd + self.ud - self.du)
        self.matrix = np.vstack(( np.hstack((self.uu, self.ud)),  
                                  np.hstack((self.du,self.dd)) )) 
        
        self.cs_matrix = np.vstack(( np.hstack((self.s, self.sc)),  
                                     np.hstack((self.cs,self.c)) )) 
        self.nu     = np.linspace(-(2*(self.Niwf-1)+1)*np.pi/self.beta,\
                                  (2*(self.Niwf-1)+1)*np.pi/self.beta,num=2*self.Niwf)

#functions
# from w2dyn.auxiliaries.compoundIndex
class GFComponent:
    """ Class for indexing green's functions.
    An instance of GFComponent holds the following fields:
    *** index: compound index of all indices (one-based single number)
    *** bands: band indices (zero-based list)
    *** spins: spin indices (zero-based list)
    *** bandspin: band-spin compound indices
    *** n_bands: number of impurity orbitals
    *** n_ops: number of operators in Greens function
             2 -> 1-particle Green's function
             4 -> 2-particle Green's function"""


    def __init__(self, index=None,
                 bands=None, spins=None, bandspin=None,
                 n_bands=0, n_ops=0, n_spins=2):

        if n_bands == 0 or n_ops == 0:
            raise ValueError('n_bands and n_ops have to be set'
                             ' to non-zero positive integers')

        self.n_bands = n_bands
        self.n_ops = n_ops
        dims_bs = n_ops * (n_bands*n_spins,)
        dims_1 = (n_bands, n_spins)

        if index is not None and bands is None:  # initialize from compound index
            self.index = index
            self.bandspin = list(np.unravel_index(self.index-1, dims_bs))
            self.bands, self.spins = np.unravel_index(self.bandspin, dims_1)

        elif bands is not None and index is None:  # initialize from bands (and spins)
            self.bands = bands
            if spins is None:  # use only band indices (e.g. d/m channel)
                self.spins = n_ops * (0,)
            else:
                self.spins = spins

            self.bandspin = np.ravel_multi_index(
                (self.bands, self.spins), (n_bands, n_spins))
            self.index = np.ravel_multi_index(self.bandspin, dims_bs) + 1

        elif bandspin is not None and index is None:
            self.index = np.ravel_multi_index(bandspin, dims_bs) + 1

        else:
            raise ValueError('index and bands both supplied')

    def bsbs(self):
        bsbs = np.vstack((self.bands, self.spins)).transpose().reshape(-1)
        return tuple(bsbs)

def component2index_general(Nbands, N, b, s):
    """ converting a band-spin pattern into an index
    :param N: number of operators
    :param b: band array of length N
    :param s: spin array of length N
    :return index: general flavor index"""
      
    comp = GFComponent(n_bands=Nbands, n_ops=N, bands=b, spins=s)
     
    return comp.index

# adaption of w2dyn_g4iw_worm_to_triqs_block2gf
def compose_g4iw_worm(g4iw, beta, norb, qtype="value"):
    """Converts a dictionary mapping zero-padded five digits long string
    representations of compound indices to components of the
    two-particle Green's function as ndarrays with two fermionic
    frequency indices nu, nu' and one bosonic frequency index omega in
    the order [nu, nu', omega], as produced by w2dynamics, into one 
    single array with indices [o, s, o, s, o, s, o, s, nu, nu', omega].
    Missing components are filled with zeros.

    Takes:
    g4iw : mapping from compound indices to components of the two-particle Green's function
    beta : inverse temperature
    norb : number of orbitals
    qtype : type/statistic of quantity to extract (value, error)

    Returns:
    np.ndarray : two-particle Green's function with one bosonic and two fermionic frequencies

    Author: Alexander Kowalski (2019) """

    # get number of positive freqs from a component of the result
    for i in range(100000):
        try:
            arr = g4iw["g4iw-worm/{:05}".format(i)][qtype][()]
            n4iwf, n4iwf_check, n4iwb = arr.shape
            assert(n4iwf == n4iwf_check)
            n4iwf, n4iwb = n4iwf//2, n4iwb//2 + 1
            break
        except KeyError:
            continue
        except AssertionError:
            raise ValueError("At least one component of g4iw-worm has an incorrect shape: should be (n4iwf, n4iwf, n4iwb)")

        return ValueError("g4iw-worm does not contain any valid components")

    nsp = 2
    # Piece blocks for the triqs block Green's function together from
    # individual components, looping over blocks and then indices,
    # with offsets keeping track of the previous block sizes for
    # constructing the right w2dynamics compound indices
    result = np.zeros((norb, nsp, norb, nsp, norb, nsp, norb, nsp, n4iwf * 2, n4iwf * 2, n4iwb * 2 - 1), arr.dtype)
    for o1 in range(norb):
        for s1 in range(nsp):
            for o2 in range(norb):
                for s2 in range(nsp):
                    for o3 in range(norb):
                        for s3 in range(nsp):
                            for o4 in range(norb):
                                for s4 in range(nsp):
                                    # we assume that spin is desired to be the
                                    # slowest changing index in the triqs
                                    # block structure, so we get orbital
                                    # indices for the compound index from the
                                    # block index by modulo and spin indices
                                    # by integer division
                                    cindex = component2index_general(
                                        norb, 4,
                                        np.array((o1, o2, o3, o4)),
                                        np.array((s1, s2, s3, s4)))
                                    try:
                                        result[o1, s1, o2, s2, o3, s3, o4, s4, :, :, :] = (
                                            beta * g4iw[("g4iw-worm/{:05}".format(cindex))]
                                            [qtype][()])
                                    except KeyError:
                                        pass  # writing into zeros, leave it zeroed

    return result


def asymp_chi(nu, beta):
    """
    Returns bubble asymptotic -2*beta/nu^2,
    excluding inner fermionic Matsubara frequencies up
    to nu for +/-omega_max = pi/beta*(2*nu+1)
    """
    summ = 0
    for n in range(nu):
        summ += 1/(2*n+1)**2
    return 2*beta*(1/8. - summ/np.pi**2)

def gradient(x, y):
    '''returns central differences and simple
    differences at begin and end of output vector'''
    assert len(x) == len(y), 'arguments must be of same length'
    yoverx=np.divide(np.diff(y), np.diff(x))
    diff = np.empty(len(x),dtype='complex')
    diff[0]=yoverx[0]
    for i in range(len(x)-2):
        f = np.diff(x)[i]/(np.diff(x)[i]+np.diff(x)[i+1])
        diff[i+1]= (1-f)*yoverx[i]+ f*yoverx[i+1]
    diff[-1]=yoverx[-1]
    return diff
    

def sub_matrix(matrix,N):
    """
    Returns n x n  numpy.matrix around mid of quadratic numpy.matrix

    Exampe: matrix=
               [[ 1, 2, 3, 4],
                [ 5, 6, 7, 8],
                [ 9,10,11,12],
                [13,14,15,16]]

    sub_matrix(matrix,2)=
                  [[6 , 7],
                   [10,11]]
    """
    if type(matrix) is np.ndarray:
        if matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1]:
            mid = matrix.shape[0]//2
            if int(N) > matrix.shape[0]:
                print('Error: shape of submatrix greater then input matrix')
                print('input N =', N, 'is set to', matrix.shape[0])
                N = matrix.shape[0]
            if matrix.shape[0]%2 == 0:
                n = (int(N)//2)*2
                if n <2:
                    n=2
                if N%2 != 0 or N<2:
                    print('even input matrix')
                    print('input N =', N, 'is set to', n)
                return matrix[ (int(mid)-int((n+1)//2)):(int(mid)+int(n//2)),\
                               (int(mid)-int((n+1)//2)):(int(mid)+int(n//2)) ]
            else:
                n = (int(N)//2)*2+1
                if n <1:
                    n=1
                if N%2 == 0 or N<1:
                    print('uneven input matrix')
                    print('input N =', N, 'is set to', n)
                return matrix[ (int(mid)-int((n)//2)):(int(mid)+int((n+1)//2)),\
                               (int(mid)-int((n)//2)):(int(mid)+int((n+1)//2)) ]
        else:
            print('Error: sub_matrix() expecting quadratic two-dimensional matrix')
    else:
        print('TypeError: sub_matrix() expecting argument of type numpy.ndarray')

def off_diag(matrix):
    """
    Returns off diagonal values of the upper left and lower right submatrix as numpy.matrix

    Exampe: matrix=
                   [[ 1, 2, 3, 4],
                    [ 5, 6, 7, 8],
                    [ 9,10,11,12],
                    [13,14,15,16]]

    off_diag(matrix)=
                   [[ 0, 2, 0, 0],
                    [ 5, 0, 0, 0],
                    [ 0, 0, 0,12],
                    [ 0, 0,15, 0]]
    """
    if type(matrix) is np.ndarray:
        if matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1]\
                            and matrix.shape[0]%2 == 0:
            end                 = matrix.shape[0]
            half                = end//2
            new                 = np.copy(matrix)
            new[:half,half:end] = 0
            new[half:end,:half] = 0
            np.fill_diagonal(new,0)
            return new
        else:
            print('Error: off_diag() expecting quadratic even two-dimensional matrix')
    else:
        raise TypeError('off_diag() expecting argument of type numpy.ndarray')


def off_counter(matrix):
    """
    Returns off diagonal values of the upper right and lower left submatrix
    along the counter diagonal as numpy.matrix

    Exampe: matrix=
                   [[ 1, 2, 3, 4],
                    [ 5, 6, 7, 8],
                    [ 9,10,11,12],
                    [13,14,15,16]]

    off_counter(matrix)=
                   [[ 0, 0, 3, 4],
                    [ 0, 0, 7, 8],
                    [ 9,10, 0, 0],
                    [13,14, 0, 0]]
    """
    if type(matrix) is np.ndarray:
        if matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1] and matrix.shape[0]%2 == 0:
            end                    = matrix.shape[0]
            half                   = end//2
            new                    = np.copy(matrix)
            new[:half,:half]       = 0
            new[half:end,half:end] = 0
            return new
        else:
            print('Error: off_counter() expecting quadratic even two-dimensional matrix')
    else:
        raise TypeError('off_counter() expecting argument of type numpy.ndarray')

# ---------------------------------------
# free lattice Hamlitonians
# ---------------------------------------
def ek(t=0.25,tpr=0,tsec=0,kpoints=48,q=[0.,0.]):
    "return 2d sqaured lattice Hamiltonian"
    k = np.linspace(0.,2*np.pi,kpoints,endpoint=False)
    kx = np.array(k+q[0])[:,None]
    ky = np.array(k+q[1])[None,:]
    # way to automatically treat arbitrary dimension
    # ---------------------------------------------
    # from sympy.utilities.iterables import multiset_permutations
    # shape = np.ones(dim,dtype=int)
    # shape[0] = -1
    # shapes = multiset_permutations(shape)
    # ek =  sum([- 2*t*np.cos(2*np.pi*k.reshape(s)) for s in shapes])\
    
    return - 2*t*(np.cos(kx) + np.cos(ky))\
               - 4*tpr*np.cos(kx)*np.cos(ky)\
               - 2*tsec*(np.cos(2*kx)+np.cos(2*ky))
               


# plotting helper:
# -------------------------------------
# colormap inspired by Patrick Chalupa
# -------------------------------------
cdict_white = {'blue':  [[0.0, 0.6, 0.6],
                   [0.499, 1.0, 1.0],
                   #[0.5, 0.0, 0.0],
                   [0.5, 1.0, 1.0],
                   [0.501, 0.0, 0.0],
                   [1.0, 0., 0.]],
         'green': [[0.0, 0.0, 0.0],
                   [0.02631578947368421, 7.673360394717657e-06, 7.673360394717657e-06],
                   [0.05263157894736842, 0.00012277376631548252, 0.00012277376631548252],
                   [0.07894736842105263, 0.0006215421919721302, 0.0006215421919721302],
                   [0.10526315789473684, 0.0019643802610477203, 0.0019643802610477203],
                   [0.13157894736842105, 0.004795850246698536, 0.004795850246698536],
                   [0.15789473684210525, 0.009944675071554084, 0.009944675071554084],
                   [0.18421052631578946, 0.018423738307717093, 0.018423738307717093],
                   [0.21052631578947367, 0.031430084176763524, 0.031430084176763524],
                   [0.23684210526315788, 0.050344917549742546, 0.050344917549742546],
                   [0.2631578947368421, 0.07673360394717657, 0.07673360394717657],
                   [0.2894736842105263, 0.11234566953906126, 0.11234566953906126],
                   [0.3157894736842105, 0.15911480114486534, 0.15911480114486534],
                   [0.3421052631578947, 0.21915884623353094, 0.21915884623353094],
                   [0.3684210526315789, 0.2947798129234735, 0.2947798129234735],
                   [0.39473684210526316, 0.3884638699825815, 0.3884638699825815],
                   [0.42105263157894735, 0.5028813468282164, 0.5028813468282164],
                   [0.4473684210526315, 0.6408867335272133, 0.6408867335272133],
                   [0.47368421052631576, 0.8055186807958807, 0.8055186807958807],
                   [0.499, 1.0, 1.0],
                   #[0.5, 0.0, 0.0],
                   [0.5, 1.0, 1.0],
                   [0.501, 1.0, 1.0],
                   [0.5263157894736843, 0.8055186807958807, 0.8055186807958807],
                   [0.5526315789473685, 0.6408867335272133, 0.6408867335272133],
                   [0.5789473684210527, 0.5028813468282164, 0.5028813468282164],
                   [0.6052631578947368, 0.3884638699825815, 0.3884638699825815],
                   [0.631578947368421, 0.2947798129234735, 0.2947798129234735],
                   [0.6578947368421053, 0.21915884623353094, 0.21915884623353094],
                   [0.6842105263157895, 0.15911480114486534, 0.15911480114486534],
                   [0.7105263157894737, 0.11234566953906126, 0.11234566953906126],
                   [0.736842105263158, 0.07673360394717657, 0.07673360394717657],
                   [0.7631578947368421, 0.050344917549742546, 0.050344917549742546],
                   [0.7894736842105263, 0.031430084176763524, 0.031430084176763524],
                   [0.8157894736842105, 0.018423738307717093, 0.018423738307717093],
                   [0.8421052631578947, 0.009944675071554084, 0.009944675071554084],
                   [0.868421052631579, 0.004795850246698536, 0.004795850246698536],
                   [0.8947368421052632, 0.0019643802610477203, 0.0019643802610477203],
                   [0.9210526315789473, 0.0006215421919721302, 0.0006215421919721302],
                   [0.9473684210526316, 0.00012277376631548252, 0.00012277376631548252],
                   [0.9736842105263158, 7.673360394717657e-06, 7.673360394717657e-06],
                   [1.0, 0.0, 0.0]],
         'red':   [[0.0, 0., 0.],
                   [0.499, 0.0, 0.0],
                   [0.5, 1.0, 1.0],
                   #[0.5, 0.0, 0.0],
                   [0.501, 1.0, 1.0],
                   [1.0, 0.6, 0.6]]}

cmap_w = mpl.colors.LinearSegmentedColormap('chalupa_white',segmentdata = cdict_white,N=10000)

# ------------------------------------------------
# colormap for spin charge (green, red) distinction
# -------------------------------------------------
# define cdict
points = 600
half = points//2
cp = np.linspace(0,1,points)

green = np.zeros(points)
blue = np.zeros(points)
red = np.zeros(points)

green[:half]= (1-2.*cp[:half])**(1/7)
red[half:]= 0.25+(np.array(1.-2*cp[:half])[::-1])**(1/7)
blue[np.where(red>1)]= red[np.where(red>1)]-1.
red[np.where(red>1)] = 1.

Gn = np.vstack((np.column_stack((cp[:half],green[:half],green[:half])), np.column_stack((cp[-1],green[-1],green[-1]))))
Rd = np.vstack((np.column_stack((cp[0],red[0],red[0])), np.column_stack((cp[half:],red[half:],red[half:]))))
Bu = np.vstack((np.column_stack((cp[0],blue[0],blue[0])), np.column_stack((cp[half:],blue[half:],blue[half:]))))

cdict_gr = {'green':  Gn,
             'blue':  Bu,
              'red':  Rd}

cmap_gr = mpl.colors.LinearSegmentedColormap('reitner_gr',segmentdata = cdict_gr,N=10000).reversed()


green2 = np.zeros(points)
green2[:half]= (1-2.*cp[:half])**(1/7)
green2[half:]= 0.8*(1-2.*cp[:half][::-1])**(1/7)
Gn2 = np.vstack((np.column_stack((cp[:half],green2[:half],green2[:half])), np.column_stack((cp[-1],green2[-1],green2[-1]))))

cdict_gy = {'green':  Gn2,
             'blue':  Bu,
              'red':  Rd}

cmap_gy = mpl.colors.LinearSegmentedColormap('reitner_gy',segmentdata = cdict_gy,N=10000).reversed()

# ---------------------------------------
# normalized colormap from stackoverflow
# ---------------------------------------
class norm(mpl.colors.Normalize):
    def __init__(self, matrix, midpoint=0, clip=False):
        #normalize only real part
        M= np.real(matrix)
        vmin = np.amin(M)
        vmax = np.amax(M)
        self.midpoint = midpoint
        mpl.colors.Normalize.__init__(self, vmin, vmax, clip)

    def __call__(self, value, clip=None):
        if self.vmax == 0:
            normalized_min = 0
        else:
            normalized_min = max(0, 1 / 2 * (1 - abs((self.midpoint - self.vmin) / (self.midpoint - self.vmax))))
        if self.vmin == 0:
            normalized_max = 1
        else:
            normalized_max = min(1, 1 / 2 * (1 + abs((self.vmax - self.midpoint) / (self.midpoint - self.vmin))))
        normalized_mid = 0.5
        x, y = [self.vmin, self.midpoint, self.vmax], [normalized_min, normalized_mid, normalized_max]
        return sp.ma.masked_array(sp.interp(value, x, y))