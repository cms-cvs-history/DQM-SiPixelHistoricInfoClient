#!/bin/bash

eval `scramv1 ru -sh`

filetype="_"$1

template="readSiPixelPerformanceSummary_all_template_cfg.py"
perfsumTag="SiPixelPerformanceSummary"$filetype

  if [ $filetype = "_DQM" -o $filetype = "_RAW" -o $filetype = "_RECO" ]; then
  sed -e "s#perfsumtag#$perfsumTag#" $template > readSiPixelPerformanceSummary_data_cfg.py
  cmsRun readSiPixelPerformanceSummary_data_cfg.py

elif [ $filetype = "_MC" ]; then 
  sed -e "s#oracle://cms_orcoff_prep/CMS_COND_PIXEL_COMM_21X#sqlite_file:SiPixelHistory_MC.db#" \
      -e "s#perfsumtag#$perfsumTag#" $template > readSiPixelPerformanceSummary_mc_cfg.py
  cmsRun readSiPixelPerformanceSummary_mc_cfg.py

else
  echo 
  echo "  USAGE:"
  echo "./readSiPixelPerformanceSummary.sh [filetype]"
  echo "  where "
  echo " [filetype] can be either DQM, RAW, RECO or MC."
  echo
fi

