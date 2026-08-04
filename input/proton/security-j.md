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

# Security
## Proton-J

| CVE-ID | Severity | Affected versions | Fixed versions | Summary |
| ------ | -------- | ----------------- | -------------- | ------- |
| [CVE-2018-17187]({{site_url}}/cves/CVE-2018-17187.html) | Important | 0.3 to 0.29.0 inclusive | 0.30.0 and later | Transport TLS wrapper hostname verification mode not implemented |
| [CVE-2026-66257]({{site_url}}/cves/CVE-2026-66257.html) | Important | Up to 0.34.1 inclusive  | 0.35.0 and later | Unbounded symbol value caching can lead to pre-authentication resource exhaustion |
| [CVE-2026-66273]({{site_url}}/cves/CVE-2026-66273.html) | Important | Up to 0.34.1 inclusive  | 0.35.0 and later | Type size/count handling can lead to excessive allocation pre-authentication |
| [CVE-2026-66274]({{site_url}}/cves/CVE-2026-66274.html) | Important | Up to 0.34.1 inclusive  | 0.35.0 and later | Unbounded type nesting can lead to pre-authentication stackoverflow |
| [CVE-2026-66275]({{site_url}}/cves/CVE-2026-66275.html) | Important | Up to 0.34.1 inclusive  | 0.35.0 and later | Incoming session flow control window can be exceeded |
| [CVE-2026-66276]({{site_url}}/cves/CVE-2026-66276.html) | Important | Up to 0.34.1 inclusive  | 0.35.0 and later | Unbounded disposition range handling can lead to denial of service  |
| [CVE-2026-66277]({{site_url}}/cves/CVE-2026-66277.html) | Important | Up to 0.34.1 inclusive  | 0.35.0 and later | Unable to govern the maximum number of transfer frames per incoming delivery |

See the main [Security]({{site_url}}/security.html) page for general
information and details for other components.
