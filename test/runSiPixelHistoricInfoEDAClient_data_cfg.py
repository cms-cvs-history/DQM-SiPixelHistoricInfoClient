import FWCore.ParameterSet.Config as cms 

process = cms.Process("SiPixelMonitorTrackResiduals") 

process.load("FWCore.MessageService.MessageLogger_cfi")

process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.GlobalRuns.ForceZeroTeslaField_cff")

process.load("Configuration.StandardSequences.Geometry_cff")

process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'IDEAL_V5::All'

# process.load("Configuration.StandardSequences.RawToDigi_cff")

process.load("EventFilter.SiPixelRawToDigi.SiPixelRawToDigi_cfi")
process.siPixelDigis.InputLabel = 'source'
process.siPixelDigis.IncludeErrors = True

process.load("EventFilter.SiStripRawToDigi.SiStripRawToDigis_standard_cff")
process.siStripDigis.ProductLabel = 'source'

# process.load("Configuration.StandardSequences.Reconstruction_cff")

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
process.SiPixelClusterSource.outputFile = '/tmp/schuang/DQMcluster_test.root'
process.load("DQM.SiPixelMonitorRecHit.SiPixelMonitorRecHit_cfi")
process.SiPixelRecHitSource.outputFile = '/tmp/schuang/DQMrecHit_test.root'
process.load("DQM.SiPixelMonitorTrack.SiPixelMonitorTrack_cfi")
process.SiPixelTrackResidualSource.debug = True
process.SiPixelTrackResidualSource.outputFile = '/tmp/schuang/DQMtrackResidual_test.root'

# process.load("IORawData.SiPixelInputSources.PixelSLinkDataInputSource_cfi")
# process.PixelSLinkDataInputSource.fileNames = ['file:/afs/cern.ch/cms/Tracker/Pixel/forward/ryd/PixelAlive_070106d.dmp']

process.source = cms.Source("PoolSource", 
  fileNames = cms.untracked.vstring(
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/530/F4A49317-AA37-DD11-B2B0-000423D6BA18.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/535/60E5342E-AA37-DD11-AF7E-000423D9853C.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/546/F243D1FA-AA37-DD11-9708-000423D6B358.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/549/409C7C75-B137-DD11-ABA6-000423D9880C.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/554/BCF84404-EB37-DD11-9CE3-000423D6BA18.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/556/BAA0940F-E037-DD11-A9F2-000423D986A8.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/562/D4A49FF1-DE37-DD11-AF29-001617E30D40.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/598/329D53EF-EA37-DD11-BC5C-000423D992A4.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/629/9CE2CDB9-F137-DD11-9840-000423D992DC.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/633/DE88C5E0-F937-DD11-81C6-000423D6C8E6.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/706/7EC89544-8638-DD11-A3CB-000423D6A6F4.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/718/DE1EDA84-7838-DD11-AC1C-001617DF785A.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/788/96875244-9838-DD11-97D4-001617E30D52.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/794/9EE1EFFA-9B38-DD11-BDBE-000423D6B42C.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/798/8EE9B8B0-9D38-DD11-A5FD-000423D98834.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/808/C0AB71B8-A238-DD11-97A7-001617E30F56.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/838/3E012B46-C438-DD11-B0FC-000423D6CA02.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/841/22B0B3D5-F538-DD11-9051-000423D9939C.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/843/F88FAD3A-D738-DD11-8E9D-000423D992A4.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/853/90A62577-F138-DD11-9370-000423D985E4.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/855/CC863342-F238-DD11-BACD-000423D9863C.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/863/0862896A-2F39-DD11-858A-000423D6CA6E.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/865/0EE79B05-0639-DD11-8E72-000423D6B42C.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/870/EEEAE370-6439-DD11-92A3-001D09F24FBA.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/873/EC001CC7-8039-DD11-A7BD-000423D98804.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/879/EEF85F24-8139-DD11-A863-000423D6B48C.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/884/923F5242-8139-DD11-8716-001617DBCF1E.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/890/0A41E634-8139-DD11-9C36-000423D6CAF2.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/911/D2EF75FF-3739-DD11-8270-001617E30D12.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/913/F4A33147-8139-DD11-A358-0019DB2F3F9B.root',
    '/store/data/CRUZET2/Cosmics/RAW/v1/000/046/931/B0FD53A2-4D39-DD11-AA21-000423D6CAF2.root'
  ),
  debugFlag = cms.untracked.bool(True),
  debugVebosity = cms.untracked.uint32(10)
) 
process.maxEvents = cms.untracked.PSet(
  input = cms.untracked.int32(-1)
)
process.load("CondCore.DBCommon.CondDBSetup_cfi")
process.CondDBSetup.DBParameters.authenticationPath = cms.untracked.string('/afs/cern.ch/cms/DB/conddb')
process.PoolDBOutputService = cms.Service("PoolDBOutputService",
  process.CondDBSetup, 
  connect = cms.string('oracle://cms_orcoff_int2r/CMS_COND_PIXEL'), # sqlite_file:test.db
  timetype = cms.untracked.string('runnumber'),
  toPut = cms.VPSet(
    cms.PSet(
      record = cms.string('SiPixelPerformanceSummaryRcd'),
      tag = cms.string('SiPixelPerformanceSummary_21X_CRUZET')
    )
  )
)
process.sipixelhistoricinfoEDAclient = cms.EDFilter("SiPixelHistoricInfoEDAClient",
  printDebug = cms.untracked.bool(True),
  writeHisto = cms.untracked.bool(True),
  outputDir = cms.untracked.string('/tmp/schuang')
)
process.preScaler = cms.EDFilter("Prescaler",
  prescaleFactor = cms.int32(1)
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

process.siPixelLocalReco = cms.Sequence(process.siPixelDigis*process.siPixelClusters*process.siPixelRecHits) 
process.siStripLocalReco = cms.Sequence(process.siStripDigis*process.siStripZeroSuppression*process.siStripClusters*process.siStripMatchedRecHits)
process.trackerLocalReco = cms.Sequence(process.siPixelLocalReco*process.siStripLocalReco)
process.trackReconstruction = cms.Sequence(process.trackerLocalReco*process.offlineBeamSpot*process.recopixelvertexing*process.ckftracks) #*process.rstracks 

process.monitorTrack = cms.Sequence(process.SiPixelTrackResidualSource)
process.monitors = cms.Sequence(process.SiPixelRawDataErrorSource*process.SiPixelDigiSource*process.SiPixelClusterSource*process.SiPixelRecHitSource*process.SiPixelTrackResidualSource)

process.dqmModules = cms.Sequence(process.dqmEnv*process.dqmSaver)

process.pathTrack = cms.Path(process.trackReconstruction*process.monitors*process.sipixelhistoricinfoEDAclient) #*process.dqmModules
# process.pathStandard = cms.Path(process.RawToDigi*process.reconstruction*process.monitors*process.sipixelhistoricinfoEDAclient*process.dqmModules)
