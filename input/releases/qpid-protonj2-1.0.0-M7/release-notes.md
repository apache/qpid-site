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

# Qpid ProtonJ2 1.0.0-M7 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2564](https://issues.apache.org/jira/browse/PROTON-2564) - [protonj2] Reduce memory allocations in codec and client API
 - [PROTON-2571](https://issues.apache.org/jira/browse/PROTON-2571) - [protonj2] Prevent multiple transport flush operation inside a single read

## Bugs fixed

 - [PROTON-2569](https://issues.apache.org/jira/browse/PROTON-2569) - [protonj2] Add tests and fix some issue with client options type clone API

## Tasks

 - [PROTON-2565](https://issues.apache.org/jira/browse/PROTON-2565) - [protonj2] Update netty and tcnative to latest releases
 - [PROTON-2572](https://issues.apache.org/jira/browse/PROTON-2572) - [protonj2] Update mockito to latest release