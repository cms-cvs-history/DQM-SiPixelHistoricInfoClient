import FWCore.ParameterSet.Config as cms

process = cms.Process("readSiPixelPerformanceSummary")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.source = cms.Source("EmptyIOVSource",
  timetype = cms.string('runnumber'),
  interval = cms.uint32(1),
  firstRun = cms.untracked.uint32(54751),
   lastRun = cms.untracked.uint32(64800)
)
# process.load("CondCore.DBCommon.CondDBCommon_cfi")
# process.CondDBCommon.connect = 'oracle://cms_orcoff_prep/CMS_COND_PIXEL' !not int2r!
# process.CondDBCommon.timetype = 'runnumber'
# process.CondDBCommon.DBParameters.authenticationPath = '/afs/cern.ch/cms/DB/conddb'
# process.CondDBCommon.DBParameters.messageLevel = 3

process.PoolDBESSource = cms.ESSource("PoolDBESSource",
  # process.CondDBCommon,
  # connect = cms.string('oracle://cms_orcoff_int2r/CMS_COND_PIXEL_COMM_21X'),
  connect = cms.string('sqlite_file:testPixelHistory.db'), 
  timetype = cms.string('runnumber'),
  DBParameters = cms.PSet(
    authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb'),
    messageLevel = cms.untracked.int32(0)
  ),
  toGet = cms.VPSet(
    cms.PSet(
      record = cms.string('SiPixelPerformanceSummaryRcd'),
      tag = cms.string('SiPixelPerformanceSummary_test')
    )
  )
)
process.siPixelHistoricInfoReader = cms.EDFilter("SiPixelHistoricInfoReader",
  variables = cms.untracked.vstring(
    "errorType",
    "ndigis", "adc",
    "nclusters", "charge", "sizeX", "sizeY",
    "nRecHits",
    "residualX", "residualY"
  ), 
  normEvents = cms.untracked.bool(False),
  printDebug = cms.untracked.bool(False),
  outputFile = cms.untracked.string('testPixelHistory.root')
)
process.path = cms.Path(process.siPixelHistoricInfoReader) 
