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

# Qpid Proton 0.27.1 Release Notes

Proton is a high-performance, lightweight messaging library. More
about [Qpid Proton]({{site_url}}/proton/index.html).

For more information about this release, including download links and
documentation, see the [release overview](index.html).

**Note**: This release addresses security issue [CVE-2019-0223]({{site_url}}/cves/CVE-2019-0223.html), a TLS Man in the Middle vulnerability while using OpenSSL prior to v1.1.0.

## Bugs fixed

 - [PROTON-1989](https://issues.apache.org/jira/browse/PROTON-1989) - TLS Configuration does not support TLSv1_3 in OpenSSL v1.1.1
 - [PROTON-2004](https://issues.apache.org/jira/browse/PROTON-2004) - allow compilation with LibreSSL
 - [PROTON-2006](https://issues.apache.org/jira/browse/PROTON-2006) - Service Bus example doesnt work
 - [PROTON-2010](https://issues.apache.org/jira/browse/PROTON-2010) - [python] JSON connection config: comments and SASL mechs don't work
 - [PROTON-2014](https://issues.apache.org/jira/browse/PROTON-2014) - [CVE-2019-0223] TLS Man in the Middle Vulnerability
 - [PROTON-2017](https://issues.apache.org/jira/browse/PROTON-2017) - [go] fix proton-c version check
 - [PROTON-2027](https://issues.apache.org/jira/browse/PROTON-2027) - Proactor connection wake after memory freed when using pn_proactor_disconnect().

## Tasks

 - [PROTON-2018](https://issues.apache.org/jira/browse/PROTON-2018) - [c] Test SSL without python bindings