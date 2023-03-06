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

# Qpid Proton-J 0.34.1 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [PROTON-2687](https://issues.apache.org/jira/browse/PROTON-2687) - [proton-j] stale entries can stick in transport work list upon freeing session with outstanding deliveries
 - [PROTON-2688](https://issues.apache.org/jira/browse/PROTON-2688) - [proton-j] stale entries can stick in transport work list upon freeing sender with buffered delivery

## Tasks

 - [PROTON-2605](https://issues.apache.org/jira/browse/PROTON-2605) - remove various .js dependencies from javadoc output