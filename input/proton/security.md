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

## Proton

<table>
  <thead>
    <tr>
      <th>CVE-ID</th><th>Severity</th><th>Affected&nbsp;Versions</th><th>Fixed&nbsp;in&nbsp;Versions</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CVE-2016-2166</td>
      <td>Moderate</td>
      <td>0.9 through 0.12.0 (inclusive)</td>
      <td>0.12.1 and later</td>
      <td>
        Python bindings silently ignore request for amqps if SSL/TLS not supported. <a id="CVE_2016_2166_details_toggle" href="javascript:_toggleDiv({divId:'CVE_2016_2166_details', controlId:'CVE_2016_2166_details_toggle', showMore:'<small>show more</small>', showLess:'<small>show less</small>'});"><small>show more</small></a>
        <div style="display:none;" id="CVE_2016_2166_details">
          <p>Versions Affected: Apache Qpid Proton python API starting
          at 0.9 up to and including version 0.12.0.</p>
          <p>Description: Messaging applications using the Proton
          Python API to provision an SSL/TLS encrypted TCP connection
          may actually instantiate a non-encrypted connection without
          notice if SSL support is unavailable.  This will result in
          all messages being sent in the clear without the knowledge
          of the user.<br/>  This issue affects those applications
          that use the Proton Reactor Python API to create SSL/TLS
          connections.  Specifically the proton.reactor.Connector,
          proton.reactor.Container, and
          proton.utils.BlockingConnection classes are vulnerable.
          These classes can create an unencrypted connections if the
          "amqps://" URL prefix is used.<br/>  The issue only occurs
          if the installed Proton libraries do not support SSL.  This
          would be the case if the libraries were built without SSL
          support or the necessary SSL libraries are not present on
          the system (e.g. OpenSSL in the case of *nix).<br/>  To
          check whether or not the Python API provides SSL support,
          use the following console command:<br/>python -c "import
          proton; print('%s' % 'SSL present' if proton.SSL.present()
          else 'SSL NOT AVAILBLE')"<br/>In addition, the issue can
          only occur if both ends of the connection connect without
          SSL.  This would be the case if the vulnerability is active
          on both ends of the connection, or the non-affected endpoint
          allows cleartext connections.</p>
          <p>Resolution: Proton release 0.12.1 resolves this issue by
          raising an SSLUnavailable exception when SSL is not
          available and a SSL/TLS connection is requested via the
          "amqps://" URL
          prefix.<br/>A <a href="https://issues.apache.org/jira/browse/PROTON-1157">patch</a>
          is also available.</p>
          <p>References: <a href="https://issues.apache.org/jira/browse/PROTON-1157">PROTON-1157</a></p>
	  <p>Credit: This issue was discovered by M. Farrellee from Red Hat.</p>
        </div>
      </td>
    </tr>
  </tbody>
</table>

</section>

See the main [Security]({{site_url}}/security.html) page for general information and details for other components.
