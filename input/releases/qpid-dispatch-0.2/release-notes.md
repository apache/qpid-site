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

# Qpid Dispatch 0.2 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-15](https://issues.apache.org/jira/browse/DISPATCH-15) - Add different forwarding semantics for addresses
 - [DISPATCH-22](https://issues.apache.org/jira/browse/DISPATCH-22) - Reduce the time to detect loss of neighbor
 - [DISPATCH-25](https://issues.apache.org/jira/browse/DISPATCH-25) - Man page updates for 0.2
 - [DISPATCH-28](https://issues.apache.org/jira/browse/DISPATCH-28) - Increase the length of the random portion of temporary addresses.

## Bugs fixed

 - [DISPATCH-17](https://issues.apache.org/jira/browse/DISPATCH-17) - Build system ignores user-defined CFLAGS
 - [DISPATCH-18](https://issues.apache.org/jira/browse/DISPATCH-18) - SSL inter-router connections seem to run in-the-clear
 - [DISPATCH-27](https://issues.apache.org/jira/browse/DISPATCH-27) - Intermittent test failures on RHEL platforms
 - [DISPATCH-29](https://issues.apache.org/jira/browse/DISPATCH-29) - Spurious Mobile Address Requests (MAR) when connecting to a remote router
 - [DISPATCH-30](https://issues.apache.org/jira/browse/DISPATCH-30) - Wrong test configuration files installed

## Tasks

<div class="none">None</div>