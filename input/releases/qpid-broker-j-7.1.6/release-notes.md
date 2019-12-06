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

# Qpid Broker-J 7.1.6 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8373](https://issues.apache.org/jira/browse/QPID-8373) - [Broker-J][REST] Operation getMessageInfo should report an id of consumer aquired the message
 - [QPID-8376](https://issues.apache.org/jira/browse/QPID-8376) - [Broker-J] Add Process CPU time to collected Broker statistics
 - [QPID-8377](https://issues.apache.org/jira/browse/QPID-8377) - [Broker-J] Allow for configuration to ignore unknown Exchange.Declare arguments
 - [QPID-8380](https://issues.apache.org/jira/browse/QPID-8380) - [Broker-J][REST] Operation getMessageInfo should report groupId of the message

## Bugs fixed

 - [QPID-8378](https://issues.apache.org/jira/browse/QPID-8378) - [Broker-J] Message references can be leaked in some rare circumstances
 - [QPID-8384](https://issues.apache.org/jira/browse/QPID-8384) - [Broker-J] LastValueQueueList can leak deleted queue entries
 - [QPID-8387](https://issues.apache.org/jira/browse/QPID-8387) - [Broker-J] JDBC based message stores do not wait for asynchronous message removal threads to complete when store is being closed

## Tasks

 - [QPID-8379](https://issues.apache.org/jira/browse/QPID-8379) - [Broker-J] Upgrade jackson dependecies to version 2.10.1