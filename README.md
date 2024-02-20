
# data-stream-with-python-and-apache-kafka

#### Get data from a youtube plyalist, see which videos are in playlist, check their statistics

url = "GET https://www.googleapis.com/youtube/v3/playlists"

* To get data we need youtube data api key
    * create google project => enable api => credentials => create api key

* youtube playlist id
*

- we get paged results, 5 results per page, Hence we need to use python generator

## Download Kafka
```
    https://dlcdn.apache.org/kafka/3.6.1/kafka_2.13-3.6.1.tgz

    tar -xzf kafka_2.13-3.6.1.tgz

    cd kafka_2.13-3.6.1

    # Start the ZooKeeper service
    $ bin/zookeeper-server-start.sh config/zookeeper.properties

    # Start the Kafka broker service in another terminal
    $ JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties

    # install kafka manager- GUI

   - need JAVA 11 => install java 11

    goto https://github.com/yahoo/CMAK
    git clone https://github.com/yahoo/CMAK.git
    cd CMAK
    ./sbt clean dist

   -inside CMAK folder there is target folder
   cd target
   cd universal
   unzip cmak-3.0.0.7.zip
   cd cmak-3.0.0.7/
   cd conf
   nano application.conf
   cmak.zkhosts="kafka-manager-zookeeper:2181"
   cmak.zkhosts="localhost:2181"
   - to run kafka manager 
   bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080
   
   
   




    # Create topic
    bin/kafka-topics.sh --create --topic quickstart-events --bootstrap-server localhost:9092

    #kafka producer - Run the console producer client to write a few events into your topic
     bin/kafka-console-producer.sh --topic quickstart-events --bootstrap-server localhost:9092
    This is my first event
    This is my second event

    # kafka consumer - Open another terminal session and run the console consumer client to read the events you just created:

    bin/kafka-console-consumer.sh --topic quickstart-events --from-beginning --bootstrap-server localhost:9092

```


** python vertual enviornment
python -m venv venv
source venv/bin/activate
deactivate

* kafka-python
pip install kafka-python
pip install Faker
#

