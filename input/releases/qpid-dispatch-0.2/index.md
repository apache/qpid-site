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
      if ("0.2" === "{{current_dispatch_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>

# Qpid Dispatch 0.2

Dispatch is a lightweight AMQP message router library. More about
[Qpid Dispatch]({{site_url}}/components/dispatch-router/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

## Downloads

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of the
files you download.

| Content | Download | Signature |
| ------- | -------- | --------- |
| Dispatch router | [qpid-dispatch-0.2.tar.gz](http://archive.apache.org/dist/qpid/dispatch/0.2/qpid-dispatch-0.2.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/dispatch/0.2/qpid-dispatch-0.2.tar.gz.asc) |

## Documentation

<div class="two-column" markdown="1">
<div class="column" markdown="1">

 - [Installing Qpid Dispatch](http://svn.apache.org/repos/asf/qpid/dispatch/branches/0.2/README)
 - [Dispatch router book](book/index.html)

</div>
</div>

## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/dispatch/0.2)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+DISPATCH+AND+fixVersion+%3D+%270.2%27+ORDER+BY+priority+DESC)
 - [Source repository branch](http://svn.apache.org/repos/asf/qpid/dispatch/branches/0.2)
 - [Source repository tag](http://svn.apache.org/repos/asf/qpid/dispatch/tags/0.2)