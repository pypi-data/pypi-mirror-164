# <img src="https://uploads-ssl.webflow.com/5ea5d3315186cf5ec60c3ee4/5edf1c94ce4c859f2b188094_logo.svg" alt="Pip.Services Logo" width="200"> <br/> Kafka components for Pip.Services in Python Changelog

## <a name="3.1.11"></a> 3.1.11 (2022-08-12)

# Features
* Added default build-in partition in publish method if write partition is not set 

## <a name="3.1.10"></a> 3.1.10 (2022-07-11)

### Features
* Added more config parameters (num_partitions, replication_factor, readable_partitions write_partition)
* Optimize Producers creation and caching

### Bug fixes
* Fixed kafka publish method, added on_delivery error callback

## <a name="3.1.9-3.1.10"></a> 3.1.9 - 3.1.10 (2022-07-09)

### Bug fixes
* Fixed kafka publish method, added on_delivery error callback

## <a name="3.1.8"></a> 3.1.8 (2022-03-26)

### Bug fixes
* Fixed build factory Kafka

## <a name="3.1.7"></a> 3.1.7 (2022-01-18)

### Features
* Improved message serialization for KafkaConnection.publish

## <a name="3.1.6"></a> 3.1.6 (2021-11-12)

### Features
* Changed *on_message* message param from bytes to Message object

## <a name="3.1.3-3.1.5"></a> 3.1.3-3.1.5 (2021-11-11)

### Features
* Added create_queue, delete_queue for KafkaConnection

### Bug fixes
* Fixed timeout producer publish
* Fixed KafkaConnection.subscribe for empty options

## <a name="3.1.1-3.1.2"></a> 3.1.1-3.1.2 (2021-11-03)

### Bug fixes
* Added flushing for kafka producer
* Fixed setup file

## <a name="3.1.0"></a> 3.1.0 (2021-11-02)

### Features
* Migrated from kafka-python on confluent_kafka
* Changed seconds on millisecond in timestamps

## <a name="3.0.0"></a> 3.0.0 (2021-09-09)

Initial release

### Features

* Added KafkaMessageQueueFactory component
* Added KafkaConnection component
* Added DefaultKafkaFactory component
* Added KafkaConnectionResolver component
* Added KafkaMessageQueue component

