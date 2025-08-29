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

# Qpid ProtonJ2 1.0.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2885](https://issues.apache.org/jira/browse/PROTON-2885) - [protonj2] Improve test driver offered and desored capabilities matcher
 - [PROTON-2894](https://issues.apache.org/jira/browse/PROTON-2894) - [protonj2] Add a peek ahead API to the buffer API to simplify codecs
 - [PROTON-2899](https://issues.apache.org/jira/browse/PROTON-2899) - [protonj2] Update code to better support Netty 4.2.x
 - [PROTON-2901](https://issues.apache.org/jira/browse/PROTON-2901) - [protonj2] Improve test peer handling of expect and send JMS selectors and no-local
 - [PROTON-2902](https://issues.apache.org/jira/browse/PROTON-2902) - [protonj2] Add convenience API for adding filters to source options

## Bugs fixed

 - [PROTON-2880](https://issues.apache.org/jira/browse/PROTON-2880) - [protonj2] UnsettledMap iterator can become out of sync with contents
 - [PROTON-2900](https://issues.apache.org/jira/browse/PROTON-2900) - [protonj2] `IdleTimeoutCheck` not rescheduled after broker's AMQP Open frame, causing premature connection closure

## Tasks

 - [PROTON-2876](https://issues.apache.org/jira/browse/PROTON-2876) - [protonj2] Update test dependencies to latest
 - [PROTON-2877](https://issues.apache.org/jira/browse/PROTON-2877) - [protonj2] Update Netty dependencies to latest
 - [PROTON-2878](https://issues.apache.org/jira/browse/PROTON-2878) - [protonj2] Update slf4j dependencies to latest
 - [PROTON-2887](https://issues.apache.org/jira/browse/PROTON-2887) - [protonj2] Perform some minor code cleanups from analysis