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

# Qpid JMS 0.9.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 1.1 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-150](https://issues.apache.org/jira/browse/QPIDJMS-150) - Scram SHA SASL support for authentication
 - [QPIDJMS-151](https://issues.apache.org/jira/browse/QPIDJMS-151) - Update build settings to depend only on specific netty modules needed
 - [QPIDJMS-152](https://issues.apache.org/jira/browse/QPIDJMS-152) - Reduce log noise from QueueBrowser on failed close of internal consumer
 - [QPIDJMS-156](https://issues.apache.org/jira/browse/QPIDJMS-156) - Improve the logs output for some JMS resources
 - [QPIDJMS-157](https://issues.apache.org/jira/browse/QPIDJMS-157) - Add support for send timeout and request timeout options
 - [QPIDJMS-159](https://issues.apache.org/jira/browse/QPIDJMS-159) - support producers having their existing credit drained
 - [QPIDJMS-161](https://issues.apache.org/jira/browse/QPIDJMS-161) - Update Proton to v0.12.1
 - [QPIDJMS-162](https://issues.apache.org/jira/browse/QPIDJMS-162) - Update ActiveMQ dependency to 5.13.2
 - [QPIDJMS-163](https://issues.apache.org/jira/browse/QPIDJMS-163) - support populating the user-id field on produced messages
 - [QPIDJMS-166](https://issues.apache.org/jira/browse/QPIDJMS-166) - Revisit some of the TODOs in the code around error messages and exception types.  
 - [QPIDJMS-168](https://issues.apache.org/jira/browse/QPIDJMS-168) - Fix various issues reported by FindBugs
 - [QPIDJMS-170](https://issues.apache.org/jira/browse/QPIDJMS-170) - Simplify the dispatching logic in the connection

## Bugs fixed

 - [QPIDJMS-154](https://issues.apache.org/jira/browse/QPIDJMS-154) - Failover mechanism does not handle connection URLs in a predictable way
 - [QPIDJMS-160](https://issues.apache.org/jira/browse/QPIDJMS-160) - The single non-daemon thread for the connection needs to be started on create.
 - [QPIDJMS-169](https://issues.apache.org/jira/browse/QPIDJMS-169) - SASL Plain Mechanism should be enforcing UTF-8 encoding

## Tasks

 - [QPIDJMS-158](https://issues.apache.org/jira/browse/QPIDJMS-158) - Update slf4j to latest release v1.7.21
 - [QPIDJMS-165](https://issues.apache.org/jira/browse/QPIDJMS-165) - document behaviour around TLS SNI