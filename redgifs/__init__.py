import requests, redgifs

class Redgifs:
    def __init__(self, token=False):
        if not token:
            self.token, self.ip, temp, temp, temp = requests.get('https://api.redgifs.com/v2/auth/temporary').json().values()
        else:
            self.token = token
        self.url = "https://api.redgifs.com"

    def request(self, path):
        return requests.get(f"{self.url}{path}", headers={"Authorization": f"Bearer {self.token}"})

    def toGif(self, d):
        gs = self
        class gif():
            def __init__(self, data):
                self.data = data
                self.id = data['id']
                self.hasAudio = data['hasAudio']
                self.likes = data['likes']
                self.tags = data['tags']
                self.verified = data['verified']
                self.views = data['views']
                self.duration = data['duration']
                self.published = data['published']
                self.author = data['userName']
                self.url = f"https://www.redgifs.com/watch/{self.id}"

            def getSimilarGifs(self):
                return gs.getSimilarGifsTo(self.id)

            def download(self):
                gs.download(self.id)
        return gif(d)

    def getGifsById(self, id):
        
        return [self.toGif(i) for i in self.request(f"/v2/gifs?ids={','.join(id.split())}").json()["gifs"]]

    def getGifById(self, id):
        return self.toGif(self.request(f"/v2/gifs/{id}").json()["gif"])

    def getSimilarGifsTo(self, name):
        return [self.toGif(y) for y in self.request(f"/v2/recommend/tags/{name}").json()["gifs"]]

    def download(self, id, filename=False, download=True, quality="hd"):
        filename = f"{id}.mp4" if not filename else filename
        sess = requests.Session()
        request = sess.get(f"https://api.redgifs.com/v2/gifs/{id}", headers={"Authorization": f"Bearer {self.token}"})
        if request is None: raise Exception("Netword or API error (seems like a skill issue LMAOO)")
        url = request.json()["gif"]["urls"][quality]
        if download:
            with sess.get(url, stream=True) as r:
                with open(filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192): f.write(chunk)

        return url

    def search(self, keyword, count):
        print("hellooo")
        print(f"/v2/gifs/search?search_text={'+'.join(keyword.split())}&order=trending&count={count}")
        if not (10 <= count <= 80): raise Exception("The Number of Gifs Cannot be less Than 10 and it Cannot Exceed 80.")        
        print(self.request(f"/v2/gifs/search?search_text={'+'.join(keyword.split())}&order=trending&count={count}").json())
        return [self.toGif(i) for i in self.request(f"/v2/gifs/search?search_text={'+'.join(keyword.split())}&order=trending&count={count}").json()["gifs"]]
    

    
