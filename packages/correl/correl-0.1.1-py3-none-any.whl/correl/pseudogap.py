# %%
import numpy as np
import matplotlib.pyplot as plt


class model(object):
    """"
    A class to co calulate the quantities for the model Hamiltonian
    H = Σ_kσ [(e_k - µ) n_kσ + (e_k+Q - µ) n_k+Qσ + U n_kσ n_k+Q-σ ]
    """
    def __init__(self, U, beta, mu, t=1, tpr=-0.2, tsec=0.1
                , Qx=np.pi, Qy=np.pi, kpoints: int=200, Niwf: int=100
                , Niwb: int=7 , deltino=1e-2, D=4, vpoints: int=401):
        self.U = U
        self.beta = beta
        self.mu = mu
        self.Qx = Qx
        self.Qy = Qy
        self.t = t
        self.tpr = tpr
        self.tsec = tsec
        self.kpoints = kpoints
        self.Niwf = Niwf
        self.Niwb = Niwb
        self.deltino = deltino
        self.k = np.linspace(-np.pi,np.pi,kpoints,endpoint=False)
        self.D = D
        self.vpoints = vpoints

    def ek(self,kx,ky):
        return  - 2*self.t*(np.cos(kx)+np.cos(ky)) \
                - 4*self.tpr*np.cos(kx)*np.cos(ky)\
                - 2*self.tsec*(np.cos(2*kx)+np.cos(2*ky))

    def Z(self,kx,ky):
        hk = self.ek(kx,ky)-self.mu
        hq = self.ek(kx+self.Qx,ky+self.Qy)-self.mu

        partsum = (1 + np.exp(-self.beta*hk) + np.exp(-self.beta*hq) \
                    + np.exp(-self.beta*(hk+hq+self.U)))
        return partsum

    def v(self):
        return np.linspace(-2*self.D,2*self.D,self.vpoints)

    def iv(self):
        return 1j*(2*np.arange(-self.Niwf,self.Niwf)+1)*np.pi/self.beta
    
    def iOmega(self):
        return 1j*(2*np.arange(-self.Niwb,self.Niwb))*np.pi/self.beta
        
    def g0(self,kx,ky,mats=True):
        hk = self.ek(kx,ky)-self.mu
        if mats:
            nu = self.iv()
        else:
            nu = self.v()+1j*self.deltino

        if (type(kx).__module__ == np.__name__ and type(ky).__module__ == np.__name__
            and kx.ndim == 2 and ky.ndim == 2):
            hk = hk[None,:,:]
            nu = nu[:,None,None]
        return 1/(nu-hk)

    def g(self,kx,ky,mats=True,fancyU=False):
        hk = self.ek(kx,ky)-self.mu
        hq = self.ek(kx+self.Qx,ky+self.Qy)-self.mu
        nq = self.nk(kx+self.Qx,ky+self.Qy,fancyU=fancyU)


        if mats:
            nu = self.iv()
        else:
            nu = self.v()+1j*self.deltino

        if (type(kx).__module__ == np.__name__ and type(ky).__module__ == np.__name__
            and kx.ndim == 2 and ky.ndim == 2):
            hk = hk[None,:,:]
            hq = hq[None,:,:]
            nq = nq[None,:,:]
            nu = nu[:,None,None]
            if fancyU:
                self.U = self.U[None,:,:]  
        

        green = (1-nq)/(nu-hk) + nq/(nu-hk-self.U) 
        return green

    def sigma(self,kx,ky,mats=True,fancyU=False):
        G0 = self.g0(kx,ky,mats=mats)
        G = self.g(kx,ky,mats=mats,fancyU=fancyU)
        return 1./G0 - 1./G

    def nk(self,kx,ky,fancyU=False):
        hk = self.ek(kx,ky)-self.mu
        hq = self.ek(kx+self.Qx,ky+self.Qy)-self.mu
        if fancyU:
            self.U = self.U *(np.cos(kx)-np.cos(ky))**2
        else:
            self.U = self.U
        return np.where(hk>0
                        ,np.where(hq+self.U>0
                                ,(np.exp(-self.beta*hk) +  np.exp(-self.beta*(hk+hq+self.U)))\
                                /(1 + np.exp(-self.beta*hk) + np.exp(-self.beta*hq) + np.exp(-self.beta*(hk+hq+self.U)))
                                ,(np.exp(-self.beta*(hk-hq-self.U)) +  np.exp(-self.beta*(hk)))\
                                /(np.exp(self.beta*(hq+self.U))+ np.exp(-self.beta*(hk-hq-self.U)) + np.exp(self.beta*self.U) + np.exp(-self.beta*(hk)))
                        )
                        ,np.where(hq+self.U>0
                                ,(1 +  np.exp(-self.beta*(hq+self.U)))\
                                /(np.exp(self.beta*hk) + 1 + np.exp(-self.beta*(hq-hk)) + np.exp(-self.beta*(hq+self.U)))
                                ,(np.exp(self.beta*(hq+self.U)) + 1)\
                                /(np.exp(self.beta*(hk+hq+self.U)) + np.exp(self.beta*(hq+self.U)) + np.exp(self.beta*(hk+self.U)) + 1)
                        )
                    )
    def Dk(self,kx,ky):
        hk = self.ek(kx,ky)-self.mu
        hq = self.ek(kx+self.Qx,ky+self.Qy)-self.mu
        z   = self.Z(kx,ky)
        return 1/z*np.exp(-self.beta*(hk+hq+self.U))
    
    def cv(self,fancyU=False):
        kx = self.k[:,None]
        ky = self.k[None,:]
        hk = self.ek(kx,ky)-self.mu
        hq = self.ek(kx+self.Qx,ky+self.Qy)-self.mu


        z = (1 + np.exp(-self.beta*hk) + np.exp(-self.beta*hq) \
                    + np.exp(-self.beta*(hk+hq+self.U)))
        dzdb = -(hk*np.exp(-self.beta*hk) + hq*np.exp(-self.beta*hq) \
                    + (hk+hq+self.U)*np.exp(-self.beta*(hk+hq+self.U)))
        d2zdb2 = (hk**2*np.exp(-self.beta*hk) + hq**2*np.exp(-self.beta*hq) \
                    + (hk+hq+self.U)**2*np.exp(-self.beta*(hk+hq+self.U)))
        
        return -self.beta**2*np.sum( (dzdb/z)**2 - d2zdb2/z)/self.kpoints**2
    

    def x0(self,q=[0.,0.],mats=True):
        if mats == True:
            Omega = self.iOmega()
        else:
            Omega = self.v()
        if q == [0.,0.]:
            xx = np.zeros(Omega.shape,dtype='complex')
            Omega = Omega[:,None,None]
            kx = self.k[None,:,None]
            ky = self.k[None,None,:]
            z  = self.Z (kx,ky)
            Hk = self.ek(kx,ky)-self.mu
            HQ = self.ek(kx+self.Qx,ky+self.Qy)-self.mu
            xx[self.Niwb] = self.beta *  np.sum(1/z**2 * (np.exp(-self.beta*Hk) \
                                        + np.exp(-self.beta*(Hk+2*HQ+self.U)))
                                        ,axis=(1,2))/self.kpoints**2

            xx = xx + np.sum(1/z**2 * ( \
                + np.exp(-self.beta*(Hk+HQ+self.U))* (np.exp(self.beta*(self.U))-1)\
                    /(Omega+self.U) \
                + np.exp(-self.beta*(Hk+HQ))* (np.exp(-self.beta*(self.U))-1)\
                    /(Omega-self.U) \
            ),axis=(1,2))/self.kpoints**2
            return xx
        else:
            xx = np.zeros(Omega.shape,dtype='complex')
            Omega = Omega[:,None,None]
            kx = self.k[None,:,None]
            ky = self.k[None,None,:]
            z   = self.Z (kx             ,ky)
            zq  = self.Z (kx+q[0]        ,ky+q[1])
            Hk  = self.ek(kx             ,ky)             -self.mu
            HQ  = self.ek(kx+self.Qx     ,ky+self.Qy)     -self.mu
            H_q = self.ek(kx+q[0]        ,ky+q[1])        -self.mu
            HQq = self.ek(kx+self.Qx+q[0],ky+self.Qy+q[1])-self.mu

            xx =  np.sum(1/z/zq*(\
                (1 + np.exp(-self.beta*(HQ+HQq+self.U)))\
                    * (np.exp(-self.beta*H_q) - np.exp(-self.beta*Hk ))\
                        /(Omega+Hk-H_q)\
                + np.exp(-self.beta*HQ)\
                    * (np.exp(-self.beta*H_q) - np.exp(-self.beta*(Hk+self.U)))\
                        /(Omega+Hk-H_q+self.U)\
                + np.exp(-self.beta*HQq)\
                    * (np.exp(-self.beta*(H_q+self.U)) - np.exp(-self.beta*Hk))\
                        /(Omega+Hk-H_q-self.U)\
            ),axis=(1,2))/self.kpoints**2
            xx[self.Niwb] = np.sum(1/z/zq*(\
                np.where(Hk==H_q,
                self.beta * (np.exp(-self.beta*Hk ) + np.exp(-self.beta*(Hk+HQ+HQq+self.U)))\
                + np.exp(-self.beta*HQ)\
                    * (np.exp(-self.beta*H_q) - np.exp(-self.beta*(Hk+self.U)))\
                        /(Hk-H_q+self.U)\
                + np.exp(-self.beta*HQq)\
                    * (np.exp(-self.beta*(H_q+self.U)) - np.exp(-self.beta*Hk))\
                        /(Hk-H_q-self.U)
                ,(1 + np.exp(-self.beta*(HQ+HQq+self.U)))\
                    * (np.exp(-self.beta*H_q) - np.exp(-self.beta*Hk ))\
                        /(Hk-H_q)\
                + np.exp(-self.beta*HQ)\
                    * (np.exp(-self.beta*H_q) - np.exp(-self.beta*(Hk+self.U)))\
                        /(Hk-H_q+self.U)\
                + np.exp(-self.beta*HQq)\
                    * (np.exp(-self.beta*(H_q+self.U)) - np.exp(-self.beta*Hk))\
                        /(Hk-H_q-self.U)\
                )\
            ),axis=(1,2))/self.kpoints**2
            return xx
    
    def chi_uu(self,q=[0.,0.],mats=True):
        if mats == True:
            Omega = self.iOmega()
        else:
            Omega = self.v()
        if q == [0.,0.]:
            chi = np.zeros(Omega.shape,dtype='complex')
            nkk = self.nk(self.k[:,None],self.k[None,:])
            chi[self.Niwb] = self.beta * np.sum(nkk-nkk**2)/self.kpoints**2
            return chi
        else:
            chi = self.x0(q=q,mats=mats)
            return chi
        
    def chi_ud(self,q=[0.,0.],mats=True):
        if mats == True:
            Omega = self.iOmega()
        else:
            Omega = self.v()
        if q == [0.,0.]:
            chi = np.zeros(Omega.shape,dtype='complex')
            nkk = self.nk(self.k[:,None],self.k[None,:])
            nQQ = self.nk(self.k[:,None]+self.Qx,self.k[None,:]+self.Qy)
            dkk = self.Dk(self.k[:,None],self.k[None,:])
            chi[self.Niwb] =  self.beta * np.sum(dkk-nkk*nQQ)/self.kpoints**2
            return chi
        else:
            return np.zeros(Omega.shape,dtype='complex')
        
    def chi_bar_ud(self,q=[0.,0.],mats=True):
        if mats == True:
            Omega = self.iOmega()
        else:
            Omega = self.v()
        if q == [self.Qx,self.Qy]:
            chi = np.zeros(Omega.shape,dtype='complex')
            Omega = Omega[:,None,None]
            kx = self.k[None,:,None]
            ky = self.k[None,None,:]
            z   = self.Z (kx             ,ky)
            Hk  = self.ek(kx             ,ky)             -self.mu
            HQ  = self.ek(kx+self.Qx     ,ky+self.Qy)     -self.mu

            chi =  np.sum(1/z *(np.exp(-self.beta*HQ) - np.exp(-self.beta*Hk))\
                    /(Omega+Hk-HQ) 
                    ,axis=(1,2))/self.kpoints**2
            chi[self.Niwb] =  np.sum(np.where(Hk==HQ,
                                        self.beta/z*np.exp(-self.beta*Hk),
                                1/z *(np.exp(-self.beta*HQ) - np.exp(-self.beta*Hk))\
                                /(Hk-HQ) 
                                )
                    ,axis=(1,2))/self.kpoints**2
            return chi
        else:
            chi = self.x0(q=q,mats=mats)
            return chi


    def chi_s(self,q=[0.,0.],mats=True):
        return 1/3*(self.chi_uu(q=q,mats=mats)-self.chi_ud(q=q,mats=mats)) \
             + 2/3*self.chi_bar_ud(q=q,mats=mats)

    def chi_c(self,q=[0.,0.],mats=True):
        return self.chi_uu(q=q,mats=mats) + self.chi_ud(q=q,mats=mats)
# %%
