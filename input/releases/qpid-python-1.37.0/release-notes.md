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

# Qpid Python 1.37.0 Release Notes

Qpid Python includes an AMQP messaging library and a suite of tests
for AMQP conformance.

For more information about this release, including download links and
documentation, see the [release overview](index.html).

**NOTE**: Look to [Qpid Proton](http://qpid.apache.org/proton) for Python 3 and AMQP 1.0 support.


## Bugs fixed

 - [QPID-2524](https://issues.apache.org/jira/browse/QPID-2524) - Fails loading dtd in Python 2.6 on Ubuntu 9.10 (Karmic) with "ValueError: unknown url type: /.../specs/amqp.0-10.dtd"
 - [QPID-7809](https://issues.apache.org/jira/browse/QPID-7809) - Python 0-10 messaging driver does not handle heartbeat timeouts, "assert rcv.received &lt; rcv.impending" occurs
 - [QPID-7833](https://issues.apache.org/jira/browse/QPID-7833) - Batch file for Windows is missing from source distribution
 - [QPID-7884](https://issues.apache.org/jira/browse/QPID-7884) - Python client should not raise exception on close() after stop.