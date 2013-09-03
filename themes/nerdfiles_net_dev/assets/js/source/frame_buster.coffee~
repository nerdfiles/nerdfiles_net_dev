((u) ->
  w = @
  t = w.top
  l = t.location
  t.onbeforeunload = ->
    # clear onbeforeunload
  if ( !u.hosts_list[l.hostname] )
    l.replace(u.default + "?blacklisted_site=" + encodeURIComponent l.href )
  else
    console.log u.hosts_list[l.hostname]
)({
  hosts_list: {
      "nerdfiles.net":  1
    , "127.0.0.1":      1
    , "127.0.0.1:8000": 1
    , "localhost":      1
    , "localhost:8000": 1
  },
  default: self.location.href
  })
