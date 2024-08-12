import matplotlib
matplotlib.use("TkAgg")
import warnings
warnings.filterwarnings('ignore')
from transformers import pipeline
from pathlib import Path

def run():
    model_writen = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

    #txt = Path('geeksData.txt').read_text()

    #print(txt)

    sentences = ["Lately, I’ve been feeling like there’s no point in anything. Every day feels like a struggle, and I’m constantly overwhelmed by feelings of sadness and hopelessness. It’s like a heavy weight that I can’t shake off, no matter what I do. I often think about how things would be if I weren’t here. The thought of disappearing, of not having to deal with this pain anymore, is becoming more and more appealing. I wonder if anyone would really miss me, or if my absence would even be noticed. It feels like I’m just a burden to everyone around me. When I look in the mirror, all I see is failure. I can’t seem to do anything right, and the future looks so bleak. It’s hard to imagine things ever getting better. I try to reach out to people, but it feels like they don’t really understand what I’m going through. Sometimes, I think it would be easier for everyone if I just wasn’t here. I’ve been thinking about how I would do it. The thoughts come and go, but they’re getting more frequent and more detailed. It scares me, but it also feels like a solution to this never-ending pain. I know I need help, but it’s hard to ask for it. Admitting how I feel seems like it would just add to my sense of failure and disappointment. Every day is a battle to get through. I’m tired of fighting, tired of pretending that everything is okay. The thought of ending it all feels like a way to find peace, a way to stop the constant pain. I know there are people who care about me, but right now, it’s hard to see beyond this darkness."]

    #sentences = [txt]

    # sentences = ["Only you can glue my blue and, Broken, shattered, battered porcelain heart, Tear my soul apart, So dark from smoking poison, Toxic, tainted love, Murder when from you is something holy, Only pure, so beautiful, When she sinks her teeth in me my flesh is red, And I bled out for us, Even hate from you would have me thankful, Only to be in your thoughts, Lonely in your arms, Lonely in your arms, In this violent dawn, Something feels so wrong"]

    # sentences = ["I don't want to live like that anymore."]

    model_outputs = model_writen(sentences)

    print(model_outputs[0])
