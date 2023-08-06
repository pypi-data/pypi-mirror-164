
function loadES5() {
  var el = document.createElement('script');
  el.src = '/dynalite_static/frontend_es5/entrypoint-a16dd963.js';
  document.body.appendChild(el);
}
if (/.*Version\/(?:11|12)(?:\.\d+)*.*Safari\//.test(navigator.userAgent)) {
    loadES5();
} else {
  try {
    new Function("import('/dynalite_static/frontend_latest/entrypoint-01aeca65.js')")();
  } catch (err) {
    loadES5();
  }
}
  