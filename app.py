
import random
import requests
import streamlit as st

passages=[
    
"""Some hawkish members of Congress say Biden should have already imposed sanctions as a consequence of moving troops. Russia, which 
insists that the United States pledged not to expand NATO after the Soviet Union's collapse, has sought guarantees that the alliance will 
not accept Ukraine or establish bases in more former Soviet republics. Western officials say that Russia cannot dictate to Ukraine whether to join NATO.""",

"""It's not cost-free by any means. But the big loser in that decision will be the Russians. Russia had already injured itself against some economic pressure 
since 2014 when the West imposed sanctions over its seizure of Crimea.""",

"""The updated Russian National Security Strategy, issued in December 2015, ‘upgraded’ the language describing the Alliance, stating that NATO activities constitute 
“a threat to the national security” of Russia""",

"""The conflict in eastern Ukraine, which still rages, has been a tragedy for Ukrainians, 14,000 
of whom have died so far. Part of the southeastern border of Ukraine is now a war zone periodically ravaged by artillery fire, mine explosions and sniper 
fire exchanged between the Ukrainian military and the pro-Russian separatists.""",

"""But for all of its terrible human toll, it has remained a localized conflict. 
Should Putin escalate Russia’s intervention in Ukraine this winter, it would almost certainly be on a larger, even more overt scale that would not only cause
much more destruction, but also have reverberations far beyond Ukraine. So it’s urgent that the U.S. do what it can to discourage such an attack.""",

"""The main idea was to convince Putin that the costs would be "very high" to an invasion.The whole idea is to make it clear to Mr. Putin that he has a choice," 
One immediate measure would likely be sanctions against Putin's inner circle and their families, depriving them of the right to travel or keep money in the West."""

"""Germany has indicated that the cost of a Ukraine invasion could be ending Nord Stream 2 -- the gas pipeline from Russia that is nearly complete despite years of 
criticism from the United States and Eastern European nations. One far-reaching option mulled in the West would be cutting Russia off the SWIFT network that connects
the world's banks, a step earlier taken against Iran but not attempted against a major global economy. But action through SWIFT, based in Belgium, would inevitably 
hurt third-nation businesses and would be unlikely to gain global consensus unless Russia brazenly defies warnings.""",

"""Ukraine imports most of its oil from Russia - although recent discoveries of shale gas in the country mean it may become less dependent on Russian supplies in future.""",

"""In early 2013 the Russian leadership introduced the practice of conducting exercises for large groups of forces without a prior announcement to the units concerned, aimed at 
testing their ability to rapidly mobilise, deploy and complete assigned combat tasks.""",

"""Firstly, nuclear-related and large-scale conventional exercises have served to amplify the basic deterrence message: any attempts to influence Russian foreign or security policy 
through military coercion, take back Crimea, or interfere with Russia's internal policy-making process, can and will be countered with military means.""",

"""In November 2014, the Ukrainian military reported intensive movement of troops and equipments from Russia into the separatist-controlled parts of the eastern Ukraine.
The Associated Press reported 40 unmarked military vehicles on the move in rebel-controlled areas. The Organization for Security and Co-operation in Europe (OSCE) 
Special Monitoring Mission observed convoys of heavy weapons and tanks in DPR-controlled territory without insignia. OSCE monitors further stated they observed 
vehicles transporting ammunition and soldiers' dead bodies crossing the Russian-Ukrainian border under the guise of humanitarian aid convoys.""",

"""Despite being an independent country since 1991, as a former Soviet republic, Ukraine has been perceived by Russia as being part of its sphere of influence.
Iulian Chifu and his co-authors claim that in regard to Ukraine, Russia pursues a modernized version of the Brezhnev Doctrine on "limited sovereignty", 
which dictates that the sovereignty of Ukraine cannot be larger than that of the Warsaw Pact prior to the demise of the Soviet sphere of influence.
This claim is based on statements of Russian leaders that possible integration of Ukraine into NATO would jeopardize Russia's national security.""",

"""The 2021-22 Russo-Ukrainian crisis is an ongoing military confrontation and international crisis between Russia and Ukraine that started in late October 2021.
The crisis has caused international tension, also involving the United States, NATO, the European Union and the Commonwealth of Independent States.""",

"""Ukraine has sharply intensified diplomatic efforts. On 15 November, 2021, Volodymyr Zelensky and the head of the European Council Charles Michel discussed 
"the security situation along the borders of Ukraine." On the same day, Dmytro Kuleba held talks on the same issues in Brussels.""",

"""The new head of the Defense Ministry, Oleksii Rezikov, went to Washington, where on 18 November,2021, he met with US Secretary of Defense Lloyd Austin. 
On 16 November,2021, British Defense Minister Ben Wallace visited Kyiv. According to the tabloid Daily Mirror, a consolidated rapid response unit of about 
600 fighters has been formed in the UK for transfer to Ukraine.""",

"""Vladimir Putin, a bold opportunist, is putting into play his most daring and menacing gambit yet. By threatening a major invasion of Ukraine, 
Putin figures he can achieve his fondest goals: Rendering Ukraine a vassal state of the Kremlin with no hope of its becoming a genuine, independent European country. 
This is critical to Putin’s desire to make puppets of all the nations that broke away from the old Soviet Empire.""",

"""In return for not invading Ukraine, Putin wants Biden to acquiesce to his making Kiev a political and economic subsidiary of the Kremlin.
But Putin has an even grander goal: neutering the credibility of NATO by having Washington agree to not placing a genuine military presence in 
NATO nations bordering or near Russia, particularly Poland and the Baltic states of Lithuania, Latvia and Estonia.
Such an agreement would severely undermine U.S. security credibility with European and Asian nations. 
That kind of basic uncertainty and insecurity would have ugly consequences. Putin—and Beijing—are licking their chops over such an outcome.""",

"""At the top of the agenda for the call Thursday afternoon between President Joe Biden and Russian President Vladimir Putin was the huge military force 
Russia has been amassing to the north, east and south of Ukraine. According to a statement released by the White House, Biden “made clear that the 
United States and its allies and partners will respond decisively if Russia further invades Ukraine.”""",

"""Putin’s troops look poised to attack in what might seem like a repeat of 2014. On that occasion, following
Putin’s seizure of the Crimean Peninsula, Russian military units rolled into eastern Ukraine in a successful bid to prevent Ukraine’s military from defeating 
Russian-speaking Ukrainian separatists backed by Moscow.""",

"""These days it feels like we are back in the days of Soviet leader Leonid Brezhnev. One could not help but feel transported to the 1970s based on Russia's national media.
Warmongering rhetoric is back and so is staple criticism of the decadent West. Back-to-the-past seems to be the mood in Moscow’s foreign policy, too. US-Russia summitry is
becoming a regular feature of relations, a flashback to the height of the Cold War.""",

"""On December 30,2021, US President Joe Biden and Russian President Vladimir Putin had a phone call to discuss tensions over Ukraine. Reportedly, each of them issued warnings to the 
other side but overall the tone was “constructive”.The exchange came on the heels of a meeting between the two leaders via a video link held on December 7, 2021 
to discuss a number of issues, including Ukraine. Six months earlier they held a face-to-face summit in Geneva, which resulted in the return of the US and Russian ambassadors to the respective capitals.""",

"""Communication has intensified at different government levels, as well. In early November, William Burns, CIA director and former ambassador to Russia, travelled to Moscow, where he met Putin, 
Russia’s Security Council Secretary Nikolai Patrushev and Russian Foreign Intelligence Service chief Sergei Naryshkin to discuss tensions with Ukraine. US National Security Adviser Jake Sullivan has also been in contact with Putin’s foreign policy aid Yuriy Ushakov."""

"""For the Kremlin, having Biden’s full attention is a success. It is a clear sign that amassing troops and threatening military action 
against Ukraine works. During the past six years, Moscow has grown frustrated with the deadlock in the Ukrainian conflict. The Minsk II Agreement 
forged in 2015 with the mediation of France and Germany has failed to end the fighting.Kyiv and Moscow are blaming each other for the lack of progress.""",

"""The Russians are claiming Ukraine has not delivered on its commitment to implement constitutional changes granting broad autonomy to the self-proclaimed 
Donetsk and Luhansk People’s Republics as a step towards reintegrating them. The Ukrainians, for their part, are accusing Russia of not allowing the government in 
Kyiv to restore control over the Russian-Ukrainian border."""

"""To overcome the deadlock, the Kremlin would like to force a new deal and do it through the US, bypassing Paris and Berlin. 
The idea is that Ukrainian President Volodymyr Zelenskyy would be presented with a fait accompli and would have no choice but to fall in line.
But in engaging with the US, Russia has also raised the stakes.""",

"""On December 17, 2014 the Russian foreign ministry circulated two treaty proposals, 
one with the US and one with NATO. They put forward a demand for the Atlantic Alliance to rescind the promise made to Ukraine and 
Georgia in April 2008 that they could one day join. The draft furthermore requires NATO not to station large combat forces in its eastern 
members, as it started doing following Russia’s 2014 annexation of Crimea. Moscow also wants NATO to commit not to deploy intermediate-range missiles close to its borders.""",

"""Last but not least, the proposals call for an end to military assistance to Ukraine, whether provided by the US or through NATO, as well as a halt on 
alliance exercises involving post-Soviet countries.""",

"""In essence, Russia wants to turn the clock back to the late 1990s, evicting the West from Eastern 
Europe and cementing its hegemonic position in its so-called “near abroad”. In pursuing those goals, the Kremlin is leveraging its military clout. 
According to estimates, more than 100,000 Russian troops and heavy weaponry are currently deployed near the Russian-Ukrainian border as well as 
in the annexed Crimean Peninsula.""",

"""A good part has been deployed since early 2021. An operation against Ukraine is, therefore, not off the table. 
Putin might be bluffing but should he decide to move against the neighbouring country, he would have no trouble whatsoever.
The US and its European allies’ response has been to draw Russia to the negotiating table in order to defuse the tensions..""",

"""After the active diplomatic outreach by the Biden administration, in late December, Russian Foreign Minister Sergey Lavrov announced talks would be held January 10,2022.
A Russia-NATO meeting is taking place two days afterwards. Even if the bulk of the Russian proposals are non-starters for the West,
engaging in a diplomatic process is preferable to violence""",

"""If everything goes well, there might be some limited progress too, especially on “deconfliction” in areas where NATO and Russia face off, 
such as the Black and the Baltic Seas. Over time, talks could yield partial security agreements acceptable to both parties as well as to the likes 
of Ukraine and Georgia which, contrary to what the Kremlin believes, have interests and agency of their own.
But to be sure, there is plenty of scepticism, too. """,

"""Some pundits are suggesting that Russia’s publication of the draft treaties, 
before the actual talks, is a clever ploy to undermine the diplomatic track and create a pretext for military action against Ukraine.""",

"""To succeed in this game, the US and its allies need to negotiate with the Russians from a position of strength. As in Brezhnev’s days, 
they need to credibly deter Moscow in order to open space for real negotiations. That is why, the US is communicating to Putin 
its readiness to ramp up economic sanctions - “like none he’d ever seen”, in Biden’s words - in case of war.""",


"""However, it is not clear to what extent European allies would follow suit. In France, President Emmanuel Macron has been calling for caution. 
Germany’s new governing coalition between the left, the Greens and the liberals, could find itself divided on the issue, with Chancellor Olaf
Scholz taking a dovish line and Foreign Minister Annalena Baerbock pushing for a tough response. Needless to say, Russia will do its best to
exploit any political rifts that might emerge within NATO. Thus far Putin’s strategy is paying off.""",

"""Moscow has been transacting with Washington
as a near geopolitical peer. At a time, when the US is fixated on rising China, this is no small feat. Brezhnev’s USSR may be long gone and today’s
Russia may be a pale shadow of its predecessor, but from the Kremlin’s perspective, it is doing its best to stay in the game.""",

"""The U.S. and its allies may further reinforce NATO’s eastern flank with major ground and air units. They might increase stocks of PGMs, such as the new medium-range 
ballistic Precision Strike Missile. Given Russia’s potential mass use of long-range PGMs, NATO may have to improve its aerospace defenses. """,

"""There is no U.S. or NATO consensus to insert their own combat forces into Ukraine. One reason may be fear that direct combat could lead to a wider 
European war, perhaps even risking a Russian nuclear threat.""",

"""Russian President Vladimir Putin has said that in 2014 “we were ready” to put nuclear weapons on alert.
In 2018, he showed a boastful video simulating a nuclear-armed missile attacking Florida. While Ukrainians may be unable to defeat a large-scale invasion, 
they could inflict high casualties, a sensitive issue in Russia.""",

"""Russian occupying forces might bestretched thin and vulnerable to stay-behind insurgents. In sum, the U.S., its NATO allies and Ukraine could impose immediate and painful costs 
on any Russian invaders. And for many years thereafter, Russia could face reinforced NATO military power.""",

"""Recent days have seen a new flurry of Western media reports that U.S. intelligence believes that Russia is planning to invade Ukraine early in the new year. 
These reports have already led to warnings by NATO and Washington that Russia would pay a heavy economic and political price in the event of a war.
Russia, for its part, has denied the dire nature of the reports, blaming “a targeted information campaign,” according to Dmitry Peskov, President Vladimir 
Putin’s spokesman, on Monday.""",

"""“This is building up tension.” Nevertheless, this should also lead to a determined and sincere new effort by the United
States and leading European governments to find a reasonable compromise with Russia over the Ukrainian disputes. For quite apart from the global economic 
damage that would result from a war in Ukraine, and the ways in which China would take advantage of such a crisis, the West has a very strong reason indeed to 
avoid a new war: the West would lose.""",

"""At the same, we have seen that forceful responses drive Russia closer to China. This was the case after the various rounds of sanctions imposed on Russia after 2014 and Russia is 
probably banking on Chinese economic support this time too, both as a safety net and as a tool to force U.S. concessions.
Russia and China’s alignment builds on shared values and interests, and the West should prepare for a joint Russia-China front, 
be that in the information sphere or in the military realm""",

"""Russia and China can easily exploit increased tensions in each other’s regions to 
enhance their own positions. Should war break out between Russia and Ukraine, and keep the U.S. and Europe preoccupied, 
China could seize the opportunity, militarily or by other means, to enhance its position vis-à-vis Taiwan, and vice versa.""",

"""After 20 years of Putin, Western countries have still not devised a comprehensive strategy to combat his ability to disrupt those he perceives as adversaries."""]

st.header("The Problem of Evil")
st.subheader("This demo uses different ML models to help people think about different shapes of the future.")
Ques = st.text_input(label='Insert a question.')



Question_topic =[]
Passage_topic =[]
Relevant = []
passages_array=[]
final_passage = []






def query():
    API_URL = "https://api-inference.huggingface.co/models/cross-encoder/nli-distilroberta-base"
    headers = {"Authorization": "Bearer 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"}
    payload = {
        "inputs": Ques,
        "parameters": {"candidate_labels": ["europe","ukraine", "russia", "united states", "china", "nato", "crimea", "diplomacy", "war"]},
    }
    output = requests.post(API_URL, headers=headers, json=payload)
    response = output.json()
    Question_topic.append(response)


    for passage in passages:
        payload = {
        "inputs": passage,
        "parameters": {"candidate_labels": ["europe","ukraine", "russia", "united states", "china", "nato", "crimea", "diplomacy", "war"]},
    }
        output = requests.post(API_URL, headers=headers, json=payload)
        response = output.json()
        Passage_topic.append(response)
    return Question_topic, Passage_topic


def query_result():
    for i in range(len(Passage_topic)):
        if Question_topic[0]['labels'][0] == Passage_topic[i]['labels'][0]:
            passages_array.append(Passage_topic[i]['sequence'])
    if len(passages_array) < 5:        
        while len(passages_array) < 6:
            for i in range(len(Passage_topic)):
                if Question_topic[0]['labels'][1] == Passage_topic[i]['labels'][0]:
                    passages_array.append(Passage_topic[i]['sequence'])
    return passages_array

def randompicker():
    final_passage.append(random.sample(query_result(),5))
    # conct_passage = " ".join(final_passage[0],final_passage[1],final_passage[2])
    return final_passage

def summarization():
    API_URL = "https://api-inference.huggingface.co/models/sshleifer/distilbart-cnn-12-6"
    headers = {"Authorization": "Bearer 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"}
    payload = ({
    "inputs": randompicker(),
    })
    output = requests.post(API_URL, headers=headers, json=payload)
    response = output.json()
    return response


def answering():
    API_URL = "https://api-inference.huggingface.co/models/phiyodr/bart-large-finetuned-squad2"
    headers = {"Authorization": "Bearer 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"}
    for i in range(len(final_passage)):
        payload = ({
        "inputs": {
            "question": Ques,
            "context": randompicker()[0][i],
            },
        })
        output = requests.post(API_URL, headers=headers, json=payload)
        response = output.json()
        if response["answer"] !=  None:
            st.write("Answer: " + response["answer"])


def questioning():
    API_URL = "https://api-inference.huggingface.co/models/Salesforce/mixqg-large"
    headers = {"Authorization": "Bearer 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"}
    payload = {"inputs": random.choice(randompicker())}
    
    output = requests.post(API_URL, headers=headers, json=payload)
    response = output.json()
    st.write("Question: " + response[0]["generated_text"])
    st.write("Question: " + response[1]["generated_text"])
    st.write("Question: " + response[2]["generated_text"])
    return response

if (not len(Ques)==0):
    query()
    answering()
    questioning()

















