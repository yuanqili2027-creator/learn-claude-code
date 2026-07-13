/* 侧边栏：移动端抽屉 + 话题过滤 + 顶部阅读进度 */
(function () {
  var burger = document.getElementById('burger');
  var backdrop = document.getElementById('backdrop');
  function close() { document.body.classList.remove('nav-open'); }
  if (burger) burger.addEventListener('click', function () { document.body.classList.toggle('nav-open'); });
  if (backdrop) backdrop.addEventListener('click', close);
  var sb = document.getElementById('sidebar');
  if (sb) sb.addEventListener('click', function (e) { if (e.target.closest('a')) close(); });

  /* 话题过滤 */
  var filter = document.getElementById('navFilter');
  var empty = document.getElementById('navEmpty');
  if (filter) {
    var items = Array.prototype.slice.call(document.querySelectorAll('#topicGroup .s-item'));
    filter.addEventListener('input', function () {
      var q = filter.value.trim().toLowerCase(), n = 0;
      items.forEach(function (it) {
        var name = (it.dataset.name || it.textContent).toLowerCase();
        var show = !q || name.indexOf(q) >= 0;
        it.style.display = show ? '' : 'none';
        if (show) n++;
      });
      if (empty) empty.hidden = n > 0;
    });
  }

  /* 顶部阅读进度 */
  var bar = document.getElementById('progress');
  if (bar) {
    var tick = function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      var p = max > 0 ? (h.scrollTop || document.body.scrollTop) / max : 0;
      bar.style.width = (p * 100).toFixed(1) + '%';
    };
    document.addEventListener('scroll', tick, { passive: true });
    window.addEventListener('resize', tick);
    tick();
  }
})();
