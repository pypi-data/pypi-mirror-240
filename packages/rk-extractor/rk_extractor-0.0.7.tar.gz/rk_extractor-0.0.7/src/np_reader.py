import os
import numpy
import utils_noroot as utnr

from ndict             import ndict
from logzero           import logger         as log
from rk.eff_yld_loader import eff_yld_loader as eyl

#----------------------------------------
class np_reader:
    '''
    Class used to read nuisance parameters to calculate RK
    '''
    #------------------------
    def __init__(self, sys=None, sta=None, yld=None):
        '''
        sys (str): Version of efficiencies obtained when assessing systematics
        sta (str): Version of efficiencies obtained when assessing statistical uncertainties with bootstrapping
        yld (str): Version of fitted data yields (only Jpsi and Psi2S)
        '''
        self._sys         = sys 
        self._sta         = sta
        self._yld         = yld

        self._eff_dir     = None
        self._cov_dir     = None
        self._d_yld       = ndict()
        self._d_eff       = ndict()
        self._sys_flg     = 'pall_tall_gall_lall_hall_rall_qall_bnom_snom'
        self._l_ds_lab    = ['r1_TOS', 'r1_TIS', 'r2p1_TOS', 'r2p1_TIS', '2017_TOS', '2017_TIS', '2018_TOS', '2018_TIS']

        self._cache       = False
        self._initialized = False 
    #------------------------
    @property
    def cache(self):
        return self._cache

    @cache.setter
    def cache(self, value):
        if value not in [True, False]:
            log.error(f'Invalid cache value: {value}')
            raise ValueError

        self._cache = value
    #------------------------
    def _initialize(self):
        if self._initialized:
            return

        self._eff_dir = os.environ['EFFDIR']
        self._cov_dir = f'{self._eff_dir}/../covariance'

        self._cache_data(channel='ee')
        self._cache_data(channel='mm')

        self._check_data()

        self._initialized = True
    #------------------------
    def _check_data(self):
        for key, arr_yld in self._d_yld.items():
            if len(arr_yld) == len(self._l_ds_lab):
                continue

            log.error(f'Lengths of yields for {key} does not align with labels: {self._l_ds_lab} <=> {arr_yld}')
            raise

        for key, arr_eff in self._d_eff.items():
            if len(arr_eff) == len(self._l_ds_lab):
                continue

            log.error(f'Lengths of efficiencies for {key} does not align with labels: {self._l_ds_lab} <=> {arr_eff}')
            raise
    #------------------------
    def _cache_data(self, channel=None):
        '''
        For a given channel, ee or mm, it will fill the dictionary of efficiencies for each
        dataset and trigger.
        '''

        cas_dir        = '/tmp/npt_reader' 
        os.makedirs(cas_dir, exist_ok=True)
        eff_cache_path = f'{cas_dir}/eff_{channel}.pkl'
        yld_cache_path = f'{cas_dir}/yld_{channel}.pkl'

        if self._cache and os.path.isfile(eff_cache_path) and os.path.isfile(yld_cache_path):
            log.info(f'Picking cached data from: {eff_cache_path}')
            log.info(f'Picking cached data from: {yld_cache_path}')

            self._d_eff = utnr.load_pickle(eff_cache_path)
            self._d_yld = utnr.load_pickle(yld_cache_path)

            return

        if channel not in ['ee', 'mm']:
            log.error(f'Wrong channel: {channel}')
            raise ValueError

        l_trg = ['ETOS', 'GTIS'] if channel == 'ee' else ['MTOS', 'MTOS']
        for proc in ['sign', 'ctrl']:
            l_eff = []
            l_yld = []
            for year in ['r1', 'r2p1', '2017', '2018']:
                for trig in l_trg:
                    eff, yld = self._get_eff_yld(f'{proc}_{channel}', year, trig)

                    l_eff.append(eff)
                    l_yld.append(yld)

            self._d_eff[proc, channel] = numpy.array(l_eff)
            self._d_yld[proc, channel] = numpy.array(l_yld)

        utnr.dump_pickle(self._d_eff, eff_cache_path)
        utnr.dump_pickle(self._d_yld, yld_cache_path)
    #------------------------
    def _get_eff_yld(self, proc, year, trig):
        '''
        Will return numerical value of efficiency and fitted yield, for a specifi process
        in a year and trigger
        '''
        obj        = eyl(proc, trig, year, self._sys_flg)
        obj.eff_var= 'B_PT'
        t_yld, d_eff = obj.get_values(eff_version = self._sys, yld_version=self._yld)

        ctf  = d_eff['nom', 'B_PT']
        deff = ctf.efficiency
        oeff = deff.efficiency()
        eff  = oeff.val[0]
        yld  = t_yld[0]

        return eff, yld
    #------------------------
    def get_cov(self, kind=None):
        '''
        Will return covariance matrix (nxn numpy array)
        '''
        self._initialize()

        if kind not in ['sys', 'sta']:
            log.error(f'Invalid uncertainty: {kind}')
            raise ValueError

        eff_ver  = self._sys if kind == 'sys' else self._sta
        pkl_path = f'{self._cov_dir}/{eff_ver}_{self._yld}/rx/matrix_abs_rc/tot.pkl'
        log.info(f'Picking up covariance from: {pkl_path}')
        cov      = utnr.load_pickle(pkl_path)

        return cov
    #------------------------
    def get_eff(self):
        '''
        Will return rare mode efficiencies

        d_eff (dict): Dictionary {ds : (eff_mm, eff_ee)} with efficiency objects
        '''
        self._initialize()

        arr_eff_rare_mm = self._d_eff['sign', 'mm'] 
        arr_eff_rare_ee = self._d_eff['sign', 'ee'] 

        d_eff = {}
        for ds_lab, eff_mm, eff_ee in zip(self._l_ds_lab, arr_eff_rare_mm, arr_eff_rare_ee):
            d_eff[ds_lab] = eff_mm, eff_ee

        return d_eff 
    #------------------------
    def get_byields(self):
        '''
        Will return dictionary with efficiency corrected yields {ds : yld}
        e.g. {'r1_TIS_ee': 40021323}
        '''
        self._initialize()

        arr_eff_jpsi_mm = self._d_eff['ctrl', 'mm'] 
        arr_eff_jpsi_ee = self._d_eff['ctrl', 'ee'] 

        arr_yld_jpsi_mm = self._d_yld['ctrl', 'mm'] 
        arr_yld_jpsi_ee = self._d_yld['ctrl', 'ee'] 

        arr_yld_jpsi_mm = arr_yld_jpsi_mm / arr_eff_jpsi_mm
        arr_yld_jpsi_ee = arr_yld_jpsi_ee / arr_eff_jpsi_ee 

        d_byld_ee = {f'{ds}_ee' : byld for ds, byld in zip(self._l_ds_lab, arr_yld_jpsi_ee)}
        d_byld_mm = {f'{ds}_mm' : byld for ds, byld in zip(self._l_ds_lab, arr_yld_jpsi_mm)}

        d_byld= {}
        d_byld.update(d_byld_ee)
        d_byld.update(d_byld_mm)

        return d_byld
    #------------------------
    def get_rjpsi(self):
        '''
        Will return an array with rjpsi for every trigger and dataset 
        '''
        self._initialize()

        arr_eff_jpsi_mm = self._d_eff['ctrl', 'mm'] 
        arr_eff_jpsi_ee = self._d_eff['ctrl', 'ee'] 

        arr_yld_jpsi_mm = self._d_yld['ctrl', 'mm'] 
        arr_yld_jpsi_ee = self._d_yld['ctrl', 'ee'] 

        arr_rjpsi = (arr_yld_jpsi_mm / arr_yld_jpsi_ee) * (arr_eff_jpsi_ee / arr_eff_jpsi_mm)

        d_rjpsi   = {ds : rjpsi for ds, rjpsi in zip(self._l_ds_lab, arr_rjpsi)}

        return d_rjpsi
#----------------------------------------

