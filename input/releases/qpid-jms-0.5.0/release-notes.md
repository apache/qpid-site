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

# Qpid JMS 0.5.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 1.1 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-92](https://issues.apache.org/jira/browse/QPIDJMS-92) - Improve the pull consumer implementation (no prefetch)
 - [QPIDJMS-96](https://issues.apache.org/jira/browse/QPIDJMS-96) - Add expired message filtering to the MessageConsumer
 - [QPIDJMS-101](https://issues.apache.org/jira/browse/QPIDJMS-101) - Close of the AMQP Provider should not forward exception if the close frame cannot be written

## Bugs fixed

 - [QPIDJMS-93](https://issues.apache.org/jira/browse/QPIDJMS-93) - Extract proper error from Rejected disposition to avoid NPE as cause of a JMSException
 - [QPIDJMS-94](https://issues.apache.org/jira/browse/QPIDJMS-94) - the failover provider can erroneously reconnect following Connection close.
 - [QPIDJMS-95](https://issues.apache.org/jira/browse/QPIDJMS-95) - the failover provider can block if the transport drops while establishing the new connection.
 - [QPIDJMS-97](https://issues.apache.org/jira/browse/QPIDJMS-97) - Pull Consumer in combination with RedeliveryPolicy enforcement can lead to stuck consumer
 - [QPIDJMS-99](https://issues.apache.org/jira/browse/QPIDJMS-99) - Race on failure processing can lead to the wrong error being propagated.
 - [QPIDJMS-100](https://issues.apache.org/jira/browse/QPIDJMS-100) - SSL Connections can fire async errors prior to the connect call completion.
 - [QPIDJMS-102](https://issues.apache.org/jira/browse/QPIDJMS-102) - initial onMessage deliveries may be delivered concurrently and in the wrong order
 - [QPIDJMS-103](https://issues.apache.org/jira/browse/QPIDJMS-103) - After failover a pull consumer can block in receive
 - [QPIDJMS-104](https://issues.apache.org/jira/browse/QPIDJMS-104) - avoid iterating a likely-empty collection on arrival of each message