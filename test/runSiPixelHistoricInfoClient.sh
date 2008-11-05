#!/bin/bash

eval `scramv1 ru -sh`

filelist=$1 
filetype="_"$2 
frontierTag=$3

if [ $filetype = "_DQM" -o $filetype = "_MC" -o $filetype = "_RAW" -o $filetype = "_RECO" ]; then
      nFiles=0 
  inputFiles=""
  for file in $(cat $filelist); do 
        nFiles=$[nFiles+1]
    inputFiles=$inputFiles"'"$file"', "
  done 

  if [ $nFiles -gt 0 ]; then
      if [ $filetype = "_DQM" ]; then
      template=runSiPixelHistoricInfoDQMClient_harvest_template_cfg.py
      sed -e "s#DQMoutputFiles#$inputFiles#" $template > runSiPixelHistoricInfoDQMClient_dqm_cfg.py
      cmsRun runSiPixelHistoricInfoDQMClient_dqm_cfg.py

    elif [ $filetype = "_RAW" ]; then
      template=runSiPixelHistoricInfoEDAClient_RAW_template_cfg.py
      sed -e "s#rawFiles#$inputFiles#" -e "s#frontag#$frontierTag#" $template > runSiPixelHistoricInfoEDAClient_raw_cfg.py
      cmsRun runSiPixelHistoricInfoEDAClient_raw_cfg.py

    elif [ $filetype = "_RECO" ]; then
      template=runSiPixelHistoricInfoEDAClient_RECO_template_cfg.py
      sed -e "s#recoFiles#$inputFiles#" -e "s#frontag#$frontierTag#" $template > runSiPixelHistoricInfoEDAClient_reco_cfg.py
      cmsRun runSiPixelHistoricInfoEDAClient_reco_cfg.py

    elif [ $filetype = "_MC" ]; then
      template=runSiPixelHistoricInfoEDAClient_MC_template_cfg.py
      sed -e "s#relvalFiles#$inputFiles#" $template > runSiPixelHistoricInfoEDAClient_mc_cfg.py
      cmsRun runSiPixelHistoricInfoEDAClient_mc_cfg.py

    fi
  fi

else
  echo 
  echo "  USAGE:"
  echo "./runSiPixelHistoricInfoClient.sh [filelist] [filetype] ([globaltag for frontier condition])"
  echo "  where "
  echo "  [filetype] can be either DQM, RAW, RECO or MC; DQM includes harvest and offline DQM output."
  echo "  DQM files must be processed from PhysicsData runs and must be located on accessible afs area."
  echo "  RAW/RECO/MC files must be in CMSSW RAW/RECO data format."
  echo "  FrontierCondition's globaltag must be supplied for RAW/RECO filetypes."
  echo 
fi
