import { J as m$1 } from './2-C0uxS_Ck.js';
import { f } from './statustracker-Dcv3b821.js';
import { r } from './Index7-Dgnp-Xma.js';
import { s as spread_props, a as attr_class, h as stringify, d as attr, b as attr_style, c as bind_props } from './renderer-B44-mkIR.js';
import './async-Cv1-GZGV.js';
import './environment-BxEoFHfh.js';
import './chunk-MAaCUEXr.js';
import 'node:module';
import './src3-BYRta5-S.js';
import './html-CfyvkLET.js';
import './server-ozwWCFiP.js';

function a(e,t){e.component(e=>{let{open:n=true,width:a,position:o=`left`,elem_classes:s=[],elem_id:c=``,onexpand:l=()=>{},oncollapse:u=()=>{},children:d}=t,f=typeof a==`number`?`${a}px`:a,p=false;let h=s?.join(` `)||``;e.push(`<div${attr_class(`sidebar ${stringify(h)}`,`svelte-1uruprb`,{open:false,right:o===`right`,"reduce-motion":p})}${attr(`id`,c)}${attr_style(`width: ${stringify(f)}; ${stringify(o)}: calc(${stringify(f)} * -1)`)}><button class="toggle-button svelte-1uruprb" aria-label="Toggle Sidebar"><div class="chevron svelte-1uruprb"><span class="chevron-left svelte-1uruprb"></span></div></button> <div class="sidebar-content svelte-1uruprb">`),d?.(e),e.push(`<!----></div></div>`),bind_props(t,{open:n,position:o});});}function o(r$1,o){r$1.component(r$1=>{let{$$slots:s,$$events:c,...l}=o,u=new m$1(l),d=true,f$1;function p(e){f(e,spread_props([{autoscroll:u.shared.autoscroll,i18n:u.i18n},u.shared.loading_status])),e.push(`<!----> `),u.shared.visible?(e.push(`<!--[-->`),a(e,{width:u.props.width,onexpand:()=>u.dispatch(`expand`),oncollapse:()=>u.dispatch(`collapse`),elem_classes:u.shared.elem_classes,elem_id:u.shared.elem_id,get open(){return u.props.open},set open(e){u.props.open=e,d=false;},get position(){return u.props.position},set position(e){u.props.position=e,d=false;},children:e=>{r(e,{children:e=>{l.children?.(e),e.push(`<!---->`);},$$slots:{default:true}});},$$slots:{default:true}})):e.push(`<!--[!-->`),e.push(`<!--]-->`);}do d=true,f$1=r$1.copy(),p(f$1);while(!d);r$1.subsume(f$1);});}

export { o as default };
//# sourceMappingURL=Index53-Dy_HL4sL.js.map
