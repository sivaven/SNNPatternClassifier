#!/bin/bash
export set JAVA_OPTS="-XX:+AggressiveHeap"
export CLASSPATH="src:bin:lib/*"
module load python-2.7
module load OpenBLAS
javac src/snn/*.java src/snn/constants/*.java src/briansim/*.java src/classifier/*.java src/dataset/*.java src/dataset/classes/*.java src/code/*.java src/outputwriter/*.java src/ecj/*.java src/utils/*.java
nohup java ecj.ECJStarter2 --slave -file input/ecj_slave.params &
