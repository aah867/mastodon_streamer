import mastodon
from mastodon import Mastodon
import argparse
import settings
import event_listener
import watchdog
from kafka_serializer import kafka_serializer
from utils.log import log

"""
Main streamer application - parses the commandline interface
to start the application according to the configuration.
"""
def main():
    settings.init()
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '--enableKafka',
        help='Whether to enable Kafka producer.',
        action='store_true',
        required=False,
        default=False)

    parser.add_argument(
        '--public',
        help='listen to public stream (instead of local).',
        action='store_true',
        required=False,
        default=False)

    parser.add_argument(
        '--watchdog',
        help='enable watchdog timer of n seconds',
        type=int,
        required=False)

    parser.add_argument(
        '--quiet',
        help='Do not echo a summary of the toot',
        action='store_true',
        required=False,
        default=False)

    parser.add_argument(
        '--baseURL',
        help='Server URL',
        required=False,
        default='https://mastodon.social')

    args = parser.parse_args()

    settings.base_url=args.baseURL
    settings.enable_kafka=args.enableKafka

    if settings.enable_kafka:
        settings.topic_name, settings.producer = kafka_serializer()

    if args.watchdog:
        settings.watchdog = watchdog.Watchdog(args.watchdog, watchdog.watchExpired)
        settings.watchdog.timer.start()

    Mastodon.create_app(
        'pytooterapp',
        api_base_url = 'https://mastodon.social',
        to_file = 'streaming_app.secret'
    )

    # mastodon = Mastodon(api_base_url = settings.base_url)
    mastodon = Mastodon(client_id = 'streaming_app.secret',)
    mastodon.log_in(
        'hasib.iut@gmail.com',
        'Abcd1234',
        to_file = 'pytooter_usercred.secret'
    )

    if args.public:
        mastodon.stream_public(event_listener.Listener())
    else:
        mastodon.stream_local(event_listener.Listener())

if __name__ == '__main__':
    main()
