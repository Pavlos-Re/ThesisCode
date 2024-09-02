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
    result = model_outputs[0][0]
    advice_result = result['label']
    print(advice_result)

    return advice(advice_result)


def advice(advice_result):

        if advice_result == "sadness":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": "Acknowledge what’s happening.",
                        "Advice": "It’s OK to not feel OK. If you are feeling sad, know that you are not alone."
                    },
                    {
                        "Title": "Take care of yourself.",
                        "Advice": " Eat well, exercise, and rest. Take time for yourself. Acknowledge your successes. You are doing the best you can."
                    },
                    {
                        "Title": "Be mindful of how you’re feeling.",
                        "Advice": "While doing an activity you enjoy, focus on the here-and-now. Notice how each part of an activity gives you satisfaction, hope, joy, or stress reduction. This can be as simple as staying present while you are making dinner and enjoying each step in that process."
                    },
                    {
                        "Title": "Maintain connections with others.",
                        "Advice": "Reach out to people you want to connect with, like your friends, family, neighbors, and co-workers."
                    },
                    {
                        "Title": "Get help from a professional, especially if your sadness does not go away.",
                        "Advice": "If you think you may be depressed, the first step to seeking treatment is to talk to a health care provider. This is especially important if your symptoms are getting worse or affecting your daily activities. Depression is not your fault. Getting support helps you and your loved ones."
                    }
                ]
            }

        if advice_result == "joy":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": "Focus on what you can control.",
                        "Advice": "Many possible stressors in life are outside of your control. The weather, how others treat you, your past, natural disasters, your relatives and other aspects of your life exist without your input. While building joy, focus your time and attention on things you can control."
                    },
                    {
                        "Title": "Express gratitude.",
                        "Advice": " Gratitude is being thankful or showing appreciation for the things and people around you. This could be sending positive thoughts to someone special, writing a text message to a friend or listing three things you are grateful for each day. Practicing this daily helps your brain shift its focus to appreciation and blessings, instead of problems and challenges."
                    },
                    {
                        "Title": "Assume good intent.",
                        "Advice": "When stressed, any additional inconvenience or misunderstanding could be viewed as unjust and an intentional barrier to your joy. In most cases, people are simply doing their best with the information and skills they possess, and their actions are not malicious or spiteful."
                    },
                    {
                        "Title": "Concentrate on building relationships.",
                        "Advice": "To various degrees, all people need social connections with others. For many, helping lift others creates a sense of purpose and joy. If building healthy relationships is at the core of your efforts, you can find happiness and joy in your life."
                    },
                    {
                        "Title": "Keep perspective.",
                        "Advice": "Some decisions or situations have serious, long-lasting effects on your life. But often, things that seem important today may only matter a little or not at all in five or 10 years. It's common to recall the feeling of stress or worry years later, but not the actual scenario that caused it."
                    }
                ]
            }

        if advice_result == "neutral":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": "Embrace the Calm.",
                        "Advice": "Neutrality isn't necessarily a bad thing. It can be a period of stability and calmness, a break from the emotional highs and lows. Sometimes, simply being at peace without intense emotions can be refreshing."
                    },
                    {
                        "Title": "Reflect on Your Emotions.",
                        "Advice": "Take a moment to think about why you might be feeling neutral. Are there underlying feelings or situations you're not addressing? Journaling can help you explore your thoughts and emotions more deeply."
                    },
                    {
                        "Title": "Set Small Goals.",
                        "Advice": "If you're looking to shift out of neutrality, setting small, achievable goals can spark a sense of purpose or excitement. Whether it's trying a new hobby, reading a book, or exercising, small steps can lead to bigger changes in mood."
                    },
                    {
                        "Title": "Practice Mindfulness",
                        "Advice": "Mindfulness exercises, such as meditation or deep breathing, can help you connect with the present moment. This practice can make you more aware of subtle emotions or sensations that you might not notice when feeling neutral."
                    },
                    {
                        "Title": "Engage in Gratitude",
                        "Advice": "Even in a neutral state, practicing gratitude can help you find positive aspects of your life. Reflecting on things you're thankful for can subtly shift your mindset towards positivity."
                    }
                ]
            }

        return advice_list
