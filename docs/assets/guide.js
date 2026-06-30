(function () {
  function ready(fn) {
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", fn);
    } else {
      fn();
    }
  }

  ready(function () {
    var root = document.querySelector(".guide-widget");
    if (!root) return;

    var endpoint = root.getAttribute("data-guide-endpoint");
    var locale = root.getAttribute("data-guide-locale") || "en";
    var toggle = root.querySelector(".guide-widget__toggle");
    var panel = root.querySelector(".guide-widget__panel");
    var close = root.querySelector(".guide-widget__close");
    var form = root.querySelector(".guide-widget__form");
    var input = root.querySelector(".guide-widget__input");
    var log = root.querySelector(".guide-widget__log");
    var submit = root.querySelector(".guide-widget__submit");

    function text(en, fr) {
      return locale.indexOf("fr") === 0 ? fr : en;
    }

    function setOpen(open) {
      panel.hidden = !open;
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      if (open) input.focus();
    }

    function addMessage(kind, value) {
      var block = document.createElement("div");
      block.className = "guide-widget__message guide-widget__message--" + kind;
      block.textContent = value;
      log.appendChild(block);
      log.scrollTop = log.scrollHeight;
      return block;
    }

    function addAnswer(data) {
      var block = document.createElement("article");
      block.className = "guide-widget__answer";

      var body = document.createElement("p");
      body.className = "guide-widget__answer-text";
      body.textContent = data.answer || text("No answer returned.", "Aucune reponse retournee.");
      block.appendChild(body);

      if (Array.isArray(data.sources) && data.sources.length) {
        var title = document.createElement("h3");
        title.className = "guide-widget__sources-title";
        title.textContent = text("Sources", "Sources");
        block.appendChild(title);

        var list = document.createElement("ol");
        list.className = "guide-widget__sources";
        data.sources.slice(0, 5).forEach(function (source) {
          var item = document.createElement("li");
          var label = source.title || source.path || source.source_id;
          if (source.url) {
            var link = document.createElement("a");
            link.href = source.url;
            link.target = "_blank";
            link.rel = "noopener";
            link.textContent = label;
            item.appendChild(link);
          } else {
            item.textContent = label;
          }
          var ref = document.createElement("span");
          ref.textContent = " " + source.source_id;
          item.appendChild(ref);
          list.appendChild(item);
        });
        block.appendChild(list);
      }

      if (Array.isArray(data.warnings) && data.warnings.indexOf("guide_chat_backend_unavailable") !== -1) {
        var warn = document.createElement("p");
        warn.className = "guide-widget__warning";
        warn.textContent = text("Conversational synthesis is temporarily unavailable.", "La synthese conversationnelle est temporairement indisponible.");
        block.appendChild(warn);
      }

      log.appendChild(block);
      log.scrollTop = log.scrollHeight;
    }

    async function ask(question) {
      addMessage("user", question);
      var pending = addMessage("status", text("Looking in the public corpus...", "Recherche dans le corpus public..."));
      submit.disabled = true;
      try {
        var response = await fetch(endpoint, {
          method: "POST",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
            "Accept": "text/event-stream, application/json",
          },
          body: JSON.stringify({ question: question, locale: locale, stream: true }),
        });
        var data = await readGuideResponse(response, pending);
        pending.remove();
        if (!response.ok || !data || data.ok === false) {
          throw new Error((data && data.message) || text("The Guide is unavailable.", "Le Guide est indisponible."));
        }
        addAnswer(data);
      } catch (error) {
        pending.remove();
        addMessage("error", error.message || text("The Guide is unavailable.", "Le Guide est indisponible."));
      } finally {
        submit.disabled = false;
      }
    }

    async function readGuideResponse(response, pending) {
      var contentType = response.headers.get("content-type") || "";
      if (contentType.indexOf("text/event-stream") === -1 || !response.body || !window.TextDecoder) {
        return response.json().catch(function () { return null; });
      }
      var reader = response.body.getReader();
      var decoder = new TextDecoder();
      var buffer = "";
      var answer = null;
      var streamError = null;
      while (true) {
        var part = await reader.read();
        if (part.done) break;
        buffer += decoder.decode(part.value, { stream: true });
        var blocks = buffer.split("\n\n");
        buffer = blocks.pop() || "";
        blocks.forEach(function (block) {
          var event = parseGuideEvent(block);
          if (!event) return;
          if ((event.name === "guide_status" || event.name === "guide_plan" || event.name === "guide_retrieval" || event.name === "guide_retrieval_query") && event.data.message) {
            pending.textContent = event.data.message;
            log.scrollTop = log.scrollHeight;
          }
          if (event.name === "guide_answer") answer = event.data;
          if (event.name === "guide_error") streamError = event.data;
        });
      }
      if (!answer && streamError) return streamError;
      return answer;
    }

    function parseGuideEvent(block) {
      var name = "message";
      var data = [];
      block.split(/\r?\n/).forEach(function (line) {
        if (line.indexOf("event:") === 0) name = line.slice(6).trim();
        if (line.indexOf("data:") === 0) data.push(line.slice(5).trim());
      });
      if (!data.length) return null;
      try {
        return { name: name, data: JSON.parse(data.join("\n")) };
      } catch (error) {
        return null;
      }
    }

    toggle.addEventListener("click", function () { setOpen(panel.hidden); });
    close.addEventListener("click", function () { setOpen(false); });
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var question = input.value.trim();
      if (!question) return;
      input.value = "";
      ask(question);
    });
    root.querySelectorAll("[data-guide-prompt]").forEach(function (button) {
      button.addEventListener("click", function () {
        setOpen(true);
        ask(button.getAttribute("data-guide-prompt"));
      });
    });
  });
}());
