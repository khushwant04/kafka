# Kafka Setup Guide

This document provides instructions for setting up and starting Zookeeper, Kafka, and CMAK (Cluster Manager for Apache Kafka).

## Prerequisites

Ensure that you have Kafka and CMAK installed in the specified directories.

## Starting Zookeeper

1. Open a terminal.
2. Navigate to the Kafka installation directory:

    ```bash
    cd ~/kafka/kafka_2.13-3.8.0
    ```

3. Start Zookeeper using the following command:

    ```bash
    bin/zookeeper-server-start.sh config/zookeeper.properties
    ```

   Zookeeper will start and listen for connections on the default port.

## Starting Kafka Broker

1. Open a new terminal.
2. Navigate to the Kafka installation directory:

    ```bash
    cd ~/kafka/kafka_2.13-3.8.0
    ```

3. Set the JMX port and start Kafka Broker using the following command:

    ```bash
    JMX_PORT=8004 bin/kafka-server-start.sh config/server.properties
    ```

   Kafka will start and listen for connections on the default port.

## Starting CMAK (Cluster Manager for Apache Kafka)

1. Open a new terminal.
2. Navigate to the CMAK installation directory:

    ```bash
    cd ~/kafka/CMAK/target/universal/cmak-3.0.0.7
    ```

3. Start CMAK using the following command:

    ```bash
    cd ~/kafka/cmak-3.0.0.7
    sudo bin/cmak -Dconfig.file=conf/application.conf -Dhttp.port=8080
    ```

   CMAK will start and be accessible via HTTP on port 8080.

## Summary

1. **Zookeeper**: Handles distributed coordination.
2. **Kafka Broker**: Manages message storage and retrieval.
3. **CMAK**: Provides a web interface for Kafka cluster management.

Ensure that Zookeeper is running before starting the Kafka Broker, and that Kafka Broker is running before starting CMAK.

For more detailed configuration and usage, refer to the respective documentation of [Zookeeper](https://zookeeper.apache.org/doc/current/), [Kafka](https://kafka.apache.org/documentation/), and [CMAK](https://github.com/yahoo/CMAK).

