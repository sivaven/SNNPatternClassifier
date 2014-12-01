#!/bin/bash
#$ -N SNNclass
#$ -pe shared 16
#$ -l mf=1G
#$ -cwd
export set JAVA_OPTS="-XX:+AggressiveHeap"
export CLASSPATH="src:bin:lib/*"
javac src/snn/*.java src/snn/constants/*.java src/briansim/*.java src/classifier/*.java src/dataset/*.java src/dataset/classes/*.java src/code/*.java src/outputwriter/*.java src/ecj/*.java src/utils/*.java
java ecj.ECJStarter
