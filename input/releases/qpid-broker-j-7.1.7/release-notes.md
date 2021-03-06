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

# Qpid Broker-J 7.1.7 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8385](https://issues.apache.org/jira/browse/QPID-8385) - [Broker-J] Improve performance of dequeuing old queue entries on triggering ring policy
 - [QPID-8388](https://issues.apache.org/jira/browse/QPID-8388) - [Broker-J] Allow for configuration to ignore unknown Queue arguments

## Bugs fixed

 - [QPID-8393](https://issues.apache.org/jira/browse/QPID-8393) - [Broker-J] Broker can crash with StackOverflowError when deleting messages
 - [QPID-8394](https://issues.apache.org/jira/browse/QPID-8394) - [Broker-J][WMC] Fix message table
 - [QPID-8398](https://issues.apache.org/jira/browse/QPID-8398) - [Broker-J] [AMQP 0-9] Improve heap usage utilization by small transient messages with headers

## Tasks

 - [QPID-8399](https://issues.apache.org/jira/browse/QPID-8399) - [Broker-J] Release Qpid Broker-J version 7.1.7
 - [QPID-8400](https://issues.apache.org/jira/browse/QPID-8400) - [Broker-J] Upgrade jackson dependencies to version 2.10.2