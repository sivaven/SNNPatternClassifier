#!/bin/bash
export CLASSPATH="src:bin:lib/*"
module load python-2.7
module load OpenBLAS
javac src/briansim/*.java src/classifier/*.java src/dataset/*.java src/dataset/classes/*.java src/encode/*.java src/outputwriter/*.java src/snn/*.java src/snn/constants/*.java src/ecj/*.java src/utils/*.java
nohup java training.ECJStarter &
