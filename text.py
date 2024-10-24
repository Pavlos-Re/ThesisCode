import matplotlib
matplotlib.use("TkAgg")
import warnings
warnings.filterwarnings('ignore')
from transformers import pipeline
from pathlib import Path
#cardiffnlp/twitter-roberta-base-emotion-multilabel-latest
def run(text):
    model_writen = pipeline(task="text-classification", model="cardiffnlp/twitter-roberta-base-emotion-multilabel-latest", top_k=None)

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

        if advice_result == "anger":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": "Think before you speak.",
                        "Advice": "In the heat of the moment, it's easy to say something you'll later regret. Take a few moments to collect your thoughts before saying anything. Also allow others involved in the situation to do the same."
                    },
                    {
                        "Title": "Once you're calm, express your concerns.",
                        "Advice": "As soon as you're thinking clearly, express your frustration in an assertive but non-confrontational way. State your concerns and needs clearly and directly, without hurting others or trying to control them."
                    },
                    {
                        "Title": "Get some exercise.",
                        "Advice": "Physical activity can help reduce stress that can cause you to become angry. If you feel your anger escalating, go for a brisk walk or run. Or spend some time doing other enjoyable physical activities."
                    },
                    {
                        "Title": "Take a timeout.",
                        "Advice": "Timeouts aren't just for kids. Give yourself short breaks during times of the day that tend to be stressful. A few moments of quiet time might help you feel better prepared to handle what's ahead without getting irritated or angry."
                    },
                    {
                        "Title": "Identify possible solutions.",
                        "Advice": "Instead of focusing on what made you mad, work on resolving the issue at hand. Does your child's messy room make you upset? Close the door. Is your partner late for dinner every night? Schedule meals later in the evening. Or agree to eat on your own a few times a week. Also, understand that some things are simply out of your control. Try to be realistic about what you can and cannot change. Remind yourself that anger won't fix anything and might only make it worse."
                    }
                ]
            }
        if  advice_result == "anticipation":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": "Practice Relaxation Techniques.",
                        "Advice": "When we feel anxious, anxiety can take over our body. It takes a conscious effort to calm it down. To relax, focus on deep breathing. Focusing on breathing can significantly decrease our feelings of panic or nervousness. It can help root us in the present. And if your mind begins to wander, bring it all back to your breath."
                    },
                    {
                        "Title": "Challenge Your Anxious Thoughts.",
                        "Advice": "It may help to challenge our anxious thoughts directly. We can wonder about the best and worst case scenarios of a given situation, then consider if what we’re thinking about is truly realistic. We may not realize how much we catastrophize the future in our heads. If we can acknowledge the uncertainty for what it is and make peace with it, then we can refocus back on the present moment."
                    },
                    {
                        "Title": "Find a Healthy Distraction.",
                        "Advice": "Sometimes, we just need to focus on something other than our anxious thoughts. We can always come back to them and work through them. But it’s okay if you need to take some time to distract yourself with something else. Going for a walk, calling a friend, listening to music, doing chores around the house, reading a book, or watching a show are all healthy ways to divert our focus for a bit."
                    },
                    {
                        "Title": "Take Action.",
                        "Advice": "Anticipatory anxiety can lead us to put off important things. We may search for ways to avoid the experiences that we fear. Although there is a lot beyond our control, there are still small things we can do to take action and feel less anxious than before. If you’re worried about the climate crisis, donate your time or money to an organization that helps with the cause. Or if you’re worried for the health of your loved ones, give them a call to connect with them and share life updates with them. There’s small ways that we can actively address our fears."
                    },
                    {
                        "Title": "Speak to Someone About It.",
                        "Advice": "It may help to talk to a trusted loved one about our concerns. They can be a source of comfort when we are feeling overcome with worry. However, if you are still experiencing persistent anticipatory anxiety, consider seeking professional help through therapy. At Eugene Therapy, our compassionate therapists will listen to your concerns and provide useful tools to manage your anxiety."
                    }
                ]
            }
        if  advice_result == "disgust":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": "Notice when judgmental thoughts pop into your head.",
                        "Advice": "Being aware uses the frontal lobe of your brain. When you activate your frontal lobe, you automatically calm an impulse like disgust. Make a mental note that you are ready to look at the bigger picture."
                    },
                    {
                        "Title": "Remember to breathe.",
                        "Advice": "Calming breaths also engage your frontal lobe. Practice deep breathing in moments when you are not feeling disgusted, so your body becomes used to it and can call on this new habit as soon as you sense a need to override the onset of such negativity."
                    },
                    {
                        "Title": "Don't let your feelings control your thinking.",
                        "Advice": "Feeling an overabundance of disgust is a habit formed early in life, which may or may not tie in with your values and beliefs. When you convince yourself you're entitled to feel disgusted, you also tell yourself that you're a victim. Being a victim feels disgusting. It is a self-destructive habit you must recognize and break."
                    },
                    {
                        "Title": "Do the opposite of what you're feeling.",
                        "Advice": "Sneering is one of those automatic reactions we have when we are judgmental. The opposite of sneering is finding a place inside yourself where you feel kind, respectful, and caring. This is your only way out when you feel disgust (in the present or when remembering a time you felt so in the past). Before you go to bed, take a note of lingering judgmental thoughts and remind yourself to look at the bigger picture. Reframe your feelings."
                    },
                    {
                        "Title": "Remember, it's not about you.",
                        "Advice": "For example, if someone cuts you off in traffic, they have no idea who you are as a person, and in that moment they couldn't care less."
                    }
                ]
            }
        if  advice_result == "fear":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": "Take time out.",
                        "Advice": "It’s difficult to think clearly when you feel scared or anxious. If you can, take time out to physically calm down. Try and get away from what’s upsetting you. For example, you could do another activity for 15 minutes."
                    },
                    {
                        "Title": "Breathe through panic.",
                        "Advice": "If you start to get a faster heartbeat or sweaty palms, try not to fight it. Stay where you are and let yourself feel the fear, even though it will be uncomfortable. Place the palm of your hand on your stomach and breathe slowly and deeply. The aim is to get your mind get used to coping with panic, which takes away the fear of feeling panicky."
                    },
                    {
                        "Title": "Face your fears.",
                        "Advice": "Avoiding fears only makes them worse. But, gradually exposing yourself to the thing you’re scared of can help you maintain control and overcome your fear. If you face your fear you might find that it isn’t as scary as you thought. For example, if you panic getting into a lift one day, it’s best to get back into a lift the next day."
                    },
                    {
                        "Title": "Remember that anxiety isn’t harmful.",
                        "Advice": "Anxiety and fear can feel overwhelming. You may worry that the signs of anxiety and panic, like a fast heartbeat, are signs of a serious health problem. These concerns can make anxiety and fear worse. So, it’s important to remember that your body’s response to fear is normal. It’s designed to protect you from danger. If you feel worried about your health, speak to your GP practice."
                    },
                    {
                        "Title": "Challenge unhelpful thoughts.",
                        "Advice": "It can sometimes help to challenge unhelpful thoughts. If you ask yourself the right questions, you can show yourself there isn’t anything to worry about. For example, if you’re scared of getting trapped in a lift, you could ask yourself questions like: “Have you ever heard of someone getting trapped in a lift?” “Does the lift look broken?” “Is there any reason to think that if I did get stuck, help would take a long time to arrive?”"
                    }
                ]
            }
        if  advice_result == "love":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": "Take time to name and process your emotions.",
                        "Advice": "Love is overwhelming, so it'll be important to deal with your feelings. Falling in love may cause you to feel things you’re not used to, like euphoria, anxiety, giddiness, nerves. If you’ve been feeling completely out of whack, don’t stress—that’s normal. These feelings will become more manageable as time goes on, especially if you work to process them in healthy ways."
                    },
                    {
                        "Title": "Talk to a friend.",
                        "Advice": "Discussions can help you express emotions in healthy ways. It can feel impossible to keep feelings of love to yourself, and you shouldn’t always have to. Choose a friend you trust and consider sharing your experience with them. This way, you can get some things off your chest, they may offer you some great advice, and, by talking it out with them, you may even get more clarity on how you’re feeling."
                    },
                    {
                        "Title": "Pamper yourself.",
                        "Advice": "While processing complicated emotions, you deserve to feel treated. Sometimes, love may make you feel like you’re underwater, completely consumed by your feelings. By investing time in you, you're sending yourself some important messages: that you love yourself, you take care of yourself, and you deserve to feel good, no matter what."
                    },
                    {
                        "Title": "Find healthy, fulfilling distractions.",
                        "Advice": "Spending time thinking about other things can help you recharge. When love is constantly on the brain, you may start to feel exhausted. If you’re struggling to think of anything else, filling your schedule with distracting activities can help. These time-fillers should positively affect your mood and help you turn off your thoughts."
                    },
                    {
                        "Title": "Be kind to yourself.",
                        "Advice": "Love can affect your self-confidence, but self-love can help. When you’re in love, especially if you’re worried that the other person may not feel the same, it’s so easy to question your value as a person. You may realize that you’re blaming another person’s feelings on yourself, even though those feelings are completely out of your control."
                    }
                ]
            }
        if  advice_result == "optimism":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": "Keep a gratitude journal.",
                        "Advice": "Write every day in a gratitude journal. A gratitude journal is a place where you regularly write things you feel grateful for. The things you're grateful for can be small, such as a good meal or a sunny day. They can also be larger or more complex, such as a loved one, a stable career or freedom. Consistently recognizing the things you're grateful for can help you refocus on the positives in your life and foster a more optimistic perspective."
                    },
                    {
                        "Title": "Create positive mantras.",
                        "Advice": "Develop positive mantras, affirmations or aphorisms for yourself. An affirmation is a message you repeat to yourself throughout the day that has a positive message. You can write down your mantras and read them regularly or simply think about them."
                    },
                    {
                        "Title": "Be positive around others.",
                        "Advice": "Strive for positive interactions with other people. Try giving people more genuine compliments or acknowledging their successes.Some positive interactions may acknowledge negative situations but ultimately focus on the beneficial aspects. For example, if a coworker feels sad, try to comfort them and find a solution to their problem instead of only commiserating."
                    },
                    {
                        "Title": "Find the good in challenging situations.",
                        "Advice": "Look for the positive aspects even when facing a challenge in your life. Optimists understand that there can be benefits to even difficult situations. For example, if you missed a deadline for a project at work, focus on what you learned from the experience, such as better productivity strategies you can use in the future."
                    },
                    {
                        "Title": "Consciously think positive thoughts.",
                        "Advice": "Create happy thoughts for yourself. While it might feel strange to purposefully give yourself positive thoughts, doing so can help train your brain over time to naturally provide more positive messages and beliefs."
                    }
                ]
            }
        if  advice_result == "pessimism":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": " Repeat positive affirmations.",
                        "Advice": "One way to keep pessimism at bay is by repeating positive statements to yourself. Try writing down a few simple positive affirmations somewhere within your reach and repeat them often."
                    },
                    {
                        "Title": "Practice gratitude.",
                        "Advice": "Pessimists tend to hold on to adverse experiences. Try flipping that script and write down a list of good things that have happened in the past and everything you appreciate. And when you recite your affirmations, also tell yourself something that you are grateful for."
                    },
                    {
                        "Title": "Practice mindfulness.",
                        "Advice": "Mindfulness is being present without judgments. Thus, you avoid attaching a negative label to everything when you practice mindfulness and see things in a more neutral (or realistic) light."
                    },
                    {
                        "Title": "Reframe your thoughts.",
                        "Advice": "If you catch yourself expecting adverse outcomes, try to reframe your thoughts. For example, if you tell yourself, “I don’t want to go to this party because I won’t enjoy it,” try saying, “I may or may not enjoy the party, but I won’t know if I don’t go.”"
                    },
                    {
                        "Title": "Do what you can, and hope for the best.",
                        "Advice": "You may still expect the worst. When thinking about a future event, it is important to remember that terrible things are actually rare. And if you put in enough effort and are prepared for the worst, great things do indeed happen.​"
                    }
                ]
            }
        if  advice_result == "surprise":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": "Acceptance.",
                        "Advice": "When life throws us some hardship, our first response could be a denial or disbelief. You may want to stay in denial for a while as a way to protect yourself. You may be thinking your partner is just threatening to leave, and he/she will be back. May be that promotion seemed to be yours until you were passed again. Some people stay in disbelief to avoid the despair, not really prepared to face reality. Acceptance is a gradual process, and if you’re not ready, you can take small steps. Remember you can only change yourself and your response to events. Accept what you cannot change."
                    },
                    {
                        "Title": "Acknowledge your feelings.",
                        "Advice": "You may experience a wide range of feelings from confusion, fear to sadness or relief. The longer you try to hold on to the old, the longer it will take you to recover. Allow yourself to be sad or upset if this is a loss but also pay attention to what might be the silver lining. What’s the meaning of all this? It is often helpful to have a therapist or someone close that you help you sort through this. Sometimes the universe brings us change quicker than we expected. Sometimes we just don’t have the courage to move forward until we find ourselves in a new place."
                    },
                    {
                        "Title": "Face what you’re most afraid of.",
                        "Advice": "Things can look really overwhelming until you’re willing to lean in the uncomfortable. Counseling could be helpful to explore your fears in a safe place but you can also journal. Tune in and see what is keeping you stuck. Learn to be an observer of what’s going on inside your skin. If we know our thoughts and emotions they tend to scare us less. You want to move in the direction of love and courage, instead of fear."
                    },
                    {
                        "Title": "Reframe.",
                        "Advice": "See the unexpected situation as an invitation to change and evolve. When there’s pain, we are far more inclined to take risks, to take action, and look deep down inside. Get to know who you are and what’s meaningful at this time. Keep in mind this may be an unfamiliar territory, and you may have to improvise or attempt new solutions. This may be a call to deal with our challenges in new ways that create more meaning and wholeness."
                    },
                    {
                        "Title": "Do something different or make new choices.",
                        "Advice": "The new situation may require you to break old habits or respond in new ways. Your default way of handling this, may be outdated, and this is a time to come up with new strategies. Doing the same old things – working endless hours or avoiding the truth, the debt or facing your partner – may no longer work. Whether it’s negativity, passivity, avoidance, this is a call to do something different."
                    }
                ]
            }
        if  advice_result == "trust":
            advice_list = {
                "AdviceList": [
                    {
                        "Title": "Learn how trust works.",
                        "Advice": "Some people trust until they have a reason not to — others don’t trust people until that trust is earned. It’s up to you if and when you choose to trust someone. It’s perfectly okay to wait for someone to earn your trust before deciding you can rely on them. Especially if you’re recovering from past betrayal."
                    },
                    {
                        "Title": "Take emotional risks.",
                        "Advice": "At some point, you’ve got to just jump in head-first. Allow yourself to be vulnerable and choose to trust (whether it’s at the beginning of a relationship or after they’ve earned your trust)."
                    },
                    {
                        "Title": "Consider those you do trust and express your appreciation.",
                        "Advice": "Friends and family members who have always been there are easy to take for granted unless you make a conscious effort to show them your appreciation. When you have a problem, those are the people you can trust to be a support network. In addition, you can learn a lot about who, what, why, and how you trust from these relationships."
                    },
                    {
                        "Title": "Distinguish Between Trust and Control.",
                        "Advice": " People with trust issues often feel a need for control. This can sometimes manifest as mistrusting behavior. You might feel like you are being betrayed or taken advantage of if you don't have complete control over every situation. However, this will only hurt your relationships in the long run. Learning how much control you should yield in a given situation is key to building trust with other people. "
                    },
                    {
                        "Title": "Make Trust a Priority.",
                        "Advice": "Trusting others can be difficult, but trust-building is an essential part of any relationship, romantic or otherwise. Make trust a priority in your life—even if it's challenging to do."
                    }
                ]
            }

        return advice_list

# if __name__ == "__main__":
#    run("the date was a very nice day")
