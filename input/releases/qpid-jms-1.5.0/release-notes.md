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

# Qpid JMS 1.5.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## Bugs fixed

 - [QPIDJMS-557](https://issues.apache.org/jira/browse/QPIDJMS-557) - ocassional connection failure log despite successfull requested connection closure

## Tasks

 - [QPIDJMS-558](https://issues.apache.org/jira/browse/QPIDJMS-558) - use slf4j-simple for tests and examples
 - [QPIDJMS-559](https://issues.apache.org/jira/browse/QPIDJMS-559) - update to slf4j 1.7.32

**Note**: QPIDJMS-558 updated the tests and examples to use slf4j-simple going forward rather than Log4J. The qpid-jms-client itself continues not have any compile or runtime dependency on Log4J or provide it transitively, so using the qpid-jms-client maven module would not have resulted in use of Log4J. It was however previously used in the tests and client examples in the download archives. Log4J was also included in the "lib/optional" directory within the apache-qpid-jms-&lt;version&gt;-bin.tar.gz convenience download, though wouldnt have been used unless you manually added it to your application classpath to do so.
