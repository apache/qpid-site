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

# Qpid JMS 0.11.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 1.1 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-187](https://issues.apache.org/jira/browse/QPIDJMS-187) - remove deprecated configuration options
 - [QPIDJMS-191](https://issues.apache.org/jira/browse/QPIDJMS-191) - Add a WebSocket based transport to the client
 - [QPIDJMS-194](https://issues.apache.org/jira/browse/QPIDJMS-194) - Update to Proton 0.13.1

## Bugs fixed

 - [QPIDJMS-189](https://issues.apache.org/jira/browse/QPIDJMS-189) - update JMSMessageID and JMSCorrelationID handling to address interop issues with non-JMS peers
 - [QPIDJMS-195](https://issues.apache.org/jira/browse/QPIDJMS-195) - misc error handling improvements
 - [QPIDJMS-196](https://issues.apache.org/jira/browse/QPIDJMS-196) - Anonymous Fallback producer does not handle send failure properly
 - [QPIDJMS-197](https://issues.apache.org/jira/browse/QPIDJMS-197) - Anonymous fallback producer doesn't handle async sends correctly
 - [QPIDJMS-198](https://issues.apache.org/jira/browse/QPIDJMS-198) - Blocked Send on a MessageProducer waiting for credit not unblocked on remote close of the producer
 - [QPIDJMS-199](https://issues.apache.org/jira/browse/QPIDJMS-199) - Remote close of a session with producer blocked waiting for credit doesn't fail the send
 - [QPIDJMS-201](https://issues.apache.org/jira/browse/QPIDJMS-201) - Consumer handling of no drain response can unsubscribe a durable subscription
 - [QPIDJMS-204](https://issues.apache.org/jira/browse/QPIDJMS-204) - Race condition on Producer / Consumer create can miss remote close signal
 - [QPIDJMS-205](https://issues.apache.org/jira/browse/QPIDJMS-205) - make shutdown of Netty executor group wait for completion

## Tasks

 - [QPIDJMS-193](https://issues.apache.org/jira/browse/QPIDJMS-193) - Update ActiveMQ test dependency to 5.13.3
 - [QPIDJMS-200](https://issues.apache.org/jira/browse/QPIDJMS-200) - Update to ActiveMQ 5.14.0 release for testing
 - [QPIDJMS-202](https://issues.apache.org/jira/browse/QPIDJMS-202) - Update to Proton 0.14.0
 - [QPIDJMS-203](https://issues.apache.org/jira/browse/QPIDJMS-203) - Update Netty to latest bugfix release 4.0.41.Final