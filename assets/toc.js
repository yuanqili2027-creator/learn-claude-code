/* 话题页：页内目录 scrollspy */
(function () {
  var links = Array.prototype.slice.call(document.querySelectorAll('.toc a'));
  if (!links.length) return;
  var map = {};
  var targets = [];
  links.forEach(function (a) {
    var id = a.getAttribute('href').slice(1);
    var el = document.getElementById(id);
    if (el) { map[id] = a; targets.push(el); }
  });
  var obs = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) {
        links.forEach(function (a) { a.classList.remove('active'); });
        var a = map[en.target.id];
        if (a) a.classList.add('active');
      }
    });
  }, { rootMargin: '-72px 0px -70% 0px' });
  targets.forEach(function (t) { obs.observe(t); });
})();
