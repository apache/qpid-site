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

# Qpid JMS 0.6.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 1.1 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-51](https://issues.apache.org/jira/browse/QPIDJMS-51) - Improve the QueueBrowser implementation
 - [QPIDJMS-105](https://issues.apache.org/jira/browse/QPIDJMS-105) - Add option to configure the Message ID Type
 - [QPIDJMS-106](https://issues.apache.org/jira/browse/QPIDJMS-106) - apply the validatePropertyNames option for messages to be sent in addition to those received
 - [QPIDJMS-109](https://issues.apache.org/jira/browse/QPIDJMS-109) - Refactor internal management of resource creation and cleanup
 - [QPIDJMS-112](https://issues.apache.org/jira/browse/QPIDJMS-112) - have receiveNoWait and receive(timeout) drain credit to ensure no message is available
 - [QPIDJMS-113](https://issues.apache.org/jira/browse/QPIDJMS-113) - update URI option documentation to be clearer and fix misleading section

## Bugs fixed

 - [QPIDJMS-107](https://issues.apache.org/jira/browse/QPIDJMS-107) - RuntimeException in onMessage can cause missed ack of message.
 - [QPIDJMS-108](https://issues.apache.org/jira/browse/QPIDJMS-108) - producers don't correctly handle modified/released delivery state
 - [QPIDJMS-110](https://issues.apache.org/jira/browse/QPIDJMS-110) - Incorrect error handling when the sender.send(...) call / message transfer causes an error
 - [QPIDJMS-111](https://issues.apache.org/jira/browse/QPIDJMS-111) - ensure outstanding sync ops get updated when the connection fails
 - [QPIDJMS-114](https://issues.apache.org/jira/browse/QPIDJMS-114) - When failover.initialReconnectDelay is set, client cannot connect
 - [QPIDJMS-115](https://issues.apache.org/jira/browse/QPIDJMS-115) - Repetitive reconnections when wrong password set
 - [QPIDJMS-116](https://issues.apache.org/jira/browse/QPIDJMS-116) - make behaviour of receive and receiveNoWait consistent when consumer closes due to a problem
 - [QPIDJMS-117](https://issues.apache.org/jira/browse/QPIDJMS-117) - dont apply the initialReconnectDelay to the first attempt to connect
 - [QPIDJMS-118](https://issues.apache.org/jira/browse/QPIDJMS-118) - timed dequeue calls on the local queue can return before they should
 - [QPIDJMS-119](https://issues.apache.org/jira/browse/QPIDJMS-119) - calling start on the local queue after it is closed should not result in it being marked started again
 - [QPIDJMS-120](https://issues.apache.org/jira/browse/QPIDJMS-120) - viewer may not see previously updated running/closed state on local queue