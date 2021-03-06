# 13TeV workflow added my Ian M. Nugent (nugent@physik.rwth-aachen.de)
#
# import the definition of the steps and input files:
from Configuration.PyReleaseValidation.relval_steps import *

# here only define the workflows as a combination of the steps defined above:
workflows = Matrix()

# each workflow defines a name and a list of steps to be done.
# if no explicit name/label given for the workflow (first arg),
# the name of step1 will be used

# 'generator' the base set of relval for generators
# 'extendedgen' extends the base set to a more thorough assesment of GEN
# the two sets are exclusive

# LO Generators
workflows[501]=['',['MinBias_TuneZ2star_13TeV_pythia6','HARVESTGEN']]
workflows[502]=['',['QCD_Pt-30_TuneZ2star_13TeV_pythia6','HARVESTGEN']]
workflows[503]=['',['MinBias_13TeV_pythia8','HARVESTGEN']]
workflows[504]=['',['QCD_Pt-30_13TeV_pythia8','HARVESTGEN']]
workflows[505]=['',['DYToLL_M-50_13TeV_pythia8','HARVESTGEN']]
workflows[506]=['',['WToLNu_13TeV_pythia8','HARVESTGEN']]
workflows[511]=['',['QCD_Pt-30_8TeV_herwigpp','HARVESTGEN']]

# Matrix Element Generations (LHE Generation)

# Hadronization (Hadronization of LHE)
workflows[512]=['',['ZJetsLL_13TeV_madgraph-pythia8','HARVESTGEN']]
workflows[513]=['',['WJetsLNu_13TeV_madgraph-pythia8','HARVESTGEN']]

# External Decays
workflows[521]=['',['TT_13TeV_pythia8-evtgen','HARVESTGEN']]
workflows[522]=['',['DYToLL_M-50_13TeV_pythia8-tauola','HARVESTGEN']]
workflows[523]=['',['WToLNu_13TeV_pythia8-tauola','HARVESTGEN']]

# Heavy Ion
workflows[531]=['',['ReggeGribovPartonMC_EposLHC_5TeV_pPb','HARVESTGEN']]

# Miscellaneous
