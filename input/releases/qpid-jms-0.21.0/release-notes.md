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

# Qpid JMS 0.21.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 1.1 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-244](https://issues.apache.org/jira/browse/QPIDJMS-244) - Connection close does not wait for acknowledgement of in-flight message delivery with asyncronous auto-ack MessageConsumer
 - [QPIDJMS-258](https://issues.apache.org/jira/browse/QPIDJMS-258) - Reduce the amount of allocation done in the consumer on async message dispatch
 - [QPIDJMS-267](https://issues.apache.org/jira/browse/QPIDJMS-267) - Support discovery of failover hosts provided in a connection property of the Open frame
 - [QPIDJMS-270](https://issues.apache.org/jira/browse/QPIDJMS-270) - update to proton-j 0.18.0
 - [QPIDJMS-271](https://issues.apache.org/jira/browse/QPIDJMS-271) - Cache transaction state dispostions for TXN producers and consumers

## Bugs fixed

 - [QPIDJMS-231](https://issues.apache.org/jira/browse/QPIDJMS-231) - closing a consumer used since prior commit/rollback holds its prefetched messages until the next commit/rollback
 - [QPIDJMS-256](https://issues.apache.org/jira/browse/QPIDJMS-256) - Closing a consumer that was used in a transaction does not stop message dispatching unitl next commit or rollback
 - [QPIDJMS-257](https://issues.apache.org/jira/browse/QPIDJMS-257) - Messages delivered from a consume in client acknowledge mode cannot be acknowledged after the consumer is closed
 - [QPIDJMS-266](https://issues.apache.org/jira/browse/QPIDJMS-266) - Race on session start and message dispatch can deliver messages in wrong order
 - [QPIDJMS-269](https://issues.apache.org/jira/browse/QPIDJMS-269) - Performance regression affecting MessageProducer on transacted Sessions.
 - [QPIDJMS-272](https://issues.apache.org/jira/browse/QPIDJMS-272) - fail fast when attempting connection to a server using unexpected protocol type

## Tasks

 - [QPIDJMS-262](https://issues.apache.org/jira/browse/QPIDJMS-262) - Update ActiveMQ Dependency to latest 5.14.3
 - [QPIDJMS-268](https://issues.apache.org/jira/browse/QPIDJMS-268) - Update Netty to 4.1.8.Final