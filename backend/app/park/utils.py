# flake8: noqa: B950
# pylint: disable=line-too-long

import json
import os

from django.conf import settings
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from openai import OpenAI
from pydantic import BaseModel
from scipy import spatial


def get_features_from_file():
    input_dir = os.path.join(settings.BASE_DIR, "park", "data")
    features_file = os.path.join(input_dir, "features.json")
    features = []

    with open(features_file) as file:
        features = json.load(file)

    return features


def get_embedding(text, model="text-embedding-3-small"):
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    text = text.replace("\n", " ")
    return client.embeddings.create(input=[text], model=model).data[0].embedding


def get_llm_object():
    # Create the OpenAI model
    models = ["gpt-3.5-turbo-0125", "gpt-4o"]
    llm = ChatOpenAI(model=models[1], temperature=0.2, api_key=settings.OPENAI_API_KEY)
    return llm


def cosine_similarity(vector1, vector2):
    return 1 - spatial.distance.cosine(vector1, vector2)


def get_most_relevant_feature(vector_store, sentence):
    pass


def find_feature(sentence_embedding, features):
    best_similarity = float("-inf")
    best_feature = None
    for feature in features:
        similarity = cosine_similarity(sentence_embedding, feature["vector"])
        if similarity > best_similarity:
            best_similarity = similarity
            best_feature = feature

    return best_feature


def get_relevant_features(query_embedding, features, k=5):
    relevant_features = []
    for feature in features:
        similarity = cosine_similarity(query_embedding, feature["vector"])
        relevant_features.append(
            {
                "name": feature["name"],
                "description": feature["description"],
                "similarity": similarity,
            }
        )

    relevant_features = sorted(
        relevant_features, key=lambda x: x["similarity"], reverse=True
    )
    return relevant_features[:k]


class BooleanOutput(BaseModel):
    valid: bool


def get_query_features(query):
    llm = get_llm_object()
    features = get_features_from_file()
    query_embedding = get_embedding(query)
    relevant_features = get_relevant_features(query_embedding, features)

    prompt_template = """
    This text was submitted by a user trying to find out more about accessibility features in a provincial park.
    Your goal is to determine whether the text is asking about the presence or the absence of this specific accessibility feature in the park.

    The sentence was matched to this feature based on the cosine similarity of their respective embeddings.
    Sentence: {query}
    Accessibility feature: {feature}

    If the text asks about the presence of the accessibility feature in the park, return True.
    If the text seems unrelated to the feature or is asking about the absence of the feature, return False.
    """
    validation_prompt = PromptTemplate.from_template(prompt_template)
    results = []
    for relevant_feature in relevant_features:
        prompt = validation_prompt.format(
            query=query,
            feature=relevant_feature["description"],
        )

        structured_output = llm.with_structured_output(BooleanOutput).invoke(prompt)

        if structured_output.valid:
            results.append(relevant_feature["name"])

    return results


def get_feedback_features(description):
    llm = get_llm_object()
    prompt_template = """
    This sentence was submitted by a volunteer and relates to an accessibility feature of a provincial park.
    Your goal is to determine whether the sentence indicates the presence or the absence of the feature in the park.

    The sentence was matched to this feature based on the cosine similarity of their respective embeddings.
    Sentence: {sentence}
    Accessibility feature: {feature}

    If the sentence confirms the presence of the accessibility feature in the park, return True.
    If the sentence explicitly denies the feature or is very unrelated to the mentioned feature, return False.
    """
    validation_prompt = PromptTemplate.from_template(prompt_template)

    features = get_features_from_file()
    sentences = [description]

    results = []
    for sentence in sentences:
        sentence_embedding = get_embedding(sentence)
        relevant_features = get_relevant_features(sentence_embedding, features, k=5)

        for relevant_feature in relevant_features:
            prompt = validation_prompt.format(
                sentence=sentence,
                feature=relevant_feature["description"],
            )

            structured_output = llm.with_structured_output(BooleanOutput).invoke(prompt)
            print("sentence: ", sentence)
            print("feature: ", relevant_feature["name"])
            print("structured_output: ", structured_output)

            if structured_output.valid:
                results.append(relevant_feature["name"])

    return results
