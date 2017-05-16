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

## AMQP 0-x JMS (AMQP 0-8, 0-9, 0-9-1, 0-10)

| CVE-ID | Severity | Affected versions | Fixed versions | Summary |
| ------ | -------- | ----------------- | -------------- | ------- |
| [CVE-2016-4974]({{site_url}}/cves/CVE-2016-4974_0-x.html) | Moderate | 6.0.3 and earlier | 6.0.4 and later | Deserialization of untrusted input while using JMS ObjectMessage |

See the [Qpid JMS Security]({{site_url}}/components/jms/security.html) page
for details of the AMQP 1.0 JMS client.

See the main [Security]({{site_url}}/security.html) page for general
information and details for other components.


