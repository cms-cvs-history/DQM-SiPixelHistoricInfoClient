import FWCore.ParameterSet.Config as cms 

process = cms.Process("SiPixelHistoricInfoEDAClient_RECO") 

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.GlobalRuns.ForceZeroTeslaField_cff")

process.load("Configuration.StandardSequences.Geometry_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'CRUZET4_V5P::All'

# process.load("Configuration.StandardSequences.RawToDigi_cff")

process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi")
process.siPixelDigis.InputLabel = 'source'
process.siPixelDigis.IncludeErrors = True

process.load("EventFilter.SiStripRawToDigi.SiStripRawToDigis_standard_cff")
process.siStripDigis.ProductLabel = 'source'

process.load("Configuration.StandardSequences.Reconstruction_cff")

process.load("RecoLocalTracker.SiPixelClusterizer.SiPixelClusterizer_cfi")
process.load("RecoLocalTracker.SiPixelRecHits.SiPixelRecHits_cfi")
process.load("RecoLocalTracker.SiPixelRecHits.PixelCPEESProducers_cff")

process.load("RecoLocalTracker.SiStripClusterizer.SiStripClusterizer_cfi")
process.load("RecoLocalTracker.SiStripRecHitConverter.SiStripRecHitConverter_cfi")
process.load("RecoLocalTracker.SiStripRecHitConverter.SiStripRecHitMatcher_cfi")
process.load("RecoLocalTracker.SiStripRecHitConverter.StripCPEfromTrackAngle_cfi")
process.load("RecoLocalTracker.SiStripZeroSuppression.SiStripZeroSuppression_cfi")

process.load("RecoVertex.BeamSpotProducer.BeamSpot_cff")
process.load("RecoPixelVertexing.Configuration.RecoPixelVertexing_cff")
process.load("RecoTracker.Configuration.RecoTracker_cff")
  
process.load("DQM.SiPixelMonitorRawData.SiPixelMonitorRawData_cfi")
process.load("DQM.SiPixelMonitorDigi.SiPixelMonitorDigi_cfi")
process.load("DQM.SiPixelMonitorCluster.SiPixelMonitorCluster_cfi")
process.load("DQM.SiPixelMonitorRecHit.SiPixelMonitorRecHit_cfi")
process.load("DQM.SiPixelMonitorTrack.SiPixelMonitorTrack_cfi")

process.source = cms.Source("PoolSource", 
  fileNames = cms.untracked.vstring(
    '/store/data/Commissioning08/Cosmics/RECO/CRUZET4_v1/000/057/313/4214986A-196D-DD11-BED7-000423D992DC.root'
  ),
  debugFlag = cms.untracked.bool(True),
  debugVebosity = cms.untracked.uint32(10)
) 
process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(10)
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
      tag = cms.string('SiPixelPerformanceSummary_21X_DQMdummy')
    )
  )
)
process.sipixelhistoricinfoEDAclient = cms.EDFilter("SiPixelHistoricInfoEDAClient",
  printDebug = cms.untracked.bool(False),
  writeHisto = cms.untracked.bool(False),
  outputDir = cms.untracked.string('/tmp/schuang')
)
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

process.siPixelLocalReco = cms.Sequence(process.siPixelClusters*process.siPixelRecHits) 
process.siStripLocalReco = cms.Sequence(process.siStripZeroSuppression*process.siStripClusters*process.siStripMatchedRecHits)
process.trackerLocalReco = cms.Sequence(process.siPixelLocalReco*process.siStripLocalReco)
process.trackReconstruction = cms.Sequence(process.trackerLocalReco*process.offlineBeamSpot*process.recopixelvertexing*process.ckftracks) #*process.rstracks 

process.monitorTrack = cms.Sequence(process.SiPixelTrackResidualSource)
process.monitors = cms.Sequence(process.SiPixelDigiSource*process.SiPixelClusterSource*process.SiPixelRecHitSource)

process.dqmModules = cms.Sequence(process.dqmEnv*process.dqmSaver)

# process.traditional = cms.Path(process.RawToDigi*process.reconstruction*process.monitors*process.sipixelhistoricinfoEDAclient*process.dqmModules)
# process.pathDigi = cms.Path(process.SiPixelDigiSource*process.sipixelhistoricinfoEDAclient) #*process.dqmModules

process.pathAll = cms.Path(process.trackReconstruction*process.monitors*process.sipixelhistoricinfoEDAclient) #*process.dqmModules