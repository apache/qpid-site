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
      if ("0.3" === "{{current_dispatch_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>

# Qpid Dispatch 0.3

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
| Dispatch router | [qpid-dispatch-0.3.tar.gz](http://archive.apache.org/dist/qpid/dispatch/0.3/qpid-dispatch-0.3.tar.gz) | [PGP](http://archive.apache.org/dist/qpid/dispatch/0.3/qpid-dispatch-0.3.tar.gz.asc) |


## Documentation

<div class="two-column" markdown="1">
<div class="column" markdown="1">
- [Dispatch router book](book.html) ([PDF](book.pdf))
- [Installing Qpid Dispatch](http://svn.apache.org/repos/asf/qpid/dispatch/branches/0.3/README)
</div>
<div class="column" markdown="1">
- [qdrouterd](qdrouterd.8.html) - Router daemon
- [qdrouterd.conf](qdrouterd.conf.5.html) - Router configuration
- [qdstat](qdstat.8.html) - Get router statistics
- [qdmanage](qdmanage.8.html) - Manage the router
</div>
</div>



## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/dispatch/0.3)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+DISPATCH+AND+fixVersion+%3D+%270.3%27+ORDER+BY+priority+DESC)
 - [Source repository branch](http://svn.apache.org/repos/asf/qpid/dispatch/branches/0.3)
 - [Source repository tag](http://svn.apache.org/repos/asf/qpid/dispatch/tags/0.3)
