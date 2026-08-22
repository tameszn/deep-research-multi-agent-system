import { O as c } from './2-C0uxS_Ck.js';
import { h, v, V as Ve, H, a as He, g, _, i as ie, I as Ie } from './src3-BYRta5-S.js';
import { t } from './Image-D9mSw2LY.js';
import './async-Cv1-GZGV.js';
import { a as attr_class, c as bind_props } from './renderer-B44-mkIR.js';

function f(f,p){f.component(f=>{let{value:m,label:h$1=void 0,show_label:g$1,buttons:_$1=[],on_custom_button_click:v$1=null,selectable:y=false,i18n:b,display_icon_button_wrapper_top_corner:x=false,fullscreen:S=false,show_button_background:C=true,onselect:w,onfullscreen:T,onshare:E,onerror:D,onload:O}=p;h(f,{show_label:g$1,Icon:H,label:g$1?h$1||b(`image.image`):``}),f.push(`<!----> `),m==null||!m?.url?(f.push(`<!--[-->`),v(f,{unpadded_box:true,size:`large`,children:e=>{H(e);}})):(f.push(`<!--[!-->`),f.push(`<div class="image-container svelte-12vrxzd">`),Ve(f,{display_top_corner:x,show_background:C,buttons:_$1,on_custom_button_click:v$1,children:t=>{_$1.some(e=>typeof e==`string`&&e===`fullscreen`)?(t.push(`<!--[-->`),He(t,{fullscreen:S,onclick:e=>{S=e,T?.(e);}})):t.push(`<!--[!-->`),t.push(`<!--]--> `),_$1.some(e=>typeof e==`string`&&e===`download`)?(t.push(`<!--[-->`),g(t,{href:m.url,download:m.orig_name||`image`,children:e=>{_(e,{Icon:ie,label:b(`common.download`)});},$$slots:{default:true}})):t.push(`<!--[!-->`),t.push(`<!--]--> `),_$1.some(e=>typeof e==`string`&&e===`share`)?(t.push(`<!--[-->`),Ie(t,{i18n:b,onshare:e=>E?.(e),onerror:e=>D?.(e),formatter:async t=>t?`<img src="${await c(t)}" />`:``,value:m})):t.push(`<!--[!-->`),t.push(`<!--]-->`);}}),f.push(`<!----> <button class="svelte-12vrxzd"><div${attr_class(`image-frame svelte-12vrxzd`,void 0,{selectable:y})}>`),t(f,{src:m.url,restProps:{loading:`lazy`,alt:``},onload:O}),f.push(`<!----></div></button></div>`)),f.push(`<!--]-->`),bind_props(p,{fullscreen:S});});}

export { f };
//# sourceMappingURL=ImagePreview-B9cTvdkV.js.map
