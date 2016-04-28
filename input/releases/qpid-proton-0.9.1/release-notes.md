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

# Qpid Proton 0.9.1 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-857](https://issues.apache.org/jira/browse/PROTON-857) - reduce memory usage for the TransportSession link handle tracking

## Bugs fixed

 - [PROTON-843](https://issues.apache.org/jira/browse/PROTON-843) - proton-j: Transport advertises idle timeout as-is whereas proton-c halves it before
 - [PROTON-844](https://issues.apache.org/jira/browse/PROTON-844) - proton-j: ArrayIndexOutOfBounds exception if remote peer sends a handle &gt;1024
 - [PROTON-845](https://issues.apache.org/jira/browse/PROTON-845) - Proton-J: Potential NPE in proton-jms outbound native transformer
 - [PROTON-848](https://issues.apache.org/jira/browse/PROTON-848) - [proton-j] TransportSession state is never discarded
 - [PROTON-849](https://issues.apache.org/jira/browse/PROTON-849) - [proton-j] TransportLink state is never discarded
 - [PROTON-850](https://issues.apache.org/jira/browse/PROTON-850) - inconsistent state when reusing link name
 - [PROTON-853](https://issues.apache.org/jira/browse/PROTON-853) - [proton-j] the transport emitted a new attach frame for a link in the process of being closed
 - [PROTON-854](https://issues.apache.org/jira/browse/PROTON-854) - [proton-j] ConnectionImpl retains all created Sessions until the Connection is freed