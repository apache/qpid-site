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

## Java Broker

### CVEs

<table>
  <thead>
    <tr>
      <th>CVE-ID</th><th>Severity</th><th>Affected&nbsp;Versions</th><th>Fixed&nbsp;in&nbsp;Versions</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CVE-2016-4432</td>
      <td>Important</td>
      <td>6.0.2 and earlier</td>
      <td><a href="{{site_url}}/releases/qpid-java-6.0.3/">6.0.3</a></td>
      <td>
        Authentication Bypass. <a id="CVE_2016_4432_details_toggle" href="javascript:toggleDiv({divId:'CVE_2016_4432_details', controlId:'CVE_2016_4432_details_toggle', showMore:'<small>show more</small>', showLess:'<small>show less</small>'});"><small>show more</small></a>
        <div style="display:none;" id="CVE_2016_4432_details">
          <p>Versions Affected: Qpid Java Broker versions 6.0.2 and
          earlier</p>
          <p>Description: The code responsible for handling incoming
          AMQP 0-8, 0-9, 0-91, and 0-10 connections contains a flaw
          that allows authentication to be bypassed.  An remote
          attacker can exploit this vulnerability to perform actions,
          without the need to specify valid credentials.  For
          instance, unauthorised messages could be injected or
          messages stolen.<br/>The vulnerability cannot be exploited
          if the Access Control List (ACL) feature is enabled AND
          access to all virtual hosts controlled.<br/>The
          vulnerability does not apply to the Broker's AMQP 1.0
          support.<br/>The vulnerability does not apply if the Broker
          is configured to require SSL client authentication for all
          messaging connections.</p>
          <p>Resolution: Users should upgrade the Qpid Java Broker to
          version 6.0.3 or later (recommended).</p>
          <p>Mitigation: If upgrading is not possible, the
          vulnerability can be mitigated using an ACL file containing
          "ACCESS VIRTUALHOST" clauses that white-lists user access to
          all virtualhosts.<br/>If AMQP 0-8, 0-9, 0-91, and 0-10
          support is not required, the vulnerability can also be
          mitigated by turning off these protocols at the Port
          level.</p>
          <p>References: <a href="https://issues.apache.org/jira/browse/QPID-7257">QPID-7257</a></p>
        </div>
      </td>
    </tr>

    <tr>
      <td>CVE-2016-3094</td>
      <td>Important</td>
      <td>6.0.0, 6.0.1, 6.0.2</td>
      <td><a href="{{site_url}}/releases/qpid-java-6.0.3/">6.0.3</a></td>
      <td>
        Denial of Service.
        <a id="CVE_2016_3094_details_toggle" href="javascript:toggleDiv({divId:'CVE_2016_3094_details', controlId:'CVE_2016_3094_details_toggle', showMore:'<small>show more</small>', showLess:'<small>show less</small>'});"><small>show more</small></a>
        <div style="display:none;" id="CVE_2016_3094_details">
          <p>Versions Affected: Qpid Java Broker versions 6.0.0,
          6.0.1, and 6.0.2</p>
          <p>Description: A malformed authentication attempt may cause
          the broker to terminate.  The Qpid Java Broker supports a
          number of configurable authentication providers each
          supporting various SASL mechanisms. Some mechanisms need (or
          can be configured to accept) plain-text passwords being sent
          to the Broker (using the SASL "PLAIN" mechanism).  Where the
          broker has been configured to allow plain-text passwords for
          authentication it is possible for a client to send a
          malformed authentication attempt which will lead the broker
          to terminate due to an uncaught Exception.<br/>  Brokers
          configured to use authentication from the
          "PlainPasswordFile", "SimpleLDAP", or
          "Base64MD5PasswordFile" providers are vulnerable if the
          "PLAIN" mechanism is enabled (by default "PLAIN" will be
          disabled on non-TLS ports, but enabled on TLS
          connections).</p>
          <p>Mitigation: Users should upgrade their Qpid Java Broker
          to version 6.0.3 or later.  If this is not possible, users
          can disable the PLAIN mechanism for their authentication
          manager on versions 0.32 and later by adding "PLAIN" to the
          list of disabledMechanisms on their authentication provider
          object.<br/>Note that the SimpleLDAP authentication provider
          requires PLAIN and so this work around does not apply
          there.</p>
          <p>Credit: This issue was discovered by Alex Szczuczko of
          Red Hat, Inc.</p>
          <p>References: <a href="https://issues.apache.org/jira/browse/QPID-7271">QPID-7271</a></p>
        </div>
      </td>
    </tr>
  </tbody>
</table>

</section>
