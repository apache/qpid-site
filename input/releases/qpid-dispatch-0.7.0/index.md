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

# Qpid Dispatch 0.7.0

Dispatch is a lightweight AMQP message router library. More about
[Qpid
Dispatch]({{site_url}}/components/dispatch-router/index.html).

For a detailed list of the changes in this release, see the [release
notes](release-notes.html).

## Downloads

It's important to [verify the
integrity]({{site_url}}/download.html#verify-what-you-download) of
the files you download.

| Content | Download | Verify |
|---------|----------|--------|
| Dispatch router | [qpid-dispatch-0.7.0.tar.gz](http://archive.apache.org/dist/qpid/dispatch/0.7.0/qpid-dispatch-0.7.0.tar.gz) | [PGP](https://archive.apache.org/dist/qpid/dispatch/0.7.0/qpid-dispatch-0.7.0.tar.gz.asc) |

## Documentation


<div class="two-column" markdown="1">

 - [Installing Qpid Dispatch](https://gitbox.apache.org/repos/asf?p=qpid-dispatch.git;a=blob_plain;f=README;hb=0.7.x)
 - [Dispatch Router User Guide](book/book.html)
 - [qdrouterd](man/qdrouterd.html) - Router daemon
 - [qdrouterd.conf](man/qdrouterd.conf.html) - Daemon configuration
 - [qdstat](man/qdstat.html) - Get router statistics
 - [qdmanage](man/qdmanage.html) - Manage the router

</div>


## More information

 - [All release artefacts](http://archive.apache.org/dist/qpid/dispatch/0.7.0)
 - [Resolved issues in JIRA](https://issues.apache.org/jira/issues/?jql=project+%3D+DISPATCH+AND+fixVersion+%3D+%270.7.0%27+AND+resolution+%3D+%27fixed%27+ORDER+BY+priority+DESC)
 - [Source repository tag](https://gitbox.apache.org/repos/asf/qpid-dispatch.git/tree/refs/tags/0.7.0)

<script type="text/javascript">
  _deferredFunctions.push(function() {
      if ("0.7.0" === "{{current_dispatch_release}}") {
          _modifyCurrentReleaseLinks();
      }
  });
</script>