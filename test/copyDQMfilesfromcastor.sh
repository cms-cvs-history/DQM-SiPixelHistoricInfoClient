#!/bin/bash

dqmDir='/castor/cern.ch/cms/store/TAC/PIXEL/P5/DQMoutput'
 myDir='DQMfiles'

if [ ! -d $myDir ]; then mkdir $myDir; fi
echo 'Pixel DQM PhysicsData runs will be copied to '$myDir

for file in $(nsls $dqmDir | grep DQM_PhysicsData_Run | grep root); do
  filenameLength=`echo $file | awk '{print(length($1))}'`
  fileLength=`nsls -l $dqmDir/$file | awk '{print $5}'`
  runNumber=`echo $file | awk '{print(substr($1,20,5))}'`
  if [ $filenameLength -eq 29 && $runNumber -gt 58738 ] 
  then 
    if [ $fileLength -ne 0 ] 
    then 
      echo $file' to be copied now'
      rfcp $dqmDir/$file $myDir
    else 
      echo 'Alternative to 0-length file '$file
      nsls $dqmDir | grep DQM_PhysicsData | grep $runNumber
    fi
  fi 
done 

for runNumber in 58555 58553 58627 58600; do
  echo DQM_PhysicsData_Run$runNumber.root' to be copied now'
  rfcp $dqmDir/DQM_PhysicsData_Run$runNumber.root $myDir         
done

