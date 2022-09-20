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

# Qpid JMS 2.1.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-571](https://issues.apache.org/jira/browse/QPIDJMS-571) - update to jakarta.jms-api 3.1.0 / Jakarta Messaging 3.1

## Bugs fixed

 - [QPIDJMS-572](https://issues.apache.org/jira/browse/QPIDJMS-572) - The internal Netty ReadableBuffer wrapper read string API not advancing position index

## Tasks

 - [QPIDJMS-570](https://issues.apache.org/jira/browse/QPIDJMS-570) - Update Netty to 4.1.82.Final
 - [QPIDJMS-576](https://issues.apache.org/jira/browse/QPIDJMS-576) - update to apache parent pom 27
 - [QPIDJMS-577](https://issues.apache.org/jira/browse/QPIDJMS-577) - test dependency updates
 - [QPIDJMS-578](https://issues.apache.org/jira/browse/QPIDJMS-578) - update maven-bundle-plugin to 5.1.8
 - [QPIDJMS-579](https://issues.apache.org/jira/browse/QPIDJMS-579) - update to proton-j 0.34.0
 - [QPIDJMS-580](https://issues.apache.org/jira/browse/QPIDJMS-580) - remove various .js dependencies from javadoc output