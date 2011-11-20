  var httpRequest,

  function makeRequest(url) {
    if (window.XMLHttpRequest) { // Mozilla, Safari, ...
      httpRequest = new XMLHttpRequest();
    } else if (window.ActiveXObject) { // IE
      try {
        httpRequest = new ActiveXObject("Msxml2.XMLHTTP");
      } 
      catch (e) {
        try {
          httpRequest = new ActiveXObject("Microsoft.XMLHTTP");
        } 
        catch (e) {}
      }
    }

    if (!httpRequest) {
      alert('Giving up :( Cannot create an XMLHTTP instance');
      return false;
    }
    httpRequest.onreadystatechange = alertContents;
    httpRequest.open('GET', url);
    httpRequest.send();
  }

  function alertContents() {
    if (httpRequest.readyState === 4) {
      if (httpRequest.status === 200) {
        alert(httpRequest.responseText);
    } else {
      alert('There was a problem with the request.');
    }
  }

function msgr(e) {

  var worker = this,
      msgSent = e.data;
  
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
        var u = makeRequest('/lastfm/');
        worker.postMessage(u);
        break;
  }

}

this.addEventListener('message', msgr, false);
