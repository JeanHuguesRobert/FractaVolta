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
    var expand = root.querySelector(".guide-widget__expand");
    var clear = root.querySelector(".guide-widget__clear");
    var form = root.querySelector(".guide-widget__form");
    var input = root.querySelector(".guide-widget__input");
    var log = root.querySelector(".guide-widget__log");
    var submit = root.querySelector(".guide-widget__submit");
    var pageTitle = root.getAttribute("data-guide-page-title") || "";
    var pagePath = root.getAttribute("data-guide-page-path") || "";
    var memoryKey = "fractavolta.guide.v1." + locale;
    var memoryTtlMs = 7 * 24 * 60 * 60 * 1000;
    var maxMemoryEntries = 20;
    var conversation = loadConversation();

    function text(en, fr) {
      return locale.indexOf("fr") === 0 ? fr : en;
    }

    function setOpen(open) {
      panel.hidden = !open;
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
      if (open) input.focus();
    }

    function setExpanded(open) {
      root.classList.toggle("guide-widget--expanded", open);
      expand.setAttribute("aria-pressed", open ? "true" : "false");
      expand.textContent = open ? text("Dock", "Reduire") : text("Full", "Agrandir");
      expand.setAttribute("aria-label", open ? text("Dock Guide", "Reduire le Guide") : text("Expand Guide", "Agrandir le Guide"));
      if (open) setOpen(true);
      if (!panel.hidden) input.focus();
    }

    function closeGuide() {
      if (root.classList.contains("guide-widget--expanded")) setExpanded(false);
      setOpen(false);
    }

    function addMessage(kind, value, remember) {
      var block = document.createElement("div");
      block.className = "guide-widget__message guide-widget__message--" + kind;
      block.textContent = value;
      log.appendChild(block);
      log.scrollTop = log.scrollHeight;
      if (remember) rememberEntry({ type: kind, text: value });
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
      } else if (event.name === "guide_web_search") {
        var webCount = Array.isArray(data.source_ids) ? data.source_ids.length : 0;
        setProgressStep(
          progress,
          "web",
          data.ok
            ? text("Checked the web: " + webCount + " result(s)", "Recherche web : " + webCount + " resultat(s)")
            : text("Web search did not add usable results", "La recherche web n'a pas ajoute de resultat exploitable"),
          data.ok ? "done" : "muted"
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

    function addAnswer(data, remember) {
      var block = document.createElement("article");
      block.className = "guide-widget__answer";

      var body = document.createElement("div");
      body.className = "guide-widget__answer-text";
      renderMarkdown(body, data.answer || text("No answer returned.", "Aucune reponse retournee."));
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

      addAgentHandoff(block, data);
      addSuggestions(block, data);

      log.appendChild(block);
      log.scrollTop = log.scrollHeight;
      if (remember) rememberEntry({ type: "answer", data: compactAnswer(data) });
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

    function appendInlineMarkdown(target, textValue) {
      var source = String(textValue || "");
      var pattern = /(\*\*[^*]+\*\*|`[^`]+`|\[[^\]]+\]\([^)]+\))/g;
      var last = 0;
      var match;
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

    function safeHref(value) {
      var href = String(value || "").trim();
      return /^(https?:|mailto:|\/|#)/i.test(href) ? href : "";
    }

    function addAgentHandoff(block, data) {
      var section = document.createElement("div");
      section.className = "guide-widget__handoff";

      var button = document.createElement("button");
      button.type = "button";
      button.className = "guide-widget__handoff-toggle";
      button.textContent = text("Deepen with your own agent", "Approfondir avec votre propre agent");
      section.appendChild(button);

      var panel = document.createElement("div");
      panel.className = "guide-widget__handoff-panel";
      panel.hidden = true;

      var intro = document.createElement("p");
      intro.className = "guide-widget__handoff-help";
      intro.textContent = text(
        "First time: copy this prompt, paste it into ChatGPT, Claude, Grok or another agent, then continue there. The prompt asks your agent to stay grounded and to bring you back here with a useful follow-up question.",
        "Premiere fois : copiez ce prompt, collez-le dans ChatGPT, Claude, Grok ou un autre agent, puis continuez la-bas. Le prompt demande a votre agent de rester ancre dans les sources et de vous proposer un retour utile vers ce Guide."
      );
      panel.appendChild(intro);

      var textarea = document.createElement("textarea");
      textarea.className = "guide-widget__handoff-prompt";
      textarea.rows = 9;
      textarea.readOnly = true;
      textarea.value = buildAgentPrompt(data);
      panel.appendChild(textarea);

      var actions = document.createElement("div");
      actions.className = "guide-widget__handoff-actions";

      var copy = document.createElement("button");
      copy.type = "button";
      copy.textContent = text("Copy prompt", "Copier le prompt");
      copy.addEventListener("click", function () {
        copyText(textarea.value).then(function (ok) {
          if (!ok) textarea.select();
          copy.textContent = ok ? text("Copied", "Copie") : text("Select and copy", "Selectionnez puis copiez");
          setTimeout(function () {
            copy.textContent = text("Copy prompt", "Copier le prompt");
          }, 1800);
        });
      });
      actions.appendChild(copy);

      var useHere = document.createElement("button");
      useHere.type = "button";
      useHere.textContent = text("Ask the Guide again", "Revenir au Guide");
      useHere.addEventListener("click", function () {
        var prompt = guideReturnPrompt(data);
        input.value = prompt;
        setOpen(true);
        input.focus();
      });
      actions.appendChild(useHere);

      panel.appendChild(actions);
      section.appendChild(panel);

      button.addEventListener("click", function () {
        panel.hidden = !panel.hidden;
        if (!panel.hidden) textarea.focus();
      });

      block.appendChild(section);
    }

    function buildAgentPrompt(data) {
      var question = String((data && data.question) || "").trim();
      var answer = String((data && data.answer) || "").trim();
      var sources = Array.isArray(data && data.sources) ? data.sources.slice(0, 8) : [];
      var excerpts = guideSourceExcerpts(data);
      var webSearch = data && data.context && data.context.web_search;
      var lines = [
        text("# FractaVolta public Guide handoff", "# Passage depuis le Guide public FractaVolta"),
        "",
        text(
          "You are helping me deepen a public FractaVolta Guide answer. Stay grounded in the supplied public sources. Distinguish corpus sources from web sources. If evidence is insufficient, say so.",
          "Aidez-moi a approfondir une reponse du Guide public FractaVolta. Restez ancre dans les sources publiques fournies. Distinguez les sources du corpus des sources web. Si les preuves sont insuffisantes, dites-le."
        ),
        "",
        text("## My question", "## Ma question"),
        question || text("No question captured.", "Aucune question capturee."),
        "",
        text("## Guide answer", "## Reponse du Guide"),
        answer || text("No answer captured.", "Aucune reponse capturee."),
        "",
        text("## Public sources", "## Sources publiques"),
      ];
      if (sources.length) {
        sources.forEach(function (source, index) {
          var parts = [
            (index + 1) + ". " + (source.title || source.path || source.source_id || text("Untitled source", "Source sans titre")),
            "source_id=" + (source.source_id || ""),
          ];
          if (source.url) parts.push("url=" + source.url);
          lines.push(parts.join(" | "));
        });
      } else {
        lines.push(text("No source list was captured.", "Aucune liste de sources n'a ete capturee."));
      }
      if (excerpts.length) {
        lines.push("", text("## Relevant public excerpts", "## Extraits publics utiles"));
        excerpts.forEach(function (item, index) {
          lines.push(
            "",
            "### " + (index + 1) + ". " + item.source_id,
            item.text
          );
        });
      }
      if (webSearch && webSearch.attempted) {
        lines.push(
          "",
          text("## Web search note", "## Note de recherche web"),
          text(
            "The Guide attempted web search. Treat web results as current external context, not as corpus authority.",
            "Le Guide a tente une recherche web. Traitez les resultats web comme un contexte externe actuel, pas comme l'autorite du corpus."
          )
        );
      }
      lines.push(
        "",
        text("## What I want from you", "## Ce que j'attends de vous"),
        text(
          "1. Explain the answer more deeply.\n2. Keep citations to the source ids or URLs above.\n3. Separate what is certain, plausible, and missing.\n4. End by proposing one precise follow-up question I can paste back into the FractaVolta Guide.",
          "1. Approfondissez la reponse.\n2. Citez les source_id ou URL ci-dessus.\n3. Separez ce qui est certain, plausible et manquant.\n4. Terminez en proposant une question de suivi precise que je pourrai recoller dans le Guide FractaVolta."
        ),
        "",
        text("Public Guide endpoint:", "Endpoint du Guide public :"),
        endpoint
      );
      return lines.join("\n");
    }

    function guideSourceExcerpts(data) {
      var raw = data && data.context && Array.isArray(data.context.excerpts) ? data.context.excerpts : [];
      var seen = {};
      return raw.map(function (item) {
        var sourceId = String(item && item.source_id || "").trim();
        var textValue = compactPromptText(item && item.text, 700);
        if (!sourceId || !textValue || seen[sourceId]) return null;
        seen[sourceId] = true;
        return { source_id: sourceId, text: textValue };
      }).filter(Boolean).slice(0, 6);
    }

    function compactPromptText(value, maxChars) {
      var clean = String(value || "").replace(/\s+/g, " ").trim();
      if (!clean) return "";
      if (clean.length <= maxChars) return clean;
      return clean.slice(0, Math.max(1, maxChars - 3)).trim() + "...";
    }

    function guideReturnPrompt(data) {
      var question = String((data && data.question) || "").trim();
      return text(
        "Help me go one level deeper than this previous question, using the public corpus and sources: " + question,
        "Aide-moi a aller un niveau plus loin que cette question precedente, en utilisant le corpus public et les sources : " + question
      );
    }

    async function copyText(value) {
      try {
        if (navigator.clipboard && window.isSecureContext) {
          await navigator.clipboard.writeText(value);
          return true;
        }
      } catch (error) {}
      return false;
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
      var topic = guideTopic(question);
      var webSearch = data && data.context && data.context.web_search;
      var suggestions = [];

      if (topic === "collectivites") {
        suggestions.push({
          label: text("Show public services", "Services communaux"),
          prompt: text(
            "Which local public services could a FractaVolta pilot support first?",
            "Quels services publics locaux une commune corse pourrait-elle soutenir en premier avec un pilote FractaVolta ?"
          ),
        });
        suggestions.push({
          label: text("Pilot checklist", "Checklist pilote"),
          prompt: text(
            "Give a cautious public checklist for a small FractaVolta municipal pilot.",
            "Donne une checklist publique et prudente pour demarrer un petit pilote communal FractaVolta."
          ),
        });
      } else if (topic === "agriculteurs") {
        suggestions.push({
          label: text("Owner value", "Valeur proprietaire"),
          prompt: text(
            "Explain the owner value proposition for a Corsican agricultural solar second-life site.",
            "Explique la proposition de valeur pour un proprietaire agricole corse avec un site solaire en seconde vie."
          ),
        });
      } else if (topic === "installateurs") {
        suggestions.push({
          label: text("Roles", "Roles"),
          prompt: text(
            "How should FractaVolta and local installers divide responsibilities?",
            "Comment FractaVolta et les installateurs locaux devraient-ils partager les responsabilites ?"
          ),
        });
      } else if (topic === "packets") {
        suggestions.push({
          label: text("Make it concrete", "Rendre concret"),
          prompt: text(
            "Give a concrete local example of energy packets in operation.",
            "Donne un exemple local concret de paquets d'energie en fonctionnement."
          ),
        });
      } else if (topic === "research") {
        suggestions.push({
          label: text("Core papers", "Textes centraux"),
          prompt: text(
            "Which public corpus documents should a researcher read first, and why?",
            "Quels documents publics du corpus un chercheur devrait-il lire en premier, et pourquoi ?"
          ),
        });
      } else if (topic === "partners") {
        suggestions.push({
          label: text("Partner fit", "Bon partenaire"),
          prompt: text(
            "What makes a good first FractaVolta partner?",
            "Qu'est-ce qui fait un bon premier partenaire FractaVolta ?"
          ),
        });
      } else if (topic === "cogentia") {
        suggestions.push({
          label: text("Traceability", "Tracabilite"),
          prompt: text(
            "How does Cogentia make the public FractaVolta story traceable?",
            "Comment Cogentia rend-il l'histoire publique de FractaVolta tracable ?"
          ),
        });
      }

      if (question.indexOf("cogentia") === -1 && question.indexOf("jumeau") === -1 && question.indexOf("twin") === -1) {
        suggestions.push({
          label: text("Connect to Cogentia", "Relier a Cogentia"),
          prompt: text(
            "How does Cogentia help explain or operate this FractaVolta idea?",
            "Quel lien avec Cogentia, le corpus public et la methode de tracabilite ?"
          ),
        });
      }
      if (sourceCount > 0 && question.indexOf("read") === -1 && question.indexOf("lecture") === -1 && question.indexOf("parcours") === -1) {
        suggestions.push({
          label: text("Reading path", "Parcours de lecture"),
          prompt: text(
            "Turn these sources into a 10-minute public reading path.",
            "Transforme ces sources en parcours de lecture public de 10 minutes pour comprendre FractaVolta en Corse."
          ),
        });
      }
      if (question.indexOf("packet") === -1 && question.indexOf("paquet") === -1 && topic !== "packets") {
        suggestions.push({
          label: text("Energy packets", "Paquets d'energie"),
          prompt: text(
            "Why does FractaVolta use the packet idea for energy and compute?",
            "Pourquoi FractaVolta parle-t-il de paquets d'energie pour les usages locaux en Corse ?"
          ),
        });
      }
      if (webSearch && webSearch.attempted && !webSearch.ok) {
        suggestions.push({
          label: text("Corpus only", "Corpus seul"),
          prompt: text(
            "Answer again using only the public corpus, without relying on current web search.",
            "Reponds a nouveau uniquement avec le corpus public, sans dependance a la recherche web actuelle."
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

    function guideTopic(question) {
      var haystack = [pagePath, pageTitle, question].join(" ").toLowerCase();
      if (/collectiv|commune|municipal/.test(haystack)) return "collectivites";
      if (/agric|propriet|owner|vigne|rural/.test(haystack)) return "agriculteurs";
      if (/installateur|installer/.test(haystack)) return "installateurs";
      if (/paquet|packet|energy-packet/.test(haystack)) return "packets";
      if (/paper|research|chercheur|papers|methodology/.test(haystack)) return "research";
      if (/partner|partenaire/.test(haystack)) return "partners";
      if (/deploy|deployer|deploi/.test(haystack)) return "deployers";
      if (/cogentia|jumeau|twin|trace/.test(haystack)) return "cogentia";
      if (/rossignol/.test(haystack)) return "rossignol";
      if (/marche|market/.test(haystack)) return "marches";
      if (/seconde|second-life|second life|logistique/.test(haystack)) return "second_life";
      return "general";
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
      var history = guideHistoryPayload();
      addMessage("user", question, true);
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
          body: JSON.stringify({ question: question, locale: locale, stream: true, history: history }),
        });
        var data = await readGuideResponse(response, pending);
        if (!response.ok || !data || data.ok === false) {
          throw new Error((data && data.message) || text("The Guide is unavailable.", "Le Guide est indisponible."));
        }
        addAnswer(data, true);
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

    function loadConversation() {
      var now = Date.now();
      try {
        var parsed = JSON.parse(localStorage.getItem(memoryKey) || "[]");
        if (!Array.isArray(parsed)) return [];
        return parsed.filter(function (entry) {
          return entry && typeof entry.at === "number" && now - entry.at < memoryTtlMs;
        }).slice(-maxMemoryEntries);
      } catch (error) {
        return [];
      }
    }

    function saveConversation() {
      try {
        localStorage.setItem(memoryKey, JSON.stringify(conversation.slice(-maxMemoryEntries)));
      } catch (error) {}
    }

    function rememberEntry(entry) {
      conversation.push(Object.assign({ at: Date.now() }, entry));
      conversation = conversation.slice(-maxMemoryEntries);
      saveConversation();
    }

    function compactAnswer(data) {
      return {
        ok: true,
        question: data.question,
        answer: data.answer,
        sources: Array.isArray(data.sources) ? data.sources.slice(0, 5) : [],
        warnings: Array.isArray(data.warnings) ? data.warnings.slice(0, 5) : [],
      };
    }

    function guideHistoryPayload() {
      return conversation.slice(-10).map(function (entry) {
        if (entry.type === "user") return { role: "user", content: entry.text || "" };
        if (entry.type === "answer") return { role: "assistant", content: (entry.data && entry.data.answer) || "" };
        return null;
      }).filter(function (entry) {
        return entry && entry.content && entry.content.trim();
      });
    }

    function renderStoredConversation() {
      conversation.forEach(function (entry) {
        if (entry.type === "user") addMessage("user", entry.text || "", false);
        if (entry.type === "answer" && entry.data) addAnswer(entry.data, false);
      });
    }

    function clearConversation() {
      conversation = [];
      try {
        localStorage.removeItem(memoryKey);
      } catch (error) {}
      log.textContent = "";
      input.focus();
    }

    toggle.addEventListener("click", function () { setOpen(panel.hidden); });
    close.addEventListener("click", closeGuide);
    expand.addEventListener("click", function () { setExpanded(!root.classList.contains("guide-widget--expanded")); });
    clear.addEventListener("click", clearConversation);
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
    renderStoredConversation();
  });
}());
