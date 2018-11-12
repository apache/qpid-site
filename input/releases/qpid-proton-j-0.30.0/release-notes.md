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

# Qpid Proton-J 0.30.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1925](https://issues.apache.org/jira/browse/PROTON-1925) - Add some enums to Section and DeliveryState to make type determination simpler
 - [PROTON-1941](https://issues.apache.org/jira/browse/PROTON-1941) - Add WritableBuffer API for requesting space when writing complex types
 - [PROTON-1948](https://issues.apache.org/jira/browse/PROTON-1948) - Refactor FrameWriter to avoid reencodes when buffer space is insufficient
 - [PROTON-1961](https://issues.apache.org/jira/browse/PROTON-1961) - Improve codec performance for certain common encoding operations

## Bugs fixed

 - [PROTON-1938](https://issues.apache.org/jira/browse/PROTON-1938) - misaligned Transport set/getErrorCondition and closed() behaviour
 - [PROTON-1958](https://issues.apache.org/jira/browse/PROTON-1958) - incorrect ordering for reactor timer tasks with matching deadlines