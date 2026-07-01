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

    function addProgress() {
      var block = document.createElement("section");
      block.className = "guide-widget__progress";

      var head = document.createElement("div");
      head.className = "guide-widget__progress-head";
      head.textContent = text("Working on it", "Traitement en cours");
      block.appendChild(head);

      var status = document.createElement("p");
      status.className = "guide-widget__progress-status";
      status.textContent = text("Looking in the public corpus...", "Recherche dans le corpus public...");
      block.appendChild(status);

      var list = document.createElement("ol");
      list.className = "guide-widget__progress-list";
      block.appendChild(list);

      log.appendChild(block);
      log.scrollTop = log.scrollHeight;

      return {
        root: block,
        head: head,
        status: status,
        list: list,
        steps: {},
        remove: function () { block.remove(); },
      };
    }

    function updateProgress(progress, event) {
      if (!progress || !event || !event.data) return;
      var data = event.data;
      if (data.message) progress.status.textContent = data.message;

      if (event.name === "guide_plan") {
        progress.head.textContent = text("Plan ready", "Plan pret");
        setProgressStep(progress, "plan", text("Prepared public corpus searches", "Recherches publiques preparees"), "done");
      } else if (event.name === "guide_retrieval_query") {
        var query = data.query || text("Corpus query", "Recherche corpus");
        var count = typeof data.count === "number" ? data.count : 0;
        setProgressStep(
          progress,
          "query:" + query,
          text("Found " + count + " source(s): ", count + " source(s) trouvee(s) : ") + shorten(query, 54),
          count > 0 ? "done" : "muted"
        );
      } else if (event.name === "guide_retrieval") {
        setProgressStep(
          progress,
          "retrieval",
          text("Selected " + (data.source_count || 0) + " public source(s)", (data.source_count || 0) + " source(s) publique(s) selectionnee(s)"),
          "done"
        );
      } else if (event.name === "guide_answer") {
        progress.head.textContent = text("Answer ready", "Reponse prete");
        progress.status.textContent = text("Answer prepared from public sources.", "Reponse preparee a partir des sources publiques.");
        setProgressStep(progress, "answer", text("Prepared the answer", "Reponse preparee"), "done");
      } else if (event.name === "guide_error") {
        progress.head.textContent = text("Guide unavailable", "Guide indisponible");
        progress.status.textContent = data.message || text("The Guide is unavailable.", "Le Guide est indisponible.");
        progress.root.classList.add("guide-widget__progress--error");
      }

      log.scrollTop = log.scrollHeight;
    }

    function setProgressStep(progress, key, label, state) {
      var item = progress.steps[key];
      if (!item) {
        item = document.createElement("li");
        progress.steps[key] = item;
        progress.list.appendChild(item);
      }
      item.className = "guide-widget__progress-step guide-widget__progress-step--" + (state || "active");
      item.textContent = label;
    }

    function shorten(value, max) {
      var clean = String(value || "").replace(/\s+/g, " ").trim();
      if (clean.length <= max) return clean;
      return clean.slice(0, Math.max(1, max - 1)).trim() + "...";
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

      addSuggestions(block, data);

      log.appendChild(block);
      log.scrollTop = log.scrollHeight;
    }

    function addSuggestions(block, data) {
      var suggestions = guideSuggestions(data).slice(0, 3);
      if (!suggestions.length) return;

      var section = document.createElement("div");
      section.className = "guide-widget__suggestions";

      var title = document.createElement("h3");
      title.className = "guide-widget__suggestions-title";
      title.textContent = text("Continue with", "Continuer avec");
      section.appendChild(title);

      var list = document.createElement("div");
      list.className = "guide-widget__suggestions-list";
      suggestions.forEach(function (suggestion) {
        var button = document.createElement("button");
        button.type = "button";
        button.textContent = suggestion.label;
        button.setAttribute("data-guide-prompt", suggestion.prompt);
        button.addEventListener("click", function () {
          ask(suggestion.prompt);
        });
        list.appendChild(button);
      });
      section.appendChild(list);
      block.appendChild(section);
    }

    function guideSuggestions(data) {
      var question = String((data && data.question) || "").toLowerCase();
      var sourceCount = Array.isArray(data && data.sources) ? data.sources.length : 0;
      var suggestions = [];

      if (question.indexOf("cogentia") === -1 && question.indexOf("jumeau") === -1 && question.indexOf("twin") === -1) {
        suggestions.push({
          label: text("Connect this to Cogentia", "Relier au corpus"),
          prompt: text(
            "How does Cogentia help explain or operate this FractaVolta idea?",
            "Quel lien avec Cogentia, le corpus public et la methode de tracabilite ?"
          ),
        });
      }
      if (question.indexOf("read") === -1 && question.indexOf("lecture") === -1 && sourceCount > 0) {
        suggestions.push({
          label: text("Give me a reading path", "Proposer un parcours"),
          prompt: text(
            "Turn these sources into a 10-minute public reading path.",
            "Transforme ces sources en parcours de lecture public de 10 minutes pour comprendre FractaVolta en Corse."
          ),
        });
      }
      if (question.indexOf("packet") === -1 && question.indexOf("paquet") === -1) {
        suggestions.push({
          label: text("Explain energy packets", "Expliquer les paquets"),
          prompt: text(
            "Why does FractaVolta use the packet idea for energy and compute?",
            "Pourquoi FractaVolta parle-t-il de paquets d'energie pour les usages locaux en Corse ?"
          ),
        });
      }
      suggestions.push({
        label: text("What should I ask next?", "Que demander ensuite ?"),
        prompt: text(
          "Suggest three good public questions I should ask next about FractaVolta.",
          "Suggere trois bonnes questions publiques a poser ensuite sur FractaVolta en Corse."
        ),
      });

      return dedupeSuggestions(suggestions);
    }

    function dedupeSuggestions(suggestions) {
      var seen = {};
      return suggestions.filter(function (item) {
        var key = item.prompt;
        if (seen[key]) return false;
        seen[key] = true;
        return true;
      });
    }

    async function ask(question) {
      addMessage("user", question);
      var pending = addProgress();
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
        pending.status.textContent = text("Reading the answer...", "Lecture de la reponse...");
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
          updateProgress(pending, event);
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
    document.querySelectorAll("[data-open-guide]").forEach(function (button) {
      button.addEventListener("click", function () {
        setOpen(true);
        input.value = text(
          "Give me a 10-minute public reading path through the FractaVolta story.",
          "Propose un parcours public de 10 minutes pour comprendre FractaVolta en Corse."
        );
        input.focus();
      });
    });
  });
}());
