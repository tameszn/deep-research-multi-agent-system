import { J as m$1 } from './2-C0uxS_Ck.js';
import { f } from './statustracker-Dcv3b821.js';
import { n, V as Ve, p as m } from './src3-BYRta5-S.js';
import './async-Cv1-GZGV.js';
import { s as spread_props, d as attr, e as escape_html, f as ensure_array_like, a as attr_class } from './renderer-B44-mkIR.js';
import './environment-BxEoFHfh.js';
import './chunk-MAaCUEXr.js';
import 'node:module';
import './server-ozwWCFiP.js';
import './html-CfyvkLET.js';

function o(o,s){o.component(o=>{let{$$slots:c,$$events:l,...u}=s,d=new m$1(u),f$1=(()=>{let e=d.props.choices.map(([,e])=>e);return d.props.value.length===0?`unchecked`:d.props.value.length===e.length?`checked`:`indeterminate`})(),p=!d.shared.interactive;d.props.value,n(o,{visible:d.shared.visible,elem_id:d.shared.elem_id,elem_classes:d.shared.elem_classes,type:`fieldset`,container:d.shared.container,scale:d.shared.scale,min_width:d.shared.min_width,children:e=>{f(e,spread_props([{autoscroll:d.shared.autoscroll,i18n:d.i18n},d.shared.loading_status,{on_clear_status:()=>d.dispatch(`clear_status`,d.shared.loading_status)}])),e.push(`<!----> `),d.shared.show_label&&d.props.buttons&&d.props.buttons.length>0?(e.push(`<!--[-->`),Ve(e,{buttons:d.props.buttons,on_custom_button_click:e=>{d.dispatch(`custom_button_click`,{id:e});}})):e.push(`<!--[!-->`),e.push(`<!--]--> `),m(e,{show_label:d.shared.show_label||d.props.show_select_all&&d.shared.interactive,info:d.props.info,children:e=>{d.props.show_select_all&&d.shared.interactive?(e.push(`<!--[-->`),e.push(`<div class="select-all-container svelte-yb2gcx"><label class="select-all-label svelte-yb2gcx"><input class="select-all-checkbox svelte-yb2gcx"${attr(`checked`,f$1===`checked`,true)}${attr(`indeterminate`,f$1===`indeterminate`,true)} type="checkbox" title="Select/Deselect All"/></label> <button type="button" class="label-text svelte-yb2gcx">${escape_html(d.shared.show_label?d.shared.label:`Select All`)}</button></div>`)):(e.push(`<!--[!-->`),d.shared.show_label?(e.push(`<!--[-->`),e.push(`${escape_html(d.shared.label||d.i18n(`checkbox.checkbox_group`))}`)):e.push(`<!--[!-->`),e.push(`<!--]-->`)),e.push(`<!--]-->`);}}),e.push(`<!----> <div class="wrap svelte-yb2gcx" data-testid="checkbox-group"><!--[-->`);let r=ensure_array_like(d.props.choices);for(let t=0,n=r.length;t<n;t++){let[n,i]=r[t];e.push(`<label${attr_class(`svelte-yb2gcx`,void 0,{disabled:p,selected:d.props.value.includes(i)})}><input${attr(`disabled`,p,true)}${attr(`checked`,d.props.value.includes(i),true)} type="checkbox"${attr(`name`,i?.toString())}${attr(`title`,i?.toString())} class="svelte-yb2gcx"/> <span class="ml-2 svelte-yb2gcx">${escape_html(d.live_i18n(n))}</span></label>`);}e.push(`<!--]--></div>`);},$$slots:{default:true}});});}

export { o as default };
//# sourceMappingURL=Index16-CKemjTQq.js.map
