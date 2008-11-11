import FWCore.ParameterSet.Config as cms 

process = cms.Process("SiPixelHistoricInfoDQMClient") 

process.load("FWCore.MessageService.MessageLogger_cfi")

process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    interval = cms.uint64(1),
  firstValue = cms.uint64(FFFFF),
   lastValue = cms.uint64(LLLLL)
)
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.CondDBSetup.DBParameters.authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
  process.CondDBSetup, 
  connect = cms.string('oracle://cms_orcoff_prep/CMS_COND_PIXEL_COMM_21X'), 
  timetype = cms.untracked.string('runnumber'),
  toPut = cms.VPSet(
    cms.PSet(
      record = cms.string('SiPixelPerformanceSummaryRcd'),
      tag = cms.string('SiPixelPerformanceSummary_DQMtier0')
    )
  )
)
process.sipixelhistoricinfoDQMclient = cms.EDFilter("SiPixelHistoricInfoDQMClient",
  inputFiles = cms.untracked.vstring(
    DQMoutputFiles
  ),
  outputDir = cms.untracked.string('.'),
  useSummary = cms.untracked.bool(True),
  printDebug = cms.untracked.bool(False),
  writeHisto = cms.untracked.bool(False)
)
process.DQMStore = cms.Service("DQMStore",
  referenceFileName = cms.untracked.string(''),
  verbose = cms.untracked.int32(0)
)
process.pathAll = cms.Path(process.sipixelhistoricinfoDQMclient)
