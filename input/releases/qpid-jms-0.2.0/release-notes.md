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

# Qpid JMS 0.2.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 1.1 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-35](https://issues.apache.org/jira/browse/QPIDJMS-35) - allow specifying a particular alias to use when selecting a keystore entry for client auth
 - [QPIDJMS-36](https://issues.apache.org/jira/browse/QPIDJMS-36) - ensure different link names for consumers and producers on the same Session
 - [QPIDJMS-37](https://issues.apache.org/jira/browse/QPIDJMS-37) - upgrade to Proton 0.9.1
 - [QPIDJMS-38](https://issues.apache.org/jira/browse/QPIDJMS-38) - updates to SSL/TLS configuration and/or handling
 - [QPIDJMS-44](https://issues.apache.org/jira/browse/QPIDJMS-44) - Add support for dealing with Connection redirections
 - [QPIDJMS-45](https://issues.apache.org/jira/browse/QPIDJMS-45) - add support for idle-timeout handling
 - [QPIDJMS-46](https://issues.apache.org/jira/browse/QPIDJMS-46) - Cleanup and improve the Discovery module code
 - [QPIDJMS-47](https://issues.apache.org/jira/browse/QPIDJMS-47) - add basic logging documentation, supply optional dep in binary for examples
 - [QPIDJMS-50](https://issues.apache.org/jira/browse/QPIDJMS-50) - upgrade to SLF4J 1.7.12

## Bugs fixed

 - [QPIDJMS-33](https://issues.apache.org/jira/browse/QPIDJMS-33) - SASL EXTERNAL doesn't seem to work against the C++ broker
 - [QPIDJMS-34](https://issues.apache.org/jira/browse/QPIDJMS-34) - a warning is logged when connecting for each unknown server SASL mechanism
 - [QPIDJMS-39](https://issues.apache.org/jira/browse/QPIDJMS-39) - transport.enabledCipherSuites option seems to be ignored / not used
 - [QPIDJMS-40](https://issues.apache.org/jira/browse/QPIDJMS-40) - When link is closed, the exceptions do not contain errors which caused the link detach
 - [QPIDJMS-41](https://issues.apache.org/jira/browse/QPIDJMS-41) - JMS Producer needs to ensure that it settles outbound deliveries after remote
 - [QPIDJMS-42](https://issues.apache.org/jira/browse/QPIDJMS-42) - When amqps connection fails, the program never exits?
 - [QPIDJMS-43](https://issues.apache.org/jira/browse/QPIDJMS-43) - QueueBrowser should not participate in session transactions