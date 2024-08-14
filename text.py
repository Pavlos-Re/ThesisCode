import matplotlib
matplotlib.use("TkAgg")
import warnings
warnings.filterwarnings('ignore')
from transformers import pipeline
from pathlib import Path

def run(text):
    model_writen = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

    sentences = [text]

    model_outputs = model_writen(sentences)

    print(model_outputs[0][0])
    result = model_outputs[0]
    return result
