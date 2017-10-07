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

# Qpid JMS 0.26.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-332](https://issues.apache.org/jira/browse/QPIDJMS-332) - enable defining destination names in tomcat resource definitions

## Bugs fixed

 - [QPIDJMS-314](https://issues.apache.org/jira/browse/QPIDJMS-314) - AssertionError from Netty during cleanup of Epoll channel with SO_LINGER configured
 - [QPIDJMS-326](https://issues.apache.org/jira/browse/QPIDJMS-326) - client should desire the DELAYED_DELIVERY connection capability
 - [QPIDJMS-330](https://issues.apache.org/jira/browse/QPIDJMS-330) - client should desire the ANONYMOUS-RELAY connection capability
 - [QPIDJMS-331](https://issues.apache.org/jira/browse/QPIDJMS-331) - client should desire the SHARED-SUBS connection capability
 - [QPIDJMS-334](https://issues.apache.org/jira/browse/QPIDJMS-334) - warning emitted by 32bit JVM during attempt to load 64bit Netty native epoll transport

## Tasks

 - [QPIDJMS-318](https://issues.apache.org/jira/browse/QPIDJMS-318) - Update Netty to 4.1.16.Final
 - [QPIDJMS-329](https://issues.apache.org/jira/browse/QPIDJMS-329) - Update to Mockito 2.10.0
 - [QPIDJMS-333](https://issues.apache.org/jira/browse/QPIDJMS-333) - update ActiveMQ test dependency to 5.15.1