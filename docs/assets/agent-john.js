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
    var memoryEl = root.querySelector("[data-john-memory]");
    var form = root.querySelector("[data-john-form]");
    var input = root.querySelector(".agent-john__input");
    var submit = root.querySelector("[data-john-submit]");
    var expandBtn = root.querySelector("[data-john-expand]");
    var storeKey = "fractavolta.agent-john.v1";
    var consentVersion = "2026-08-22";
    var ttlMs = 7 * 24 * 60 * 60 * 1000;
    var maxThreads = 12;
    var maxEntries = 80;
    var recentKeep = 12;
    var compactLimit = 8000;
    var historyWireLimit = 16;
    var historyChunk = 1150;
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
        compact: threadCompact(thread),
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

    function renderMemoryHint() {
      if (!memoryEl) return;
      var thread = activeThread();
      var compact = threadCompact(thread);
      var older = thread && thread.entries.length > recentKeep ? thread.entries.length - recentKeep : 0;
      var dropped = thread && thread.compactedTurns ? thread.compactedTurns : 0;
      var n = older + dropped;
      if (!compact || n < 1) {
        memoryEl.hidden = true;
        memoryEl.textContent = "";
        return;
      }
      memoryEl.hidden = false;
      memoryEl.textContent = text(
        "John keeps a continuity brief of " + n + " earlier turns, plus the last " + recentKeep + " in full.",
        "John garde un brief de continuité sur " + n + " tours plus anciens, plus les " + recentKeep + " derniers in extenso."
      );
    }

    function renderThreads() {
      renderMemoryHint();
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

    function clipText(value, max) {
      var clean = String(value || "").replace(/\s+/g, " ").trim();
      if (clean.length <= max) return clean;
      return clean.slice(0, Math.max(1, max - 1)).trim() + "…";
    }

    function summarizeEntries(entries) {
      var lines = [];
      var pendingQ = "";
      (entries || []).forEach(function (entry) {
        if (entry.type === "user") {
          pendingQ = clipText(entry.text, 240);
          return;
        }
        if (entry.type === "answer" && entry.data) {
          var answer = clipText(entry.data.answer, 700);
          var sources = Array.isArray(entry.data.sources)
            ? entry.data.sources.slice(0, 4).map(function (s) { return s.source_id || s.title || ""; }).filter(Boolean)
            : [];
          var line = pendingQ ? "Visitor: " + pendingQ + "\nJohn: " + answer : "John: " + answer;
          if (sources.length) line += "\nSources: " + sources.join("; ");
          lines.push(line);
          pendingQ = "";
        }
      });
      if (pendingQ) lines.push("Visitor: " + pendingQ);
      return lines.join("\n\n");
    }

    function mergeCompact(previous, added) {
      var parts = [String(previous || "").trim(), String(added || "").trim()].filter(Boolean);
      if (!parts.length) return "";
      var merged = parts.join("\n");
      if (merged.length <= compactLimit) return merged;
      return "…" + merged.slice(-(compactLimit - 1));
    }

    function foldOverflow(thread) {
      if (!thread || thread.entries.length <= maxEntries) return;
      var dropped = thread.entries.slice(0, thread.entries.length - maxEntries);
      thread.overflow = mergeCompact(thread.overflow, summarizeEntries(dropped));
      thread.compactedTurns = (thread.compactedTurns || 0) + dropped.length;
      thread.entries = thread.entries.slice(-maxEntries);
    }

    function threadCompact(thread) {
      if (!thread) return "";
      var older = thread.entries.length > recentKeep ? thread.entries.slice(0, -recentKeep) : [];
      return mergeCompact(thread.overflow, summarizeEntries(older));
    }

    function continuityText(thread) {
      var generated = thread && String(thread.generatedCompact || "").trim();
      if (generated) return generated;
      return threadCompact(thread);
    }

    function chunkHistory(textValue, header) {
      var body = String(textValue || "").trim();
      if (!body) return [];
      var full = header + "\n\n" + body;
      var chunks = [];
      var start = 0;
      while (start < full.length && chunks.length < 6) {
        chunks.push(full.slice(start, start + historyChunk));
        start += historyChunk;
      }
      return chunks.map(function (chunk, i) {
        var prefix = chunks.length > 1 ? "[" + (i + 1) + "/" + chunks.length + "] " : "";
        return { role: "assistant", content: prefix + chunk };
      });
    }

    function scheduleCompact(thread) {
      if (!thread || thread.compacting) return;
      if (!state.consent || !state.consent.processing) return;
      var older = thread.entries.length > recentKeep ? thread.entries.slice(0, -recentKeep) : [];
      if (older.length < 2 && !thread.overflow) return;
      if (thread.generatedCompact && thread.entries.length - (thread.lastCompactAt || 0) < 4) return;
      thread.compacting = true;
      var hist = older.slice(-12).map(function (entry) {
        if (entry.type === "user") return { role: "user", content: entry.text || "" };
        if (entry.type === "answer") return { role: "assistant", content: (entry.data && entry.data.answer) || "" };
        return null;
      }).filter(function (item) { return item && item.content; });
      if (thread.overflow) {
        hist.unshift({
          role: "assistant",
          content: clipText(
            text("Earlier overflow notes: ", "Notes plus anciennes : ") + thread.overflow,
            historyChunk
          ),
        });
      }
      fetch(endpoint, {
        method: "POST",
        mode: "cors",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify({
          question: text(
            "Write a continuity brief of the earlier conversation, in Agent John's first person as the twin (not as Jean Hugues the living person). Keep the visitor's name if any, goals, corrections, decisions, and open questions. Do not invent. This brief is not corpus evidence. About 300 to 500 words.",
            "Rédige un brief de continuité à la première personne de l'agent John, le jumeau (pas Jean Hugues la personne vivante). Garde le nom du visiteur s'il est connu, les buts, corrections, décisions et questions ouvertes. N'invente pas. Ce brief n'est pas une preuve du corpus. Environ 300 à 500 mots."
          ),
          locale: locale,
          stream: false,
          history: hist,
          surface: "agent-john-compact",
        }),
      }).then(function (res) { return res.json(); }).then(function (data) {
        if (data && data.ok && data.answer) {
          thread.generatedCompact = String(data.answer).trim();
          thread.lastCompactAt = thread.entries.length;
          persist();
          renderMemoryHint();
        }
      }).catch(function () {}).finally(function () {
        thread.compacting = false;
      });
    }

    function remember(entry) {
      var thread = ensureThread();
      thread.entries.push(Object.assign({ at: Date.now() }, entry));
      foldOverflow(thread);
      thread.updated = Date.now();
      if (entry.type === "user" && (!thread.title || thread.title === text("Conversation", "Conversation"))) {
        thread.title = String(entry.text || "").slice(0, 48);
      }
      persist();
      renderThreads();
      if (entry.type === "answer") scheduleCompact(thread);
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
      } else if (event.name === "guide_trace" && data.provider_trace && data.provider_trace.step === "acp.queue") {
        var position = data.provider_trace.queue_position || 1;
        progress.head.textContent = text("Waiting for local capacity", "Attente d'une capacite locale");
        progress.status.textContent = text(
          "Another request is using the local assistant. Your turn is queued.",
          "Une autre demande utilise l'assistant local. Votre tour est en file."
        );
        setProgressStep(
          progress,
          "provider-queue",
          text("Queued behind " + position + " request(s)", "En file derriere " + position + " demande(s)"),
          "active"
        );
      } else if (event.name === "guide_trace" && data.provider_trace && data.provider_trace.step === "acp.queue_acquired") {
        progress.head.textContent = text("Local capacity available", "Capacite locale disponible");
        progress.status.textContent = text("Preparing the answer...", "Preparation de la reponse...");
        setProgressStep(
          progress,
          "provider-queue",
          text("Local capacity acquired", "Capacite locale obtenue"),
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
      // Public rendering stays DOM-based: support common Markdown while
      // keeping model output inert rather than injecting HTML.
      var pattern = /(\*\*[^*\n]+\*\*|__[^_\n]+__|~~[^~\n]+~~|`[^`\n]+`|\[[^\]]+\]\([^)\n]+\)|\*[^*\n]+\*|_[^_\n]+_|<https?:\/\/[^\s>]+>|https?:\/\/[^\s<]+)/g;
      var last = 0;
      var match;
      source = String(source || "");
      while ((match = pattern.exec(source))) {
        if (match.index > last) target.appendChild(document.createTextNode(source.slice(last, match.index)));
        var token = match[0];
        if (token.indexOf("**") === 0 || token.indexOf("__") === 0) {
          var strong = document.createElement("strong");
          strong.textContent = token.slice(2, -2);
          target.appendChild(strong);
        } else if (token.indexOf("*") === 0 || token.indexOf("_") === 0) {
          var emphasis = document.createElement("em");
          emphasis.textContent = token.slice(1, -1);
          target.appendChild(emphasis);
        } else if (token.indexOf("~~") === 0) {
          var deleted = document.createElement("del");
          deleted.textContent = token.slice(2, -2);
          target.appendChild(deleted);
        } else if (token.indexOf("`") === 0) {
          var code = document.createElement("code");
          code.textContent = token.slice(1, -1);
          target.appendChild(code);
        } else if (token.indexOf("[") === 0) {
          var parts = token.match(/^\[([^\]]+)\]\(([^)]+)\)$/);
          var href = parts ? safeHref(parts[2]) : "";
          appendSafeLink(target, href, parts ? parts[1] : token);
        } else {
          var bareHref = safeHref(token.replace(/^<|>$/g, ""));
          appendSafeLink(target, bareHref, token.replace(/^<|>$/g, ""));
        }
        last = pattern.lastIndex;
      }
      if (last < source.length) target.appendChild(document.createTextNode(source.slice(last)));
    }

    function renderMarkdown(target, markdown) {
      if (window.CogentiaMarkdown) return window.CogentiaMarkdown.render(target, markdown);
      target.textContent = "";
      var lines = String(markdown || "").replace(/\r\n/g, "\n").split("\n");
      var index = 0;
      while (index < lines.length) {
        var line = lines[index];
        if (!line.trim()) {
          index += 1;
          continue;
        }
        if (/^```/.test(line.trim())) {
          var code = [];
          index += 1;
          while (index < lines.length && !/^```/.test(lines[index].trim())) {
            code.push(lines[index]);
            index += 1;
          }
          if (index < lines.length) index += 1;
          var pre = document.createElement("pre");
          var codeEl = document.createElement("code");
          codeEl.textContent = code.join("\n");
          pre.appendChild(codeEl);
          target.appendChild(pre);
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
        if (/^\s*\d+\.\s+/.test(line)) {
          var ol = document.createElement("ol");
          while (index < lines.length && /^\s*\d+\.\s+/.test(lines[index])) {
            var oli = document.createElement("li");
            appendInlineMarkdown(oli, lines[index].replace(/^\s*\d+\.\s+/, ""));
            ol.appendChild(oli);
            index += 1;
          }
          target.appendChild(ol);
          continue;
        }
        if (/^>\s?/.test(line)) {
          var quote = document.createElement("blockquote");
          var quoteLines = [];
          while (index < lines.length && /^>\s?/.test(lines[index])) {
            quoteLines.push(lines[index].replace(/^>\s?/, ""));
            index += 1;
          }
          appendInlineMarkdown(quote, quoteLines.join(" "));
          target.appendChild(quote);
          continue;
        }
        var paragraph = [];
        while (index < lines.length && lines[index].trim() && !/^```/.test(lines[index].trim()) && !/^(#{1,3})\s+/.test(lines[index]) && !/^\s*[-*]\s+/.test(lines[index]) && !/^\s*\d+\.\s+/.test(lines[index]) && !/^>\s?/.test(lines[index])) {
          paragraph.push(lines[index]);
          index += 1;
        }
        var p = document.createElement("p");
        appendInlineMarkdown(p, paragraph.join(" "));
        target.appendChild(p);
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
      var recent = thread.entries.slice(-recentKeep).map(function (entry) {
        if (entry.type === "user") return { role: "user", content: entry.text || "" };
        if (entry.type === "answer") return { role: "assistant", content: (entry.data && entry.data.answer) || "" };
        return null;
      }).filter(function (entry) {
        return entry && entry.content && entry.content.trim();
      });
      var header = text(
        "Continuity brief of earlier conversation. Use it to stay consistent. It is not evidence; cite only public corpus or web context.",
        "Brief de continuité de la conversation plus ancienne. Utilise-le pour rester cohérent. Ce n'est pas une preuve ; ne citer que le corpus public ou le web."
      );
      var chunks = chunkHistory(continuityText(thread), header);
      var keepRecent = Math.min(recent.length, Math.max(8, historyWireLimit - Math.min(chunks.length, 4)));
      var room = Math.max(0, historyWireLimit - keepRecent);
      return chunks.slice(0, room).concat(recent.slice(-keepRecent));
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
