'''
import hoover
import logging

i = hoover.LogglySession('subdomain', 'user', 'pass')
i.config_inputs()
loggingitup = logging.getLogger('test_input')
loggingitup.setLevel(logging.INFO)
loggingitup.info("Now logging to Loggly w/ .info")
'''

import hoover
handler = hoover.LogglyHttpHandler(token='f08bca85-51cb-43de-92d6-a190c348762d')
import logging
log = logging.getLogger('nerdfiles_net')
log.addHandler(handler)
log.setLevel(logging.INFO)
#log.info("If Einstein was alive today, he'd be stuck working at Google making adwords.")
log.info("#logping")

#import httplib2
#insert_url = "http://logs.loggly.com/inputs/f08bca85-51cb-43de-92d6-a190c348762d"
#insert_http = httplib2.Http(timeout=10)
#body = "#logping"
#resp, content = insert_http.request(insert_url, "POST", body=body, headers={'content-type':'text/plain'})

