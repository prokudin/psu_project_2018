conf={}

############################################################################
#mcsamp
conf['nruns']=10
conf['factor']=3
conf['tol']=1e-4
conf['itmax']=int(1e7)
conf['block size']=5000
conf['kappa']=1.3
conf['nll shift']=0

############################################################################
# params
conf['params']={}
# Parameters in gaussian approximation, parton model:
# GK approximate
conf['params']['gk']={}
conf['params']['gk']['gk0']  ={'value':   -8.18823e-02,'min': -0.3,'max':0,'fixed':False}
conf['params']['gk']['Q0']  ={'value':    1.82814e+00,'min':0.8,'max':2,'fixed':False}

# TMD PDF:
conf['params']['pdf']={}
conf['params']['pdf']['widths1_uv']  ={'value':    3.02739e-01,'min': 0.1,'max':0.7,'fixed':False}
conf['params']['pdf']['widths2_uv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['pdf']['widths1_dv']  ={'value':    3.02739e-01,'min': 0,'max':1,'fixed':'widths1_uv'}
conf['params']['pdf']['widths2_dv']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':'widths2_uv'}
conf['params']['pdf']['widths1_sea'] ={'value':    3.18638e-01,'min': 0.1,'max':0.9,'fixed':False}
conf['params']['pdf']['widths2_sea'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}

# TMD FF:
conf['params']['ffpi']={}
conf['params']['ffpi']['widths1_fav']   ={'value':    1.83933e-01,'min': 0,'max':0.5,'fixed':False}
conf['params']['ffpi']['widths2_fav']   ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffpi']['widths1_ufav'] ={'value':    1.68400e-01,'min': 0,'max':0.5,'fixed':False}
conf['params']['ffpi']['widths2_ufav'] ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffk']={}
conf['params']['ffk']['widths1_fav']    ={'value':    1.62704e-01,'min': 0,'max':0.5,'fixed':False}
conf['params']['ffk']['widths2_fav']    ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffk']['widths1_ufav']  ={'value':    3.36407e-01,'min': 0,'max':0.5,'fixed':False}
conf['params']['ffk']['widths2_ufav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffh']={}
conf['params']['ffh']['widths1_fav']    ={'value':    1.32925e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffh']['widths2_fav']    ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}
conf['params']['ffh']['widths1_ufav']  ={'value':    1.86073e-01,'min': 0,'max':1,'fixed':True}
conf['params']['ffh']['widths2_ufav']  ={'value':    0.00000e+00,'min':-1,'max':1,'fixed':True}

############################################################################
# set data sets

conf['datasets']={}
conf['datasets']['sidis']={}

conf['datasets']['sidis']['xlsx']={}
conf['datasets']['sidis']['xlsx'][1000]='sidis/expdata/1000.xlsx'  # |  proton   | pi+   | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1001]='sidis/expdata/1001.xlsx'  # |  proton   | pi-   | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1004]='sidis/expdata/1004.xlsx'  # |  deuteron | pi+   | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1005]='sidis/expdata/1005.xlsx'  # |  deuteron | pi-   | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1002]='sidis/expdata/1002.xlsx'  # |  proton   | k+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1003]='sidis/expdata/1003.xlsx'  # |  proton   | k-    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1006]='sidis/expdata/1006.xlsx'  # |  deuteron | k+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1007]='sidis/expdata/1007.xlsx'  # |  deuteron | k-    | M_Hermes | hermes 

conf['datasets']['sidis']['norm']={}
for idx in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][idx]={'value':1,'fixed':True,'min':0,'max':1} 

conf['datasets']['sidis']['filters']=["z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9 and dy>3."]

#conf['datasets']['sidis']['filters']=["z>0.2 and z<0.6  and Q2>1.69 and (pT/z)**2<0.25*Q2"]






