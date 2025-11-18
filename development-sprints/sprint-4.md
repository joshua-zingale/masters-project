**State**: File uploading, chatting, and user authentication

**Objective**: HS presentation preparation, assistant messages, test RAG
methods

**Future**: Improved RAG, Improved Styling, Preparation for final
presentation

**Introduction**

In less than three weeks, we shall have reached the end of the Data
Science Fellowship and shall be presenting our work to the entire group.
Given this, we need to approach a usable product by then.

Currently, an instructor can upload a document, which our chatbot then
can reference when compiling a response for a student in a
student-chatbot conversation. This is the essential RAG-powered chatbot
that we want. We also have authentication in place to gate access as
appropriate. We lack one essential feature---deferral to a ULA when the
chatbot cannot help.

Beyond implementing ULA-deferral, our RAG system is completely untested.
We need to test our current method and tweaked versions thereof,
allowing us to optimize our procedure later. Finally, we have the
presentation for the high schoolers to prepare for this Wednesday the
30th.

This sprint is to be completed before next Monday, the 4th.

**Presentation for High Schoolers --- Student #3, Student #2, Student #5, and Student #1**

You four need to work together to put together a single slide
presentation. You each already have assigned topics available for
reading
[[here]{.underline}](https://docs.google.com/document/d/1JgifrBJzWz6zPlsPQOyOWJjHlGcMQqt9YfTdzkzTp6o/edit?tab=t.0).
The fifteen minute time slots are maximums. While you should definitely
take at least five minutes for your topic, you should feel no need to
stretch each slot to fifteen minutes.

If our application is in a working state, one of you can demonstrate our
in-progress application at the end of the presentation.

**Testing RAG Methods --- Student #3, Student #2, Student #5, and Student #1**

Get our current web server running, upload some documents, and ask what
you think are some realistic questions to the chatbot. Converse with the
chatbot and document how well it answers questions based on the uploaded
documents. You should use the Gemini API when evaluating the responses.

Make modifications along the following dimensions, in isolation and
together, and document how the performance is affected:

-   Try playing around with the system prompt and where the RAG context
    is inserted into it.

-   Change what documents are uploaded to see how different documents
    work.

-   Modify the length of segments obtained from uploaded documents.

    -   From the segments that I inspected, it looked to me like many of
        the segments are longer than they should be, but I could be
        wrong.

(For Student #2 and Student #1) If feasible, evaluate against the systems that
you studied last sprint.

This testing is to take priority after the presentation for the high
schoolers is complete.

**Assistant Messages --- Shreyes and Student #4 (DB help as needed from
Student #1 and Student #3)**

This is the last of the primary features to be implemented. You must add
the functionality for a conversation to get deferred to a human
assistant. This human assistant will be a ULA in our case: however, to
make our application more general, refer to this role simply as
*assistant* in the code.

As a first order of business, the user that started a conversation
should have a button available in each conversation's page called "Mark
As Resolved", which should be pressable at any time by the user. If the
user, or someone else, sends any messages to a resolved conversation,
the conversation should be marked as no longer resolved.

Here is what the new application flow for a student:

-   The chatbot is not helpful for the student so he presses an "Invite
    Course Assistant to Join" button.

-   Henceforth, the chatbot should no longer respond to anything sent by
    the student, though the student should still be able to send
    messages.

-   The student's conversation should appear on a page accessible to the
    course's Assistants.

-   An Assistant should be able to enter the conversation and
    communicate back and forth with the student.

-   The Assistant, like the initiator of the conversation, should be
    able to mark the conversation as resolved.

New webpage: There should be a new webpage accessible to each Assistant
that shows all conversations elevated to the Assistant level. The
conversations ideally will be broken up into three categories: those to
which no Assistant has written a message, those to which the
authenticated Assistant has written a message, and those that are
resolved.

Modified webpage: You will need to modify the existing conversation web
page to support Assistants entering the

DB Modification: There should be a new boolean column in the
Conversations table called "resolved" that indicates whether the
initiating user or an Assistant has marked the conversation as resolved.

*IMPORTANT NOTE*: Ensure that Assistants can only access conversations
from students that were explicitly elevated by the students. We want a
student to be able to keep his messages unread by assistants if that is
what he wants.
