from django.conf import settings

# == CONTEXT PROCESSORS ======================================== #

'''
def kippt_rss(request):
  from kippt import kippt_wrapper
  #TIMEOUT = settings.KIPPT_TIMEOUT
  TIMEOUT = 300 #secs

  from django.core.cache import cache
  # @nerdfiles

  imp_feed = cache.get('imp_feed')
  if imp_feed:
    return {
      "imp_feed": imp_feed
    }
  imp_feed = feedparser.parse('https://kippt.com/nerdfiles/important/feed')
  
  #hit_list = ['https://kippt.com/nerdfiles/important/feed']
  #future_calls = [__future__(feedparser.parse,rss_url) for rss_url in hit_list]
  #feeds = [future_obj() for future_obj in future_calls]

  #entries = []
  #for feed in feeds:
  #  entries.extend( feed['items'] )

  #sorted_entries = sorted(entries, key=lambda entry: entry["date_parsed"])
  #sorted_entries.reversed()

  cache.set(
    "imp_feed",
    imp_feed,
    TIMEOUT
  )
  return {
    "imp_feed": imp_feed
  }
'''

def kippt_rss(request):
  from django.core.cache import cache
  from settings import API_KEY, API_SECRET, username, password_hash
  from kippt import kippt_wrapper
  k = kippt_wrapper.user('%s' % settings.KIPPT_API_USER, '%s' % settings.KIPPT_API_TOKEN,)

  TIMEOUT = (3600*48/60)*5 # ten days

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

  tweet = twitter.Api().GetUserTimeline( settings.TWITTER_USER )[0]
  tweet.date = datetime.strptime( tweet.created_at, "%a %b %d %H:%M:%S +0000 %Y" )
  cache.set( 
    'tweet', 
    tweet, 
    settings.TWITTER_TIMEOUT 
  )

  return {
    "tweet": tweet
  }

'''
def lastfm(request):

  import pylast 
  from django.core.cache import cache
  #cache
  lfm_data = cache.get('lfm_data')
  TIMEOUT = 3600*48/60 # two days (48 hours)
  if lfm_data:
    return {
      "rt": lfm_data
    }

  network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
      API_SECRET, username = username, password_hash = password_hash)

  network.enable_caching()

  user_data = network.get_user('wittysense')
  r_tracks = user_data.get_recent_tracks(limit=5)
  recent_tracks = [r.track for r in r_tracks]

  #raw
  lfm_data = recent_tracks

  #set cache for next time
  cache.set(
    "lfm_data",
    lfm_data,
    TIMEOUT
  )

  #pprint(lfm_data)

  #load raw
  return {
    'rt': lfm_data,
  }
'''

def site_info(request):
    from django.contrib.sites.models import Site
    domain = Site.objects.get_current().domain
    http_host = request.META.get('HTTP_HOST')

    return {
        'SITE_URL': 'http://' + http_host + '/',
        'ASSETS_URL': '//' + http_host + '/assets/',
        'COFFEE_URL': 'build'
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
