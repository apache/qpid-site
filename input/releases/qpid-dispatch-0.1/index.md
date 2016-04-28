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

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("0.1" === "{{current_dispatch_release}}") {
          _modifyCurrentReleaseLinks();
      }
});
</script>

# Qpid Dispatch Router 0.1

Dispatch Router is a lightweight AMQP message router library. More
about [Qpid Dispatch]({{site_url}}/components/dispatch-router/index.html).

For a detailed list of the changes in this release, see the [release
notes](notes.html).

## Downloads

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

| Content | Download | Signature |
| ------- | -------- | --------- |
| Dispatch Router | [qpid-dispatch-0.1.tar.gz](http://archive.apache.org/dist/qpid/dispatch/0.1/qpid-dispatch-0.1.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/dispatch/0.1/qpid-dispatch-0.1.tar.gz.asc) |

## Documentation

<div class="two-column" markdown="1">

 - [Initial Release Overview](notes.html)
 - [Usage of AMQP](amqp-mapping.html)

</div>

## More information

 - [All release artifacts](http://archive.apache.org/dist/qpid/dispatch/0.1)
;; - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+PROTON+AND+fixVersion+%3D+%270.6%27+ORDER+BY+priority+DESC)
 - [Source repository branch](http://svn.apache.org/repos/asf/qpid/dispatch/branches/0.1)
 - [Source repository tag](http://svn.apache.org/repos/asf/qpid/dispatch/tags/0.1)
