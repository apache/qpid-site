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

# Qpid ProtonJ2 1.0.0-M11 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2636](https://issues.apache.org/jira/browse/PROTON-2636) - [protonj2] Allow the awaitAccepted API to work with transactional states
 - [PROTON-2637](https://issues.apache.org/jira/browse/PROTON-2637) - [protonj2] Performance improvements for the codec

## Bugs fixed

 - [PROTON-2646](https://issues.apache.org/jira/browse/PROTON-2646) - [protonj2] Message not sent with multiple senders on the same session

## Tasks

 - [PROTON-2634](https://issues.apache.org/jira/browse/PROTON-2634) - [protonj2] Update some javadocs with additional details and fix typos
 - [PROTON-2635](https://issues.apache.org/jira/browse/PROTON-2635) - [protonj2] Add additional tests to fill coverage gaps