from pathlib import Path
import sys

import pandas as pd
from matplotlib import pyplot as plt

invalid_usage = ValueError("Invalid usage: must have a single argument, the file containing the survey data.")
def main():
    
    if len(sys.argv) != 2:
        raise invalid_usage
    filepath = Path(sys.argv[1])

    with open(filepath) as f:
        df = pd.read_csv(f, skiprows = [1,2]) # type: ignore

    print(f"{len(df)} total respondents")
    df = categorize(remove_previews(keep_only_consents(df)))
    print(f"{len(df)} consented to having their data used in the study.")

    used_ai_tutor_more_df = df[(df["Q2"] != "Prefer not to answer") & (df["Q3"] != "Prefer not to answer") & (df["Q2"].cat.codes > df["Q3"].cat.codes)]
    used_ai_tutor_less_df = df[(df["Q2"] != "Prefer not to answer") & (df["Q3"] != "Prefer not to answer") & (df["Q2"].cat.codes < df["Q3"].cat.codes)]
    used_ai_tutor_same_df = df[(df["Q2"] != "Prefer not to answer") & (df["Q3"] != "Prefer not to answer") & (df["Q2"].cat.codes == df["Q3"].cat.codes)]
    prefer_not_to_answer_ai_tutor_usage = df[(df["Q2"] == "Prefer not to answer") | (df["Q3"] == "Prefer not to answer")]
    print(f"{len(used_ai_tutor_less_df)} used the AI Tutor less that other AI, {len(used_ai_tutor_same_df)} used it the same, and {len(used_ai_tutor_more_df)} used it more, {len(prefer_not_to_answer_ai_tutor_usage)} selected 'Prefer not to answer'")
    # plt.figure(figsize=(10, 7))

    # df["Q2"].value_counts(sort=False).plot(
    #     kind="bar",
    #     title="How often did you use the tutoring chatbot during this academic quarter?", 
    #     rot=40,
    #     ylabel="# of Students")
    # plt.savefig("images/survey-data/Q2.png", bbox_inches="tight") # type: ignore
    # plt.close()
    # df["Q3"].value_counts(sort=False).plot(
    #     kind="bar",
    #     title="How often did you use other generative AI tools for this course? For example, ChatGPT, Gemini, or Claude.\nNote: This survey is anonymous and answering this question will not implicate you in any way for academic dishonesty", 
    #     rot=40,
    #     ylabel="# of Students")
    # plt.savefig("images/survey-data/Q3.png", bbox_inches="tight") # type: ignore
    # plt.close()
    # df["Q4"].value_counts(sort=False).plot(
    #     kind="bar",
    #     title="About what percentage of the time was the AI Tutor correct?", 
    #     rot=40,
    #     ylabel="# of Students")
    # plt.savefig("images/survey-data/Q4.png", bbox_inches="tight") # type: ignore
    # plt.close()

    # df["Q5"].value_counts(sort=False).plot(
    #     kind="bar",
    #     title="Indicate which statement you most strongly agree with:", 
    #     rot=40,
    #     ylabel="# of Students")
    # plt.savefig("images/survey-data/Q5.png", bbox_inches="tight") # type: ignore
    # plt.close()
    # df["Q6"].value_counts(sort=False).plot(
    #     kind="bar",
    #     title="How does the AI Tutor compare to publicly available AI tools like ChatGPT as a study tool?", 
    #     rot=40,
    #     ylabel="# of Students")
    # plt.savefig("images/survey-data/Q6.png", bbox_inches="tight") # type: ignore
    # plt.close()



def keep_only_consents(df: pd.DataFrame):
    return df[df["Q1"] == "I have read and understood the consent form, and I provide my consent to participate in this study."]
def remove_previews(df: pd.DataFrame):
    return df[df["Status"] != "Survey Preview"]
def categorize(df: pd.DataFrame):
    df = df.copy()
    df["Q2"] = pd.Categorical(
        df["Q2"],
        categories=[
            "Prefer not to answer",
            "Never",
            "Fewer than 2 times per week",
            "2-5 times per week",
            "5 to 10 times per week",
            "More than 10 times per week",
        ],
        ordered=True)
    df["Q3"] = pd.Categorical(
        df["Q3"],
        categories=[
            "Prefer not to answer",
            "Never",
            "Fewer than 2 times per week",
            "2-5 times per week",
            "5 to 10 times per week",
            "More than 10 times per week",
        ],
        ordered=True
    )
    df["Q4"] = pd.Categorical(
        df["Q4"],
        categories=[
            "Prefer not to answer",
            "5%",
            "20%",
            "40%",
            "60%",
            "80%",
            "95%",
            "100%"
        ],
        ordered=True
    )

    df["Q5"] = pd.Categorical(
        df["Q5"],
        categories=[
            "The AI Tutor was useful as a personal study tool.",
            "The AI Tutor was somewhat useful as a personal study tool.",
            "The AI Tutor was hardly useful as a personal study tool.",
            "The AI Tutor was not useful as a personal study tool.",
            "Prefer not to answer",
        ],
        ordered=True
    )

    df["Q6"] = pd.Categorical(
        df["Q6"],
        categories=[
            "The AI Tutor is significantly better.",
            "The AI Tutor is better.",
            "The AI Tutor is marginally better.",
            "Other chatbots are marginally better.",
            "Other chatbots are better.",
            "Other chatbots are significantly better.",
            "Prefer not to answer",
        ],
        ordered=True
    )
    return df



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e, file=sys.stderr)
        sys.exit(1)