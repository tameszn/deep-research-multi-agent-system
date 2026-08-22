import { J as m$1 } from './2-C0uxS_Ck.js';
import { r } from './Index5-D1FZcrsg.js';
import { m } from './src4-BxCKxrXN.js';
import { d as attr, h as stringify, e as escape_html } from './renderer-B44-mkIR.js';
import './async-Cv1-GZGV.js';
import './environment-BxEoFHfh.js';
import './chunk-MAaCUEXr.js';
import 'node:module';
import './Image-D9mSw2LY.js';
import './src3-BYRta5-S.js';
import './html-CfyvkLET.js';

function i(e,i){e.component(e=>{let{elem_id:a=``,elem_classes:o=[],visible:s=true,label:c,value:l,file_count:u,file_types:d=[],root:f,size:p=`lg`,icon:m$1=null,scale:h=null,min_width:g=void 0,variant:_=`secondary`,disabled:v=false,max_file_size:y=null,upload:b,onclick:x,onchange:S,onupload:C,onerror:w,children:T}=i,E=d==null?null:d.map(e=>e.startsWith(`.`)?e:e+`/*`).join(`, `);function D(){x?.(),(void 0).click();}e.push(`<input class="hide svelte-94gmgt"${attr(`accept`,m(E))} type="file"${attr(`multiple`,u===`multiple`||void 0,true)}${attr(`webkitdirectory`,u===`directory`||void 0,true)}${attr(`mozdirectory`,u===`directory`||void 0)}${attr(`data-testid`,`${stringify(c)}-upload-button`)}/> `),r(e,{size:p,variant:_,elem_id:a,elem_classes:o,visible:s,onclick:D,scale:h,min_width:g,disabled:v,children:e=>{m$1?(e.push(`<!--[-->`),e.push(`<img class="button-icon svelte-94gmgt"${attr(`src`,m$1.url)}${attr(`alt`,`${l} icon`)}/>`)):e.push(`<!--[!-->`),e.push(`<!--]--> `),T?(e.push(`<!--[-->`),T(e),e.push(`<!---->`)):e.push(`<!--[!-->`),e.push(`<!--]-->`);}}),e.push(`<!---->`);});}function a(t,n){t.component(t=>{let{$$slots:a,$$events:o,...s}=n,c=new m$1(s),l=c.props.value;async function u(e,t){c.props.value=e,c.dispatch(t);}let d=!c.shared.interactive;i(t,{elem_id:c.shared.elem_id,elem_classes:c.shared.elem_classes,visible:c.shared.visible,file_count:c.props.file_count,file_types:c.props.file_types,size:c.props.size,scale:c.shared.scale,icon:c.props.icon,min_width:c.shared.min_width,root:c.shared.root,value:l,disabled:d,variant:c.props.variant,label:c.shared.label,max_file_size:c.shared.max_file_size,onclick:()=>c.dispatch(`click`),onchange:e=>u(e,`change`),onupload:e=>u(e,`upload`),onerror:e=>{c.dispatch(`error`,e);},upload:(...e)=>c.shared.client.upload(...e),children:e=>{e.push(`<!---->${escape_html(c.shared.label??``)}`);}});});}

export { i as BaseUploadButton, a as default };
//# sourceMappingURL=Index60-B9Rka2nb.js.map
