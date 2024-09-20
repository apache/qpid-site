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

# Qpid ProtonJ2 1.0.0-M22 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2841](https://issues.apache.org/jira/browse/PROTON-2841) - [protonj2] Add support for enabling WebSocket compression
 - [PROTON-2845](https://issues.apache.org/jira/browse/PROTON-2845) - [protonj2] Improve test peer API for transferring messages and dispositions

## Bugs fixed

 - [PROTON-2847](https://issues.apache.org/jira/browse/PROTON-2847) - [protonj2] Notifications executor is not closed in ClientConnection
 - [PROTON-2849](https://issues.apache.org/jira/browse/PROTON-2849) - [protonj2] ClientRejected returns released type

## Tasks

 - [PROTON-2840](https://issues.apache.org/jira/browse/PROTON-2840) - [protonj2] Update Netty to latest release
 - [PROTON-2846](https://issues.apache.org/jira/browse/PROTON-2846) - [protonj2] Update test dependencies to latest releases
 - [PROTON-2850](https://issues.apache.org/jira/browse/PROTON-2850) - [protonj2] Fix some sporadic test failures