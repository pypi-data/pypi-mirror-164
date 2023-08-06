
try {
    new Function("import('/reactfiles/frontend/main.4274a632.js')")();
} catch (err) {
    var el = document.createElement('script');
    el.src = '/reactfiles/frontend/main.4274a632.js';
    el.type = 'module';
    document.body.appendChild(el);
}
