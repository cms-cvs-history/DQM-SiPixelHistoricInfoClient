#!/bin/bash

eval `scramv1 ru -sh`

filelist=$1 
floss="_"$1

if [ $floss = "_" ]; then
  echo 
  echo "  USAGE:"
  echo "./runSiPixelHistoricInfoClient.sh [filelist]"
  echo "  where "
  echo "  the files must be DQM (PhysicsData on AFS)"
  echo 
else
  for file in $(cat $filelist); do 
    midRun=`echo $file | awk '{print substr($1,match($1,"R0000")+5,5)}'`    
    firstRun=$[midRun-1]
    lastRun=$[midRun+1]
    
    inputFile="'"$file"'"

    template=runSiPixelHistoricInfoDQMClient_template_perFile_cfg.py
    sed -e "s#DQMoutputFiles#$inputFile#" \
        -e "s#FFFFF#$firstRun#" \
	-e "s#LLLLL#$lastRun#" $template > runSiPixelHistoricInfoDQMClient_dqm_cfg.py
    cmsRun runSiPixelHistoricInfoDQMClient_dqm_cfg.py
  done 
fi
