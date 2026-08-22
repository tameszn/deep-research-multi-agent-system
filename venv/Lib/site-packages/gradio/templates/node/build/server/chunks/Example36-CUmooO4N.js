import { t } from './Image-D9mSw2LY.js';
import './2-C0uxS_Ck.js';
import { a as attr_class, e as escape_html, f as ensure_array_like, d as attr } from './renderer-B44-mkIR.js';
import './async-Cv1-GZGV.js';
import { z as zu } from './Video-D7v-pvA7.js';

function r(r,i){r.component(r=>{let{value:a={text:``,files:[]},type:o,selected:s=false}=i;r.push(`<div${attr_class(`container svelte-xz0m7l`,void 0,{table:o===`table`,gallery:o===`gallery`,selected:s,border:a})}><p>${escape_html(a.text?a.text:``)}</p> <!--[-->`);let c=ensure_array_like(a.files);for(let i=0,a=c.length;i<a;i++){let a=c[i];a.mime_type&&a.mime_type.includes(`image`)?(r.push(`<!--[-->`),t(r,{src:a.url,alt:``})):(r.push(`<!--[!-->`),a.mime_type&&a.mime_type.includes(`video`)?(r.push(`<!--[-->`),zu(r,{src:a.url,alt:``,loop:true,is_stream:false})):(r.push(`<!--[!-->`),a.mime_type&&a.mime_type.includes(`audio`)?(r.push(`<!--[-->`),r.push(`<audio${attr(`src`,a.url)} controls></audio>`)):(r.push(`<!--[!-->`),r.push(`${escape_html(a.orig_name)}`)),r.push(`<!--]-->`)),r.push(`<!--]-->`)),r.push(`<!--]-->`);}r.push(`<!--]--></div>`);});}

export { r };
//# sourceMappingURL=Example36-CUmooO4N.js.map
