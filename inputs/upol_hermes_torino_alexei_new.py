conf={}

############################################################################
# resouce allocation

conf['ncpus']=1

############################################################################
# maxlike setup

conf['screen mode']='plain'
#conf['screen mode']='curses'

############################################################################
# mcsetup
conf['nruns']=10
conf['factor']=3
conf['tol']=1e-6
conf['itmax']=int(1e7)
conf['block size']=1000
conf['kappa']=1.3
conf['nll shift']=0

############################################################################
 
############################################################################
# params

conf['params']={}
conf['basis']='default'


conf['params']['pdf']={}
conf['params']['pdf']['widths0 valence']  = {'value':<<    5.76268738484120857102e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['pdf']['widths0 sea']      = {'value':<<    5.30657435247871234196e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['pdf']['Q0']      = {'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':0,'max':10}
conf['params']['pdf']['gk']      = {'value':<<    0.00000000000000000000e+00>>,'fixed':False,'min':0,'max':10}


conf['params']['ff']={}
conf['params']['ff']['widths0 pi+ fav']   = {'value':<<    1.20364572723908547225e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['ff']['widths0 pi+ unfav'] = {'value':<<    1.44170161905080473908e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['ff']['widths0 k+ fav']    = {'value':<<    1.32862274213378872556e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['ff']['widths0 k+ unfav']  = {'value':<<    1.86642762387136229574e-01>>,'fixed':False,'min':0,'max':1}
conf['params']['ff']['Q0']      = {'value':<<    1.00000000000000000000e+00>>,'fixed':True,'min':0,'max':10}
conf['params']['ff']['gk']      = {'value':<<    0.00000000000000000000e+00>>,'fixed':True,'min':0,'max':10}



############################################################################
# set data sets

conf['datasets']={}

# SIDIS

conf['datasets']['sidis']={}


conf['datasets']['sidis']['filters']={}
conf['datasets']['sidis']['filters'][0]={}
conf['datasets']['sidis']['filters'][0]['idx']=[1000,1001,1004,1005,1002,1003,1006,1007]
#conf['datasets']['sidis']['filters'][0]['filter']="z<0.6 and Q2>1.69 and pT>0.2 and pT<0.9" # npts    = 978 chi2    = 1206.873681
conf['datasets']['sidis']['filters'][0]['filter']="z<0.6 and Q2>1.69 and pT> 0.2 and pT<0.9" # rapidity Gunar wrote z< 0.2 and z>0.8 are padding bins TORINO's CUTS HERE
#conf['datasets']['sidis']['filters'][0]['filter']="Q2>1.69 and z>0.2 and z<0.6 and pT>0.2 and pT<0.9 and dy>-2" 

conf['datasets']['sidis']['xlsx']={}

conf['datasets']['sidis']['xlsx'][1000]='sidis/expdata/1000.xlsx'  # |  proton   | pi+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1001]='sidis/expdata/1001.xlsx'  # |  proton   | pi-    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1004]='sidis/expdata/1004.xlsx'  # |  deuteron | pi+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1005]='sidis/expdata/1005.xlsx'  # |  deuteron | pi-    | M_Hermes | hermes 

conf['datasets']['sidis']['xlsx'][1002]='sidis/expdata/1002.xlsx'  # |  proton   | k+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1003]='sidis/expdata/1003.xlsx'  # |  proton   | k-    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1006]='sidis/expdata/1006.xlsx'  # |  deuteron | k+    | M_Hermes | hermes 
conf['datasets']['sidis']['xlsx'][1007]='sidis/expdata/1007.xlsx'  # |  deuteron | k-    | M_Hermes | hermes 

conf['datasets']['sidis']['norm']={}
for k in conf['datasets']['sidis']['xlsx']: conf['datasets']['sidis']['norm'][k]={'value':1,'fixed':True,'min':0,'max':1} 






