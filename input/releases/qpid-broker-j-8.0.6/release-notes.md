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

# Qpid Broker-J 8.0.6 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8530](https://issues.apache.org/jira/browse/QPID-8530) - [Broker-J] Duplicated functionality of the Selector::wakeup method in SelectorThread
 - [QPID-8541](https://issues.apache.org/jira/browse/QPID-8541) - [Broker-J] Enhance Broker Rest API to include certificate alias
 - [QPID-8556](https://issues.apache.org/jira/browse/QPID-8556) - [Broker-J] Expose virtual host threshold for triggering flow to disk on direct memory utilization
 - [QPID-8559](https://issues.apache.org/jira/browse/QPID-8559) - [Broker-J] Add debug logs for flow to disk events
 - [QPID-8560](https://issues.apache.org/jira/browse/QPID-8560) - [Broker-J] Upgrade fasterxml jackson dependency

## Bugs fixed

 - [QPID-8546](https://issues.apache.org/jira/browse/QPID-8546) - [Broker-J] BDB HA replication of atomic BDB transactions for message acknowldgements impacts consumer performance
 - [QPID-8552](https://issues.apache.org/jira/browse/QPID-8552) - [Broker-J] Http management interface should ignore OPTIONS command
 - [QPID-8555](https://issues.apache.org/jira/browse/QPID-8555) - [Broker-J] Http management does not allow to set OPTIONS method in attribute for  CORS allowed methods
