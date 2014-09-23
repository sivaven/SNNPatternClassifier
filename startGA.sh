#!/bin/bash
export CLASSPATH="src:bin:lib/*"
javac src/classifier/*.java src/dataset/*.java src/dataset/classes/*.java src/encode/*.java src/outputwriter/*.java src/snn/*.java src/snn/constants/*.java src/training/*.java src/utils/*.java
nohup java training.ECJStarter &
