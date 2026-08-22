import { J as m$1 } from './2-C0uxS_Ck.js';
import { f } from './statustracker-Dcv3b821.js';
import { n, p as m } from './src3-BYRta5-S.js';
import { s as spread_props, d as attr, e as escape_html } from './renderer-B44-mkIR.js';
import './async-Cv1-GZGV.js';
import './environment-BxEoFHfh.js';
import './chunk-MAaCUEXr.js';
import 'node:module';
import './server-ozwWCFiP.js';
import './html-CfyvkLET.js';

var a=0;function o(o,s){o.component(o=>{let{$$slots:c,$$events:l,...u}=s,d=new m$1(u);d.props.value,d.props.value;let f$1=`range_id_${a++}`,p=d.props.minimum??0;(()=>{let e=d.props.minimum,t=d.props.maximum,n=d.props.value;return n>t?100:n<e?0:(n-e)/(t-e)*100})();let m$2=!d.shared.interactive;n(o,{visible:d.shared.visible,elem_id:d.shared.elem_id,elem_classes:d.shared.elem_classes,container:d.shared.container,scale:d.shared.scale,min_width:d.shared.min_width,children:e=>{f(e,spread_props([{autoscroll:d.shared.autoscroll,i18n:d.i18n},d.shared.loading_status,{on_clear_status:()=>d.dispatch(`clear_status`,d.shared.loading_status)}])),e.push(`<!----> <div class="wrap svelte-8epfm4"><div class="head svelte-8epfm4"><label${attr(`for`,f$1)} class="svelte-8epfm4">`),m(e,{show_label:d.shared.show_label,info:d.props.info,children:e=>{e.push(`<!---->${escape_html(d.shared.label||`Slider`)}`);}}),e.push(`<!----></label> <div class="tab-like-container svelte-8epfm4"><input${attr(`aria-label`,`number input for ${d.shared.label}`)} data-testid="number-input" type="number"${attr(`value`,d.props.value)}${attr(`min`,d.props.minimum)}${attr(`max`,d.props.maximum)}${attr(`step`,d.props.step)}${attr(`disabled`,m$2,true)} class="svelte-8epfm4"/> `),d.props.buttons?.includes(`reset`)??true?(e.push(`<!--[-->`),e.push(`<button class="reset-button svelte-8epfm4"${attr(`disabled`,m$2,true)} aria-label="Reset to default value" data-testid="reset-button">↺</button>`)):e.push(`<!--[!-->`),e.push(`<!--]--></div></div> <div class="slider_input_container svelte-8epfm4"><span class="min_value svelte-8epfm4" data-testid="min-value">${escape_html(p)}</span> <input type="range"${attr(`id`,f$1)} name="cowbell" data-testid="range-input"${attr(`value`,d.props.value)}${attr(`min`,d.props.minimum)}${attr(`max`,d.props.maximum)}${attr(`step`,d.props.step)}${attr(`disabled`,m$2,true)}${attr(`aria-label`,`range slider for ${d.shared.label}`)} class="svelte-8epfm4"/> <span class="max_value svelte-8epfm4" data-testid="max-value">${escape_html(d.props.maximum)}</span></div></div>`);},$$slots:{default:true}});});}

export { o as default };
//# sourceMappingURL=Index54-DytU8O44.js.map
