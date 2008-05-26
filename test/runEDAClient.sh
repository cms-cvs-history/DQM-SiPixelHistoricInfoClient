#!/bin/bash

USAGE="`basename $0` -run / -read"
case $# in
1)
  case "$1" in
        -run)  MODE="run"; ;;
        -read) MODE="read"; ;;
        *)     echo $USAGE; exit 1; ;;
  esac
  shift ;;
*)
  echo $USAGE; exit 1; ;;
esac

eval `scramv1 runtime -sh`
SealPluginRefresh
export CORAL_AUTH_USER=""
export CORAL_AUTH_PASSWORD=""

if [ "$MODE" == "run" ]; then
  rm -f /tmp/schuang/EDAClient.log
  cmsRun runSiPixelHistoricInfoEDAClient.cfg >& /tmp/schuang/runSiPixelHistoricInfoEDAClient.log &

elif [ "$MODE" == "read" ]; then
  cmsRun readSiPixelPerformanceSummary.cfg >& /tmp/schuang/readSiPixelPerformanceSummary.log &
fi

