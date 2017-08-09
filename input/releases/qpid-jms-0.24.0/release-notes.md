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

# Qpid JMS 0.24.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-303](https://issues.apache.org/jira/browse/QPIDJMS-303) - Add support for SASL GSSAPI Kerberos mechanism
 - [QPIDJMS-304](https://issues.apache.org/jira/browse/QPIDJMS-304) - Cleanup the Session handling of its executor thread tracking
 - [QPIDJMS-306](https://issues.apache.org/jira/browse/QPIDJMS-306) - Use a more fitting data structure for inbound message queue

## Bugs fixed

 - [QPIDJMS-293](https://issues.apache.org/jira/browse/QPIDJMS-293) - the WebSocket transport does not handle continuation frames
 - [QPIDJMS-294](https://issues.apache.org/jira/browse/QPIDJMS-294) - The SCRAM-SHA-* SASL mechanisms should verify the server final message if it is sent in the additional-data field of sasl-outcome
 - [QPIDJMS-299](https://issues.apache.org/jira/browse/QPIDJMS-299) - executor thread factories can retain closed connection objects due to implicit parent references
 - [QPIDJMS-300](https://issues.apache.org/jira/browse/QPIDJMS-300) - Possible thread leak on simultaneous local and remote connection close
 - [QPIDJMS-301](https://issues.apache.org/jira/browse/QPIDJMS-301) - Pooled Buffer leak possible on send when connection has dropped
 - [QPIDJMS-302](https://issues.apache.org/jira/browse/QPIDJMS-302) - an NPE can occur when trying to throw a JMSException to indicate the connection failed
 - [QPIDJMS-305](https://issues.apache.org/jira/browse/QPIDJMS-305) - Potential race on sasl authentication failures can throw wrong exception on connect
 - [QPIDJMS-307](https://issues.apache.org/jira/browse/QPIDJMS-307) - fix handling of tx declare rejection while creating a transacted Session

## Tasks

 - [QPIDJMS-308](https://issues.apache.org/jira/browse/QPIDJMS-308) - update to proton-j 0.20.0
 - [QPIDJMS-309](https://issues.apache.org/jira/browse/QPIDJMS-309) - Update the ActiveMQ version used in tests to 5.15.0
 - [QPIDJMS-310](https://issues.apache.org/jira/browse/QPIDJMS-310) - Update Netty to latest 4.1.14.Final