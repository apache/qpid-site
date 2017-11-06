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

# Qpid JMS 0.27.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-338](https://issues.apache.org/jira/browse/QPIDJMS-338) - SSL configuration should support setting keyStoreType and trustStoreType independently
 - [QPIDJMS-339](https://issues.apache.org/jira/browse/QPIDJMS-339) - Allow setting keystore and truststore type from system properties

## Bugs fixed

 - [QPIDJMS-335](https://issues.apache.org/jira/browse/QPIDJMS-335) - SCRAM-SHA mechanism impls erroneously escape "=" and "," in the password during processing
 - [QPIDJMS-336](https://issues.apache.org/jira/browse/QPIDJMS-336) - Refine failover reconnect behavior
 - [QPIDJMS-340](https://issues.apache.org/jira/browse/QPIDJMS-340) - Build fails with group id is too big error
 - [QPIDJMS-342](https://issues.apache.org/jira/browse/QPIDJMS-342) - Missed connect error on start can lead to hung failover reconnect cycle
 - [QPIDJMS-344](https://issues.apache.org/jira/browse/QPIDJMS-344) - FailoverWithAmqpOpenProvidedServerListIntegrationTest sporadic test failures in CI

## Tasks

 - [QPIDJMS-341](https://issues.apache.org/jira/browse/QPIDJMS-341) - update to proton-j 0.23.0
 - [QPIDJMS-343](https://issues.apache.org/jira/browse/QPIDJMS-343) - Update testing dependencies (ActiveMQ and Mockito)