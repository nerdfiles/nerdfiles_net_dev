from django.conf import settings


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

    return {
        'SITE_URL': 'http://' + http_host + '/'
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
