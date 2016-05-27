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

# Qpid Java 6.0.3 Release Notes

Qpid Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7209](https://issues.apache.org/jira/browse/QPID-7209) - [Java Broker, WMC] Enable HTTP compression by default
 - [QPID-7210](https://issues.apache.org/jira/browse/QPID-7210) - [Java Broker, WMC] REST requests to VirtualHost and getConnections should be made in parallel
 - [QPID-7211](https://issues.apache.org/jira/browse/QPID-7211) - [Java Broker, WMC] Do not transfer inherited context variables
 - [QPID-7216](https://issues.apache.org/jira/browse/QPID-7216) - [Java Broker, WMC] add new ManagedOperation to retrieve Connections less verbose
 - [QPID-7255](https://issues.apache.org/jira/browse/QPID-7255) - Support delivery delay
 - [QPID-7271](https://issues.apache.org/jira/browse/QPID-7271) - Improve exception handling for PlainSaslServer

## Bugs fixed

 - [QPID-5816](https://issues.apache.org/jira/browse/QPID-5816) - [Java Client 0-10] If a resolved destination is used to create a consumer on a new connection created after destination was resolved, the client does not try to create the destination on the broker
 - [QPID-6096](https://issues.apache.org/jira/browse/QPID-6096) - java broker doesn't indicate that port is already in use
 - [QPID-7231](https://issues.apache.org/jira/browse/QPID-7231) - Example of REST call to invoke the Queue clear queue operation is incorrect
 - [QPID-7237](https://issues.apache.org/jira/browse/QPID-7237) - Excessive threads creation when suspending/resuming flow
 - [QPID-7253](https://issues.apache.org/jira/browse/QPID-7253) - [Java Client 0-10] Application allowed to create new JMS session whilst failover is in progress
 - [QPID-7257](https://issues.apache.org/jira/browse/QPID-7257) - [Java Broker] Correct connection state logging
 - [QPID-7260](https://issues.apache.org/jira/browse/QPID-7260) - apache-release profile fails under JDK 1.8 due to javadoc errors
 - [QPID-7267](https://issues.apache.org/jira/browse/QPID-7267) - [Java Broker] Content-Length header is set incorrectly when using compression
 - [QPID-7268](https://issues.apache.org/jira/browse/QPID-7268) - message sent over 0-10 can't be received over 1.0
 - [QPID-7269](https://issues.apache.org/jira/browse/QPID-7269) - broker issues disposition for delivery that is already settled

## Tasks

 - [QPID-7265](https://issues.apache.org/jira/browse/QPID-7265) - migrate the AMQP 0-10 JMS client docs out of the old combined doc book.
 - [QPID-7266](https://issues.apache.org/jira/browse/QPID-7266) - RAT check fails on release archive due to generated file