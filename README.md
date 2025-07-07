# social-media-happiness-analysis
Each platform usually has its own kind of community, and the way people react and speak varies depending on the platform. I Mohamed Rashad and Alaa Abdelnaser worked on a data analysis project because we were curious to see how people react to the exact same video on Facebook and YouTube.

First, we went through a long research journey to find videos that appeared on both platforms, covering different topics like sports, weddings, social experiments, and politics. We ended up using around 7 different topics and 15 different videos.

Then we used the API to pull YouTube comments. But Facebook didn’t have that option, so we had to use automation tools to collect the Facebook comments. We ended up with around 1000 comments from each platform.

The next step was cleaning the data — which didn’t need too much work. We removed empty rows and most of the comments that weren’t in English because the next step involved a Pretrained Transformer Model that only worked with English.

The closer the score was to 1, the more positive the comment. The model wasn’t super accurate and couldn’t really understand sarcasm, but it was accurate enough for the project.

The outcome: we discovered that people on YouTube were 30% more positive in their reactions than people on Facebook. Interestingly, political videos (we used ones about the Israel-Iran war) received more positive comments on Facebook than videos about weddings or business ideas!

There were even some videos I pulled comments from where I thought “no way someone would say something negative here” — but people always found a way to surprise me. Even when I uploaded a cute baby video, hoping for less negativity, I found a comment wondering what would happen if the baby grew up to be like Hitler!

Sports had a lot of negativity, but I intentionally included controversial stories like Kerri Strug, who completed her Olympic routine even though she knew it would be her last due to injury, and Eric Moussambani, who wasn't ready for the Olympic pool but won because his competitors misheard the start whistle. It made sense for there to be criticism, but there was much more direct attack on the athletes themselves on Facebook than on YouTube.

In general, across all platforms, you’ll always find a large amount of negativity. And maybe it's become harder for people to maintain a positive mindset. But this project might give you a little insight — that often the negativity doesn’t come from the event itself or what’s happening, but from within the person themselves, their tendency to look for what’s wrong, and how much they're influenced by the community and communication style around them.

And here’s the cute baby video — just so you’ve seen something wholesome today 😊:
https://lnkd.in/d64G_wfg

