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

# Qpid Proton 0.24.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1354](https://issues.apache.org/jira/browse/PROTON-1354) - Disable problematic SASL mechanisms if they are not explicitly enabled
 - [PROTON-1683](https://issues.apache.org/jira/browse/PROTON-1683) - support static library output
 - [PROTON-1848](https://issues.apache.org/jira/browse/PROTON-1848) - [Python] Update to only support versions 2.6, 2.7 and 3.3 onwards
 - [PROTON-1850](https://issues.apache.org/jira/browse/PROTON-1850) - [Python] Split up monolithic proton __init__.py
 - [PROTON-1858](https://issues.apache.org/jira/browse/PROTON-1858) - [Python] Rewrite wrapped C handlers in python
 - [PROTON-1865](https://issues.apache.org/jira/browse/PROTON-1865) - Improve split between general SASL code and the specific implementations
 - [PROTON-1869](https://issues.apache.org/jira/browse/PROTON-1869) - [Python] Compiler conversion warnings with Win64 builds

## Bugs fixed

 - [PROTON-1854](https://issues.apache.org/jira/browse/PROTON-1854) - [Python binding] Using message properties under Python 3 generates NameError 'unicode'
 - [PROTON-1855](https://issues.apache.org/jira/browse/PROTON-1855) - [ruby] copy link terminus state for incoming links
 - [PROTON-1856](https://issues.apache.org/jira/browse/PROTON-1856) - [ruby] auto-accept over-writing user transfer state
 - [PROTON-1857](https://issues.apache.org/jira/browse/PROTON-1857) - [cpp] no access to AMQP connection offered/desired capabilities
 - [PROTON-1859](https://issues.apache.org/jira/browse/PROTON-1859) - [cpp] auto-accept over-writing user transfer state
 - [PROTON-1860](https://issues.apache.org/jira/browse/PROTON-1860) - [cpp] connection::container_id should return the *remote* container-id
 - [PROTON-1861](https://issues.apache.org/jira/browse/PROTON-1861) - [ruby] offered/desired capabilities should be decoded as "multiple" fields
 - [PROTON-1863](https://issues.apache.org/jira/browse/PROTON-1863) - [cpp] need support for anonymous link targets
 - [PROTON-1866](https://issues.apache.org/jira/browse/PROTON-1866) - cannot tell whether peer specified expiry-policy on terminus
 - [PROTON-1867](https://issues.apache.org/jira/browse/PROTON-1867) - Debug libs missing in Windows build
 - [PROTON-1868](https://issues.apache.org/jira/browse/PROTON-1868) - [Python] pn_handle_t binding does not reliably work with Win64