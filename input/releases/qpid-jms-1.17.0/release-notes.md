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

# Qpid JMS 1.17.0 Release Notes

Qpid JMS is a complete [Jakarta Messaging](https://jakarta.ee/specifications/messaging/) 2.0
client built using the [Qpid Proton]({{site_url}}/proton/index.html) protocol engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPIDJMS-624](https://issues.apache.org/jira/browse/QPIDJMS-624) - AMQP JMS Binding Type Annotations should also support non-byte datatypes

## Bugs fixed

 - [QPIDJMS-622](https://issues.apache.org/jira/browse/QPIDJMS-622) - JMSConsumer receiveBody should throw if message is a bare Message instance

## Tasks

 - [QPIDJMS-623](https://issues.apache.org/jira/browse/QPIDJMS-623) - Update to Netty 4.1.137.Final
 - [QPIDJMS-625](https://issues.apache.org/jira/browse/QPIDJMS-625) - Update jacoco plugin to 0.8.15
 - [QPIDJMS-626](https://issues.apache.org/jira/browse/QPIDJMS-626) - Update slf4j to version 2.0.18
 - [QPIDJMS-627](https://issues.apache.org/jira/browse/QPIDJMS-627) - Update mockito to v5.23.0
 - [QPIDJMS-628](https://issues.apache.org/jira/browse/QPIDJMS-628) - Update commons io to version 2.22.0
 - [QPIDJMS-629](https://issues.apache.org/jira/browse/QPIDJMS-629) - Update JUnit to version 5.14.4
 - [QPIDJMS-630](https://issues.apache.org/jira/browse/QPIDJMS-630) - Update ActiveMQ version in compatibility tests to 5.19.9
 - [QPIDJMS-631](https://issues.apache.org/jira/browse/QPIDJMS-631) - Update kerb-simplekdc test dep to 2.1.2
 - [QPIDJMS-632](https://issues.apache.org/jira/browse/QPIDJMS-632) - Update to proton-j 0.35.0