from rkex_model import model

#----------------------
def test_simple():
    d_eff = {'d1' : (0.5, 0.4), 'd2' : (0.4, 0.3), 'd3' : (0.3, 0.2), 'd4' : (0.2, 0.1)}

    mod         = model(preffix='simple', d_eff=d_eff)
    mod.out_dir = 'tests/rkex_model/simple' 
    d_dat       = mod.get_data(d_nent={'d1' : 1e4, 'd2' : 1e4, 'd3' : 1e4, 'd4' : 1e4})
    d_mod       = mod.get_model()
#----------------------
if __name__ == '__main__':
    test_simple()

