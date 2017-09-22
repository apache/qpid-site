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

# Qpid JMS 0.25.0 Release Notes

Qpid JMS is a complete [Java Message Service][jms] 2.0 client built
using the [Qpid Proton]({{site_url}}/proton/index.html) protocol
engine.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

[jms]: http://en.wikipedia.org/wiki/Java_Message_Service


## New features and improvements

 - [QPIDJMS-315](https://issues.apache.org/jira/browse/QPIDJMS-315) - Add support for Netty KQueue transport
 - [QPIDJMS-317](https://issues.apache.org/jira/browse/QPIDJMS-317) - Performance improvements for transfer tag cache
 - [QPIDJMS-319](https://issues.apache.org/jira/browse/QPIDJMS-319) - Remove uneeded buffer duplication on incoming deliveries
 - [QPIDJMS-321](https://issues.apache.org/jira/browse/QPIDJMS-321) - pre-size the inbound message queue
 - [QPIDJMS-323](https://issues.apache.org/jira/browse/QPIDJMS-323) - improve exception message when no SASL mechanism can be negotiated

## Bugs fixed

 - [QPIDJMS-312](https://issues.apache.org/jira/browse/QPIDJMS-312) - Exception is not thrown when user attempts to create context with invalid session mode value
 - [QPIDJMS-320](https://issues.apache.org/jira/browse/QPIDJMS-320) - selector parser LRU cache isn't thread safe
 - [QPIDJMS-322](https://issues.apache.org/jira/browse/QPIDJMS-322) - handle edge cases when driving transport#tick(now) with nanoTime derived values

## Tasks

 - [QPIDJMS-311](https://issues.apache.org/jira/browse/QPIDJMS-311) - Enable building and testing on JDK 9
 - [QPIDJMS-316](https://issues.apache.org/jira/browse/QPIDJMS-316) - set up Travis CI to test on OSX and Linux
 - [QPIDJMS-324](https://issues.apache.org/jira/browse/QPIDJMS-324) - update to proton-j 0.22.0