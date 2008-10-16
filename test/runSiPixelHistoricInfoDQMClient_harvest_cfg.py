import FWCore.ParameterSet.Config as cms 

process = cms.Process("SiPixelHistoricInfoDQMClient") 

process.load("FWCore.MessageService.MessageLogger_cfi")

process.source = cms.Source("EmptyIOVSource",
  timetype = cms.string('runnumber'),
  interval = cms.uint32(1),
  firstRun = cms.untracked.uint32(54751),
   lastRun = cms.untracked.uint32(64800)
)
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.CondDBSetup.DBParameters.authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
  process.CondDBSetup, 
  # connect = cms.string('oracle://cms_orcoff_prep/CMS_COND_PIXEL'), 
  connect = cms.string('sqlite_file:testPixelHistory.db'),
  timetype = cms.untracked.string('runnumber'),
  toPut = cms.VPSet(
    cms.PSet(
      record = cms.string('SiPixelPerformanceSummaryRcd'),
      tag = cms.string('SiPixelPerformanceSummary_test')
    )
  )
)
process.sipixelhistoricinfoDQMclient = cms.EDFilter("SiPixelHistoricInfoDQMClient",
  inputFiles = cms.untracked.vstring(
    'DQMoutput/DQM_PhysicsData_Run62938.root',
    'DQMoutput/DQM_PhysicsData_Run62940.root',
  ),
  outputDir = cms.untracked.string('.'),
  useSummary = cms.untracked.bool(True),
  printDebug = cms.untracked.bool(False),
  writeHisto = cms.untracked.bool(False)
)
process.pathAll = cms.Path(process.sipixelhistoricinfoDQMclient)
