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

# Qpid ProtonJ2 1.0.0-M13 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-2681](https://issues.apache.org/jira/browse/PROTON-2681) - [protonj2] Add ability to assign a linked resource to a SASLContext
 - [PROTON-2682](https://issues.apache.org/jira/browse/PROTON-2682) - [protonj2] Add deffered writes to AMQP test peer API
 - [PROTON-2683](https://issues.apache.org/jira/browse/PROTON-2683) - [protonj2] Add some convenience methods in the SASL APIs 
 - [PROTON-2685](https://issues.apache.org/jira/browse/PROTON-2685) - [protonj2] Add some convenience methods in the Symbol APIs
 - [PROTON-2686](https://issues.apache.org/jira/browse/PROTON-2686) - [protonj2] Improve API docs and some minor cleanups
 - [PROTON-2692](https://issues.apache.org/jira/browse/PROTON-2692) - [protonj2] Add API to scan encoded types for specific byte encodings
 - [PROTON-2693](https://issues.apache.org/jira/browse/PROTON-2693) - [protonj2] Add API to buffer to expose native address if the underlying buffer supports it
 - [PROTON-2694](https://issues.apache.org/jira/browse/PROTON-2694) - [protonj2] AMQP test peer should support both Netty 4 and 5

## Bugs fixed

 - [PROTON-2697](https://issues.apache.org/jira/browse/PROTON-2697) - Receiver.receive() throws java.lang.IllegalArgumentException: timeout value is negative

## Tasks

 - [PROTON-2670](https://issues.apache.org/jira/browse/PROTON-2670) - [protonj2] Update Netty to latest release
 - [PROTON-2671](https://issues.apache.org/jira/browse/PROTON-2671) - [protonj2] Update project test dependencies to latest