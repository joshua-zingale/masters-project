**State:** Initial.

**Objective**: Complete core components of our system in isolation.

**Future**: Integrate into central repository.

**Introduction**

Our [[project
outline]{.underline}](https://joshua-zingale.github.io/ucr-chatbot-pathway-program/project-plan/)
contains many components. We are going to structure our work on a weekly
basis, where we set incremental goals to achieve along the way. We shall
call these "sprints." In this first sprint, we are going to work on the
three fundamental components of our retrieval-augmented-generation
pipeline: *document parsing*, the *database api,* and the *language
model api*. With these three components, we shall be able to create a
basic web-interface for chatting with an AI that has access to course
documents.

We are targeting **working prototypes**, meaning that we expect to
modify our work as the summer continues.

Since we have six members on this team, you will be split into three
teams of two, one term per component. We plan to integrate the work into
one solution on Wednesday, July 9th.

You do **not** need to work on integrating your work into the repository
this week. We shall go over integration when we meet on July 9th. If you
are up to it, you may look over the [[contributing
guide]{.underline}](https://github.com/joshua-zingale/ucr-chatbot-pathway-program/blob/master/CONTRIBUTING.md)
to help you write better Python.

**Document Parsing - Student #2 and Student #5**

**Objective:** Write code to parse files of various types into plain
text.

We want professors to be able to upload all sorts of documents for their
courses, from which the language models will be able to draw information
to answer student questions. Some files, like text files, are easy to
parse. Others, like CSV, audio, PDF, and ebooks, present challenges
unique to their media.

Complete the [[skeleton
code]{.underline}](https://github.com/joshua-zingale/ucr-chatbot-pathway-program/blob/master/ucr_chatbot/api/file_parsing/file_parsing.py)
to parse text out of files. Add support for

-   txt

-   md

-   PDF

-   Audio

    -   wav

    -   Mp3

-   Ebook

    -   epub

Consider if you need to extract metadata, or if certain formatting (like
headings) should be preserved or discarded.

**Database API - Student #3 and Student #1**

**Objective**: Write code for a Python API for initializing, modifying,
and reading data for our application.

In the [[project
outline]{.underline}](https://joshua-zingale.github.io/ucr-chatbot-pathway-program/project-plan/),
there is what is called an entity relationship diagram, before which is
a short description on how to interpret the diagram. The diagram
contains, at a high-level, the information that we shall need to store
for our application alongside the relationships between them. Use
[[SQLAlchemy]{.underline}](https://www.sqlalchemy.org/) to initialize a
database that models our application's data and develop an API for
modifying data in and reading data from the database. Refer to the
[[documentation]{.underline}](https://docs.sqlalchemy.org/en/14/orm/quickstart.html#declare-models)
for a tutorial on how to use the Object Relational Mapping (ORM)
provided by SQLAlchemy.

Use
[[PostgreSQL]{.underline}](https://docs.sqlalchemy.org/en/13/dialects/postgresql.html#module-sqlalchemy.dialects.postgresql.psycopg2)
as your SQLAlchemy
[[engine]{.underline}](https://docs.sqlalchemy.org/en/13/core/connections.html),
so you will need to have [[PostgreSQL
installed]{.underline}](https://www.postgresql.org/download/) on your
development machine. We shall need a way to store vector embeddings in
our database.
[[This]{.underline}](https://github.com/pgvector/pgvector-python?tab=readme-ov-file)
package may be of use for storing embedding vectors in our database.

**Language Model API - Student #6 and Student #4**

**Objective:** Write code for a Python API to access a language model
and to embed text.

As our application grows throughout development, we may switch from one
LLM vendor to another. Moreover, after production, we may change the
language model based on new developments in the Gen AI marketplace. To
make changing vendors as easy as possible, we are going to develop our
own internal API for our application. Thus, to change vendors we shall
need only to change this component of our system.

First, complete the [[skeleton
functions]{.underline}](https://github.com/joshua-zingale/ucr-chatbot-pathway-program/blob/master/ucr_chatbot/api/language_model/response.py)
for the language model API that exist in the repository by adding in
logic that calls some language model API. Add any useful keyword
arguments to the functions that you see fit, like temperature,
max_tokens, or stop_sequences. You should make two versions: one version
for production that will use either the [[Gemini
API]{.underline}](https://ai.google.dev/gemini-api/docs) or another
provider [[permitted by campus IT]{.underline}](https://its.ucr.edu/ai);
and another version for testing that uses
[[Ollama]{.underline}](https://discord.com/invite/ollama), which is a
local hosting tool for language models. For Ollama, use a small model
like [[Gemma3n]{.underline}](https://ollama.com/library/gemma3n:latest)
or the 1.5 Billion parameter version of
[[Deepseek]{.underline}](https://ollama.com/library/deepseek-r1), that
it may work on a development machine without a GPU.

Second, in addition to a language model, we want the ability to get a
vectorized representation of text. We later shall use this for
retrieval-augmented generation. For now, complete the [[skeleton
function]{.underline}](https://github.com/joshua-zingale/ucr-chatbot-pathway-program/blob/master/ucr_chatbot/api/embedding/embedding.py)
for text embedding. Use one of the [[embedding
models]{.underline}](https://ollama.com/search?c=embedding) available
through Ollama.
[[This]{.underline}](https://ollama.com/library/nomic-embed-text)
embedding model is lightweight and reports some good benchmark results:
it may be a good one to use.

Third, modify the [[API endpoint for
generation]{.underline}](https://github.com/joshua-zingale/ucr-chatbot-pathway-program/blob/master/ucr_chatbot/api/routes.py)
with the language model. Make it accept useful parameters in json format
to change how the language model responds. The data retrieval method
returns mock data right now, but the interface should remain consistent
as we work to update things.
