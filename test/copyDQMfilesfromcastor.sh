#!/bin/bash

dqmDir="/castor/cern.ch/cms/store/TAC/PIXEL/P5/DQMoutput"
 myDir=$1
amyDir=$1"a"

if [ $amyDir == "a" ]; then 
  echo 
  echo "  USAGE: ./copyDQMfilesfromcastor.sh [destination directory in full path]"
  echo 
  exit 
else 
  if [ ! -d $myDir ]; then 
    mkdir $myDir 
  fi
  echo 'Pixel DQM PhysicsData runs will be copied to '$myDir
fi 

for file in $(nsls $dqmDir | grep DQM_PhysicsData_Run | grep root); do
  filenameLength=`echo $file | awk '{print(length($1))}'`
  fileLength=`nsls -l $dqmDir/$file | awk '{print $5}'`
  runNumber=`echo $file | awk '{print(substr($1,20,5))}'`
  if [ $filenameLength -eq 29 -a $runNumber -ne 54842 ] 
  then 
    if [ $fileLength -ne 0 ] 
    then 
      echo $file" to be staged now"
      stager_get -M $dqmDir/$file 
      stager_qry -M $dqmDir/$file
    else 
      echo "Alternative to 0-length file "$file
      nsls $dqmDir | grep DQM_PhysicsData | grep $runNumber
    fi
  fi 
done 

for file in $(nsls $dqmDir | grep DQM_PhysicsData_Run | grep root); do
  filenameLength=`echo $file | awk '{print(length($1))}'`
  fileLength=`nsls -l $dqmDir/$file | awk '{print $5}'`
  runNumber=`echo $file | awk '{print(substr($1,20,5))}'`
  if [ $filenameLength -eq 29 -a $runNumber -ne 54842 ] 
  then 
    if [ $fileLength -ne 0 ] 
    then 
      echo $file" to be copied now"
      rfcp $dqmDir/$file $myDir
    else 
      echo "Alternative to 0-length file "$file
      nsls $dqmDir | grep DQM_PhysicsData | grep $runNumber
    fi
  fi 
done 

exit

for runNumber in 54842; do
  echo DQM_PhysicsData_Run$runNumber.root" to be copied now"
  rfcp $dqmDir/DQM_PhysicsData_Run$runNumber.root $myDir         
done

