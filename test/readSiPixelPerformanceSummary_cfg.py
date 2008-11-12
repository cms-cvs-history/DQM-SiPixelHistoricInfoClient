import FWCore.ParameterSet.Config as cms

process = cms.Process("readSiPixelPerformanceSummary")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.source = cms.Source("EmptyIOVSource",
    timetype = cms.string('runnumber'),
    interval = cms.uint64(1),
  firstValue = cms.uint64(68496),
   lastValue = cms.uint64(70200)
)
# process.load("CondCore.DBCommon.CondDBCommon_cfi")
# process.CondDBCommon.connect = 'sqlite_file:SiPixelHistory_MC.db'
# process.CondDBCommon.timetype = 'runnumber'
# process.CondDBCommon.DBParameters.authenticationPath = '/afs/cern.ch/cms/DB/conddb'
# process.CondDBCommon.DBParameters.messageLevel = 3

process.PoolDBESSource = cms.ESSource("PoolDBESSource",
  # process.CondDBCommon,
  connect = cms.string('oracle://cms_orcoff_prep/CMS_COND_PIXEL_COMM_21X'),
  timetype = cms.string('runnumber'),
  DBParameters = cms.PSet(
    authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb'),
    messageLevel = cms.untracked.int32(0)
  ),
  toGet = cms.VPSet(
    cms.PSet(
      record = cms.string('SiPixelPerformanceSummaryRcd'),
      tag = cms.string('SiPixelPerformanceSummary_DQMtier0')
    )
  )
)
process.siPixelHistoricInfoReader = cms.EDFilter("SiPixelHistoricInfoReader",
  variables = cms.untracked.vstring(
    "errorType",
    "ndigis", "adc",
    "nclusters", "charge", "size", "sizeX", "sizeY",
    # "nRecHits",
    # "residualX", "residualY", 
    # "nPixHitsTrk", 
    # "nNoisPixels", "nDeadPixels"
  ), 
  normEvents = cms.untracked.bool(False),
  printDebug = cms.untracked.bool(False),
   makePlots = cms.untracked.bool(True), 
   typePlots = cms.untracked.string('gif'),
  outputDir  = cms.untracked.string('.'),
  outputFile = cms.untracked.string('SiPixelHistory.root')
)
process.path = cms.Path(process.siPixelHistoricInfoReader) 
