## IMPORTS
if 'Imports':

    if 'Standard Python Library':
        import os                           # local file operations, mainly os.path.join

    if 'Local File':
        from ._appdata import *                  # stores local application data, like global variables
        from .download_queue import Queue    # podRacer lib - handles queues for download operations
        from .organize import Organize       # podRacer lib - handles various organization tasks
        from .process import Process         # podRacer lib - processes requests for rss feeds
        from .settings import Settings       # podRacer lib - handles lib usage settings, such as error logging

## HANDLES DOWNLOADS
class Download:

    ## INITIALIZE CLASS
    def __init__(self):
        self.process = Process()
        self.organize = Organize()
        self.settings = Settings()

    ## CREATES AND RETURNS AUDIO DIR
    def get_audio_dir(self, show_title):

        ## CLEAN SHOW TITLE
        show_title = self.organize.text_remove_specials(show_title)

        ## SHOW DIRECTORIES
        show_dir = self.organize.dir_paths(os.path.join(APP_DIR, show_title))

        ## CREATE DIRECTORIES
        self.organize.dir_create(APP_DIR, show_dir['root'], audio_dir=True, metadata_dir=False)

        ## RETURN AUDIO DIR
        return show_dir['audio']

    ## DOWNLOAD A PODCAST
    def podcast(self, url):

        ## PARSE RSS FEED
        rss = self.process.parse_feed(url)

        ## GET AUDIO DIR
        audio_dir = self.get_audio_dir(rss.feed.title)

        ## GET ALL EPISODES
        total_episodes = len(rss.entries)

        ## START DOWNLOAD
        queue = Queue(max_workers=10)  # Initial max workers

        ## BENCHMARK DOWNLOAD QUEUE AND ADJUST MAX WORKERS ACCORDINGLY
        max_workers_after_benchmark = queue.benchmark(rss.entries, audio_dir, total_episodes)
        queue.executor._max_workers = max_workers_after_benchmark

        ## ADD EPISODES TO DOWNLOAD QUEUE
        for episode_number, episode in enumerate(rss.entries, start=1):
            correct_episode_number = total_episodes - episode_number + 1
            queue.add(episode, audio_dir, correct_episode_number, skip_existing=True)

        ## START PROGRESS BAR
        queue.progress_bar(total_episodes, desc=f"Downloading Podcast - {rss.feed.title}")

    ## DOWNLOAD SELECT EPISODES FROM A PODCAST
    def episode(self, show_url, *episode_args):

        ## PARSE RSS FEED
        rss = self.process.parse_feed(show_url)
        total_episodes = len(rss.entries)

        ## GET AUDIO DIR
        audio_dir = self.get_audio_dir(rss.feed.title)

        ## CREATE EPISODE LIST
        try:
            episode_numbers = self.organize.list_episodes_to_download(episode_args, total_episodes)
        except ValueError as error:
            self.settings.error(error, 'Invalid episode number or range',
                                f"{episode_args}",
                                "20, '20', '10-15', [1, 2, '3-5']",
                                'Use integers, strings, or ranges')
            return None

        ## UPDATE PROGRESS BAR TEXT IF MORE THAN ONE EPISODE
        desc = f"{rss.feed.title} | Downloading {len(episode_numbers)} Episodes" if len(episode_numbers) > 1 else f"{rss.feed.title} | Episode {episode_numbers[0]} - {rss.entries[total_episodes - episode_numbers[0]]['title']}"

        ## START DOWNLOAD QUEUE
        queue = Queue(max_workers=10)
        for episode_number in episode_numbers:
            episode_index = total_episodes - episode_number
            episode = rss.entries[episode_index]
            queue.add(episode, audio_dir, episode_number, skip_existing=True)

        ## START PROGRESS BAR
        queue.progress_bar(len(episode_numbers), desc=desc)
