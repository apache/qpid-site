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

# Qpid Proton-J 0.31.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1963](https://issues.apache.org/jira/browse/PROTON-1963) - Improve performance of the codec for certain common encoding operations
 - [PROTON-1965](https://issues.apache.org/jira/browse/PROTON-1965) - Optimize CompositeReadableBuffer::equals on single chunk spans
 - [PROTON-1967](https://issues.apache.org/jira/browse/PROTON-1967) - Reduce garbage created in the Transport layer

## Bugs fixed

 - [PROTON-1966](https://issues.apache.org/jira/browse/PROTON-1966) - CompositeReadableBuffer#equals() can affect position for some content mismatches
 - [PROTON-1972](https://issues.apache.org/jira/browse/PROTON-1972) - test failures with TLS 1.3 / Java 11

## Tasks

 - [PROTON-1971](https://issues.apache.org/jira/browse/PROTON-1971) - update parent pom, plugins, and test dependencies