import mastodon
from mastodon import Mastodon
import argparse
import settings
import producer
from utils.log import log

'''
CLI for the app - initial interface.
TODO: convert it ot REST-API + json using SPA/Mobile app
'''
def main():
    settings.init()
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
        '--public',
        help='listen to public stream (instead of local).',
        action='store_true',
        required=False,
        default=False)

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

    # Mastodon.create_app(
    #     'pytooterapp',
    #     api_base_url = 'https://mastodon.social',
    #     to_file = 'pytooter_clientcred.secret'
    # )

    # mastodon = Mastodon(api_base_url = settings.base_url)

    mastodon = Mastodon(client_id = 'pytooter_clientcred.secret',)
    mastodon.log_in(
        'hasib.iut@gmail.com',
        'Abcd1234',
        to_file = 'pytooter_usercred.secret'
    )

    if args.public:
        mastodon.stream_public(producer.Listener())
    else:
        mastodon.stream_local(producer.Listener())

if __name__ == '__main__':
    main()
