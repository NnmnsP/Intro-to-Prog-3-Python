import os
import asyncio
import aiohttp
import aiofiles
from bs4 import BeautifulSoup

class ImageData:
    def __init__(self, title, img_url):
        self.title = title
        self.img_url = img_url

# get data (text, image or anything) from url
async def downloadAndSave(url, path, session):
    print(path)
    async with session.get(url) as response:
        if response.status == 200:
            data = await response.read()
            f = await aiofiles.open(path, 'wb')
            await f.write(data)
            await f.close()
      
  
async def scrape(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.text()

                soup = BeautifulSoup(data, 'html.parser')

                images = []

                image_blocks = soup.find_all('li', {'class': 'gallerybox'})
                
                count = 0
                for block in image_blocks:
                    count += 1
                    if count > 100:
                       break

                    imgs = block.find_all('img')
                    if len(imgs) > 0:
                        img_url = imgs[0]['src']

                        header = block.find('div', {'class': 'gallerytext'})
                        link = header.find('a')
                        title = link.text
                    
                        images.append(ImageData(title, img_url))
                
                # create images folder if it doesn't exist
                if not os.path.exists('images'):
                    os.makedirs('images')
                
                i = 1
                for image in images:
                    await downloadAndSave(image.img_url, f'images/{i}.jpg', session)
                    i += 1        
      
# run some coroutine (main function)
async def main():
    await scrape('https://commons.wikimedia.org/wiki/Category:Pictures_of_the_day_(2023)')
    
if __name__ == '__main__':
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")