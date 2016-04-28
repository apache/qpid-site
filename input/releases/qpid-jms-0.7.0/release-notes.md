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

# Qpid JMS 0.7.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 1.1 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-121](https://issues.apache.org/jira/browse/QPIDJMS-121) - add ability to send different AMQP dispositions when using client-acknowledge mode
 - [QPIDJMS-122](https://issues.apache.org/jira/browse/QPIDJMS-122) - Profile performance and investigate improvements 
 - [QPIDJMS-125](https://issues.apache.org/jira/browse/QPIDJMS-125) - Refactor the local transaction context for better thread safety and failover support
 - [QPIDJMS-127](https://issues.apache.org/jira/browse/QPIDJMS-127) - Throw an exception if a connection URI contains the User-Info section
 - [QPIDJMS-133](https://issues.apache.org/jira/browse/QPIDJMS-133) - Rename option alwaysSyncSend to forceSyncSend and deprecate the old option
 - [QPIDJMS-134](https://issues.apache.org/jira/browse/QPIDJMS-134) - Rename option sendAcksAsync to forceAsyncAcks and deprecate the old option
 - [QPIDJMS-135](https://issues.apache.org/jira/browse/QPIDJMS-135) - Add AutoCloseable to the JMS implementations 
 - [QPIDJMS-142](https://issues.apache.org/jira/browse/QPIDJMS-142) - Clean up the IdGenerator used to create ID values for JMS resources
 - [QPIDJMS-144](https://issues.apache.org/jira/browse/QPIDJMS-144) - Transport resources need to be more proactively cleaned up on failed operations.
 - [QPIDJMS-145](https://issues.apache.org/jira/browse/QPIDJMS-145) - update proton-j dependency to 0.11.1

## Bugs fixed

 - [QPIDJMS-123](https://issues.apache.org/jira/browse/QPIDJMS-123) - Potential thread safety issue in the QueueBrowser implementation 
 - [QPIDJMS-126](https://issues.apache.org/jira/browse/QPIDJMS-126) - Handle tx coordinator link being closed by the transactional resource
 - [QPIDJMS-130](https://issues.apache.org/jira/browse/QPIDJMS-130) - clearing the properties of a received message should make them writable again
 - [QPIDJMS-136](https://issues.apache.org/jira/browse/QPIDJMS-136) - use System.nanoTime() when deriving time to tick the transport with for idle-timeout handling
 - [QPIDJMS-139](https://issues.apache.org/jira/browse/QPIDJMS-139) - Message flow to synchronous consumer from Qpid Java broker unexpectedly ceases
 - [QPIDJMS-140](https://issues.apache.org/jira/browse/QPIDJMS-140) - JmsMessage.copy method incorrectly assigns readOnlyBody to readOnlyProperties

## Tasks

 - [QPIDJMS-137](https://issues.apache.org/jira/browse/QPIDJMS-137) - handle the detach frame not arriving after attach response indicating link refusal