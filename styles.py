"""UI assets for the Deep Research app: content, theme tokens, CSS and client-side JS."""

# ============================================================================
# CONTENT: example prompts, one set per theme
# ============================================================================
EXAMPLES = {
    "dark": [  # Slate & Sage: technical / analytical
        "Most popular AI Agent frameworks in 2026",
        "Most commercially successful Agentic AI implementations in 2026",
        "Benchmarking open-weights reasoning models on multi-hop search",
    ],
    "light": [  # Warm Alabaster: editorial / broad research
        "The economics of next-generation nuclear microreactors",
        "How global supply chains adapted to autonomous freight",
        "Celebrities who don't like cheese",
    ],
}

HEADER_HTML = """
<nav class="dr-nav" aria-label="Main">
    <div class="dr-brand">
        <div class="dr-mark" aria-hidden="true"><span></span><span></span><span></span></div>
        <div>
            <h1>Deep<span class="dr-sep">/</span>Research</h1>
            <p>Multi-search web investigation</p>
        </div>
    </div>
    <div class="dr-actions">
        <div class="dr-soon" aria-disabled="true">
            <span class="dr-soon-pill">QA Room</span>
            <span class="dr-soon-badge">Coming Soon</span>
        </div>
        <button type="button" id="dr-theme-toggle" aria-label="Switch colour theme">
            <span class="dr-when-dark">&#9728; Light</span>
            <span class="dr-when-light">&#9790; Dark</span>
        </button>
    </div>
</nav>
"""

# ============================================================================
# DAILY REMINDER: a link to Google Calendar's pre-filled event page (no OAuth)
# ============================================================================
REMINDER_HTML = """
<section class="dr-reminder" aria-labelledby="dr-remind-title">
    <svg class="dr-cal-art" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="0.8"
         stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
        <rect x="3" y="5" width="18" height="16" rx="3"/>
        <path d="M3 10h18M8 3v4M16 3v4M8.5 15.5l2.5 2.5 4.5-4.5"/>
    </svg>
    <span class="dr-brain" aria-hidden="true">&#129504;</span>
    <h2 id="dr-remind-title">Add a daily reminder</h2>
    <p>Block out a daily research session in Google Calendar.</p>
    <div class="dr-remind-controls">
        <label for="dr-remind-time">Time</label>
        <input type="time" id="dr-remind-time" value="19:00">
        <a id="dr-remind-link" href="https://calendar.google.com/calendar/render?action=TEMPLATE"
           target="_blank" rel="noopener noreferrer">Add to Google Calendar</a>
    </div>
    <small> better, daily</small>
</section>
"""

# ============================================================================
# HEAD: fonts and all client-side JS.
# The JS lives here because launch(js=...) did not run it on some Gradio 6 releases.
# ============================================================================
HEAD = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<script>
(() => {
    if (window.__drUI) return;  // never bind twice, or one click would toggle twice
    window.__drUI = true;

    const root = document.documentElement;
    const load = (key) => { try { return localStorage.getItem(key); } catch (e) { return null; } };
    const store = (key, value) => { try { localStorage.setItem(key, value); } catch (e) {} };

    // ---- Theme ----
    // Gradio toggles its own `.dark` class from the OS setting; keep it in step with ours.
    const syncGradio = () => {
        const dark = root.dataset.theme !== "light";
        [root, document.body].filter(Boolean).forEach((el) => {
            if (el.classList.contains("dark") !== dark) el.classList.toggle("dark", dark);
        });
    };
    const watchBody = () => {
        syncGradio();
        new MutationObserver(syncGradio).observe(document.body, { attributeFilter: ["class"] });
    };
    root.dataset.theme = load("dr-theme") === "light" ? "light" : "dark";
    if (document.body) watchBody();
    else document.addEventListener("DOMContentLoaded", watchBody);

    // ---- Daily reminder ----
    const reminderUrl = (time) => {
        const [hours, minutes] = (time || "19:00").split(":").map(Number);
        const now = new Date();
        const start = new Date(now);
        start.setHours(hours, minutes, 0, 0);
        if (start <= now) start.setDate(start.getDate() + 1);
        const end = new Date(start.getTime() + 30 * 60 * 1000);
        const pad = (n) => String(n).padStart(2, "0");
        const stamp = (d) => `${d.getFullYear()}${pad(d.getMonth() + 1)}${pad(d.getDate())}`
            + `T${pad(d.getHours())}${pad(d.getMinutes())}00`;
        const params = new URLSearchParams({
            action: "TEMPLATE",
            text: "🧠 Daily research session",
            details: "Pick one question and run it in Deep Research.",
            dates: `${stamp(start)}/${stamp(end)}`,
            recur: "RRULE:FREQ=DAILY",
            ctz: Intl.DateTimeFormat().resolvedOptions().timeZone,
        });
        return `https://calendar.google.com/calendar/render?${params}`;
    };

    // ---- Events: delegated and in the capture phase, so Gradio re-renders don't matter ----
    document.addEventListener("click", (event) => {
        if (event.target.closest("#dr-theme-toggle")) {
            root.dataset.theme = root.dataset.theme === "light" ? "dark" : "light";
            syncGradio();
            store("dr-theme", root.dataset.theme);
        }
    }, true);

    // Build the link just before it is followed (left, middle or right click, or keyboard).
    ["click", "auxclick", "contextmenu"].forEach((type) => document.addEventListener(type, (event) => {
        const link = event.target.closest("#dr-remind-link");
        if (link) link.href = reminderUrl(document.getElementById("dr-remind-time").value);
    }, true));

    document.addEventListener("change", (event) => {
        if (event.target.id === "dr-remind-time") store("dr-remind-time", event.target.value);
    }, true);

    // Restore the saved time once Gradio has rendered the section.
    let tries = 0;
    const timer = setInterval(() => {
        const input = document.getElementById("dr-remind-time");
        if (input && load("dr-remind-time")) input.value = load("dr-remind-time");
        if (input || ++tries > 100) clearInterval(timer);
    }, 100);
})();
</script>
"""

# ============================================================================
# CSS 1/6: theme tokens
# ============================================================================
_TOKENS = """
:root {
    --dr-bg: #0F1419;
    --dr-surface: #171F26;
    --dr-border: rgba(230, 237, 243, 0.10);
    --dr-accent: #529471;
    --dr-accent-hover: #5FA882;
    --dr-on-accent: #0F1419;
    --dr-text: #E6EDF3;
    --dr-muted: #8B949E;
    --dr-danger: #E5776E;
    --dr-ui: 'Inter', system-ui, -apple-system, 'Segoe UI', sans-serif;
    --dr-mono: 'JetBrains Mono', ui-monospace, Menlo, Consolas, monospace;
    color-scheme: dark;
}

:root[data-theme="light"] {
    --dr-bg: #F8F7F4;
    --dr-surface: #FFFFFF;
    --dr-border: rgba(17, 24, 39, 0.10);
    --dr-accent: #1E293B;
    --dr-accent-hover: #334155;
    --dr-on-accent: #FFFFFF;
    --dr-text: #111827;
    --dr-muted: #6B7280;
    --dr-danger: #B42318;
    color-scheme: light;
}

/* Point Gradio's own variables at our tokens so built-in components follow the theme. */
body, .dark, .gradio-container {
    --body-background-fill: var(--dr-bg);
    --background-fill-primary: var(--dr-bg);
    --background-fill-secondary: var(--dr-surface);
    --block-background-fill: transparent;
    --body-text-color: var(--dr-text);
    --body-text-color-subdued: var(--dr-muted);
    --border-color-primary: var(--dr-border);
    --color-accent: var(--dr-accent);
    --link-text-color: var(--dr-accent);
    --link-text-color-hover: var(--dr-accent-hover);
    --link-text-color-visited: var(--dr-accent);
    --link-text-color-active: var(--dr-accent);
    --code-background-fill: var(--dr-surface);
    --table-even-background-fill: transparent;
    --table-odd-background-fill: var(--dr-surface);
    --font: var(--dr-ui);
    --font-mono: var(--dr-mono);
}
"""

# ============================================================================
# CSS 2/6: page shell and navigation
# ============================================================================
_NAV = """
html, body, gradio-app, .gradio-container {
    background: var(--dr-bg) !important;
    color: var(--dr-text) !important;
}
.gradio-container { font-family: var(--dr-ui) !important; }
.gradio-container main {
    width: 100% !important;
    max-width: 960px !important;
    margin: 0 auto !important;
    padding: 1.25rem 1rem 4rem !important;
}
footer { display: none !important; }
/* Align custom HTML (nav, labels) with the search bar edges. */
.gradio-container .html-container { padding-inline: 0 !important; }

.dr-nav {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
    padding: 0.25rem 0 2rem;
}
.dr-brand, .dr-actions { display: flex; gap: 0.75rem; }
.dr-brand { align-items: center; }
.dr-actions { align-items: flex-start; }

.dr-mark { display: flex; flex-direction: column; gap: 4px; width: 26px; }
.dr-mark span { height: 5px; border-radius: 2px; background: var(--dr-accent); }
.dr-mark span:nth-child(2) { width: 70%; opacity: 0.7; }
.dr-mark span:nth-child(3) { width: 45%; opacity: 0.45; }

.dr-brand h1 {
    margin: 0 !important;
    font-size: 1.35rem !important;
    font-weight: 800;
    letter-spacing: -0.03em;
    line-height: 1.1;
    text-transform: uppercase;
    color: var(--dr-text) !important;
}
.dr-sep { color: var(--dr-accent); font-weight: 400; }
.dr-brand p {
    margin: 0.2rem 0 0 !important;
    font: 500 0.62rem var(--dr-mono);
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--dr-muted) !important;
}

.dr-soon { display: flex; flex-direction: column; align-items: center; gap: 3px; cursor: default; user-select: none; }
.dr-soon-pill, #dr-theme-toggle {
    box-sizing: border-box;
    height: 34px;
    display: inline-flex;
    align-items: center;
    padding: 0 0.9rem;
    border: 1px solid var(--dr-border);
    border-radius: 999px;
    font: 500 0.8rem var(--dr-ui);
}
.dr-soon-pill { color: var(--dr-muted); opacity: 0.65; }
.dr-soon-badge { font: 500 10px var(--dr-mono); text-transform: uppercase; color: var(--dr-muted); }

#dr-theme-toggle { background: var(--dr-surface); color: var(--dr-text); cursor: pointer; }
#dr-theme-toggle:hover { border-color: var(--dr-accent); }
#dr-theme-toggle:focus-visible { outline: 2px solid var(--dr-accent); outline-offset: 2px; }
:root:not([data-theme="light"]) .dr-when-light,
:root[data-theme="light"] .dr-when-dark { display: none; }
"""

# ============================================================================
# CSS 3/6: unified search pill
# ============================================================================
_SEARCH = """
#dr-search {
    display: flex !important;
    flex-wrap: nowrap !important;
    align-items: center !important;
    gap: 0.5rem !important;
    padding: 6px !important;
    background: var(--dr-surface) !important;
    border: 1px solid var(--dr-border) !important;
    border-radius: 12px !important;
    transition: border-color 0.15s, box-shadow 0.15s;
}
#dr-search:focus-within {
    border-color: var(--dr-accent) !important;
    box-shadow: 0 0 0 3px color-mix(in srgb, var(--dr-accent) 30%, transparent);
}
#dr-query { flex: 1 1 auto !important; min-width: 0 !important; }
#dr-query, #dr-query label, #dr-query .input-container {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}
#dr-query textarea, #dr-query input {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    outline: none !important;
    padding: 0.6rem 0.75rem !important;
    color: var(--dr-text) !important;
    font-family: var(--dr-mono) !important;
    font-size: 0.95rem !important;
}
#dr-query textarea::placeholder, #dr-query input::placeholder {
    font-family: var(--dr-mono) !important;
    color: var(--dr-muted) !important;
    opacity: 1;
}
#dr-run {
    flex: 0 0 auto !important;
    width: auto !important;
    min-width: 84px !important;
    height: 38px;
    padding: 0 1.25rem !important;
    border: none !important;
    border-radius: 999px !important;
    background: var(--dr-accent) !important;
    color: var(--dr-on-accent) !important;
    font: 600 0.85rem var(--dr-ui) !important;
    box-shadow: none !important;
}
#dr-run:hover { background: var(--dr-accent-hover) !important; }
#dr-run:focus-visible { outline: 2px solid var(--dr-text) !important; outline-offset: 2px; }
"""

# ============================================================================
# CSS 4/6: example pills (one set visible per theme)
# ============================================================================
_EXAMPLES = """
.dr-examples-label {
    margin-top: 1rem;
    font: 500 0.65rem var(--dr-mono);
    letter-spacing: 0.24em;
    text-transform: uppercase;
    color: var(--dr-muted);
}
#dr-examples { gap: 0 !important; }
/* Each selector is scoped by theme: Gradio re-prefixes plain ones, which breaks overrides. */
:root:not([data-theme="light"]) #dr-examples-light,
:root[data-theme="light"] #dr-examples-dark { display: none !important; }

#dr-examples-dark, #dr-examples-light { flex-wrap: wrap !important; gap: 8px !important; }
#dr-examples .dr-example {
    flex: 0 1 auto !important;
    width: auto !important;
    min-width: 0 !important;
    max-width: 100%;
    height: auto;
    padding: 0.55rem 0.95rem !important;
    background: var(--dr-surface) !important;
    border: 1px solid var(--dr-border) !important;
    border-radius: 999px !important;
    box-shadow: none !important;
    color: var(--dr-text) !important;
    font: 400 0.85rem/1.4 var(--dr-ui) !important;
    text-align: left;
    white-space: normal !important;
}
#dr-examples .dr-example:hover { border-color: var(--dr-accent) !important; }
"""

# ============================================================================
# CSS 5/6: status pill
# ============================================================================
_STATUS = """
#dr-report .dr-status {
    display: flex;
    width: fit-content;
    max-width: 100%;
    align-items: center;
    gap: 0.6rem;
    margin: 0 0 1.5rem;
    padding: 0.45rem 0.9rem;
    background: var(--dr-surface);
    border: 1px solid var(--dr-border);
    border-radius: 999px;
    font: 500 0.8rem/1.5 var(--dr-ui);
    color: var(--dr-text);
    overflow-wrap: anywhere;
}
#dr-report .dr-status-error { border-color: var(--dr-danger); border-radius: 12px; }
.dr-dot { flex: 0 0 auto; width: 8px; height: 8px; border-radius: 50%; background: var(--dr-accent); }
.dr-status-busy .dr-dot { animation: dr-pulse 1.2s ease-in-out infinite; }
.dr-status-done .dr-dot { background: #3FB67A; }
.dr-status-error .dr-dot { background: var(--dr-danger); }
@keyframes dr-pulse { 50% { opacity: 0.25; } }
@media (prefers-reduced-motion: reduce) { .dr-status-busy .dr-dot { animation: none; } }
"""

# ============================================================================
# CSS 6/6: report typography and small screens
# ============================================================================
_REPORT = """
#dr-report {
    width: 100% !important;
    max-width: 820px !important;
    margin: 1.75rem auto 0 !important;
}
#dr-report .prose, #dr-report .prose :is(h1, h2, h3, h4, h5, h6, p, li, strong, em, th, td, blockquote, code) {
    color: var(--dr-text) !important;
}
#dr-report .prose :is(p, li) { line-height: 1.75; }
#dr-report .prose :is(h1, h2, h3) { letter-spacing: -0.02em; margin: 1.6em 0 0.6em; }
#dr-report .prose a { color: var(--dr-accent) !important; text-decoration: underline; }
#dr-report .prose :is(th, td) { border-color: var(--dr-border) !important; }

@media (max-width: 600px) {
    .dr-brand p { letter-spacing: 0.1em; }
    #dr-run { min-width: 64px !important; padding: 0 0.9rem !important; }
}
"""

# ============================================================================
# CSS: daily reminder section (sits just below the fold until a report appears)
# ============================================================================
_REMINDER = """
#dr-reminder { margin-top: max(3rem, calc(100vh - 440px)) !important; }
body:has(#dr-report .dr-status) #dr-reminder { margin-top: 3rem !important; }

.dr-reminder {
    position: relative;
    isolation: isolate;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 380px;
    padding: 3rem 1.5rem;
    text-align: center;
    background: var(--dr-surface);
    border: 1px solid var(--dr-border);
    border-radius: 16px;
}
.dr-cal-art {
    position: absolute;
    z-index: -1;
    top: calc(50% - 22px);
    left: 50%;
    width: min(360px, 100%);
    height: 360px;
    transform: translate(-50%, -50%);
    color: var(--dr-accent);
    opacity: 0.09;
    pointer-events: none;
}
.dr-brain { position: absolute; top: 14px; right: 18px; font-size: 1.9rem; line-height: 1; }
.dr-reminder h2 {
    margin: 0 !important;
    font-size: 1.4rem !important;
    letter-spacing: -0.02em;
    color: var(--dr-text) !important;
}
.dr-reminder p { margin: 0.5rem 0 1.5rem !important; color: var(--dr-muted) !important; }
.dr-reminder small { display: block; margin-top: 1rem; color: var(--dr-muted); }
.dr-remind-controls { display: flex; flex-wrap: wrap; justify-content: center; align-items: center; gap: 0.75rem; }
.dr-remind-controls label { font: 500 0.65rem var(--dr-mono); letter-spacing: 0.2em; text-transform: uppercase; color: var(--dr-muted); }
#dr-remind-time {
    height: 40px;
    padding: 0 0.75rem;
    background: var(--dr-bg);
    color: var(--dr-text);
    border: 1px solid var(--dr-border);
    border-radius: 10px;
    font: 500 0.95rem var(--dr-mono);
}
#dr-remind-time:focus-visible, #dr-remind-link:focus-visible { outline: 2px solid var(--dr-accent); outline-offset: 2px; }
.dr-reminder a#dr-remind-link {
    display: inline-flex;
    align-items: center;
    height: 40px;
    padding: 0 1.25rem;
    background: var(--dr-accent);
    color: var(--dr-on-accent) !important;
    border-radius: 999px;
    font: 600 0.85rem var(--dr-ui);
    text-decoration: none !important;
}
.dr-reminder a#dr-remind-link:hover { background: var(--dr-accent-hover); }
"""

CSS = _TOKENS + _NAV + _SEARCH + _EXAMPLES + _STATUS + _REPORT + _REMINDER