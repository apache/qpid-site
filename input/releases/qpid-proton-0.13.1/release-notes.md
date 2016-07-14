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

# Qpid Proton 0.13.1 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).

**Note**: This release addresses a security vulnerability,
CVE-2016-4467, via PROTON-1228 and PROTON-1233.

## New features and improvements

 - [PROTON-1248](https://issues.apache.org/jira/browse/PROTON-1248) - There is no way to query the state of deliveries or trackers

## Bugs fixed

 - [PROTON-1233](https://issues.apache.org/jira/browse/PROTON-1233) - Windows schannel: match OpenSSL and require non-null hostname for PN_SSL_VERIFY_PEER_NAME
 - [PROTON-1235](https://issues.apache.org/jira/browse/PROTON-1235) - C Reactor: connection fails if hostname with no port is used for transport address
 - [PROTON-1236](https://issues.apache.org/jira/browse/PROTON-1236) - Reactor - segfault if connection address cannot be resolved
 - [PROTON-1247](https://issues.apache.org/jira/browse/PROTON-1247) - Link errors when using proton::delivery::accept(), ...::reject() etc.
 - [PROTON-1249](https://issues.apache.org/jira/browse/PROTON-1249) - proton-j: unsafe type initialisations
