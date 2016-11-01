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

# Qpid for Java 6.0.5 Release Notes

Qpid for Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7338](https://issues.apache.org/jira/browse/QPID-7338) - Use maven release plugin's tagNameFormat to avoid manual release step
 - [QPID-7454](https://issues.apache.org/jira/browse/QPID-7454) - [Java Broker] Queue Message Durability default (and others) should be overridable by context variables

## Bugs fixed

 - [QPID-6377](https://issues.apache.org/jira/browse/QPID-6377) - Connection's taskpool not shutdown if Connection is closed from the broker side
 - [QPID-7223](https://issues.apache.org/jira/browse/QPID-7223) - [Java Broker] Broker does not decrement consumer statistics "unacknowledgedBytes" and "unacknowledgedMessages" after receiving message.release command for 0.10 AMQP protocol
 - [QPID-7328](https://issues.apache.org/jira/browse/QPID-7328) - [Java Broker, WMC] The Help Menu link in the WMC is broken
 - [QPID-7342](https://issues.apache.org/jira/browse/QPID-7342) - [Java Broker] ForbiddingAuthorisationFilter carelessly matches request paths
 - [QPID-7363](https://issues.apache.org/jira/browse/QPID-7363) - [Java Broker] Unhandled 'Message store is not open exception' during Broker shutdown
 - [QPID-7382](https://issues.apache.org/jira/browse/QPID-7382) - Message dialogue tries to inline the text of a text message content regardless of the its length
 - [QPID-7386](https://issues.apache.org/jira/browse/QPID-7386) - [Java Broker, WMC] Session Cookie should set the HttpOnly flag
 - [QPID-7387](https://issues.apache.org/jira/browse/QPID-7387) - [Java Broker, AMQP 0-8..0-91] Correct handling of consumer credit
 - [QPID-7394](https://issues.apache.org/jira/browse/QPID-7394) - [0-8..0-91] Prefetch accounting incorrect when session rolled back / recovered
 - [QPID-7412](https://issues.apache.org/jira/browse/QPID-7412) - [Java Broker] Set default max message size to 100 MB
 - [QPID-7417](https://issues.apache.org/jira/browse/QPID-7417) - [Java Broker] Ensure message instance listeners only fire on state changes of the associated object
 - [QPID-7451](https://issues.apache.org/jira/browse/QPID-7451) - [Java Broker] MessageTransferMessage should cache message size
 - [QPID-7455](https://issues.apache.org/jira/browse/QPID-7455) - [Java Broker] Object references in configuration files should be able to use context variables
 - [QPID-7456](https://issues.apache.org/jira/browse/QPID-7456) - [Java Broker, WMC] Fix edit dialogue of BDB HA VHNs
 - [QPID-7464](https://issues.apache.org/jira/browse/QPID-7464) - [Java Broker] Increase of flow credit might cause superfluous notification of FlowCreditManagerListeners from FlowCreditManagers which might provoke unexpected message dilivery
 - [QPID-7465](https://issues.apache.org/jira/browse/QPID-7465) - [Java Broker] Stop ServerEncoder on AMQP 0-10 from unnecessarily allocating ByteBuffers

## Tasks

 - [QPID-7341](https://issues.apache.org/jira/browse/QPID-7341) - Names such as "Apache Qpid Java" cause trademark violations