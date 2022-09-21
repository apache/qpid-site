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

# Qpid JMS 1.6.0 Release Notes

Qpid JMS is a complete [Jakarta Messaging](https://jakarta.ee/specifications/messaging/) 2.0
client built using the [Qpid Proton]({{site_url}}/proton/index.html) protocol engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [QPIDJMS-553](https://issues.apache.org/jira/browse/QPIDJMS-553) - add option to use shared Netty event loop group

## Tasks

 - [QPIDJMS-560](https://issues.apache.org/jira/browse/QPIDJMS-560) - Avoid unnecessary cast when throwing IllegalArgumentException
 - [QPIDJMS-561](https://issues.apache.org/jira/browse/QPIDJMS-561) - update test dependencies
 - [QPIDJMS-562](https://issues.apache.org/jira/browse/QPIDJMS-562) - Update to Netty 4.1.75
 - [QPIDJMS-564](https://issues.apache.org/jira/browse/QPIDJMS-564) - Update to SLF4J 1.7.36
 - [QPIDJMS-566](https://issues.apache.org/jira/browse/QPIDJMS-566) - Replace org.apache.geronimo.specs:geronimo-jms_2.0_spec with vendor neutral jakarta.jms:jakarta.jms-api