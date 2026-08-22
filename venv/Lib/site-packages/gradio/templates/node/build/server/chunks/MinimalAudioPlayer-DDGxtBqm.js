import { L as onDestroy, P as u } from './2-C0uxS_Ck.js';
import './async-Cv1-GZGV.js';
import { d as attr, e as escape_html } from './renderer-B44-mkIR.js';

var _=(e,t)=>(t||=5,e/100*t||5);function v(i,a){i.component(i=>{let{value:o,label:s,loop:c=false}=a;o.url;onDestroy(()=>{}),i.push(`<div class="minimal-audio-player svelte-15unlcf"${attr(`aria-label`,s||`Audio`)}${attr(`data-testid`,s&&typeof s==`string`&&s.trim()?`waveform-`+s:`unlabelled-audio`)}><button class="play-btn svelte-15unlcf"${attr(`aria-label`,`Play`)}>`),i.push(`<!--[!-->`),i.push(`<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="svelte-15unlcf"><path d="M8 5.74537C8 5.06444 8.77346 4.64713 9.35139 5.02248L18.0227 10.2771C18.5518 10.6219 18.5518 11.3781 18.0227 11.7229L9.35139 16.9775C8.77346 17.3529 8 16.9356 8 16.2546V5.74537Z" fill="currentColor"></path></svg>`),i.push(`<!--]--></button> <div class="waveform-wrapper svelte-15unlcf"></div> <div class="timestamp svelte-15unlcf">${escape_html(u(0))}</div></div>`);});}

export { _, v };
//# sourceMappingURL=MinimalAudioPlayer-DDGxtBqm.js.map
