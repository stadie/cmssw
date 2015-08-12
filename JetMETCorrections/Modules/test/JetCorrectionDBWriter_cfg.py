import FWCore.ParameterSet.Config as cms

filename = "Summer15_50nsV3_DATA_HS.db"
era = "Summer15_50nsV3_DATA"
jetalgos = ['AK4PFPuppi','AK4PF','AK4PFchs','AK8PFPuppi','AK8PF','AK8PFchs']

process = cms.Process('jecdb')
process.load('CondCore.DBCommon.CondDBCommon_cfi')
process.CondDBCommon.connect = 'sqlite_file:'+filename
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1))
process.source = cms.Source('EmptySource')
process.PoolDBOutputService = cms.Service('PoolDBOutputService',
   process.CondDBCommon,
   toPut = cms.VPSet()
)

process.writeSequence = cms.Sequence()

for algo in jetalgos:
    process.PoolDBOutputService.toPut.append(cms.PSet(
         record = cms.string(algo),
         tag    = cms.string('JetCorrectorParametersCollection_'+era+'_'+algo),
         label  = cms.string(algo)
    ))
    writer  = cms.EDAnalyzer('JetCorrectorDBWriter',
                             era = cms.untracked.string(era),
                             algo   = cms.untracked.string(algo))
    setattr(process,'dbWriter'+algo,writer)
    process.writeSequence += writer


process.p = cms.Path(process.writeSequence)
