**State**: A file uploading and chat pipeline.

**Objective:** Explore relevant modern technologies, add user
authentication, and fix up the repo.

**Future:** A working product with basic RAG question and answering

**Introduction**

At this point, we have a repository with some minimally functioning
components. Before moving on to introduce more features, we shall look
into what other methods are out there for RAG, finish up user
authentication, and clean up the existent code to ensure it works
together.

Different team members will be given different tasks for the week, some
working on the repository and others researching methods.

Watch [[Don\'t Write
Comments]{.underline}](https://www.youtube.com/watch?v=Bf7vDBBOBUA) and
apply the principles therein to any future codebase edits. The gist is
that non-documentation comments that explain *what* the code is doing
should almost never exist: if you need to put a comment to explain what
your code is doing, then you should probably rewrite your code to make
it easier to understand without a comment.

This sprint should be finished before next Monday, July 28th.

**Authentication ---** Student #5 & Student #3

Finish the authentication pipeline:

-   Students and instructors should be able to log in.

-   Access to web endpoints (including the API LLM generation endpoint)
    should be gated based on what permissions the authenticated user
    has.

    -   Only the instructor of a course (which we can set manually on
        our end) should be able to upload documents for a course.

    -   Only students added by the instructor of a course should be able
        to access the chat feature for that course.

        -   Implement this by allowing the instructor to upload a CSV of
            student email addresses for his course, granting access to
            all students in the list.

            -   Try to make it work with the downloadable Canvas CSV
                roster

        -   The instructor should also be able to add/remove names
            individually.

Put together a report on the safety of your methods. For example,
explain what is needed to get access to a user's permissions and explain
different attacks that are defended against with the pipeline.

**GraphRAG Exploration --- Student #4 & Student #2**

Read [[A Survey on Knowledge-Oriented Retrieval-Augmented
Generation]{.underline}](https://arxiv.org/pdf/2503.10677) to get an
idea of what RAG methods are out there. Then, read into
[[GraphRAG]{.underline}](https://microsoft.github.io/graphrag/). Put
together a presentation on GraphRag, including a live demonstration
using the method. In the presentation, discuss the method, how it works,
and its benefits/drawbacks against what we are currently doing for RAG.
Plan to present for at most twenty minutes next Monday, the 28th. If
more/less time is needed to present, let me know.

**Brace Exploration --- Student #1**

Read into [[Brace]{.underline}](https://brace.tools/). If possible, get
Brace running on your machine. Then, put together a presentation on
Brace, discussing the technical methodology of Brace and what Brace can
offer to students as a tutor. Look into the code on Github and focus on
how his approach differs from ours, both in code structure and in
generation methodology. Get it running on your machine and prepare a
live demonstration.

**Sundry Code Issues --- Shreyes**

Resolve the various issues that I have opened on GitHub for our
repository. I may open up more issues throughout the week. I will try to
have everything in by Wednesday the 23rd.
