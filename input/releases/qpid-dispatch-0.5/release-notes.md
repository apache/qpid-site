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

# Qpid Dispatch 0.5 Release Notes

Dispatch is a lightweight AMQP message router library. More about
[Qpid Dispatch]({{site_url}}/components/dispatch-router/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [DISPATCH-98](https://issues.apache.org/jira/browse/DISPATCH-98) - Refactor the handling of Message Annotations
 - [DISPATCH-99](https://issues.apache.org/jira/browse/DISPATCH-99) - Allow override of the forwarding logic on a per-address basis.
 - [DISPATCH-101](https://issues.apache.org/jira/browse/DISPATCH-101) - Create a field iterator that is specific to handling address fields
 - [DISPATCH-121](https://issues.apache.org/jira/browse/DISPATCH-121) - Allow pool allocation to be switched for plain allocation at build time.
 - [DISPATCH-123](https://issues.apache.org/jira/browse/DISPATCH-123) - Separate target to build documentation.
 - [DISPATCH-136](https://issues.apache.org/jira/browse/DISPATCH-136) - qdstat -n doesn't show the local router in the list
 - [DISPATCH-145](https://issues.apache.org/jira/browse/DISPATCH-145) - Add identifying information to the properties map of the Open performative
 - [DISPATCH-149](https://issues.apache.org/jira/browse/DISPATCH-149) - Properly handle different detach/close scenarios for links
 - [DISPATCH-152](https://issues.apache.org/jira/browse/DISPATCH-152) - Expose SASL-related data via management
 - [DISPATCH-153](https://issues.apache.org/jira/browse/DISPATCH-153) - Expose full set of security capabilities via configuration

## Bugs fixed

 - [DISPATCH-110](https://issues.apache.org/jira/browse/DISPATCH-110) - Provide access to recent log messages via management agent.
 - [DISPATCH-131](https://issues.apache.org/jira/browse/DISPATCH-131) - Valgrind errors during the system tests are not reported
 - [DISPATCH-132](https://issues.apache.org/jira/browse/DISPATCH-132) - Time values overflow on 32 bit systems
 - [DISPATCH-133](https://issues.apache.org/jira/browse/DISPATCH-133) - Router Link use-after-free
 - [DISPATCH-134](https://issues.apache.org/jira/browse/DISPATCH-134) - Driver runs at 100% CPU intermittently
 - [DISPATCH-137](https://issues.apache.org/jira/browse/DISPATCH-137) - Dispatch Code should be updated to support newer SASL calls in qpid-proton
 - [DISPATCH-143](https://issues.apache.org/jira/browse/DISPATCH-143) - Link-routing - Various robustness problems
 - [DISPATCH-146](https://issues.apache.org/jira/browse/DISPATCH-146) - management query sends non string values
 - [DISPATCH-154](https://issues.apache.org/jira/browse/DISPATCH-154) - dispatch-router coredumps when connector address is unresolvable
 - [DISPATCH-167](https://issues.apache.org/jira/browse/DISPATCH-167) - Dispatch crashes running the 6-node test configuration