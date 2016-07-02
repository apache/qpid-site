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

## C++ Broker

<table>
  <thead>
    <tr>
      <th>CVE-ID</th><th>Severity</th><th>Affected&nbsp;Versions</th><th>Fixed&nbsp;in&nbsp;Versions</th><th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>CVE-2015-0224</td>
      <td>Moderate</td>
      <td>0.30 and earlier</td>
      <td>0.32 and later</td>
      <td>qpidd can be crashed by unauthenticated user
	<a id="CVE_2015_0224_details_toggle" href="javascript:_toggleDiv({divId:'CVE_2015_0224_details', controlId:'CVE_2015_0224_details_toggle', showMore:'<small>show more</small>', showLess:'<small>show less</small>'});"><small>show more</small></a>
	<div style="display:none;" id="CVE_2015_0224_details">
	  <p>Description: In CVE-2015-0203 it was announced that
	    certain unexpected protocol sequences cause the broker
	    process to crash due to insufficient checking, but that
	    authentication could be used to restrict the exploitation
	    of this vulnerability.<br/>  It has now been discovered
	    that in fact failing authentication does not necessarily
	    prevent exploitation of those reported
	    vulnerabilities.<br/>  Further, it was stated that one of
	    the specific vulnerabilities was that the qpidd broker can
	    be crashed by sending it a sequence-set containing an
	    invalid range, where the start of the range is after the
	    end. This was an incorrect analysis of the vulnerability,
	    which is in fact caused by a sequence-set containing a
	    single range expressing the maximum possible gap.</p>

	  <p>Solution: A further patch is available that handles a
	  range expressing the maximum possible gap without assertion
	  (<a href="https://issues.apache.org/jira/browse/QPID-6310">QPID-6310</a>). The
	  fix will be included in subsequent releases, but can be
	  applied to 0.30 if desired.</p>

	  <p>Credit: This issue was discovered by G. Geshev from MWR
	  Labs</p>
	</div>
     </td>
    </tr>

    <tr>
      <td>CVE-2015-0223</td>
      <td>Moderate</td>
      <td>0.30 and earlier</td>
      <td>0.32 and later</td>
      <td>anonymous access to qpidd cannot be prevented
	<a id="CVE_2015_0223_details_toggle" href="javascript:_toggleDiv({divId:'CVE_2015_0223_details', controlId:'CVE_2015_0223_details_toggle', showMore:'<small>show more</small>', showLess:'<small>show less</small>'});"><small>show more</small></a>
	<div style="display:none;" id="CVE_2015_0223_details">
	  <p>Description: An attacker can gain access to qpidd as an
	  anonymous user, even if the ANONYMOUS mechanism is
	  disallowed.</p>

	  <p>Solution: A patch is available
	  (<a href="https://issues.apache.org/jira/browse/QPID-6325">QPID-6325</a>)
	  that addresses this vulnerability. The fix will be included
	  in subsequent releases, but can be applied to 0.30 if
	  desired.</p>

	  <p>Common Vulnerability Score information: Authorization can
	  be used to restrict access to broker entities such as queue
	  and exchanges.</p>

	  <p>Credit: This issue was discovered by G. Geshev from MWR
	  Labs</p>
	</div>
     </td>
    </tr>

    <tr>
      <td>CVE-2015-0203</td>
      <td>Moderate</td>
      <td>0.30 and earlier</td>
      <td>0.32 and later</td>
      <td>qpidd can be crashed by authenticated user
	<a id="CVE_2015_0203_details_toggle" href="javascript:_toggleDiv({divId:'CVE_2015_0203_details', controlId:'CVE_2015_0203_details_toggle', showMore:'<small>show more</small>', showLess:'<small>show less</small>'});"><small>show more</small></a>
	<div style="display:none;" id="CVE_2015_0203_details">
	  <p>Description: Certain unexpected protocol sequences cause
	  the broker process to crash due to insufficient
	  checking. Three distinct cases were identified as follows:<br/>
	  The AMQP 0-10 protocol defines a sequence set containing
	  id ranges. The qpidd broker can be crashed by sending it a
	  sequence-set containing an invalid range, where the start of
	  the range is after the end. This condition causes an
	  assertion, which causes the broker process to exit.<br/>
	  The AMQP 0-10 protocol defines header- and body- segments
	  that may follow certain commands. The only command for which
	  such segments are expected by qpidd is the message-transfer
	  command. If another command is sent that includes header
	  and/or body segments, this will cause a segmentation fault
	  in the broker process, causing it then to exit.<br/>
	  The AMQP 0-10 protocol defines a session-gap control that
	  can be sent on any established session. The qpidd broker
	  does not support this control and responds with an
	  appropriate error if requested on an established
	  session. However, if the control is sent before the session
	  is opened, the brokers handling causes an assertion which
	  results in the broker process exiting.</p>

	  <p>Solution: A patch is available
	  (<a href="https://issues.apache.org/jira/browse/QPID-6310">QPID-6310</a>)
	  that handles all these errors by sending an exception
	  control to the remote peer and leave the broker available to
	  all other users. The fix will be included in subsequent
	  releases, but can be applied to 0.30 if desired.</p>

	  <p>Common Vulnerability Score information: Authentication
	  can be used to restrict access to the broker. However any
	  authenticated user would be able to trigger this condition
	  which could therefore be considered a form of denial of
	  service.</p>

	  <p>Credit: This issue was discovered by G. Geshev from MWR
	  Labs</p>
	</div>
     </td>
    </tr>

    <tr>
      <td>CVE-2014-3629</td>
      <td>Low</td>
      <td>0.30 and earlier</td>
      <td>0.32 and later</td>
      <td>qpidd can be induced to make http requests
	<a id="CVE_2014_3629_details_toggle" href="javascript:_toggleDiv({divId:'CVE_2014_3629_details', controlId:'CVE_2014_3629_details_toggle', showMore:'<small>show more</small>', showLess:'<small>show less</small>'});"><small>show more</small></a>
	<div style="display:none;" id="CVE_2014_3629_details">
	  <p>Description: The XML exchange type is an optional,
	  dynamically loaded module for qpidd that allows creation of
	  exchanges that route messages based on evaluating an xquery
	  expression against them.<br/>On parsing a message sent to an
	  XML exchange, whose body is XML containing a link to a DTD,
	  the broker process will attempt to retrieve the referenced
	  resource(s). I.e. the broker process may be induced to make
	  outgoing HTTP connections by publishing a message containing
	  links to an XML exchange.</p>

	  <p>Solution:
	  A <a href="https://issues.apache.org/jira/secure/attachment/12680198/QPID-6218.patch">patch</a>
	  is available that prevents any retrieval of external
	  entities referenced in the XML. This will be included in
	  subsequent releases, but can be applied to 0.30 if
	  desired.</p>

	  <p>Common Vulnerability Score information: If the XML
	  exchange functionality is not required, the module in
	  question need not be loaded at all. This can be done either
	  by moving the module - named xml.so - out of the module
	  directory, or by setting the --no-module-dir option and
	  adding an explicit --load-module argument for every required
	  module.<br/>Where the XML exchange functionality is
	  required, authorisation may be enabled to prevent all but
	  trusted users from creating or publishing to xml
	  exchanges.</p>

	  <p>Credit: This issue was discovered by G. Geshev from MWR
	  Labs</p>
	</div>
     </td>
    </tr>
  </tbody>
</table>

</section>

See the main [Security]({{site_url}}/security.html) page for general information and details for other components.
