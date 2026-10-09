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

# Qpid ProtonJ2 1.4.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2963](https://issues.apache.org/jira/browse/PROTON-2963) - [protonj2] Improve handling of dispositions with ranges
 - [PROTON-2964](https://issues.apache.org/jira/browse/PROTON-2964) - [protonj2] Update netty to latest release

## Bugs fixed

 - [PROTON-2956](https://issues.apache.org/jira/browse/PROTON-2956) - [protonj2] Pooled delivery-tag generator emits duplicate tags when more than 256 tags are checked out
 - [PROTON-2982](https://issues.apache.org/jira/browse/PROTON-2982) - [protonj2] ProtonCompositeBufferImpl.copy() throws IndexOutOfBoundsException when the copied range starts in a non-first chunk

## Tasks

 - [PROTON-2965](https://issues.apache.org/jira/browse/PROTON-2965) - [protonj2] Update slf4j to latest release
 - [PROTON-2983](https://issues.apache.org/jira/browse/PROTON-2983) - [protonj2] Update mockito to latest release