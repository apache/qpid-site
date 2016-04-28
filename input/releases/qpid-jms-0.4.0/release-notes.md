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

# Qpid JMS 0.4.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 1.1 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-68](https://issues.apache.org/jira/browse/QPIDJMS-68) - add support for not using a SASL layer
 - [QPIDJMS-69](https://issues.apache.org/jira/browse/QPIDJMS-69) - add support for configuring allowed SASL mechanism(s)
 - [QPIDJMS-74](https://issues.apache.org/jira/browse/QPIDJMS-74) - add useful details to the connection properties
 - [QPIDJMS-78](https://issues.apache.org/jira/browse/QPIDJMS-78) - document supported SASL mechanisms
 - [QPIDJMS-84](https://issues.apache.org/jira/browse/QPIDJMS-84) - update proton-j dependency to 0.10
 - [QPIDJMS-85](https://issues.apache.org/jira/browse/QPIDJMS-85) - ensure deliveries have state when settled during cleanup
 - [QPIDJMS-87](https://issues.apache.org/jira/browse/QPIDJMS-87) - make the local maxFrameSize value configurable
 - [QPIDJMS-88](https://issues.apache.org/jira/browse/QPIDJMS-88) - update examples readme to include details for users running on Windows

## Bugs fixed

 - [QPIDJMS-77](https://issues.apache.org/jira/browse/QPIDJMS-77) - update selection of default multicast discovery interface for consistency, and include trace logging of the process
 - [QPIDJMS-81](https://issues.apache.org/jira/browse/QPIDJMS-81) - the trace logging of initial idle-timeout task sheduling outputs wrong value
 - [QPIDJMS-83](https://issues.apache.org/jira/browse/QPIDJMS-83) - file watcher discovery agent fails on Windows if the watch interval is configured
 - [QPIDJMS-90](https://issues.apache.org/jira/browse/QPIDJMS-90) - Received empty frames are not logged