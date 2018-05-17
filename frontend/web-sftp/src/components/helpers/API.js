'use strict';

function sendRequest(method, url, data, json = true, contentType = '') {
  return new Promise((res, rej) => {
    let xhr = new XMLHttpRequest();
    xhr.open(method, url, true);
    xhr.onload = e => {
      if (xhr.readyState === 4 && xhr.status === 200)
        res(json ? JSON.parse(xhr.responseText) : xhr.responseText);
      else
        rej(e, xhr.statusText);
    };
    xhr.onerror = e => rej(xhr.statusText);
    if (contentType) xhr.setRequestHeader('Content-Type', contentType);
    xhr.send(data);
  });
}

function sendJson(method, url, obj, json = true) {
  return sendRequest(method, url, JSON.stringify(obj), json, 'application/json;charset=UTF-8');
}

export default {
  getHostContent: () => sendJson('GET', 'http://localhost:5000/files')
};
