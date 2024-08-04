## xG Fantasy Helper

This is a small project that I started out of curiosity. I wanted to build something using Django and be able to deploy it using GCP App Engine. It's ugly, simple and unfinished but was created just for learning purposes.

The App scrapes data from FBref.com and creates 7 tables per league, for the top 5 Football/Soccer leagues in the world. The tables heavily use [xG (Expected Goals)](https://fbref.com/en/expected-goals-model-explained/).
- **Squad Index:** metric created by me that measures the team moment, giving more value to omre recent results and considering only the last 5 games for the team
- **Squad xG:** Used to identify the most attacking teams in the league
- **Squad xGA:** Used to identify the best defensive teams in the league
- **Player npxG:** Ranks league players by non-penalty expected goals
- **Player npG-xG:** Ranks league players by how they outperformed their non-penalty expected goals
- **Player Assists:** Ranks league players by expected assists
- **Keepers:** Ranks goalkeepers by how they outperformed the expected goals against them

Deployment was done following this guide: [Running Django on the App Engine standard environment](https://cloud.google.com/python/django/appengine#windows_4)

**Disclaimer:** All data found here belongs to FBref. This app was created only for learning purposes.
