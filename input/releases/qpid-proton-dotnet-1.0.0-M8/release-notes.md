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

# Qpid Proton Dotnet 1.0.0-M8 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2721](https://issues.apache.org/jira/browse/PROTON-2721) - [proton-dotnet] Add implicit conversions for Symbol type

## Bugs fixed

 - [PROTON-2720](https://issues.apache.org/jira/browse/PROTON-2720) - [proton-dotnet] virtual host connection option not applied correctly
 - [PROTON-2722](https://issues.apache.org/jira/browse/PROTON-2722) - [proton-dotnet] Concurrency issue in NextReceiver and Receiver delivery count API

## Tasks

 - [PROTON-2672](https://issues.apache.org/jira/browse/PROTON-2672) - [proton-dotnet] Fix some tests that fail when CI boxes are loaded
 - [PROTON-2723](https://issues.apache.org/jira/browse/PROTON-2723) - [proton-dotnet] Update some build and test dependencies to latest
 - [PROTON-2726](https://issues.apache.org/jira/browse/PROTON-2726) - [proton-dotnet] v1.0.0-M8 release tasks