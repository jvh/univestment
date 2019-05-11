def test2():
   import requests, json
   url = "http://localhost:5555/search"
   data = {
       "image_url": "http://placehold.it/350x150.png",
       "resized_images": True,  # Or True
       "cloud_api": True
   }
   headers = {'Content-type': 'application/json'}
   r = requests.post(url, headers=headers, data=json.dumps(data))
   # r.json to get the response as json
   print(r)

if __name__ == '__main__':
    print('hs')
    test2()
