;;
;; Licensed to the Apache Software Foundation (ASF) under one
;; or more contributor license agreements.  See the NOTICE file
;; distributed with this work for additional information
;; regarding copyright ownership.  The ASF licenses this file
;; to you under the Apache License, Version 2.0 (the
;; "License"); you may not use this file except in compliance
;; with the License.  You may obtain a copy of the License at
;; 
;;   http://www.apache.org/licenses/LICENSE-2.0
;; 
;; Unless required by applicable law or agreed to in writing,
;; software distributed under the License is distributed on an
;; "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
;; KIND, either express or implied.  See the License for the
;; specific language governing permissions and limitations
;; under the License.
;;

# Qpid for Java 6.1.3 Release Notes

Qpid for Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7468](https://issues.apache.org/jira/browse/QPID-7468) - [Java Broker] Upgrade logback to 1.1.11 and SLF4J to 1.7.24
 - [QPID-7730](https://issues.apache.org/jira/browse/QPID-7730) - [Java Broker] Upgrade logback to latest version (1.2.2)
 - [QPID-7736](https://issues.apache.org/jira/browse/QPID-7736) - [Java Broker] Upgrade SLF4j to 1.7.25
 - [QPID-7737](https://issues.apache.org/jira/browse/QPID-7737) - [JMS AMQP 0-x Client] Upgrade SLF4j to 1.7.25
 - [QPID-7745](https://issues.apache.org/jira/browse/QPID-7745) - [Java Broker] Bump dependency version of Apache Derby

## Bugs fixed

 - [QPID-7505](https://issues.apache.org/jira/browse/QPID-7505) - [JMS AMQP 0-x Client] The subsequenct synchronous #recieve(long) might return null even when there are messages on the queue and client has enough credits
 - [QPID-7732](https://issues.apache.org/jira/browse/QPID-7732) - [Java Broker] Issues with using global address domains
 - [QPID-7733](https://issues.apache.org/jira/browse/QPID-7733) - [Java Broker] Misplaced ch.qos.logback.classic.spi.Configurator services file prevents use of logback in the Broker without the Qpid logging-logback module
 - [QPID-7743](https://issues.apache.org/jira/browse/QPID-7743) - [Java Broker] Propagate current IO thread when switching protocol engine
 - [QPID-7763](https://issues.apache.org/jira/browse/QPID-7763) - [Java Broker] Flow to disk if allocated direct memory exceeds broker wide broker.flowToDiskThreshold
 - [QPID-7766](https://issues.apache.org/jira/browse/QPID-7766) - [Java Broker] [Derby Store] Unsigned byte type should be used when reading stored message metada type
 - [QPID-7774](https://issues.apache.org/jira/browse/QPID-7774) - [JMS Client 0-x] [0-8..0-91] MessageConsumer#receiveNoWait() always returns null after a successful failover
 - [QPID-7783](https://issues.apache.org/jira/browse/QPID-7783) - [Java Broker] Closing a virtualhost does not dispose QBBs associated with messages on queues
 - [QPID-7784](https://issues.apache.org/jira/browse/QPID-7784) - [Java Broker] Closing a virtualhost does not dispose QBBs still associated with pooled IO threads
 - [QPID-7794](https://issues.apache.org/jira/browse/QPID-7794) - [Java Broker] Periodically report the number of bytes evacuated from memory by flow to disk (6.1/6.0)
 - [QPID-7795](https://issues.apache.org/jira/browse/QPID-7795) - [Java Broker] Ensure that a newly enqueued message that is flowed to disk does not immediately have meta-data reloaded (6.1/6.0)
 - [QPID-7796](https://issues.apache.org/jira/browse/QPID-7796) - [Java Broker] Guard against NPE in 0-10 when storing messages without header