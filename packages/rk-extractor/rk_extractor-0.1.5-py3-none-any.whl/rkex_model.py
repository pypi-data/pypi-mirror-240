import numpy
import zfit
import os
import matplotlib.pyplot as plt

from logzero     import logger  as log
from zutils.plot import plot    as zfp
from scipy.stats import poisson

#----------------------------------------------------
class model:
    def __init__(self, rk=1, preffix='', d_eff=None):
        self._obs    = zfit.Space('x', limits=(0, 100))
        self._rk     = rk
        self._preffix= preffix
        self._d_eff  = d_eff 
        self._out_dir= None

        zfit.settings.changed_warnings.hesse_name = False

        self._d_mod = None
    #----------------------------------------------------
    @property
    def out_dir(self):
        return self._out_dir

    @out_dir.setter
    def out_dir(self, value):
        try:
            os.makedirs(value, exist_ok=True)
        except:
            log.error(f'Cannot create: {value}')
            raise

        self._out_dir = value
        log.debug(f'Using output directory: {self._out_dir}')
    #----------------------------------------------------
    def _get_data_simple(self, nentries):
        nentries = int(nentries)

        arr_sig = numpy.random.normal(size=nentries, loc=50, scale=3)
        arr_bkg = numpy.random.exponential(size=nentries, scale=100)
    
        arr_dat = numpy.concatenate([arr_sig, arr_bkg])
    
        return arr_dat
    #----------------------------------------------------
    def _get_gauss(self, preffix=''):
        preffix= f'{preffix}_{self._preffix}'

        mu     = zfit.Parameter(f'mu_{preffix}', 50., 40,  60)
        sg     = zfit.Parameter(f'sg_{preffix}', 2.0,  1,   5)
        gauss  = zfit.pdf.Gauss(obs=self._obs, mu=mu, sigma=sg)
        nsg    = zfit.Parameter(f'nsg_{preffix}', 10, 0, 100000)
        esig   = gauss.create_extended(nsg)
    
        lb     = zfit.Parameter(f'lb_{preffix}', -0.05,  -0.10, 0.00)
        exp    = zfit.pdf.Exponential(obs=self._obs, lam=lb)
        nbk    = zfit.Parameter(f'nbk_{preffix}', 10, 0, 100000)
        ebkg   = exp.create_extended(nbk)
    
        pdf    = zfit.pdf.SumPDF([esig, ebkg]) 
    
        return pdf 
    #----------------------------------------------------
    def _get_ds_model(self, ds):
        self._pdf_mm = self._get_gauss(preffix=f'mm_{ds}')
        self._pdf_ee = self._get_gauss(preffix=f'ee_{ds}')
    
        return self._pdf_mm, self._pdf_ee
    #----------------------------------------------------
    def _get_ds_data(self, nentries, eff_ee=1.0, eff_mm=1.0):
        nentries_mm = poisson.rvs(nentries, size=1)[0]
        nentries_ee = poisson.rvs(nentries, size=1)[0]

        arr_mm      = self._get_data_simple(self._rk * nentries_mm)
        arr_ee      = self._get_data_simple(           nentries_ee)

        arr_flg_mm  = numpy.random.binomial(1, eff_mm, arr_mm.shape[0]) == 1
        arr_flg_ee  = numpy.random.binomial(1, eff_ee, arr_ee.shape[0]) == 1
    
        arr_mm      = arr_mm[arr_flg_mm] 
        arr_ee      = arr_ee[arr_flg_ee] 
        
        dst_mm = zfit.Data.from_numpy(obs=self._obs, array=arr_mm)
        dst_ee = zfit.Data.from_numpy(obs=self._obs, array=arr_ee)
    
        return dst_mm, dst_ee
    #----------------------------------------------------
    def get_data(self, d_nent=None, rseed=3):
        if self._d_eff is None:
            log.error(f'No efficiencies found, cannot provide data')
            raise

        numpy.random.seed(seed=rseed)

        d_data     = {}
        dst_mm_tos = None
        for ds, (eff_mm, eff_ee) in self._d_eff.items():
            ds_only    = ds.split('_')[0]
            nentries   = d_nent[ds_only]
            log.debug(f'Dataset: {ds}[{nentries}]')

            dst_mm, dst_ee = self._get_ds_data(nentries, eff_ee=eff_ee, eff_mm=eff_mm)
            if 'TIS' in ds:
                dst_mm     = dst_mm_tos
            else:
                dst_mm_tos = dst_mm

            log.debug(f'Electron data: {dst_ee.numpy().shape[0]}')
            log.debug(f'Muon data: {dst_mm.numpy().shape[0]}')

            d_data[ds]     = dst_mm, dst_ee

        for key, (dat_mm, dat_ee) in d_data.items():
            self._plot_data(f'{key}_mm', dat_mm)
            self._plot_data(f'{key}_ee', dat_ee)
    
        return d_data
    #----------------------------------------------------
    def get_cov(self, kind='diag', c = 0.01):
        l_mat = []
        if kind == 'diag_eq':
            l_mat = [[ c, 0, 0, 0 ],
                     [ 0, c, 0, 0 ],
                     [ 0, 0, c, 0 ],
                     [ 0, 0, 0, c ]]
        else:
            log.error(f'Invalid kind: {kind}')
            raise
    
        return numpy.array(l_mat)
    #----------------------------------------------------
    def get_rjpsi(self, kind='one'):
        d_rjpsi = {}
    
        if   kind == 'one':
            d_rjpsi['d1'] = 1 
            d_rjpsi['d2'] = 1 
            d_rjpsi['d3'] = 1 
            d_rjpsi['d4'] = 1 
        elif kind == 'eff_bias':
            d_rjpsi['d1'] = 0.83333333 
            d_rjpsi['d2'] = 0.83333333 
            d_rjpsi['d3'] = 0.83333333 
            d_rjpsi['d4'] = 0.83333333 
        else:
            log.error(f'Wrong kind: {kind}')
            raise
    
        return d_rjpsi
    #----------------------------------------------------
    def _plot_model(self, key, mod):
        if self._out_dir is None:
            return

        plt_dir = f'{self._out_dir}/plots/models'
        os.makedirs(plt_dir, exist_ok=True)

        obj= zfp(data=mod.create_sampler(n=10000), model=mod)
        obj.plot(nbins=50) 

        log.info(f'Saving to: {plt_dir}/{key}.png')
        plt.savefig(f'{plt_dir}/{key}.png')
        plt.close('all')
    #----------------------------------------------------
    def _plot_data(self, key, dat):
        if self._out_dir is None:
            return

        plt_dir = f'{self._out_dir}/plots/data'
        os.makedirs(plt_dir, exist_ok=True)

        arr_dat = dat.value().numpy()

        plt.hist(arr_dat, bins=50)

        log.info(f'Saving to: {plt_dir}/{key}.png')
        plt.savefig(f'{plt_dir}/{key}.png')
        plt.close('all')
    #----------------------------------------------------
    def get_model(self):
        if self._d_mod is not None:
            return self._d_mod
    
        d_mod       = {}
        if self._d_eff is None:
            d_mod['d1'] = self._get_ds_model('d1')
            d_mod['d2'] = self._get_ds_model('d2')
            d_mod['d3'] = self._get_ds_model('d3')
            d_mod['d4'] = self._get_ds_model('d4')
        else:
            d_mod       = { ds : self._get_ds_model(ds) for ds in self._d_eff }

        for key, (mod_ee, mod_mm) in d_mod.items():
            self._plot_model(f'{key}_ee', mod_ee)
            self._plot_model(f'{key}_mm', mod_mm)
    
        self._d_mod = d_mod
    
        return self._d_mod
    #----------------------------------------------------
    @staticmethod
    def get_eff(kind='equal'):
        d_eff = {}
        if   kind == 'diff':
            d_eff['d1'] = (0.6, 0.3)
            d_eff['d2'] = (0.5, 0.2)
            d_eff['d3'] = (0.7, 0.3)
            d_eff['d4'] = (0.8, 0.4)
        elif kind == 'half':
            d_eff['d1'] = (0.6, 0.3)
            d_eff['d2'] = (0.6, 0.3)
            d_eff['d3'] = (0.6, 0.3)
            d_eff['d4'] = (0.6, 0.3)
        elif kind == 'equal':
            d_eff['d1'] = (0.3, 0.3)
            d_eff['d2'] = (0.3, 0.3)
            d_eff['d3'] = (0.3, 0.3)
            d_eff['d4'] = (0.3, 0.3)
        elif kind == 'bias':
            d_eff['d1'] = (0.6, 0.25)
            d_eff['d2'] = (0.6, 0.25)
            d_eff['d3'] = (0.6, 0.25)
            d_eff['d4'] = (0.6, 0.25)
        else:
            log.error(f'Invalid kind: {kind}')
            raise
    
        return d_eff
#----------------------------------------------------

