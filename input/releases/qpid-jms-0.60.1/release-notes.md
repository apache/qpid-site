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

# Qpid JMS 0.60.1 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-542](https://issues.apache.org/jira/browse/QPIDJMS-542) - Support configuring default ConnectionFactory via the naming provider url property

## Bugs fixed

 - [QPIDJMS-544](https://issues.apache.org/jira/browse/QPIDJMS-544) - JmsDefaultPrefetchPolicy#getMaxPrefetchLimit logs incorrect MAX_PREFETCH_SIZE
 - [QPIDJMS-549](https://issues.apache.org/jira/browse/QPIDJMS-549) - NPE logged during failover after remote close during connection creation

## Tasks

 - [QPIDJMS-546](https://issues.apache.org/jira/browse/QPIDJMS-546) - update test dependencies
 - [QPIDJMS-551](https://issues.apache.org/jira/browse/QPIDJMS-551) - update to proton-j 0.33.10
 - [QPIDJMS-555](https://issues.apache.org/jira/browse/QPIDJMS-555) - update to Netty 4.1.72
 - [QPIDJMS-556](https://issues.apache.org/jira/browse/QPIDJMS-556) - update test/examples dependencies

**Note**: QPIDJMS-556 updated from Log4J 2.14.1 to 2.16.0 to pick up its fixes for CVE-2021-44228 and CVE-2021-45046. The qpid-jms-client itself does not have any compile or runtime dependency on Log4J or provide it transitively, so using the qpid-jms-client maven module does not result in use of Log4J. It is however used in the tests and as an example logging framework in the client examples in the download archives. Log4J is also included in the "lib/optional" directory within the apache-qpid-jms-&lt;version&gt;-bin.tar.gz convenience download, though wont be used unless you manually add it to your application classpath to do so. See the [Log4J 2 security page](https://logging.apache.org/log4j/2.x/security.html) for more details of the issues themselves.
