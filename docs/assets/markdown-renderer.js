(function (global) {
  "use strict";

  /**
   * Shared rich Markdown renderer for public conversational surfaces.
   *
   * `marked` provides GFM parsing; DOMPurify removes unsafe HTML produced by
   * untrusted model output before it ever reaches the document.
   */
  function render(target, markdown) {
    var source = String(markdown || "");
    if (!global.marked || !global.DOMPurify) {
      target.textContent = source;
      return { rendered: false, reason: "markdown_dependencies_unavailable" };
    }

    var html = global.marked.parse(source, { gfm: true, breaks: true });
    target.innerHTML = global.DOMPurify.sanitize(html, {
      USE_PROFILES: { html: true },
      ADD_ATTR: ["target"],
    });
    hardenLinks(target);
    return { rendered: true };
  }

  function hardenLinks(target) {
    target.querySelectorAll("a[href]").forEach(function (link) {
      var href = String(link.getAttribute("href") || "").trim();
      if (/^https?:/i.test(href) || /^mailto:/i.test(href)) {
        link.target = "_blank";
        link.rel = "noopener noreferrer";
      } else {
        link.removeAttribute("target");
        link.removeAttribute("rel");
      }
    });
  }

  global.CogentiaMarkdown = { render: render };
})(window);
