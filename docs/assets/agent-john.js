(function () {
  function ready(fn) {
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", fn);
    else fn();
  }

  ready(function () {
    var root = document.querySelector(".agent-john");
    if (!root) return;

    var locale = root.getAttribute("data-john-locale") || "en";
    var endpoint = root.getAttribute("data-john-endpoint");
    var consentBox = root.querySelector("[data-john-consent]");
    var appBox = root.querySelector("[data-john-app]");
    var log = root.querySelector("[data-john-log]");
    var threadsEl = root.querySelector("[data-john-threads]");
    var form = root.querySelector("[data-john-form]");
    var input = root.querySelector(".agent-john__input");
    var submit = root.querySelector("[data-john-submit]");
    var expandBtn = root.querySelector("[data-john-expand]");
    var storeKey = "fractavolta.agent-john.v1";
    var consentVersion = "2026-08-22";
    var ttlMs = 7 * 24 * 60 * 60 * 1000;
    var maxThreads = 12;
    var maxEntries = 40;
    var state = loadState();

    function text(en, fr) {
      return locale.indexOf("fr") === 0 ? fr : en;
    }

    function loadState() {
      try {
        var parsed = JSON.parse(localStorage.getItem(storeKey) || "null");
        if (!parsed || parsed.consentVersion !== consentVersion) {
          return { consentVersion: consentVersion, consent: null, threads: [], activeId: null };
        }
        var now = Date.now();
        parsed.threads = (parsed.threads || []).filter(function (t) {
          return t && now - (t.updated || t.at || 0) < ttlMs;
        }).slice(0, maxThreads);
        return parsed;
      } catch (e) {
        return { consentVersion: consentVersion, consent: null, threads: [], activeId: null };
      }
    }

    function persist() {
      if (!state.consent || !state.consent.memory) return;
      try {
        localStorage.setItem(storeKey, JSON.stringify(state));
      } catch (e) {}
    }

    function clearStore() {
      try {
        localStorage.removeItem(storeKey);
      } catch (e) {}
    }

    function uid() {
      return "t" + Date.now().toString(36) + Math.random().toString(36).slice(2, 6);
    }

    function activeThread() {
      return state.threads.filter(function (t) { return t.id === state.activeId; })[0] || null;
    }

    function ensureThread() {
      var current = activeThread();
      if (current) return current;
      var thread = { id: uid(), title: text("Conversation", "Conversation"), at: Date.now(), updated: Date.now(), entries: [] };
      state.threads.unshift(thread);
      state.activeId = thread.id;
      persist();
      return thread;
    }

    function showConsent() {
      consentBox.hidden = false;
      appBox.hidden = true;
    }

    function showApp() {
      consentBox.hidden = true;
      appBox.hidden = false;
      renderThreads();
      renderLog();
      input.focus();
    }

    function applyGate() {
      if (state.consent && state.consent.processing && state.consent.version === consentVersion) showApp();
      else showConsent();
    }

    root.querySelector("[data-john-consent-accept]").addEventListener("click", function () {
      var processing = root.querySelector("[data-john-consent-processing]").checked;
      var memory = root.querySelector("[data-john-consent-memory]").checked;
      if (!processing) {
        alert(text("Processing consent is required to talk to the agent.", "Le consentement de traitement est requis pour parler à l'agent."));
        return;
      }
      state.consent = { processing: true, memory: memory, version: consentVersion, at: Date.now() };
      if (!memory) {
        state.threads = [];
        state.activeId = null;
        clearStore();
      } else persist();
      showApp();
    });

    root.querySelector("[data-john-withdraw]").addEventListener("click", function () {
      state.consent = null;
      state.threads = [];
      state.activeId = null;
      clearStore();
      log.textContent = "";
      showConsent();
    });

    function isImmersive() {
      return root.classList.contains("agent-john--immersive") || document.fullscreenElement === root;
    }

    function setImmersive(on) {
      root.classList.toggle("agent-john--immersive", on);
      document.documentElement.classList.toggle("agent-john-immersive", on);
      if (expandBtn) {
        expandBtn.setAttribute("aria-pressed", on ? "true" : "false");
        expandBtn.textContent = on ? text("Exit full page", "Réduire") : text("Full page", "Plein écran");
      }
    }

    if (expandBtn) {
      expandBtn.addEventListener("click", function () {
        var next = !isImmersive();
        setImmersive(next);
        if (next && root.requestFullscreen) {
          root.requestFullscreen().catch(function () {});
        } else if (!next && document.fullscreenElement && document.exitFullscreen) {
          document.exitFullscreen().catch(function () {});
        }
      });
    }
    document.addEventListener("fullscreenchange", function () {
      if (document.fullscreenElement === root) setImmersive(true);
      if (!document.fullscreenElement) setImmersive(false);
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && isImmersive() && !document.fullscreenElement) setImmersive(false);
    });

    root.querySelector("[data-john-new]").addEventListener("click", function () {
      state.activeId = null;
      ensureThread();
      renderThreads();
      renderLog();
      input.focus();
    });

    root.querySelector("[data-john-delete]").addEventListener("click", function () {
      state.threads = state.threads.filter(function (t) { return t.id !== state.activeId; });
      state.activeId = state.threads[0] ? state.threads[0].id : null;
      persist();
      renderThreads();
      renderLog();
    });

    root.querySelector("[data-john-export]").addEventListener("click", function () {
      var thread = activeThread() || { entries: [] };
      var blob = new Blob([JSON.stringify({
        agent: "john",
        locale: locale,
        exported_at: new Date().toISOString(),
        thread: thread,
      }, null, 2)], { type: "application/json" });
      var url = URL.createObjectURL(blob);
      var a = document.createElement("a");
      a.href = url;
      a.download = "agent-john-conversation.json";
      a.click();
      URL.revokeObjectURL(url);
    });

    root.querySelectorAll("[data-john-prompt]").forEach(function (button) {
      button.addEventListener("click", function () {
        ask(button.getAttribute("data-john-prompt"));
      });
    });

    form.addEventListener("submit", function (event) {
      event.preventDefault();
      var question = String(input.value || "").trim();
      if (!question) return;
      input.value = "";
      ask(question);
    });

    function renderThreads() {
      threadsEl.textContent = "";
      state.threads.forEach(function (thread) {
        var btn = document.createElement("button");
        btn.type = "button";
        btn.className = "agent-john__thread" + (thread.id === state.activeId ? " is-current" : "");
        btn.textContent = thread.title || text("Conversation", "Conversation");
        btn.addEventListener("click", function () {
          state.activeId = thread.id;
          persist();
          renderThreads();
          renderLog();
        });
        threadsEl.appendChild(btn);
      });
    }

    function renderLog() {
      log.textContent = "";
      var thread = activeThread();
      if (!thread) return;
      thread.entries.forEach(function (entry) {
        if (entry.type === "user") addMessage("user", entry.text, false);
        if (entry.type === "answer" && entry.data) addAnswer(entry.data, false);
      });
    }

    function remember(entry) {
      var thread = ensureThread();
      thread.entries.push(Object.assign({ at: Date.now() }, entry));
      thread.entries = thread.entries.slice(-maxEntries);
      thread.updated = Date.now();
      if (entry.type === "user" && (!thread.title || thread.title === text("Conversation", "Conversation"))) {
        thread.title = String(entry.text || "").slice(0, 48);
      }
      persist();
      renderThreads();
    }

    function addMessage(kind, value, store) {
      var block = document.createElement("div");
      block.className = "guide-widget__message guide-widget__message--" + kind;
      block.textContent = value;
      log.appendChild(block);
      log.scrollTop = log.scrollHeight;
      if (store) remember({ type: kind, text: value });
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

    function setProgressStep(progress, key, label, stateName) {
      var item = progress.steps[key];
      if (!item) {
        item = document.createElement("li");
        progress.steps[key] = item;
        progress.list.appendChild(item);
      }
      item.className = "guide-widget__progress-step guide-widget__progress-step--" + (stateName || "active");
      item.textContent = label;
    }

    function updateProgress(progress, event) {
      if (!progress || !event || !event.data) return;
      var data = event.data;
      if (data.message) progress.status.textContent = data.message;
      if (event.name === "guide_answer") {
        progress.head.textContent = text("Answer ready", "Réponse prête");
        setProgressStep(progress, "answer", text("Prepared the answer", "Réponse préparée"), "done");
      } else if (event.name === "guide_error") {
        progress.head.textContent = text("Agent unavailable", "Agent indisponible");
        progress.status.textContent = data.message || text("Agent John is unavailable.", "L'agent John est indisponible.");
        progress.root.classList.add("guide-widget__progress--error");
      } else if (event.name === "guide_retrieval") {
        setProgressStep(
          progress,
          "retrieval",
          text("Selected " + (data.source_count || 0) + " public source(s)", (data.source_count || 0) + " source(s) publique(s) sélectionnée(s)"),
          "done"
        );
      }
      log.scrollTop = log.scrollHeight;
    }

    function safeHref(value) {
      var href = String(value || "").trim();
      return /^(https?:|mailto:|\/|#)/i.test(href) ? href : "";
    }

    function appendInlineMarkdown(target, source) {
      var pattern = /\*\*[^*]+\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\)/g;
      var last = 0;
      var match;
      source = String(source || "");
      while ((match = pattern.exec(source))) {
        if (match.index > last) target.appendChild(document.createTextNode(source.slice(last, match.index)));
        var token = match[0];
        if (token.indexOf("**") === 0) {
          var strong = document.createElement("strong");
          strong.textContent = token.slice(2, -2);
          target.appendChild(strong);
        } else if (token.indexOf("`") === 0) {
          var code = document.createElement("code");
          code.textContent = token.slice(1, -1);
          target.appendChild(code);
        } else {
          var parts = token.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
          var href = parts ? safeHref(parts[2]) : "";
          if (href) {
            var link = document.createElement("a");
            link.href = href;
            link.target = "_blank";
            link.rel = "noopener";
            link.textContent = parts[1];
            target.appendChild(link);
          } else {
            target.appendChild(document.createTextNode(parts ? parts[1] : token));
          }
        }
        last = pattern.lastIndex;
      }
      if (last < source.length) target.appendChild(document.createTextNode(source.slice(last)));
    }

    function renderMarkdown(target, markdown) {
      target.textContent = "";
      var lines = String(markdown || "").replace(/\r\n/g, "\n").split("\n");
      var index = 0;
      while (index < lines.length) {
        var line = lines[index];
        if (!line.trim()) {
          index += 1;
          continue;
        }
        var heading = line.match(/^(#{1,3})\s+(.+)$/);
        if (heading) {
          var h = document.createElement("h" + Math.min(4, heading[1].length + 2));
          appendInlineMarkdown(h, heading[2]);
          target.appendChild(h);
          index += 1;
          continue;
        }
        if (/^\s*[-*]\s+/.test(line)) {
          var ul = document.createElement("ul");
          while (index < lines.length && /^\s*[-*]\s+/.test(lines[index])) {
            var li = document.createElement("li");
            appendInlineMarkdown(li, lines[index].replace(/^\s*[-*]\s+/, ""));
            ul.appendChild(li);
            index += 1;
          }
          target.appendChild(ul);
          continue;
        }
        var p = document.createElement("p");
        appendInlineMarkdown(p, line);
        target.appendChild(p);
        index += 1;
      }
    }

    function addAnswer(data, store) {
      var block = document.createElement("article");
      block.className = "guide-widget__answer";
      var body = document.createElement("div");
      body.className = "guide-widget__answer-text";
      renderMarkdown(body, data.answer || text("No answer returned.", "Aucune réponse retournée."));
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
          } else item.textContent = label;
          var ref = document.createElement("span");
          ref.textContent = " " + (source.source_id || "");
          item.appendChild(ref);
          list.appendChild(item);
        });
        block.appendChild(list);
      }
      log.appendChild(block);
      log.scrollTop = log.scrollHeight;
      if (store) {
        remember({
          type: "answer",
          data: {
            question: data.question,
            answer: data.answer,
            sources: Array.isArray(data.sources) ? data.sources.slice(0, 5) : [],
          },
        });
      }
    }

    function historyPayload() {
      var thread = activeThread();
      if (!thread) return [];
      return thread.entries.slice(-10).map(function (entry) {
        if (entry.type === "user") return { role: "user", content: entry.text || "" };
        if (entry.type === "answer") return { role: "assistant", content: (entry.data && entry.data.answer) || "" };
        return null;
      }).filter(function (entry) {
        return entry && entry.content && entry.content.trim();
      });
    }

    async function readGuideResponse(response, pending) {
      var contentType = response.headers.get("content-type") || "";
      if (contentType.indexOf("text/event-stream") === -1 || !response.body || !window.TextDecoder) {
        pending.status.textContent = text("Reading the answer...", "Lecture de la réponse...");
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
        blocks.forEach(function (chunk) {
          var event = parseGuideEvent(chunk);
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
      } catch (e) {
        return null;
      }
    }

    async function ask(question) {
      if (!state.consent || !state.consent.processing) {
        showConsent();
        return;
      }
      addMessage("user", question, true);
      var pending = addProgress();
      submit.disabled = true;
      try {
        var response = await fetch(endpoint, {
          method: "POST",
          mode: "cors",
          headers: {
            "Content-Type": "application/json",
            Accept: "text/event-stream, application/json",
          },
          body: JSON.stringify({
            question: question,
            locale: locale,
            stream: true,
            history: historyPayload(),
            surface: "agent-john",
          }),
        });
        var data = await readGuideResponse(response, pending);
        pending.remove();
        if (!response.ok || !data || data.ok === false) {
          throw new Error((data && data.message) || text("Agent John is unavailable.", "L'agent John est indisponible."));
        }
        addAnswer(data, true);
      } catch (error) {
        pending.remove();
        addMessage("error", error.message || text("Agent John is unavailable.", "L'agent John est indisponible."), false);
      } finally {
        submit.disabled = false;
      }
    }

    applyGate();
  });
})();
