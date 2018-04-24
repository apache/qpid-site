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

# Qpid Proton-J 0.27.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1774](https://issues.apache.org/jira/browse/PROTON-1774) - performance improvements in sasl transport wrapper
 - [PROTON-1808](https://issues.apache.org/jira/browse/PROTON-1808) - FrameWriter allocates additional buffer capacity inefficiently
 - [PROTON-1811](https://issues.apache.org/jira/browse/PROTON-1811) - FrameWriter refactoring to reduce code on the hot path and reduce allocations of EmptyFrame
 - [PROTON-1828](https://issues.apache.org/jira/browse/PROTON-1828) - add ability to limit outgoing frame sizes
 - [PROTON-1829](https://issues.apache.org/jira/browse/PROTON-1829) - adjust fallback sizing for internal buffers

## Bugs fixed

 - [PROTON-1672](https://issues.apache.org/jira/browse/PROTON-1672) - Large deliveries comprising many transfers are handled inefficiently