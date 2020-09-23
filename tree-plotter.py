import yaml
import uproot
from ROOT import *
import ROOT
import sys
import numpy as np
#from array import array

gROOT.SetBatch(1)

with open('LionKing2018_ROOTfiles.yml', 'r') as f_yml:
    _dict_yml = yaml.load(f_yml)

xsections = {}
with open("xsections_{}.yaml".format(2018), 'r') as stream:
    xsections = yaml.safe_load(stream)

Dict = [
        {'dataset':'GluGluToContinToZZTo2e2mu_13TeV_MCFM701_pythia8',                           'name':'ZZ',                    'Scale':1.0/1000.0,                     'FillColor': 800-2,             'LineColor':800-2},
        {'dataset':'GluGluToContinToZZTo2e2nu_13TeV_MCFM701_pythia8',                           'name':'ZZ',                    'Scale':1.0/1000.0,                     'FillColor': 800-2,             'LineColor':800-2 },
        {'dataset':'GluGluToContinToZZTo2e2tau_13TeV_MCFM701_pythia8',                          'name':'ZZ',                    'Scale':1.0/1000.0,                     'FillColor': 800-2,             'LineColor':800-2 },
        {'dataset':'GluGluToContinToZZTo2mu2nu_13TeV_MCFM701_pythia8',                          'name':'ZZ',                    'Scale':1.0/1000.0,                     'FillColor': 800-2,             'LineColor':800-2 },
        {'dataset':'GluGluToContinToZZTo2mu2tau_13TeV_MCFM701_pythia8',                         'name':'ZZ',                    'Scale':1.0/1000.0,                     'FillColor': 800-2,             'LineColor':800-2 },
        {'dataset':'GluGluToContinToZZTo4e_13TeV_MCFM701_pythia8',                              'name':'ZZ',                    'Scale':1.0/1000.0,                     'FillColor': 800-2,             'LineColor':800-2 },
        {'dataset':'GluGluToContinToZZTo4mu_13TeV_MCFM701_pythia8',                             'name':'ZZ',                    'Scale':1.0/1000.0,                     'FillColor': 800-2,             'LineColor':800-2 },
        {'dataset':'GluGluToContinToZZTo4tau_13TeV_MCFM701_pythia8',                            'name':'ZZ',                    'Scale':1.0/1000.0,                     'FillColor': 800-2,             'LineColor':800-2 },
        {'dataset':'ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8',                                    'name':'ZZ',                    'Scale':1.0,                     'FillColor': 800-2,             'LineColor':800-2 },
        {'dataset':'ZZTo4L_TuneCP5_13TeV_powheg_pythia8',                                       'name':'ZZ',                    'Scale':1.0,                     'FillColor': 800-2,             'LineColor':800-2 },
        {'dataset':'WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8',                               'name':'WZ',                    'Scale':4.65,               'FillColor': 860-4,             'LineColor':860-4 },
        {'dataset':'WWTo2L2Nu_NNPDF31_TuneCP5_13TeV-powheg-pythia8',                            'name':'WW',                    'Scale':1.0,                    'FillColor': 840+2,             'LineColor':840+2 },
        {'dataset':'ZZZ_TuneCP5_13TeV-amcatnlo-pythia8',                                        'name':'VVV',                   'Scale':1.0,                       'FillColor': 900-5,             'LineColor':900-5 },
        {'dataset':'WZZ_TuneCP5_13TeV-amcatnlo-pythia8',                                        'name':'VVV',                   'Scale':1.0,                     'FillColor': 900-5,             'LineColor':900-5 },
        {'dataset':'WWZ_TuneCP5_13TeV-amcatnlo-pythia8',                                        'name':'VVV',                   'Scale':1.0,                     'FillColor': 900-5,             'LineColor':900-5 },
        {'dataset':'TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8',                                    'name':'TT',                    'Scale':1.0,                     'FillColor': 920+1,             'LineColor':920+1 },
        {'dataset':'TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8',                           'name':'TT',                    'Scale':1.0,                      'FillColor': 920+1,             'LineColor':920+1 },
        {'dataset':'TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',                   'name':'TT',                    'Scale':1.0,                     'FillColor': 920+1,             'LineColor':920+1 },
        {'dataset':'TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',                    'name':'TT',                    'Scale':1.0,                     'FillColor': 920+1,             'LineColor':920+1 },
        {'dataset':'ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',             'name':'TT',                    'Scale':1.0,                   'FillColor': 920+1,             'LineColor':920+1 },
        {'dataset':'ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8',                 'name':'TT',                    'Scale':1.0,                   'FillColor': 920+1,             'LineColor':920+1 },
        #{'dataset':'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8',                          		'name':'TT',                    'Scale':1.0,                   'FillColor': 920+1,             'LineColor':920+1 },
        #{'dataset':'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',                       'name':'DY',                    'Scale':1.0,               'FillColor': 900+1,             'LineColor':900+1 },
        {'dataset':'DY1JetsToLL_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8',           'name':'DY',                    'Scale':1.0,                 'FillColor': 900+1,             'LineColor':900+1 },
        {'dataset':'DY1JetsToLL_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8',          'name':'DY',                    'Scale':1.0,                   'FillColor': 900+1,             'LineColor':900+1 },
        {'dataset':'DY1JetsToLL_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8',          'name':'DY',                    'Scale':1.0,                    'FillColor': 900+1,             'LineColor':900+1 },
        {'dataset':'DY1JetsToLL_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8',          'name':'DY',                    'Scale':1.0,                     'FillColor': 900+1,             'LineColor':900+1 },
        {'dataset':'DY2JetsToLL_M-50_LHEZpT_50-150_TuneCP5_13TeV-amcnloFXFX-pythia8',           'name':'DY',                    'Scale':1.0,                  'FillColor': 900+1,             'LineColor':900+1 },
        {'dataset':'DY2JetsToLL_M-50_LHEZpT_150-250_TuneCP5_13TeV-amcnloFXFX-pythia8',          'name':'DY',                    'Scale':1.0,                   'FillColor': 900+1,             'LineColor':900+1 },
        {'dataset':'DY2JetsToLL_M-50_LHEZpT_250-400_TuneCP5_13TeV-amcnloFXFX-pythia8',          'name':'DY',                    'Scale':1.0,                    'FillColor': 900+1,             'LineColor':900+1 },
        {'dataset':'DY2JetsToLL_M-50_LHEZpT_400-inf_TuneCP5_13TeV-amcnloFXFX-pythia8',          'name':'DY',                    'Scale':1.0,                     'FillColor': 900+1,             'LineColor':900+1 }
        ]

_ndatasets = len(Dict)

_PDs = [# for now since we remove the HLTs here we need this to be in this specific order. Look to change this soon with skimmed trees by HLTs
	'SingleMuon_Run2018A-Nano1June2019-v1',
	'SingleMuon_Run2018B-Nano1June2019-v1',
	'SingleMuon_Run2018C-Nano1June2019-v1',
	'SingleMuon_Run2018D-Nano1June2019-v1',
	'MuonEG_Run2018A-Nano1June2019-v1',
	'MuonEG_Run2018B-Nano1June2019-v1',
	'MuonEG_Run2018C-Nano1June2019-v1',
	'MuonEG_Run2018D-Nano1June2019_ver2-v1',
	'DoubleMuon_Run2018A-Nano1June2019-v1',
	'DoubleMuon_Run2018B-Nano1June2019-v1',
	'DoubleMuon_Run2018C-Nano1June2019-v1',
	'DoubleMuon_Run2018D-Nano1June2019_ver2-v1',
	'EGamma_Run2018A-Nano1June2019-v1',
	'EGamma_Run2018B-Nano1June2019-v1',
	'EGamma_Run2018C-Nano1June2019-v1',
	'EGamma_Run2018D-Nano1June2019-v1'
]

_nPDs = len(_PDs)


#Signal = [
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-1000_Mv-1000_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',	'name':'DMSimp',	'Scale':1688800.2565479695,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-10_Mv-10000_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':18494750.709021863,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-10_Mv-100_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':0.8669904588601057,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-150_Mv-10000_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':22365848.79274756,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-150_Mv-1000_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':140.06885877406805,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-1_Mv-10000_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':18543163.4943631,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-1_Mv-10_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':9.935543533037409,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-1_Mv-500_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':17.03813928243835,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-1_Mv-50_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':0.2818141214397169,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-50_Mv-200_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':3.1078816042797013,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-75_Mv-1000_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':130.8990124375216,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Axial_Mx-75_Mv-500_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':18.396549833051896,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-100_Mv-750_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-10_Mv-10_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-1_Mv-1000_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-1_Mv-100_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-1_Mv-20_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-200_Mv-500_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-50_Mv-10_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-50_Mv-350_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-50_Mv-400_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-10_Mv-100_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-10_Mv-50_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Pseudo_Mx-1_Mv-400_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-100_Mv-300_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-100_Mv-400_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-10_Mv-100_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-10_Mv-10_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-1_Mv-200_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-1_Mv-300_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-1_Mv-350_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-1_Mv-50_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-1_Mv-750_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-50_Mv-200_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-50_Mv-50_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-100_Mv-500_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-1_Mv-400_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-1_Mv-500_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-200_Mv-500_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-40_Mv-100_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Scalar_Mx-50_Mv-400_gDM1_gQ1_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Vector_Mx-0_Mv-20_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':7.222300258571872,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Vector_Mx-150_Mv-200_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':279.36285713413304,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Vector_Mx-1000_Mv-10000_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':106387675.22075082,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Vector_Mx-1000_Mv-1000_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':381006.49332780531,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Vector_Mx-150_Mv-500_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':18.914989725063801,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Vector_Mx-1_Mv-1000_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':130.11587861695793,          'FillColor':632 ,             'LineColor':632 },
#        {'dataset':'DarkMatter_MonoZToLL_NLO_Vector_Mx-1_Mv-100_gDM1_gQ0p25_TuneCUETP8M1_13TeV-madgraph',    'name':'DMSimp',        'Scale':1.0163086269068204,          'FillColor':632 ,             'LineColor':632 }
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
        #{'dataset':'',    'name':'DMSimp',        'Scale':,          'FillColor':632 ,             'LineColor':632 },
#	]




Var_Dict = [
        #{'variable':'delta_phi_ZMet',        	'nBins':32,             'xLow':-3.2,            'xHi':3.2,	'title':'#Delta #phi(Z,p_{T}^{miss})'},
        #{'variable':'Z_mass',        		'nBins':30,             'xLow':0,               'xHi':300,	'title':'M_{ll} [GeV]'},
        #{'variable':'sca_balance',   		'nBins':10,             'xLow':0,               'xHi':5,	'title':'|p_{T}^{miss}|/|p_{T}^{ll}|'},
        #{'variable':'emulatedMET',         	'nBins':10,             'xLow':0,               'xHi':600,	'title':'Emulated p_{T}^{miss} [GeV]'},
        #{'variable':'Z_pt',         		'nBins':15,             'xLow':0,		'xHi':500,	'title':'p_{T}^{ll} [GeV]'},
        #{'variable':'ngood_jets',              'nBins':15,             'xLow':0,               'xHi':15,	'title':'# jets'},
        #{'variable':'PV_npvs',                 'nBins':100,            'xLow':0,               'xHi':100,	'title':'# vtx'}
        #{'variable':'delta_R_ll',               'nBins':15,             'xLow':0,               'xHi':5,	'title':'#Delta R_{ll}'}
        #{'variable':'delta_phi_j_met',               'nBins':32,             'xLow':-3.2,               'xHi':3.2,        'title':'#Delta#phi(Jet,p_{T}^{miss})'},
        #{'variable':'met_phi',               'nBins':32,             'xLow':-3.2,               'xHi':3.2,        'title':'p_{T}^{miss} #phi'}
        {'variable':'met_pt',                  'nBins':10,             'xLow':50,               'xHi':100,	'title':'p_{T}^{miss} [GeV]'}
	]

_nVars = len(Var_Dict)

_cuts = "((lep_category==3 || lep_category==1) && Z_mass > 76 && Z_mass < 106 && Z_pt>60 && ngood_jets < 2 && ngood_bjets == 0 && met_pt<100 && met_pt > 50 && abs(delta_phi_ZMet) > 2.6 && delta_R_ll < 1.8 && abs(delta_phi_j_met) > 0.5 && sca_balance > 0.5 && sca_balance < 1.5 && nhad_taus == 0 )"

def test(_variable,_nBins,_xLow,_xHi,title):
   prf = TProof.Open("lite://")
   hists = [None] * _ndatasets
   stk = ROOT.THStack("stk", ";;Events / Bin ")
   mc = TH1F('h', 'h', _nBins, _xLow, _xHi)
   for i in range(_ndatasets):
      dictionary = Dict[i]
      dataset = dictionary['dataset']
      name = dictionary['name']
      chain = TChain("Events")
      run_chain = TChain("Runs")
      Nevt = 0
      neg_fac = 0.0
      for file in _dict_yml[dataset]['files']:
        chain.Add(file)
	file_in = uproot.open(file)
	Nevt += file_in["Runs"].array("genEventCount").sum()
      	original_xsec = abs(file_in["Events"].array("xsecscale")[0])
        neg_fac += np.mean(file_in["Events"].array("xsecscale")/original_xsec)*file_in["Runs"].array("genEventCount").sum()
        print " /doing this file : ", file
	print " ---- ", np.mean(file_in["Events"].array("xsecscale"))/original_xsec
      	#scale /= np.mean((1.0+file_in["Events"].array("xsecscale")/original_xsec)/2.0)
      if Nevt == 0 : continue
      scale = 60.0/float(Nevt)
      #scale = 1.0
      print neg_fac
      neg_fac /= float(Nevt)
      #print neg_fac
      print (1+neg_fac)/2.0
      xsec  = xsections[dataset]["xsec"]
      xsec *= xsections[dataset]["kr"]
      xsec *= xsections[dataset]["br"]
      xsec *= 1000.0
      scale *= xsec/original_xsec
      scale /= (1+neg_fac)/2.0
      #scale /= np.mean((1.0+file_in["Events"].array("xsecscale")/original_xsec)/2.0)
      chain.SetProof()
      hists[i] = TH1F(name, name,_nBins, _xLow, _xHi)
      chain.Project(name, _variable, "puWeight * xsecscale * btagEventWeight *" + _cuts)
      hists[i].SetName(name)
      chain.Reset()
      chain.Delete()
      hists[i].Scale(scale)
      print "========================================================"
      print "       ++  dataset :", dataset
      print "       + old xsec [fb] = ", original_xsec
      print "       + new xec [fb]  = ", xsec
      print "       + nevents       = ", Nevt
      print "       + scale         = ", scale
      print "       + yield in hist = ", hists[i].Integral()*scale
      print "========================================================"
      #hists[i].Scale(dictionary['Scale'])
      hists[i].SetFillColor(dictionary['FillColor'])
      hists[i].SetLineColor(dictionary['LineColor'])
      stk.Add(hists[i])
      mc.Add(hists[i])

   #Other.SetFillColor(880+1)
   ZZ.SetFillColor(800-2)
   WZ.SetFillColor(860-4)
   WW.SetFillColor(840+2)
   TT.SetFillColor(920+1)
   VVV.SetFillColor(900-5)
   DY.SetFillColor(900+1)

   leg  = TLegend(.7,.7,.9,.9, "", "fNDC")
   #leg.AddEntry(Other, "Other","F")
   leg.AddEntry(ZZ,"ZZ","F")
   leg.AddEntry(WZ, "WZ","F")
   leg.AddEntry(WW,"WW","F")
   leg.AddEntry(TT,"TT","F")
   leg.AddEntry(VVV,"VVV","F")
   leg.AddEntry(DY,"DY","F")


   dathists = [None] * _nPDs
   dat = TH1F('data', 'data',_nBins, _xLow, _xHi)
   dat2 = TH1F('data', 'data',_nBins, _xLow, _xHi)
   for j in range(_nPDs):
      pd = _PDs[j]
      chain = TChain("Events")
      for file in _dict_yml[pd]['files']:
         chain.Add(file)
      chain.SetProof()
      hist_name = pd.split('_')[0]
      dathists[j] = TH1F('data', 'data',_nBins, _xLow, _xHi)
      chain.Project('data', _variable, _cuts)
      dathists[j].SetName(hist_name)
      chain.Reset()
      chain.Delete()
      dat.Add(dathists[j])


   integ = mc.Integral(0,31)
   print " MC : "
   print " sumW    : ", integ
   integ2 = dat.Integral(0,31)
   print " data : "
   print " sumW    : ", integ2
   cOutput = TCanvas("cOutput", "cOutput", 800, 800)
   cOutput.SetFillStyle(4000)
   gStyle.SetOptStat(0)
   p1 = TPad("p1", "p1", 0, 0.25, 1, 1)
   p1.SetLogy()
   p1.SetBottomMargin(0)  # joins upper and lower plot
   p1.Draw()
   p1.cd()

   stk.SetMinimum(1.0)
   #stk.SetMaximum(520)
   stk.SetTitle(" ;"+ title + ";Events / Bin")
   stk.Draw("hist")
   dat.SetMarkerStyle(20)
   dat.SetMarkerColor(kBlack)
   dat.SetMarkerSize(0.5)
   dat.Draw("Esame")
   leg.Draw("same")
   pad = cOutput.cd()
   l = pad.GetLeftMargin()
   t = pad.GetTopMargin()
   r = pad.GetRightMargin()
   b = pad.GetBottomMargin()
   lab1 = TLatex()
   lab1.SetTextSize(0.03)
   lab1.SetTextAlign(11)
   lab1.SetTextFont(42)
   cmsTag = '#bf{CMS}'
   lab1.DrawLatexNDC(l+0.01, 1-t+0.029, cmsTag)
   lab2 = TLatex()
   lab2.SetTextSize(0.03)
   lab2.SetTextAlign(11)
   lab2.SetTextFont(42)
   cmsTag = 'll ch., 60.0 fb^{-1} (13 TeV)'
   lab1.DrawLatexNDC(l+0.5, 1-t+0.029, cmsTag)

   cOutput.cd()
   p2 = TPad("p2", "p2", 0, 0.05, 1, 0.25)
   p2.SetTopMargin(0)  # joins upper and lower plot
   p2.SetBottomMargin(0.2)
   p2.SetGridx()
   p2.Draw()
   p2.cd()

   #Ratio Parameters
   dat2 = dat.Clone()
   dat2.Divide(mc)
   dat2.SetTitle("")
   dat2.SetMaximum(1.75)
   dat2.SetMinimum(0.25)
   dat2.SetStats(0)
   dat2.SetMarkerColor(kBlack)
   dat2.SetMarkerStyle(20)

   #Adjust y-axis settings
   y = dat2.GetYaxis()
   y.SetTitle("Data/#Sigma MC")
   y.SetNdivisions(505)
   y.SetTitleSize(15)
   y.SetTitleFont(43)
   y.SetTitleOffset(1.75)
   y.SetLabelFont(43)
   y.SetLabelSize(15)

   # Adjust x-axis settings
   x = dat2.GetXaxis()
   x.SetTitle(title)
   x.SetTitleSize(15)
   x.SetTitleFont(43)
   x.SetTitleOffset(4.2)
   x.SetLabelFont(43)
   x.SetLabelSize(15)

   #Add a line at 1 for the ratio plot
   ll = TLine(_xLow, 1., _xHi, 1.)
   ll.SetLineWidth(2)
   ll.SetLineStyle(7)
   ll.SetLineColor(kBlack)

   dat2.Draw("P")
   ll.Draw("same")

   cOutput.SaveAs("plots/" + _variable + "_2018.png")

   dat.Delete()
   dat2.Delete()
   stk.Delete()
   mc.Delete()
   prf.Close()
   prf.Delete()
   return ()

def ratioplot():

   for var in range( _nVars):
        var_dictionary = Var_Dict[var]
        test(var_dictionary['variable'],var_dictionary['nBins'],var_dictionary['xLow'],var_dictionary['xHi'],var_dictionary['title'])
if __name__ == "__main__":
   ratioplot()
