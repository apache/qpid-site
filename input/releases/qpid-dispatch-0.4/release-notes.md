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

# Qpid Dispatch 0.4 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-6](https://issues.apache.org/jira/browse/DISPATCH-6) - Implement link-routing
 - [DISPATCH-97](https://issues.apache.org/jira/browse/DISPATCH-97) - Router Engine Redesign
 - [DISPATCH-100](https://issues.apache.org/jira/browse/DISPATCH-100) - Accelerate the router-advert interval during topology fluctuations
 - [DISPATCH-102](https://issues.apache.org/jira/browse/DISPATCH-102) - Provide qdrouter schema via management interface
 - [DISPATCH-108](https://issues.apache.org/jira/browse/DISPATCH-108) - Identify settable,  updatable and read-only attributes in management schema.
 - [DISPATCH-109](https://issues.apache.org/jira/browse/DISPATCH-109) - Support parsing of the Subject field from the message properties
 - [DISPATCH-125](https://issues.apache.org/jira/browse/DISPATCH-125) - Convert documentation to rst, generate book and HTML man pages from sphinx.
 - [DISPATCH-128](https://issues.apache.org/jira/browse/DISPATCH-128) - Documentation updates for 0.4

## Bugs fixed

 - [DISPATCH-90](https://issues.apache.org/jira/browse/DISPATCH-90) - Routing table is corrupt after a router quickly restarts
 - [DISPATCH-96](https://issues.apache.org/jira/browse/DISPATCH-96) - Installing qpid_dispatch_site and qpid_dispatch/management does not work with "make DESTDIR"
 - [DISPATCH-106](https://issues.apache.org/jira/browse/DISPATCH-106) - pn link corruption after router restart
 - [DISPATCH-107](https://issues.apache.org/jira/browse/DISPATCH-107) - Links are not detached if the remote ends the session prematurely
 - [DISPATCH-112](https://issues.apache.org/jira/browse/DISPATCH-112) - Router fails with duplicate link ID errors.
 - [DISPATCH-114](https://issues.apache.org/jira/browse/DISPATCH-114) - SSL configuration fails to translate to proper internal names
 - [DISPATCH-116](https://issues.apache.org/jira/browse/DISPATCH-116) - Qpid dispatch management tools do not use SSL and SASL correctly.
 - [DISPATCH-117](https://issues.apache.org/jira/browse/DISPATCH-117) - SEG Fault when outgoing SSL connections fail
 - [DISPATCH-118](https://issues.apache.org/jira/browse/DISPATCH-118) - crash due to race on proton-c/src/error.c  error structures.
 - [DISPATCH-122](https://issues.apache.org/jira/browse/DISPATCH-122) - Message annotations are not indexed by Symbol types
 - [DISPATCH-124](https://issues.apache.org/jira/browse/DISPATCH-124) - Error handling when SSL is not available.
 - [DISPATCH-130](https://issues.apache.org/jira/browse/DISPATCH-130) - qdrouterd with --daemon and --user options does not dump core.