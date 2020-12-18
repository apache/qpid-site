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

# Qpid JMS 0.56.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-522](https://issues.apache.org/jira/browse/QPIDJMS-522) - add toggle for controlling the local validation of message selector strings

## Bugs fixed

 - [QPIDJMS-521](https://issues.apache.org/jira/browse/QPIDJMS-521) - ExceptionListener fired due to async dispatch failure is unable to close the Session/Connection

## Tasks

 - [QPIDJMS-523](https://issues.apache.org/jira/browse/QPIDJMS-523) - update to Netty 4.1.55
 - [QPIDJMS-524](https://issues.apache.org/jira/browse/QPIDJMS-524) - Update log4j-slf4j version to 2.14.0 and Mockito to 3.6.28