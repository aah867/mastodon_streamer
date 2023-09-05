import mastodon
from mastodon import Mastodon
from bs4 import BeautifulSoup
import datetime
import settings
import watchdog

# Listener for Mastodon events
class Listener(mastodon.StreamListener):

    def on_update(self, status):

        if settings.watchdog:
            settings.watchdog.reset()

        m_text = BeautifulSoup(status.content, 'html.parser').text
        num_tags = len(status.tags)
        num_chars = len(m_text)
        num_words = len(m_text.split())
        m_lang = status.language
        if m_lang is None:
            m_lang = 'unknown'
        m_user = status.account.username

        app=''
        # attribute only available on local
        if hasattr(status, 'application'):
            app = status.application.get('name')

        now_dt=datetime.datetime.now()

        value_topic = {
            'm_id': status.id,
            'created_at': int(now_dt.strftime('%Y')),
            'created_at_str': now_dt.strftime('%Y %m %d %H:%M:%S'),
            'app': app,
            'url': status.url,
            'base_url': settings.base_url,
            'language': m_lang,
            'favourites': status.favourites_count,
            'username': m_user,
            'bot': status.account.bot,
            'tags': num_tags,
            'characters': num_chars,
            'words': num_words,
            'mastodon_text': m_text
        }

        if not settings.quiet:
            print(f'{m_user} {m_lang}', m_text[:30])

        if settings.enable_kafka:
            settings.producer.produce(topic = settings.topic_name, value = value_topic)
            settings.producer.flush()

