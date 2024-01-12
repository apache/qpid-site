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

# Qpid ProtonJ2 1.0.0-M19 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2780](https://issues.apache.org/jira/browse/PROTON-2780) - [protonj2] Improve test stability under slow CI conditions
 - [PROTON-2781](https://issues.apache.org/jira/browse/PROTON-2781) - [protonj2] Clean up some code and API docs in the SASL layer
 - [PROTON-2784](https://issues.apache.org/jira/browse/PROTON-2784) - [protonj2] Improve test peer completion handling when connection drops

## Bugs fixed

 - [PROTON-2783](https://issues.apache.org/jira/browse/PROTON-2783) - [protonj2] Test driver expect for connection drop can hang script

## Tasks

 - [PROTON-2778](https://issues.apache.org/jira/browse/PROTON-2778) - [protonj2] Update test dependencies to latest releases
 - [PROTON-2779](https://issues.apache.org/jira/browse/PROTON-2779) - [protonj2] Update Netty to latest release