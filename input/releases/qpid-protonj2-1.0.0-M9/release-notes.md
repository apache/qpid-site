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

# Qpid ProtonJ2 1.0.0-M9 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2593](https://issues.apache.org/jira/browse/PROTON-2593) - [protonj2] Add additional tests for split frame decoding
 - [PROTON-2599](https://issues.apache.org/jira/browse/PROTON-2599) - [protonj2] Reduce creation of temporary object during receive and send processing
 - [PROTON-2600](https://issues.apache.org/jira/browse/PROTON-2600) - [protonj2] Fix potential leak of tracked delivery in a session
 - [PROTON-2601](https://issues.apache.org/jira/browse/PROTON-2601) - [protonj2] Add the possibility the set custom TagGenerator in the client sender
 - [PROTON-2603](https://issues.apache.org/jira/browse/PROTON-2603) - [protonj2] Improve the encoding performance of the client sender

## Tasks

 - [PROTON-2598](https://issues.apache.org/jira/browse/PROTON-2598) - [protonj2] Update apache parent pom to v27
 - [PROTON-2606](https://issues.apache.org/jira/browse/PROTON-2606) - remove various .js dependencies from javadoc output
 - [PROTON-2607](https://issues.apache.org/jira/browse/PROTON-2607) - [protonj2] Update Netty to latest release
 - [PROTON-2608](https://issues.apache.org/jira/browse/PROTON-2608) - [protonj2] update project test dependencies to latest
 - [PROTON-2610](https://issues.apache.org/jira/browse/PROTON-2610) - [protonj2] fix some javadoc warnings and add missing tags