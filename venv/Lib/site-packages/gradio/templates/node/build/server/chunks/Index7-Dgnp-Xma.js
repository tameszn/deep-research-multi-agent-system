import { J as m$1 } from './2-C0uxS_Ck.js';
import { f } from './statustracker-Dcv3b821.js';
import './async-Cv1-GZGV.js';
import { d as attr, a as attr_class, h as stringify, b as attr_style, s as spread_props } from './renderer-B44-mkIR.js';

function r(e,r){e.component(e=>{let{$$slots:i,$$events:a,...o}=r,s=o.scale??null,c=o.min_width??0,l=o.elem_id??``,u=o.elem_classes??[],d=o.visible??true,f$1=o.variant??`default`,p=o.loading_status;o.show_progress,e.push(`<div${attr(`id`,l)}${attr_class(`column ${stringify(u.join(` `))}`,`svelte-siq5d6`,{compact:f$1===`compact`,panel:f$1===`panel`,hide:!d})}${attr_style(``,{"flex-grow":s,"min-width":`calc(min(${stringify(c)}px, 100%))`})}>`),p&&p.show_progress?(e.push(`<!--[-->`),f(e,spread_props([{autoscroll:o.autoscroll??false,i18n:o.i18n??(e=>e)},p,{queue_size:p.queue_size??null,status:p?p.status==`pending`?`generating`:p.status:null}]))):e.push(`<!--[!-->`),e.push(`<!--]--> `),o.children?.(e),e.push(`<!----></div>`);});}function i(t,i){t.component(t=>{let{$$slots:a,$$events:o,...s}=i,c=new m$1(s);r(t,spread_props([c.shared,c.props,{children:e=>{s.children?.(e),e.push(`<!---->`);},$$slots:{default:true}}]));});}

export { i, r };
//# sourceMappingURL=Index7-Dgnp-Xma.js.map
