import aiohttp
import asyncio
from userge import userge, Message

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            return await response.json()
    except aiohttp.ClientError as err:
        return f'An error occurred while trying to fetch data from {url}: {err}'

async def description(movieDet, magnetLink, message: Message):
      descriptions = f"<b>Title</b><a href='{movieDet['image']}'>🎬</a>: <code>{movieDet['title']}</code>"
      descriptions += f"""
  <b>Genres: </b><code>{' '.join(movieDet['genre']) if len(movieDet['genre']) > 0 else ''}</code>
  <b>Rating⭐: </b><code>{movieDet['rating']['star']}</code>
  <b>Magnet Link🔗: </b>{magnetLink}
  <b>IMDB URL Link🔗: </b>{movieDet['imdb']}
  <b>Story Line : </b><em>{movieDet['plot']}</em>"""
      await message.edit(descriptions)

@userge.on_cmd("rkdb", about={
    'header': "Scrap Movies & Tv Shows from IMDB ",
    'description': "Get info about a Movie on IMDB with magnet url.\n",
    'usage': "!rkdb moviename"})
async def main(message: Message):
    movie_name = message.input_str
    async with aiohttp.ClientSession() as session:
        try:
            search_url = f'https://imdb-api.tprojects.workers.dev/search?query={movie_name}'
            movie_id = (await fetch(session, search_url))['results'][0]['id']
            magnetURL = ""
            title_url = f'https://imdb-api.tprojects.workers.dev/title/{movie_id}'
            final_result = await fetch(session, title_url)
            if final_result['contentType'] == "Movie":
                movieTorURL = f'https://yts.mx/api/v2/list_movies.json?query_term={movie_id}'
                movieMagnet = await fetch(session, movieTorURL)
                magnetURL = movieMagnet['data']['movies'][0]['torrents'][0]['url']
            await description(final_result, magnetURL, message)
        except aiohttp.ClientError as err:
            await message.edit(f'An error occurred while trying to fetch movie information: {err}')
        except IndexError as err:
            await message.edit(f'An error occurred while trying to access the results: {err}')
        except KeyError as err:
            await message.edit(f'<b>Brush enter valid movie name<b>')
        except Exception as err:
            await message.edit(f'An error occured with bot.')
