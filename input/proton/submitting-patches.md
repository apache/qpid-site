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

# Submitting Patches

All contributions are greatly appreciated, but the process can be
significantly streamlined by taking note of the following guidelines.

## Run the full test suite

Make sure the full test suite runs with your change in place. Even if
you think your change is very localized, there may be subtle
repurcussions that impact other parts of the code. If your change
causes the test suite to fail, then it can't be accepted until a more
complete fix is prepared.

## Keep it small

Most of the people that work on proton have a day job of some kind. If
reviewing a patch requires carving out multiple hours/days, then it is
much less likely to happen. On the other hand if the patch is neat,
self contained, and just works then it can be reviewed and applied
quite quickly.

If you happen to have a larger body of work you'd like to contribute
and there is a good reason that it's difficult to break it down into
small pieces, that's ok too, but expect the whole process to take a
bit longer. In this situation you can help things along by providing
an outline/overview in english to make the work easier to digest.

## Keep it clean

Extraneous whitespace can clutter up diffs and make them more
difficult to read than they need to be. It's generally good practice
to avoid introducing extraneous whitespace into files under source
control. Most editors can be configured to remove and/or display
extraneous whitespace automatically.
