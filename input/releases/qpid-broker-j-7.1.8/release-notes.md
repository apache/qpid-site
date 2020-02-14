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

# Qpid Broker-J 7.1.8 Release Notes

Qpid Broker-J is a message broker written in Java that stores, routes,
and forwards messages using AMQP.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPID-8406](https://issues.apache.org/jira/browse/QPID-8406) - [Broker-J] Display connection transport information in web management console
 - [QPID-8408](https://issues.apache.org/jira/browse/QPID-8408) - [Broker-J] JDBC store supports MS SQL Server

## Bugs fixed

 - [QPID-8403](https://issues.apache.org/jira/browse/QPID-8403) - [Broker-J] Configuring HTTP port for External Authentication causes Web Management Console to throw HTTP 403 errors 
 - [QPID-8404](https://issues.apache.org/jira/browse/QPID-8404) - [Broker-J] Use of TLS client certificates in versions &gt; = 7.1.5 broken by Jetty changes
 - [QPID-8407](https://issues.apache.org/jira/browse/QPID-8407) - [Broker-J][BDB HA] Asynchronous message store recoverer can fail to recover messages on switching the master node
 - [QPID-8411](https://issues.apache.org/jira/browse/QPID-8411) - [Broker-J][REST] Invocation of operation fails when reserved parameter is specified

## Tasks

 - [QPID-8410](https://issues.apache.org/jira/browse/QPID-8410) - [Broker-J] Release Qpid Broker-J version 7.1.8