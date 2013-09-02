from django.conf import settings


def kippt_rss(request):
    from django.core.cache import cache
    from settings import API_KEY, API_SECRET, username, password_hash
    from kippt import kippt_wrapper
    k = kippt_wrapper.user('%s' %
                           settings.KIPPT_API_USER, '%s' % settings.KIPPT_API_TOKEN,)

    TIMEOUT = (3600*48/60)*5  # ten days

    kippt_imps = cache.get('kippt_imps')
    if kippt_imps:
        return {
            "imp_feed": kippt_imps
        }

    kippt_imps = k.getClips(134737, 2)
    cache.set(
        'kippt_imps',
        kippt_imps[1],
        TIMEOUT
    )

    return {
        "imp_feed": kippt_imps[1],
    }


def latest_tweet(request):
    from django.core.cache import cache
    tweet = cache.get('tweet')

    if tweet:
        return {
            "tweet": tweet
        }

    tweet = twitter.Api().GetUserTimeline(settings.TWITTER_USER)[0]
    tweet.date = datetime.strptime(
        tweet.created_at, "%a %b %d %H:%M:%S +0000 %Y")
    cache.set(
        'tweet',
        tweet,
        settings.TWITTER_TIMEOUT
    )

    return {
        "tweet": tweet
    }


def site_info(request):
    from django.contrib.sites.models import Site
    domain = Site.objects.get_current().domain
    http_host = request.META.get('HTTP_HOST')

    COFFEE_URL = 'build'

    if domain == 'example.com':
        domain = http_host

    if settings.LOCAL_DEVELOPMENT:
        # domain = 'localhost:8001'
        settings.ASSETS_URL = '/_assets/'
        COFFEE_URL = 'brew'

    return {
        'LOCAL': settings.LOCAL_DEVELOPMENT,
        'SITE_URL': 'http://' + domain + '/',
        'ASSETS_URL': 'http://' + domain + settings.ASSETS_URL,
        'COFFEE_URL': COFFEE_URL,
    }


def google_analytics(request):

    if not settings.GA_PATH:
        return {}

    f = None
    try:
        f = file(settings.GA_PATH)
        GA_CODE = f.read()
    finally:
        if f is not None:
            f.close()

    return dict(GA_CODE=GA_CODE)
