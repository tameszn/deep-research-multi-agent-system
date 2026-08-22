import './2-C0uxS_Ck.js';
import './Index17-CX97JLQ0.js';
import { d } from './Index42-BX1RRbsK.js';
import { b as attr_style, h as stringify, a as attr_class, f as ensure_array_like, e as escape_html, d as attr } from './renderer-B44-mkIR.js';
import './async-Cv1-GZGV.js';
import './environment-BxEoFHfh.js';
import './chunk-MAaCUEXr.js';
import 'node:module';
import './statustracker-Dcv3b821.js';
import './src3-BYRta5-S.js';
import './html-CfyvkLET.js';
import './server-ozwWCFiP.js';
import './markdown-code-OsHIP1Mw.js';

function r(r,i){r.component(r=>{let {app:a,root:o}=i,s=350,l=[],u=[];(async()=>{a.post_data(`${o}/gradio_api/vibe-starter-queries/`,{}).then(async([e,t])=>{if(t!==200)throw Error(`Error: ${t}`);u=e.starter_queries;}).catch(async e=>{console.error(`Failed to fetch starter queries:`,e);});})();let p=true,m;function h(t){t.push(`<div class="vibe-editor svelte-1s2fnws"${attr_style(`width: ${stringify(s)}px;`)}><button class="resize-handle svelte-1s2fnws" aria-label="Resize sidebar"></button> <div class="tab-header svelte-1s2fnws"><button${attr_class(`tab-button svelte-1s2fnws`,void 0,{active:true})}>Chat</button> <button${attr_class(`tab-button svelte-1s2fnws`,void 0,{active:false})}>Code `),t.push(`<!--[!-->`),t.push(`<!--]--></button></div> <div class="tab-content svelte-1s2fnws">`);{t.push(`<!--[-->`),t.push(`<div class="message-history svelte-1s2fnws"><!--[-->`);let r=ensure_array_like(l);for(let i=0,a=r.length;i<a;i++){let a=r[i];t.push(`<div${attr_class(`message-item svelte-1s2fnws`,void 0,{"bot-message":a.isBot,"user-message":!a.isBot})}><div class="message-content svelte-1s2fnws"><span class="message-text svelte-1s2fnws">`),d(t,{value:a.text,latex_delimiters:[],theme_mode:`system`}),t.push(`<!----></span> `),!a.isBot&&a.hash&&!a.isPending?(t.push(`<!--[-->`),t.push(`<button class="undo-button svelte-1s2fnws" title="Undo this change">Undo</button>`)):t.push(`<!--[!-->`),t.push(`<!--]--></div></div>`);}if(t.push(`<!--]--> `),l.length===0?(t.push(`<!--[-->`),t.push(`<div class="no-messages svelte-1s2fnws">No messages yet</div>`)):t.push(`<!--[!-->`),t.push(`<!--]--> `),l.length===0){t.push(`<!--[-->`),t.push(`<div class="starter-queries-container svelte-1s2fnws"><div class="starter-queries svelte-1s2fnws"><!--[-->`);let e=ensure_array_like(u);for(let r=0,i=e.length;r<i;r++){let i=e[r];t.push(`<button class="starter-query-button svelte-1s2fnws">${escape_html(i)}</button>`);}t.push(`<!--]--></div></div>`);}else t.push(`<!--[!-->`);t.push(`<!--]--></div>`);}t.push(`<!--]--></div> <div class="input-section svelte-1s2fnws"><div class="powered-by svelte-1s2fnws">Powered by: <code>gpt-oss</code></div> <textarea placeholder="What can I add or change?" class="prompt-input svelte-1s2fnws">`);let r=escape_html(``);r&&t.push(`${r}`),t.push(`</textarea> <button class="submit-button svelte-1s2fnws"${attr(`disabled`,true,true)}>Send</button></div></div>`);}do p=true,m=r.copy(),h(m);while(!p);r.subsume(m);});}

export { r as default };
//# sourceMappingURL=Index61-DUtI7p1r.js.map
