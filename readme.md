```bash
docker build -t webserv-test .

docker run --rm -it \
  --name webserv \
  -p 8081:8081 \
  -v "$PWD/webserv:/webserv" \
  -w /webserv \
  webserv-test \
  bash -lc 'make re && exec ./webserv conf/complete_webserv.conf'
```


```bash
docker run --rm -it \
  --name webserv \
  -p 8081:8081 \
  -p 8082:8082 \
  -v "$PWD/webserv:/webserv" \
  -w /webserv \
  webserv-test \
  bash -lc 'make re && exec ./webserv conf/complete_webserv.conf'
  
  ----

  docker run --rm -it \
  --platform linux/amd64 \
  --name webserv \
  -p 8081:8081 \
  -p 8082:8082 \
  -v "$PWD/webserv:/webserv" \
  -w /webserv \
  webserv-test-amd64 \
  bash -lc 'make re && exec ./webserv conf/testerconf.conf'

----

docker exec -it webserv bash
./tester http://localhost:8081
```


Lascia quel terminale aperto. Da un secondo terminale:
```bash
curl -v http://localhost:8081/
```

Potrai quindi fermarlo con:
```bash
docker stop webserv
```
