# CMSDAS-MonoZ-Tutorial

## Quick start with combine: 

Setting up CMSSW: 
```bash
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_10_2_13 
cd CMSSW_10_2_13/src 
cmsenv
```

fetching combine: 

```bash
git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit 
cd $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit 
git fetch origin 
git checkout v8.0.1

# and combinetool
cd $CMSSW_BASE/src 
bash <(curl -s https://raw.githubusercontent.com/cms-analysis/CombineHarvester/master/CombineTools/scripts/sparse-checkout-https.sh) 

# compile everything
cd $CMSSW_BASE/src/ 
scramv1 b clean; scramv1 b -j 10
```

Fetching a Mono-Z datacard:

```bash
cp -r /eos/user/c/cmsdas/long-exercises/MonoZ/datacards/cards-DMSimp_MonoZLL_NLO_Axial_1000_MXd-1 .

# remove the old combine output
rm cards-DMSimp_MonoZLL_NLO_Axial_1000_MXd-1/combined.root
```

Transform the datacard into a worspace format (this step can be skipped if you run combine on `combined.dat` directly, see below)
```bash
text2workspace.py cards-DMSimp_MonoZLL_NLO_Axial_1000_MXd-1/combined.dat -o cards-DMSimp_MonoZLL_NLO_Axial_1000_MXd-1/combined.root
```

run combine

```bash
combine  -M AsymptoticLimits --datacard cards-DMSimp_MonoZLL_NLO_Axial_1000_MXd-1/combined.root
```

Making impacts plot

```bash
export PARAM = " --rMin=-10 --cminFallbackAlgo Minuit2,Migrad,0:0.05  --X-rtd MINIMIZER_analytic --X-rtd FAST_VERTICAL_MORPH --rMax=10"

combineTool.py -M Impacts -d cards-DMSimp_MonoZLL_NLO_Axial_1000_MXd-1/combined.root -m 125 -n TEST --robustFit 1 --X-rtd FITTER_DYN_STEP --rMin=-1 --rMax=4 --doInitialFit --allPars $PARAM
combineTool.py -M Impacts -d cards-DMSimp_MonoZLL_NLO_Axial_1000_MXd-1/combined.root -m 125 -n TEST --robustFit 1 --X-rtd FITTER_DYN_STEP --rMin=-1 --rMax=4 --doFits --allPars $PARAM
combineTool.py -M Impacts -d cards-DMSimp_MonoZLL_NLO_Axial_1000_MXd-1/combined.root -m 125 -n TEST -o impactsTEST.json --allPars $PARAM

# plot everything now:
plotImpacts.py -i impactsTEST.json -o impactsTEST
```
