# Docker Postgres Spark cluster

---
### Skills and tools:
`Docker` `Docker-compose` `PostgreSQL` `AWS Cli` `Terminal` `PySpark` 

---
### Task: Create Spark testing environment cluster on local PC

1. Compile docker image to run spark master and worker containers.
2. Create a spark standalone cluster using docker and docker-compose.
3. Cluster must contain 2 workers nodes and 1 master node.
4. Copy data from S3 bucket to run demo applications.
5. Ran demo application on created cluster.

---
### Pre requisites:

1. Docker installed
2. Docker-compose installed
---
## Progress of work:
1. Creating [*Dockerfile*][1] with commands that will provide all necessary image configs:
    * PySpark configuration
    * version configuration
    * initiation script
   

2. Creating [*Docker-compose.yaml*][2] with container configuration
    * master node config
    * specifying resources volumes for data & apps
    * worker node config
    * cluster resource allocation
      - CPU cores allocation for each spark worker is 1 core.
      - RAM for each spark-worker is 1024 MB.
      - RAM allocation for spark executors is 256mb.
      - RAM allocation for spark driver is 128mb
    * postgres DB config


3. Creating [*PySpark job task*][3] to run demo application


4. Run [*shell script*][4] to:
    * install *AWS CLI*
    * Download [*data*][5] from *aws S3* bucket
    * Download *JDBC* driver for *Postgres* connection
   

5. Building *Docker* image:
```shell
docker build -t postgres-spark-cluster:1.0 .
```

6. Creating [*Spark configuration shell*][6], that will initiate with *docker-compose Container*


7. Run the *Docker-compose* to create *Docker* container:
```sh
docker-compose up -d
```

6. Veryfi work of all containers:
```shell
docker ps
```

7. Validating proper work of cluster in browser:
```html
http://localhost:9090/
http://localhost:9091/
http://localhost:9092/
```
 
7. Run demo application:
```shell
docker ps
docker exec -it container_id /bin/bash
```

   * paste next command to *terminal*:
```shell
/opt/spark/bin/spark-submit --master spark://spark-master:7077 \
--jars /opt/spark-app/postgresql-42.2.22.jar \
--driver-memory 1G \
--executor-memory 1G \
/opt/spark-app/main.py
```
   * Application make aggregations from Datasource and saves results to *Postgresql*.

8. Stop all containers:
```shell
docker-compose down --volumes
```


[1]: https://github.com/Amboss/Docker_Spark_cluster/blob/191bf55816f1c82ad7976629b0f165c0c8c451ac/Dockerfile
[2]: https://github.com/Amboss/Docker_Spark_cluster/blob/191bf55816f1c82ad7976629b0f165c0c8c451ac/docker-compose.yml
[3]: https://github.com/Amboss/Docker_Spark_cluster/blob/191bf55816f1c82ad7976629b0f165c0c8c451ac/app/main.py
[4]: https://github.com/Amboss/Docker_Spark_cluster/blob/191bf55816f1c82ad7976629b0f165c0c8c451ac/scripts/prepare_data.sh
[5]: http://web.mta.info/developers/MTA-Bus-Time-historical-data.html
[6]: https://github.com/Amboss/Docker_Spark_cluster/blob/191bf55816f1c82ad7976629b0f165c0c8c451ac/scripts/spark_config.sh
