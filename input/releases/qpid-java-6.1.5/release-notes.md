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

# Qpid for Java 6.1.5 Release Notes

Qpid for Java offers an AMQP-fluent implementation of JMS and a message
broker written in Java that stores, routes, and forwards messages
using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-7974](https://issues.apache.org/jira/browse/QPID-7974) - JdbcUtils.TableExists is very slow on big databases such as Oracle
 - [QPID-8021](https://issues.apache.org/jira/browse/QPID-8021) - [Broker-J] [BDB] Make BDB store module compatible with JE release 7.4.5   [6.1.x]

## Bugs fixed

 - [QPID-7836](https://issues.apache.org/jira/browse/QPID-7836) - NPE logged at WARN during management view of messages whilst consumer active
 - [QPID-7853](https://issues.apache.org/jira/browse/QPID-7853) - Message enqueued twice to the same queue leads to Broker failure
 - [QPID-7947](https://issues.apache.org/jira/browse/QPID-7947) - [Java Broker] [AMQP 1.0] Improve handling of empty and overlarge frames
 - [QPID-7973](https://issues.apache.org/jira/browse/QPID-7973) - Table Name Prefix is set to NULL if no prefix is provided instead of empty String