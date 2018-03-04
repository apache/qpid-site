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

# Qpid Broker-J 7.0.2 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8091](https://issues.apache.org/jira/browse/QPID-8091) - [Broker-J] [AMQP 1.0] Store transaction timeout feature
 - [QPID-8101](https://issues.apache.org/jira/browse/QPID-8101) - [Broker-J] [Web Management Console] Add ability to close more than one connection at once
 - [QPID-8102](https://issues.apache.org/jira/browse/QPID-8102) - [Broker-J][Web Management Console] Add UI for virtual host node auto-creation policies
 - [QPID-8110](https://issues.apache.org/jira/browse/QPID-8110) - [Broker-J] Add ability to check ERRORED state of entire configured object hierarchy on broker startup

## Bugs fixed

 - [QPID-8098](https://issues.apache.org/jira/browse/QPID-8098) - [Broker-J] [AMQP 0-10] Queue browsers erroneously increment the delivery count
 - [QPID-8099](https://issues.apache.org/jira/browse/QPID-8099) - [Broker-J] [AMQP Management] Operation Queue#getMessageInfo response returned as serialised java object rather list of maps
 - [QPID-8100](https://issues.apache.org/jira/browse/QPID-8100) - [Broker-J] [AMQP 0-10] SESSION_BUSY sent on wrong channel leading to hung Messaging API based application
 - [QPID-8104](https://issues.apache.org/jira/browse/QPID-8104) - [Broker-J] [Query] [WMC] Ordering connections tables by port column fails with '422 - The orderBy expression at position '0' is unsupported'
 - [QPID-8106](https://issues.apache.org/jira/browse/QPID-8106) - [Broker-J] [Alternate Binding] On virtualhost recovery, message "Gave up waiting for Queue 'xxxx' to attain state" written to the log and startup delayed