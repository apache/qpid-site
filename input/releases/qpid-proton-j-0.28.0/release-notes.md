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

# Qpid Proton-J 0.28.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1876](https://issues.apache.org/jira/browse/PROTON-1876) - expose newer encode/decode operations through the Message interface
 - [PROTON-1894](https://issues.apache.org/jira/browse/PROTON-1894) - expose the position within current backing array of a composite buffer
 - [PROTON-1895](https://issues.apache.org/jira/browse/PROTON-1895) - add ability to append other buffer contents to the composite buffer

## Bugs fixed

 - [PROTON-1889](https://issues.apache.org/jira/browse/PROTON-1889) - failure reading from composite buffer if expanded with new data after prior content was exhausted
 - [PROTON-1891](https://issues.apache.org/jira/browse/PROTON-1891) - empty composite buffer slice should not allow appending new data
 - [PROTON-1892](https://issues.apache.org/jira/browse/PROTON-1892) - transfers for multiplexed deliveries on the same session can have the wrong delivery-id