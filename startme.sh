CS6065
P1 Docker


Please use below steps to load docker image run wordstatistics
gzip -d wordstatistics.tar.gz
docker load -i wordstatistics.tar
docker run -d -p 5555:5555 wordstatistics /home/startme.sh

Please use below url to access application
http://localhost:5555/wordstatistics
