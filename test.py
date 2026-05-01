import urllib.request
import re
import json

words = ['hello', 'hi', 'goodbye', 'thankyou', 'thanks', 'please', 'sorry', 'yes', 'no', 'drink', 'home', 'good', 'bad', 'name', 'family', 'friend', 'work', 'school', 'pain', 'doctor', 'toilet', 'food', 'brother', 'sister', 'mother', 'father', 'what', 'where', 'why', 'how', 'time', 'money', 'day', 'love', 'help', 'water', 'eat', 'i', 'you', 'my']

out = {}
for w in words:
    try:
        url = f'https://www.lifeprint.com/asl101/pages-signs/{w[0]}/{w}.htm'
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
        gifs = re.findall(r'src=["\']([^"\']+\.gif)["\']', html, re.IGNORECASE)
        valid = [g for g in gifs if 'transparent' not in g.lower() and 'space' not in g.lower()]
        if valid:
            gif_url = valid[0]
            if not gif_url.startswith('http'):
                if gif_url.startswith('../../'):
                    gif_url = 'https://www.lifeprint.com/asl101/' + gif_url[6:]
                else:
                    gif_url = f'https://www.lifeprint.com/asl101/pages-signs/{w[0]}/{gif_url}'
            out[w] = gif_url
    except Exception as e:
        pass

print(json.dumps(out, indent=2))
