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

# Qpid Broker-J 8.0.5 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8483](https://issues.apache.org/jira/browse/QPID-8483) - [Broker-J] Change session operational log subject to have a session name in it
 - [QPID-8511](https://issues.apache.org/jira/browse/QPID-8511) - [Broker-J] Upgrade dojotoolkit to version 1.16.3
 - [QPID-8515](https://issues.apache.org/jira/browse/QPID-8515) - [Broker-J] Improve operational logging and log every change to the broker state
 - [QPID-8535](https://issues.apache.org/jira/browse/QPID-8535) - [Broker-J] Add a switch to ignore SNI host errors
 - [QPID-8539](https://issues.apache.org/jira/browse/QPID-8539) - [Broker-J] Upgrade Jackson version to 2.12.3

## Bugs fixed

 - [QPID-8509](https://issues.apache.org/jira/browse/QPID-8509) - [Broker-J] java.util.NoSuchElementException in AMQPConnection_1_0Impl.next()
 - [QPID-8510](https://issues.apache.org/jira/browse/QPID-8510) - [Broker-J] [AMQP 1.0] Connection transaction management is not thread-safe
 - [QPID-8514](https://issues.apache.org/jira/browse/QPID-8514) - [Broker-J] High CPU usage and stucked connections
 - [QPID-8518](https://issues.apache.org/jira/browse/QPID-8518) - [Broker-J] Message transfer freezes when session runs out of transfer frames
 - [QPID-8520](https://issues.apache.org/jira/browse/QPID-8520) - [Broker-J] ReadPendingException thrown by Broker-J intermittently
 - [QPID-8525](https://issues.apache.org/jira/browse/QPID-8525) - [Broker-J] An attempt to add a duplicate member or group into group provider of type GroupFile results in a removal of existing member or group from a file where data is stored
 - [QPID-8526](https://issues.apache.org/jira/browse/QPID-8526) - [Broker-J] Connection looping in NonBlockingConnectionTLSDelegate.doWrite()
 - [QPID-8529](https://issues.apache.org/jira/browse/QPID-8529) - [Broker-J] NPE when trying to access cached user credentials

## Tasks

 - [QPID-8537](https://issues.apache.org/jira/browse/QPID-8537) - [Broker-J] Replace use of constructors marked deprecated for-removal
 - [QPID-8540](https://issues.apache.org/jira/browse/QPID-8540) - [Broker-J] Release Qpid Broker-J 8.0.5