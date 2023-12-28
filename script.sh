#! /bin/bash

# website we want to use for crawling
website="about.cilabs.com"
# create the directory where I want to put the file after the crawling
mkdir -p $website
cd $website
mkdir -p "crawlingOutput"
# start mitmdump
gnome-terminal -- bash -c "cd ..; cd crawljax-cli-5.2.3; java -jar crawljax-cli-5.2.3.jar https://$website/ -o ../$website/crawlingOutput -b firefox -proxy localhost:8080; exit" &&pid=$!
mitmproxy -w flowDump
wait $pid
# executes the python script in order to extract the URLs
cd ..
rm -rf $website/crawlingOutput
python httpExtractor.py $website