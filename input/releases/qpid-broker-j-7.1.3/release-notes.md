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

# Qpid Broker-J 7.1.3 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8299](https://issues.apache.org/jira/browse/QPID-8299) - [Broker-J][JDBC Config Store] Possibility to customize the connection provider for the config of the Broker
 - [QPID-8301](https://issues.apache.org/jira/browse/QPID-8301) - [Broker-J] Expose information about keystore certificate details
 - [QPID-8304](https://issues.apache.org/jira/browse/QPID-8304) - [Broker-J][JDBC Message Store] Performance bottleneck at the level of the executor
 - [QPID-8305](https://issues.apache.org/jira/browse/QPID-8305) - [Broker-J][JDBC Message Store] Performance regression when increasing the number of queues linked to a topic
 - [QPID-8307](https://issues.apache.org/jira/browse/QPID-8307) - [Broker-J] Document the virtualHostInitialConfiguration
 - [QPID-8311](https://issues.apache.org/jira/browse/QPID-8311) - [Broker-J][WMC] Allow setting replaceExistingArguments in UI for bind creation

## Bugs fixed

 - [QPID-8294](https://issues.apache.org/jira/browse/QPID-8294) - [Broker-J][JDBC Message Store][Oracle] Batch delete fails for more than 1000 messages
 - [QPID-8297](https://issues.apache.org/jira/browse/QPID-8297) - [Broker-J][JDBC Message Store][Oracle] QPID_MESSAGE_CONTENT reserved space keeps growing until it reaches the limit and crashes
 - [QPID-8302](https://issues.apache.org/jira/browse/QPID-8302) - [Broker-J] NonJavaKeystore does not validate private key and certificate matching on certificate update
 - [QPID-8303](https://issues.apache.org/jira/browse/QPID-8303) - [Broker-J][JDBC Message Store] Batch delete fails when deleting exactly 1000 messages
 - [QPID-8309](https://issues.apache.org/jira/browse/QPID-8309) - [Broker-J] [AMQP 0-8..0-91] Concurrent transaction commit can fail with: Cannot commit transaction with state 'DISCHARGING'

## Tasks

 - [QPID-8312](https://issues.apache.org/jira/browse/QPID-8312) - [Broker-J] Release Qpid Broker-J version 7.1.3