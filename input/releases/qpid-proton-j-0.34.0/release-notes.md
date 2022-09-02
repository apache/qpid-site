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

# Qpid Proton-J 0.34.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## Bugs fixed

 - [PROTON-2347](https://issues.apache.org/jira/browse/PROTON-2347) - Reactor leaks file handles when an IO Exception is encountered
 - [PROTON-2554](https://issues.apache.org/jira/browse/PROTON-2554) - CompositeReadableBuffer read string API not advancing position index

## Tasks

 - [PROTON-2595](https://issues.apache.org/jira/browse/PROTON-2595) - update test dependencies
 - [PROTON-2596](https://issues.apache.org/jira/browse/PROTON-2596) - update to apache parent pom 27
 - [PROTON-2597](https://issues.apache.org/jira/browse/PROTON-2597) - update maven-bundle-plugin to 5.1.8