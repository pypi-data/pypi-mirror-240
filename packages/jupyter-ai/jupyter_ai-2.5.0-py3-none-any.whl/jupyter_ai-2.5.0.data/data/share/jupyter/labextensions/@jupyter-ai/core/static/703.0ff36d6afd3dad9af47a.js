"use strict";(self.webpackChunk_jupyter_ai_core=self.webpackChunk_jupyter_ai_core||[]).push([[703],{45450:(e,t,n)=>{n.d(t,{f:()=>r});var u=n(17544);function r(e,t,n,r){const i=r?r-1:Number.POSITIVE_INFINITY;let o=0;return function(r){return(0,u.xz)(r)?(e.enter(n),a(r)):t(r)};function a(r){return(0,u.xz)(r)&&o++<i?(e.consume(r),a):(e.exit(n),t(r))}}},17544:(e,t,n)=>{n.d(t,{jv:()=>u,H$:()=>r,n9:()=>i,Av:()=>o,pY:()=>a,AF:()=>c,sR:()=>l,Ch:()=>s,z3:()=>h,xz:()=>F,Xh:()=>f,B8:()=>m});const u=A(/[A-Za-z]/),r=A(/[\dA-Za-z]/),i=A(/[#-'*+\--9=?A-Z^-~]/);function o(e){return null!==e&&(e<32||127===e)}const a=A(/\d/),c=A(/[\dA-Fa-f]/),l=A(/[!-/:-@[-`{-~]/);function s(e){return null!==e&&e<-2}function h(e){return null!==e&&(e<0||32===e)}function F(e){return-2===e||-1===e||32===e}const f=A(/[!-\/:-@\[-`\{-~\xA1\xA7\xAB\xB6\xB7\xBB\xBF\u037E\u0387\u055A-\u055F\u0589\u058A\u05BE\u05C0\u05C3\u05C6\u05F3\u05F4\u0609\u060A\u060C\u060D\u061B\u061D-\u061F\u066A-\u066D\u06D4\u0700-\u070D\u07F7-\u07F9\u0830-\u083E\u085E\u0964\u0965\u0970\u09FD\u0A76\u0AF0\u0C77\u0C84\u0DF4\u0E4F\u0E5A\u0E5B\u0F04-\u0F12\u0F14\u0F3A-\u0F3D\u0F85\u0FD0-\u0FD4\u0FD9\u0FDA\u104A-\u104F\u10FB\u1360-\u1368\u1400\u166E\u169B\u169C\u16EB-\u16ED\u1735\u1736\u17D4-\u17D6\u17D8-\u17DA\u1800-\u180A\u1944\u1945\u1A1E\u1A1F\u1AA0-\u1AA6\u1AA8-\u1AAD\u1B5A-\u1B60\u1B7D\u1B7E\u1BFC-\u1BFF\u1C3B-\u1C3F\u1C7E\u1C7F\u1CC0-\u1CC7\u1CD3\u2010-\u2027\u2030-\u2043\u2045-\u2051\u2053-\u205E\u207D\u207E\u208D\u208E\u2308-\u230B\u2329\u232A\u2768-\u2775\u27C5\u27C6\u27E6-\u27EF\u2983-\u2998\u29D8-\u29DB\u29FC\u29FD\u2CF9-\u2CFC\u2CFE\u2CFF\u2D70\u2E00-\u2E2E\u2E30-\u2E4F\u2E52-\u2E5D\u3001-\u3003\u3008-\u3011\u3014-\u301F\u3030\u303D\u30A0\u30FB\uA4FE\uA4FF\uA60D-\uA60F\uA673\uA67E\uA6F2-\uA6F7\uA874-\uA877\uA8CE\uA8CF\uA8F8-\uA8FA\uA8FC\uA92E\uA92F\uA95F\uA9C1-\uA9CD\uA9DE\uA9DF\uAA5C-\uAA5F\uAADE\uAADF\uAAF0\uAAF1\uABEB\uFD3E\uFD3F\uFE10-\uFE19\uFE30-\uFE52\uFE54-\uFE61\uFE63\uFE68\uFE6A\uFE6B\uFF01-\uFF03\uFF05-\uFF0A\uFF0C-\uFF0F\uFF1A\uFF1B\uFF1F\uFF20\uFF3B-\uFF3D\uFF3F\uFF5B\uFF5D\uFF5F-\uFF65]/),m=A(/\s/);function A(e){return function(t){return null!==t&&e.test(String.fromCharCode(t))}}},7703:(e,t,n)=>{n.r(t),n.d(t,{default:()=>A});var u=n(45450),r=n(17544);const i={tokenize:function(e,t,n){const i=this,a=i.events[i.events.length-1],c=a&&"linePrefix"===a[1].type?a[2].sliceSerialize(a[1],!0).length:0;let l=0;return function(t){return e.enter("mathFlow"),e.enter("mathFlowFence"),e.enter("mathFlowFenceSequence"),s(t)};function s(t){return 36===t?(e.consume(t),l++,s):l<2?n(t):(e.exit("mathFlowFenceSequence"),(0,u.f)(e,h,"whitespace")(t))}function h(t){return null===t||(0,r.Ch)(t)?f(t):(e.enter("mathFlowFenceMeta"),e.enter("chunkString",{contentType:"string"}),F(t))}function F(t){return null===t||(0,r.Ch)(t)?(e.exit("chunkString"),e.exit("mathFlowFenceMeta"),f(t)):36===t?n(t):(e.consume(t),F)}function f(n){return e.exit("mathFlowFence"),i.interrupt?t(n):e.attempt(o,m,d)(n)}function m(t){return e.attempt({tokenize:E,partial:!0},d,A)(t)}function A(t){return(c?(0,u.f)(e,p,"linePrefix",c+1):p)(t)}function p(t){return null===t?d(t):(0,r.Ch)(t)?e.attempt(o,m,d)(t):(e.enter("mathFlowValue"),x(t))}function x(t){return null===t||(0,r.Ch)(t)?(e.exit("mathFlowValue"),p(t)):(e.consume(t),x)}function d(n){return e.exit("mathFlow"),t(n)}function E(e,t,n){let o=0;return(0,u.f)(e,(function(t){return e.enter("mathFlowFence"),e.enter("mathFlowFenceSequence"),a(t)}),"linePrefix",i.parser.constructs.disable.null.includes("codeIndented")?void 0:4);function a(t){return 36===t?(o++,e.consume(t),a):o<l?n(t):(e.exit("mathFlowFenceSequence"),(0,u.f)(e,c,"whitespace")(t))}function c(u){return null===u||(0,r.Ch)(u)?(e.exit("mathFlowFence"),t(u)):n(u)}}},concrete:!0},o={tokenize:function(e,t,n){const u=this;return function(n){return null===n?t(n):(e.enter("lineEnding"),e.consume(n),e.exit("lineEnding"),r)};function r(e){return u.parser.lazy[u.now().line]?n(e):t(e)}},partial:!0};function a(e){let t=(e||{}).singleDollarTextMath;return null==t&&(t=!0),{tokenize:function(e,n,u){let i,o,a=0;return function(t){return e.enter("mathText"),e.enter("mathTextSequence"),c(t)};function c(n){return 36===n?(e.consume(n),a++,c):a<2&&!t?u(n):(e.exit("mathTextSequence"),l(n))}function l(t){return null===t?u(t):36===t?(o=e.enter("mathTextSequence"),i=0,h(t)):32===t?(e.enter("space"),e.consume(t),e.exit("space"),l):(0,r.Ch)(t)?(e.enter("lineEnding"),e.consume(t),e.exit("lineEnding"),l):(e.enter("mathTextData"),s(t))}function s(t){return null===t||32===t||36===t||(0,r.Ch)(t)?(e.exit("mathTextData"),l(t)):(e.consume(t),s)}function h(t){return 36===t?(e.consume(t),i++,h):i===a?(e.exit("mathTextSequence"),e.exit("mathText"),n(t)):(o.type="mathTextData",s(t))}},resolve:c,previous:l}}function c(e){let t,n,u=e.length-4,r=3;if(!("lineEnding"!==e[r][1].type&&"space"!==e[r][1].type||"lineEnding"!==e[u][1].type&&"space"!==e[u][1].type))for(t=r;++t<u;)if("mathTextData"===e[t][1].type){e[u][1].type="mathTextPadding",e[r][1].type="mathTextPadding",r+=2,u-=2;break}for(t=r-1,u++;++t<=u;)void 0===n?t!==u&&"lineEnding"!==e[t][1].type&&(n=t):t!==u&&"lineEnding"!==e[t][1].type||(e[n][1].type="mathTextData",t!==n+2&&(e[n][1].end=e[t-1][1].end,e.splice(n+2,t-n-2),u-=t-n-2,t=n+2),n=void 0);return e}function l(e){return 36!==e||"characterEscape"===this.events[this.events.length-1][1].type}function s(e){if(!e._compiled){const t=(e.atBreak?"[\\r\\n][\\t ]*":"")+(e.before?"(?:"+e.before+")":"");e._compiled=new RegExp((t?"("+t+")":"")+(/[|\\{}()[\]^$+*?.-]/.test(e.character)?"\\":"")+e.character+(e.after?"(?:"+e.after+")":""),"g")}return e._compiled}function h(e,t){return F(e,t.inConstruct,!0)&&!F(e,t.notInConstruct,!1)}function F(e,t,n){if("string"==typeof t&&(t=[t]),!t||0===t.length)return n;let u=-1;for(;++u<t.length;)if(e.includes(t[u]))return!0;return!1}function f(e,t){return e-t}function m(e,t){const n=/\\(?=[!-/:-@[-`{-~])/g,u=[],r=[],i=e+t;let o,a=-1,c=0;for(;o=n.exec(i);)u.push(o.index);for(;++a<u.length;)c!==u[a]&&r.push(e.slice(c,u[a])),r.push("\\"),c=u[a];return r.push(e.slice(c)),r.join("")}function A(e={}){const t=this.data();function n(e,n){(t[e]?t[e]:t[e]=[]).push(n)}n("micromarkExtensions",function(e){return{flow:{36:i},text:{36:a(e)}}}(e)),n("fromMarkdownExtensions",function(){return{enter:{mathFlow:function(e){this.enter({type:"math",meta:null,value:"",data:{hName:"div",hProperties:{className:["math","math-display"]},hChildren:[{type:"text",value:""}]}},e)},mathFlowFenceMeta:function(){this.buffer()},mathText:function(e){this.enter({type:"inlineMath",value:"",data:{hName:"span",hProperties:{className:["math","math-inline"]},hChildren:[{type:"text",value:""}]}},e),this.buffer()}},exit:{mathFlow:function(e){const t=this.resume().replace(/^(\r?\n|\r)|(\r?\n|\r)$/g,""),n=this.exit(e);n.value=t,n.data.hChildren[0].value=t,this.setData("mathFlowInside")},mathFlowFence:function(){this.getData("mathFlowInside")||(this.buffer(),this.setData("mathFlowInside",!0))},mathFlowFenceMeta:function(){const e=this.resume();this.stack[this.stack.length-1].meta=e},mathFlowValue:e,mathText:function(e){const t=this.resume(),n=this.exit(e);n.value=t,n.data.hChildren[0].value=t},mathTextData:e}};function e(e){this.config.enter.data.call(this,e),this.config.exit.data.call(this,e)}}()),n("toMarkdownExtensions",function(e){let t=(e||{}).singleDollarTextMath;return null==t&&(t=!0),n.peek=function(){return"$"},{unsafe:[{character:"\r",inConstruct:"mathFlowMeta"},{character:"\n",inConstruct:"mathFlowMeta"},{character:"$",after:t?void 0:"\\$",inConstruct:"phrasing"},{character:"$",inConstruct:"mathFlowMeta"},{atBreak:!0,character:"$",after:"\\$"}],handlers:{math:function(e,t,n,u){const r=e.value||"",i=function(e){const t=e||{},n=t.now||{};let u=t.lineShift||0,r=n.line||1,i=n.column||1;return{move:function(e){const t=e||"",n=t.split(/\r?\n|\r/g),o=n[n.length-1];return r+=n.length-1,i=1===n.length?i+o.length:1+o.length+u,t},current:function(){return{now:{line:r,column:i},lineShift:u}},shift:function(e){u+=e}}}(u),o="$".repeat(Math.max(function(e,t){const n=String(e);let u=n.indexOf(t),r=u,i=0,o=0;for(;-1!==u;)u===r?++i>o&&(o=i):i=1,r=u+1,u=n.indexOf(t,r);return o}(r,"$")+1,2)),a=n.enter("mathFlow");let c=i.move(o);if(e.meta){const t=n.enter("mathFlowMeta");c+=i.move(function(e,t,n){const u=(n.before||"")+(t||"")+(n.after||""),r=[],i=[],o={};let a=-1;for(;++a<e.unsafe.length;){const t=e.unsafe[a];if(!h(e.stack,t))continue;const n=s(t);let i;for(;i=n.exec(u);){const e="before"in t||Boolean(t.atBreak),n="after"in t,u=i.index+(e?i[1].length:0);r.includes(u)?(o[u].before&&!e&&(o[u].before=!1),o[u].after&&!n&&(o[u].after=!1)):(r.push(u),o[u]={before:e,after:n})}}r.sort(f);let c=n.before?n.before.length:0;const l=u.length-(n.after?n.after.length:0);for(a=-1;++a<r.length;){const e=r[a];e<c||e>=l||e+1<l&&r[a+1]===e+1&&o[e].after&&!o[e+1].before&&!o[e+1].after||r[a-1]===e-1&&o[e].before&&!o[e-1].before&&!o[e-1].after||(c!==e&&i.push(m(u.slice(c,e),"\\")),c=e,!/[!-/:-@[-`{-~]/.test(u.charAt(e))||n.encode&&n.encode.includes(u.charAt(e))?(i.push("&#x"+u.charCodeAt(e).toString(16).toUpperCase()+";"),c++):i.push("\\"))}return i.push(m(u.slice(c,l),n.after)),i.join("")}(n,e.meta,{before:c,after:"\n",encode:["$"],...i.current()})),t()}return c+=i.move("\n"),r&&(c+=i.move(r+"\n")),c+=i.move(o),a(),c},inlineMath:n}};function n(e,n,u){let r=e.value||"",i=1;for(t||i++;new RegExp("(^|[^$])"+"\\$".repeat(i)+"([^$]|$)").test(r);)i++;const o="$".repeat(i);/[^ \r\n]/.test(r)&&(/^[ \r\n]/.test(r)&&/[ \r\n]$/.test(r)||/^\$|\$$/.test(r))&&(r=" "+r+" ");let a=-1;for(;++a<u.unsafe.length;){const e=u.unsafe[a],t=s(e);let n;if(e.atBreak)for(;n=t.exec(r);){let e=n.index;10===r.codePointAt(e)&&13===r.codePointAt(e-1)&&e--,r=r.slice(0,e)+" "+r.slice(n.index+1)}}return o+r+o}}(e))}}}]);