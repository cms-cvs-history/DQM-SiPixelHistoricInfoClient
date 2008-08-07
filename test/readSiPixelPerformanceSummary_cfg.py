import FWCore.ParameterSet.Config as cms

process = cms.Process("readSiPixelPerformanceSummary")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.source = cms.Source("EmptyIOVSource",
  timetype = cms.string('runnumber'),
  interval = cms.uint32(1),
  firstRun = cms.untracked.uint32(1),
  lastRun = cms.untracked.uint32(99999)
)
process.PoolDBESSource = cms.ESSource("PoolDBESSource",
  connect = cms.string('oracle://cms_orcoff_int2r/CMS_COND_PIXEL'), # sqlite_file:test.db
  timetype = cms.string('runnumber'),
  DBParameters = cms.PSet(
    authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb'),
    messageLevel = cms.untracked.int32(3)
  ),
  toGet = cms.VPSet(
    cms.PSet(
      record = cms.string('SiPixelPerformanceSummaryRcd'),
      tag = cms.string('SiPixelPerformanceSummary_21X')
    )
  )
)
process.siPixelHistoricInfoReader = cms.EDFilter("SiPixelHistoricInfoReader",
  printDebug = cms.untracked.bool(False),
  outputDir = cms.untracked.string('/tmp/schuang')
)
process.path = cms.Path(process.siPixelHistoricInfoReader)

process.printAscii = cms.OutputModule("AsciiOutputModule")

process.endPath = cms.EndPath(process.printAscii)


