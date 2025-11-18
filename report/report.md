---
title: The Development and Introduction in Computer-Science Courses of an AI Tutor
author: Joshua Zingale
abstract: "Teaching with general-purpose generative AI as an aid poses multiple challenges to educators: for instance, providing false information, teaching out-of-scope concepts, and giving full assignment answers to students all lower the degree of confidence with which generative AI may be deployed. We therefore present a prototype AI Tutor. This report covers the AI Tutor's development and deployment in three computer-science courses, from which we collect data to inform future research directions." 
bibliography: references.bib
---

# Introduction

Aligning general-purpose generative AI to meet domain specific needs is an active area of research and development in both academia and industry.

In this study, we introduce a prototype AI Tutor to three UC Riverside computer science sections across two courses. The AI Tutor was made available to all students in the sections and students' usage data were collected.

After a discussion of related works, we describe the AI Tutor's design and functionality.
Next, we describe the development process for the AI Tutor and its means of deployment.
To aid researchers in getting similar studies approved by their Internal Review Boards, we also document some of the contention points from our experience. After we report on some aggregate data from our students' usage, we finally identify future directions of research.

# Related Works


Generative AI, powered by language models, has developed tremendously over the last several years and the number of publications on the topic has exploded [@naveed2025comprehensive].
Language models are now capable enough to understand open-ended messages from human users and to generate textual responses that resemble those of humans.

Seeking a fuller understanding of the limits at which this emergent technology may be used,
educators have taken to implement language models as instructional aids in varying contexts and to varying extents.

For example, @qinjin_jia_llm-generated_2024 and @neyem_exploring_2024 use language models to generate automated feedback on student work. @taylor_dcc_2024 integrated language-model generation into a C compiler to enhance the explanatory power of compiler errors for students. @kazemitabaar_codeaid_2024 created an interactive web environment wherein students can submit code before asking questions about it. In what may be the most comprehensive published adoption of language models in a university course, @liu2024teaching deployed a suite of custom language-model powered tools to provide students with 24/7 support during Harvard's introductory computer science course, including a chat interface for general logistic or material questions, an IDE extension for in-editor assistance, and a bot that contributes to a course forum.

There are two concerns shared among educators who have implemented language models in their
courses: (1) that faulty information may be shared with a student due to *hallucination*,
i.e. the generation of fabricated information [@ji2023survey],
and (2) that too much information may be shared with a student,
such as to complete an assignment for the student.

One approach for combatting hallucination is fine-tuning, which performs additional training of a pretrained language model using a course-specific dataset that is much smaller than the pretraining dataset. However, the compute and cost associated with training a state-of-the-art language model are often prohibitive.
Therefore, Retrieval Augmented Generation (RAG) [@lewis2020retrieval] can be deployed to reduce hallucination [@kirchenbauer2024hallucination]. RAG works by augmenting user prompts with relevant context that should guide the language model's generation.

# The AI Tutor

Retrieval-Augmented Generation (RAG) and prompt engineering wrapped around a pretrained language model to align it for our courses' contexts.
This system was then presented to students via a web interface similar to ChatGPT or Google Gemini.


## Technologies

### Language Model Choice
Having observed the success of large pretrained language models in other works,
and given an extant contract between UC Riverside and Google,
we opted to pick a pretrained model from Google's Gemini lineup.
Among Google's available models, Gemini 2.0 Flash was selected to balance cost with effectiveness.
The effectiveness was gauged by informally prompting multiple models with student-like questions
alongside course-relevant documents, then comparing the responses.
More powerful models were not observed to provide substantive improvement;
however, such a conclusion is not a research finding and should be taken lightly as the evaluation was not empirical nor comprehensive.

### Retrieval Augmented Generation

Taking after recent works, we implemented RAG  to help align generations to our courses' contexts. RAG works by proving contextual information, like sentences from a textbook or website, alongside with a user's prompt to the language model for generation. 


# Development

# Study Approval

# Deployment

# Preliminary Results

# Future Work

@baillifard2025effective showed that an AI Tutor that tracks each student's progress individually
was able to improve course performance significantly.

# References