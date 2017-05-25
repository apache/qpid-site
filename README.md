# Qpid Site

## Setup your environment

To setup paths in your environment, source the `config.sh` script.

    ~$ cd qpid-site/
    [qpid-site]$ source config.sh

## Project layout

    config.sh                     # Sets up your project environment
    Makefile                      # Defines the make targets
    python/                       # Python library code; used by scripts
    scripts/                      # Scripts called by the make rules
    input/                        # The site content before rendering
    output/                       # Rendered result for local testing
    content/                      # Rendered result for publication to the site

Some notable files in `input/`:

    input/_transom_template.html  # The standard page template
    input/_transom_config.py      # Site variables, values for {{placeholders}}
    input/site.js                 # Site javascript code
    input/site.css                # Site CSS

## Make targets

After that most everything is accomplished by running make targets.
These are the important ones:

    [qpid-site]$ make render      # Renders input/* to output/
    [qpid-site]$ make clean       # Removes output/
    [qpid-site]$ make publish     # Renders input/* to content/ in preparation
                                  # for a live site update

## Adding content

1. Use your editor to create or edit a file under `input/`

        [qpid-site]$ emacs input/somepage.md

2. Render the site

        [qpid-site]$ make render

3. To look at the result in your browser, navigate to

        file:///$somepath/site/output/somepage.html

## Render transformations

The render step takes files under `input/` and reproduces them under
`output/`.  The following transformations are applied in the process:

 - `.html.in` files are wrapped in the site template and copied
 - `.md` (Markdown) files are converted to HTML, wrapped in the site
   template, and copied
 - All other files are simply copied
 - All Markdown, HTML, Javascript, and CSS files undergo substitution
   for `{{placeholders}}`

## Markdown syntax

Markdown is a markup language inspired by plain text conventions.
This page is written in markdown.  See this [syntax guide][syntax].

The particular markdown implementation the site code uses is
[python-markdown2][markdown2].

I personally benefit from using [emacs markdown mode][emacs].  On
Fedora it is part of the `emacs-goodies` package.

[syntax]: http://daringfireball.net/projects/markdown/syntax
[markdown2]: https://github.com/trentm/python-markdown2
[emacs]:  http://jblevins.org/projects/markdown-mode/

## Placeholders

`input/_transom_config.py` defines some variables usable for any input
page.  To illustrate:

    {{site_url}}                 -> http://qpid.apache.org
    {{current_proton_release}}   -> 0.17.0
    {{current_dispatch_release}} -> 0.8.0

Under `output/`, `{{site_url}}` is set to a path in your development
environment, to allow for local testing.  Under `content/`,
`{{site_url}}` is set to <http://qpid.apache.org>, for publication to
the live site.

You can see more definitions in `input/_transom_config.py`.

## Style guide

See <http://qpid.apache.org/site.html#style-guide> for site guidelines
for formatting and style.

## Checking links

The site tools offer a way to check that all your hyperlinks are
working.

    # Usage: make check-links [INTERNAL=1] [EXTERNAL=0]

    # Check internal links only
    [qpid-site]$ make check-links

    # Check external links as well
    [qpid-site]$ make check-links EXTERNAL=1

## Generating release content

Most of the site content is written by human beings.  Release content,
however, is automated.  Use the following commands to generate content
for a new release.

    # Usage: make gen-$module-release RELEASE=$VERSION [CHECKOUT_DIR=$DIR]

    # For new Qpid C++ releases
    [qpid-site]$ make gen-cpp-release RELEASE=$VERSION

    # For new Qpid Java releases
    [qpid-site]$ make gen-java-release RELEASE=$VERSION

    # For new Qpid JMS releases
    [qpid-site]$ make gen-jms-release RELEASE=$VERSION

    # For new Qpid Proton releases
    [qpid-site]$ make gen-proton-release RELEASE=$VERSION

    # For new Qpid Dispatch releases
    [qpid-site]$ make gen-dispatch-release RELEASE=$VERSION

These will produce a new tree of release content under
`input/releases/`.  The content includes API docs, examples, and
books.  Once generated, you can make any edits you'd like and check it
in.

In addition to specifying `RELEASE`, you can override the particular
release identifier used for querying issues and exporting source using
`ISSUES_RELEASE` and `SOURCE_RELEASE` respectively.  If not set,
`ISSUES_RELEASE` and `SOURCE_RELEASE` take the value of `RELEASE`.

By default, the scripts will fetch the source for you based on the
release script inputs.  By setting the optional `CHECKOUT_DIR`
parameter to the location of a local Subversion checkout, the scripts
will instead use the provided content.

When you add release content, you should also update the following
files:

    input/_transom_config.py   # Update the current release pointer
    input/releases/index.md    # Add current release, move the previous

The scripts depend on the availability of the following tools in your
environment: cmake, dot, doxygen, epydoc, fop, gcc, javadoc, make,
pygments, PyYAML, rdoc, git, pandoc, pdflatex and xsltproc.  The
following yum command works to install all the required dependencies
on Fedora or RHEL.

    $ sudo yum install cmake doxygen epydoc fop gcc graphviz java-devel \
          libxslt make python-pygments PyYAML rubygem-rdoc git \
          pandoc-pdf python-sphinx maven

## Publishing your work

Qpid uses gitpubsub to send new content to the Qpid website.  Any file
committed under the 'content' dir on the 'asf-site' branch of the
https://git-wip-us.apache.org/repos/asf/qpid-site.git repo is
automatically propagated to the live site.  `make publish` renders to
this same `content/` directory.

To publish, run `make publish` and use git to commit and push the
changes.  Any additions or other structural changes under the `input/` and
`content/` directories may require git adds or removes.

    [qpid-site]$ make publish
    scripts/render "" input content
    git status input content
    # On branch asf-site
    # Changes not staged for commit:
    #   (use "git add <file>..." to update what will be committed)
    #   (use "git checkout -- <file>..." to discard changes in working directory)
    #
    #	modified:   content/discussion.html
    #	modified:   input/discussion.md
    #
    # Untracked files:
    #   (use "git add <file>..." to include in what will be committed)
    #
    #	content/new_file.html
    #	input/new_file.md
    no changes added to commit (use "git add" and/or "git commit -a")
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    NOTICE! One more step remains!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Use git to commit and push the changes.
    Keep in mind that you may need to git add new files.
    Also keep in mind to git rm matching files from content/ that have been removed from input/.


## More information

 - The Qpid site code internally uses
   [Transom](http://www.ssorj.net/projects/transom.html)
