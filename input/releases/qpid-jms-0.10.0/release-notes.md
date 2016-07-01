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

# Qpid JMS 0.10.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 1.1 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-131](https://issues.apache.org/jira/browse/QPIDJMS-131) - Provide for finer grained control over sending of messages as presettled.
 - [QPIDJMS-173](https://issues.apache.org/jira/browse/QPIDJMS-173) - Provide for finer grained control over automatic presettling of received messages
 - [QPIDJMS-175](https://issues.apache.org/jira/browse/QPIDJMS-175) - Add support for a timeout value for drain requests.
 - [QPIDJMS-176](https://issues.apache.org/jira/browse/QPIDJMS-176) - Cleanup creation of the anonymous fallback producer when remote does not support anonymous relay.
 - [QPIDJMS-177](https://issues.apache.org/jira/browse/QPIDJMS-177) - Make the policy objects used in the client more extensable and give more control over their controlled  behaviors
 - [QPIDJMS-185](https://issues.apache.org/jira/browse/QPIDJMS-185) - update to Proton 0.13.0
 - [QPIDJMS-188](https://issues.apache.org/jira/browse/QPIDJMS-188) - Further ObjectMessage improvements

## Bugs fixed

 - [QPIDJMS-172](https://issues.apache.org/jira/browse/QPIDJMS-172) - Potential NPE in Failover error handling
 - [QPIDJMS-178](https://issues.apache.org/jira/browse/QPIDJMS-178) - ObjectMessage does not always snapshot the store value
 - [QPIDJMS-179](https://issues.apache.org/jira/browse/QPIDJMS-179) - The internal ID generator is appending an extra ':' value to ID prefixes
 - [QPIDJMS-182](https://issues.apache.org/jira/browse/QPIDJMS-182) - TransportOptions and TransportSslOptions clone methods are incomplete
 - [QPIDJMS-184](https://issues.apache.org/jira/browse/QPIDJMS-184) - JMS Selector parsing will not fail if a valid selector is followed by invalid text

## Tasks

 - [QPIDJMS-171](https://issues.apache.org/jira/browse/QPIDJMS-171) - Remove configuration options that were deprecated in 0.7.0
 - [QPIDJMS-174](https://issues.apache.org/jira/browse/QPIDJMS-174) - Update ActiveMQ dependency to 5.13.3