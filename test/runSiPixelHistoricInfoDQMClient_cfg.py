import FWCore.ParameterSet.Config as cms 

process = cms.Process("SiPixelHistoricInfoDQMClient") 

process.load("FWCore.MessageService.MessageLogger_cfi")

process.source = cms.Source("EmptySource")
process.maxEvents = cms.untracked.PSet( 
  input = cms.untracked.int32(0) 
)
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.CondDBSetup.DBParameters.authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
  process.CondDBSetup, 
  connect = cms.string('oracle://cms_orcoff_prep/CMS_COND_PIXEL'), 
  # connect = cms.string('sqlite_file:test.db'),
  timetype = cms.untracked.string('runnumber'),
  toPut = cms.VPSet(
    cms.PSet(
      record = cms.string('SiPixelPerformanceSummaryRcd'),
      tag = cms.string('SiPixelPerformanceSummary_21X_DQM')
    )
  )
)
process.sipixelhistoricinfoDQMclient = cms.EDFilter("SiPixelHistoricInfoDQMClient",
  inputFiles = cms.untracked.vstring(
    '/tmp/schuang/DQM_Scurve_Run54268.root'
  ),
  outputDir = cms.untracked.string('/tmp/schuang'),
  printDebug = cms.untracked.bool(False),
  writeHisto = cms.untracked.bool(False)
)
process.pathAll = cms.Path(process.sipixelhistoricinfoDQMclient) 



process.dqmEnv = cms.EDFilter("DQMEventInfo",
  subSystemFolder = cms.untracked.string('Pixel'),
  eventInfoFolder = cms.untracked.string('EventInfo')
)
process.dqmSaver = cms.EDFilter("DQMFileSaver",
  prescaleEvt = cms.untracked.int32(-1),
  prescaleLS = cms.untracked.int32(1),
  saveAtJobEnd = cms.untracked.bool(False),
  fileName = cms.untracked.string('Pixel'),
  environment = cms.untracked.string('Online'),
  saveAtRunEnd = cms.untracked.bool(True),
  prescaleTime = cms.untracked.int32(-1),
  dirName = cms.untracked.string('/tmp/schuang')
)
process.DQMStore = cms.Service("DQMStore",
  referenceFileName = cms.untracked.string(''),
  verbose = cms.untracked.int32(0)
)
process.LockService = cms.Service("LockService", 
  labels = cms.untracked.vstring('source') 
)
process.ModuleWebRegistry = cms.Service("ModuleWebRegistry")

process.AdaptorConfig = cms.Service("AdaptorConfig") 


process.dqmModules = cms.Sequence(process.dqmEnv*process.dqmSaver)

