# Purpose

This project takes:

1. __Model:__ PDFs for each dataset
1. __Data:__ 1D data with masses, one for each dataset
1. __Efficiencies:__ Pairs of muon and electron efficiencies
1. __Covariance matrix:__ Covariance matrix for c_{k}
1. __$r_{jpsi}$:__ Same as before.

and does a simultaneous fit to calculate $r_K$.

# Usage

Check the unit tests in `tests`, but in short:

```python
from extractor import extractor as ext

def main():
    obj          = ext()
    obj.rjpsi    = d_rjpsi
    obj.eff      = d_eff
    obj.cov      = cvmat
    obj.data     = d_dat
    obj.model    = d_mod 
    obj.plt_dir  = 'plots'

    result       = obj.get_rk()
```

where optionally, the fit plots are saved to the `plots` directory. All the structures starting with `d_` are dictionaries with the dataset as the key.

# Toy tests

## Sending jobs
Given that many toys are needed to check the fit, the fits are ran in the grid. For this do:

```bash
. /cvmfs/lhcb.cern.ch/lib/LbEnv
#make grid proxy for 100 hours
lhcb-proxy-init -v 100:00
lb-dirac bash

#you might need tqdm installed locally, in case it is not available in your system.
pip install --user tqdm

cd grid/

./rkex_jobs -j J -f F -m [local, wms]
```
where:

1. `J` is the number of jobs
1. `F` is the number of fits per jobs
1. `local` or `wms` specify wether the jobs are ran locally (for tests) or in the grid.

these jobs can be monitored in the dirac website as any other job.

__IMPORTANT:__ Do not send more than 1000 fits per job. Otherwise (given the way `submit.py` is written) random seeds will overlap between jobs.

## Retrieving outputs

In the same directory where the submission happened, a file called `jobids.out` will be created with the job ids. The following command:

```bash
dirac-wms-job-get-output -f jobids.out -D sandbox
```

will put all the job outputs in the `sandbox/` directory.

## Plotting

Run:

```bash
./rkex_plot
```

to 

1. Read all the `JSON` files in the retrieved sandboxes
1. Make a dataframe with the fit parameters.
3. Make plots and send them to the `plots` directory.


# Installing

Run:

```bash
pip install rk-extractor
```

# Developing and testing

Development should be done in a custom virtual environment, so first make one, then:

```bash
pip install pytest
```

then:

```bash
pytest tests -W ignore::DeprecationWarning
```
