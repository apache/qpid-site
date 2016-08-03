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

<section markdown="1">

## JMS Client (AMQP 1.0)

<table>
  <thead>
    <tr>
      <th>CVE-ID</th><th>Severity</th><th>Affected&nbsp;Versions</th><th>Fixed&nbsp;in&nbsp;Versions</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CVE-2016-4974</td>
      <td>Moderate</td>
      <td>0.9.0 and earlier</td>
      <td>0.10.0 and later</a></td>
      <td>
        Deserialization of untrusted input while using JMS ObjectMessage. <a id="CVE-2016-4974_details_toggle" href="javascript:_toggleDiv({divId:'CVE-2016-4974_details', controlId:'CVE-2016-4974_details_toggle', showMore:'<small>show more</small>', showLess:'<small>show less</small>'});"><small>show more</small></a>
        <div style="display:none;" id="CVE-2016-4974_details">
            <p>Description: When applications call getObject() on a consumed JMS ObjectMessage they are
            subject to the behaviour of any object deserialization during the process
            of constructing the body to return.  Unless the application has taken outside
            steps to limit the deserialization process, they can't protect against
            input that might try to make undesired use of classes available on the
            application classpath that might be vulnerable to exploitation.
            In order to exploit this vulnerability, an attacker would need
            to be able to inject a suitably crafted AMQP message containing the
            malicious JMS Object Message into the AMQP message network. For this,
            the attacker would require valid authentication credentials and
            suitable authorisation.</p>

            <p> Mitigation: Users using ObjectMessage can upgrade to
            Qpid JMS client 0.10.0 or later, and use the new
            configuration options to whitelist trusted content permitted for
            deserialization. When so configured, attempts to deserialize input
            containing other content will be prevented. Alternatively, users of older
            client releases may utilise other means such as agent-based approaches to help
            govern content permitted for deserialization in their application.</p>

            <p> Credit: This issue was discovered by Matthias Kaiser of Code White (www.code-white.com)</p>

            <p>References: <a href="https://issues.apache.org/jira/browse/QPIDJMS-188">QPIDJMS-188</a></p>
        </div>
      </td>
    </tr>
  </tbody>
</table>

</section>

See the main [Security]({{site_url}}/security.html) page for general information and details for other components.
