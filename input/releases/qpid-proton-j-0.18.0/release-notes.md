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

# Qpid Proton-J 0.18.0 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).


## New features and improvements

 - [PROTON-1405](https://issues.apache.org/jira/browse/PROTON-1405) - Capability to use SSLContext provided by the application.
 - [PROTON-1409](https://issues.apache.org/jira/browse/PROTON-1409) - expose the number of bytes currently available for the delivery
 - [PROTON-1425](https://issues.apache.org/jira/browse/PROTON-1425) - Add copy constructor to Header and Properties

## Bugs fixed

 - [PROTON-1384](https://issues.apache.org/jira/browse/PROTON-1384) - the 'Data' utility incorrectly encodes str32 type length
 - [PROTON-1393](https://issues.apache.org/jira/browse/PROTON-1393) - Memory leak with delayed / out-of-order settlement
 - [PROTON-1426](https://issues.apache.org/jira/browse/PROTON-1426) - verify the SASL layer protocol header
 - [PROTON-1427](https://issues.apache.org/jira/browse/PROTON-1427) - verify the SASL frame size

## Tasks

 - [PROTON-1428](https://issues.apache.org/jira/browse/PROTON-1428) - remove invalid constructor deprecation markers