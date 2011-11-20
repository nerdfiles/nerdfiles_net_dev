function msgr(e) {

  var worker = this,
      msgSent = data; // e.data;
  
  switch (msgSent.cmd) {
    case 'init':
        var defaults = {
          'name': 'lastfm'
        };
        worker.postMessage(msgSent.msg);
        break;
    case 'sendr':
        var msgRtn = msgSent.msg;
        worker.postMessage(msgSent.msg);
        break;
  }

}

this.addEventListener('message', msgr, false);